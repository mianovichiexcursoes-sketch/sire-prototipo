"""Imagens do catálogo no Google Drive pessoal da autora, por OAuth de usuário.

Requer credenciais SIRE_DRIVE_* em variáveis de ambiente do servidor.
O token da conexão do ChatGPT não pode ser usado automaticamente pelo Django.
Usa apenas o escopo drive.file: acesso aos arquivos criados por este aplicativo.
Nenhuma foto é gravada no disco efêmero do Render ou no PostgreSQL.
"""

import io
import json
import re
import uuid
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.conf import settings
from django.core.cache import cache
from PIL import Image, ImageOps, UnidentifiedImageError

LIMITE_FOTOS = 6
LIMITE_UPLOAD = 5 * 1024 * 1024
LIMITE_PIXELS = 20_000_000
PASTA = "SIRE - Fotos de excursões"
API = "https://www.googleapis.com/drive/v3/files"
IMAGE_MAX = (1600, 1600)


class FalhaDrive(Exception):
    """Erro controlado de armazenamento, sem revelar credenciais ao usuário."""


def configurado():
    return all(
        (
            settings.SIRE_DRIVE_CLIENT_ID,
            settings.SIRE_DRIVE_CLIENT_SECRET,
            settings.SIRE_DRIVE_REFRESH_TOKEN,
        )
    )


def _json_request(url, *, data=None, method="GET", headers=None, timeout=20):
    requisicao = Request(url, data=data, method=method, headers=headers or {})
    try:
        with urlopen(requisicao, timeout=timeout) as resposta:
            corpo = resposta.read()
            return json.loads(corpo) if corpo else {}
    except (HTTPError, URLError, OSError, ValueError) as erro:
        # Não registrar resposta do Google, tokens ou dados do usuário.
        raise FalhaDrive("Não foi possível comunicar com o Google Drive.") from erro


def _token():
    if not configurado():
        raise FalhaDrive("O Google Drive ainda não foi configurado pela administração.")
    token = cache.get("sire_drive_token")
    if token:
        return token
    dados = urlencode(
        {
            "client_id": settings.SIRE_DRIVE_CLIENT_ID,
            "client_secret": settings.SIRE_DRIVE_CLIENT_SECRET,
            "refresh_token": settings.SIRE_DRIVE_REFRESH_TOKEN,
            "grant_type": "refresh_token",
        }
    ).encode()
    resposta = _json_request(
        "https://oauth2.googleapis.com/token",
        data=dados,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    token = resposta.get("access_token")
    if not token:
        raise FalhaDrive("Autorização do Google Drive indisponível.")
    cache.set("sire_drive_token", token, max(60, int(resposta.get("expires_in", 3600)) - 90))
    return token


def _headers():
    return {"Authorization": f"Bearer {_token()}"}


def _pasta():
    # drive.file permite ver a pasta que o próprio SIRE criou. Não acessa
    # indiscriminadamente as outras pastas privadas da conta Google.
    q = f"name = '{PASTA}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    url = f"{API}?{urlencode({'q': q, 'fields': 'files(id,name)', 'pageSize': '10'})}"
    existentes = _json_request(url, headers=_headers()).get("files", [])
    if existentes:
        return existentes[0]["id"]
    novo = _json_request(
        API + "?fields=id",
        data=json.dumps({"name": PASTA, "mimeType": "application/vnd.google-apps.folder"}).encode(),
        method="POST",
        headers={**_headers(), "Content-Type": "application/json; charset=UTF-8"},
    )
    if not novo.get("id"):
        raise FalhaDrive("O Google Drive não retornou o identificador da pasta.")
    return novo["id"]


def preparar_jpeg(arquivo):
    """Validação real pelo decodificador, conversão RGB e redução de tamanho."""
    if arquivo.size > LIMITE_UPLOAD or arquivo.size <= 0:
        raise ValueError("A foto deve ter entre 1 byte e 5 MB.")
    try:
        with Image.open(arquivo) as foto:
            if foto.format not in {"JPEG", "PNG", "WEBP"}:
                raise ValueError("Envie uma foto JPG, PNG ou WebP.")
            largura, altura = foto.size
            if largura * altura > LIMITE_PIXELS:
                raise ValueError("A imagem possui resolução acima do limite permitido.")
            foto = ImageOps.exif_transpose(foto)
            foto.thumbnail(IMAGE_MAX, Image.Resampling.LANCZOS)
            if foto.mode in {"RGBA", "LA"} or (foto.mode == "P" and "transparency" in foto.info):
                base = Image.new("RGB", foto.size, "white")
                base.paste(foto.convert("RGBA"), mask=foto.convert("RGBA").getchannel("A"))
                foto = base
            else:
                foto = foto.convert("RGB")
            saida = io.BytesIO()
            foto.save(saida, "JPEG", quality=78, optimize=True, progressive=True)
            dados = saida.getvalue()
            if len(dados) > 2 * 1024 * 1024:
                raise ValueError("A foto otimizada ultrapassou 2 MB.")
            return dados
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as erro:
        raise ValueError(
            "O arquivo enviado não é uma foto válida. Envie somente fotos JPG, PNG ou "
            "WebP; vídeos não são aceitos."
        ) from erro


def enviar(excursao_id, imagem_jpeg):
    """Cria foto em Drive pessoal; devolve ID para persistência relacional."""
    pasta_id = _pasta()
    nome = f"sire-excursao-{excursao_id}-{uuid.uuid4().hex}.jpg"
    metadados = json.dumps(
        {"name": nome, "mimeType": "image/jpeg", "parents": [pasta_id]}
    ).encode()
    limite = f"sire_{uuid.uuid4().hex}"
    separador = limite.encode()
    corpo = (
        b"--" + separador + b"\r\n"
        + b"Content-Type: application/json; charset=UTF-8\r\n\r\n"
        + metadados + b"\r\n"
        + b"--" + separador + b"\r\n"
        + b"Content-Type: image/jpeg\r\n\r\n"
        + imagem_jpeg + b"\r\n"
        + b"--" + separador + b"--\r\n"
    )
    resposta = _json_request(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id",
        data=corpo,
        method="POST",
        headers={**_headers(), "Content-Type": f"multipart/related; boundary={limite}"},
        timeout=40,
    )
    if not resposta.get("id"):
        raise FalhaDrive("O Google Drive não confirmou o envio da foto.")
    return resposta["id"]


def _validar_drive_id(drive_id):
    """Fail closed before constructing an authenticated Google API URL.

    Drive file IDs are opaque URL-safe identifiers, not arbitrary URL paths,
    fragments or query parameters supplied by the database.
    """
    if not isinstance(drive_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,128}", drive_id):
        raise FalhaDrive("Identificador de foto inválido.")
    return drive_id


def baixar(drive_id):
    drive_id = _validar_drive_id(drive_id)
    requisicao = Request(f"{API}/{drive_id}?alt=media", headers=_headers())
    try:
        with urlopen(requisicao, timeout=20) as resposta:
            # Fotos do SIRE são JPEG otimizadas, de no máximo 2 MB.
            dados = resposta.read(2 * 1024 * 1024 + 1)
            if len(dados) > 2 * 1024 * 1024:
                raise FalhaDrive("A foto armazenada ultrapassou o tamanho permitido.")
            return dados
    except (HTTPError, URLError, OSError) as erro:
        raise FalhaDrive("Não foi possível carregar a foto no Drive.") from erro


def excluir(drive_id):
    drive_id = _validar_drive_id(drive_id)
    requisicao = Request(f"{API}/{drive_id}", method="DELETE", headers=_headers())
    try:
        with urlopen(requisicao, timeout=20) as resposta:
            resposta.read()
    except HTTPError as erro:
        if erro.code != 404:
            raise FalhaDrive("Não foi possível remover a foto do Google Drive.") from erro
    except (URLError, OSError) as erro:
        raise FalhaDrive("Não foi possível remover a foto do Google Drive.") from erro
