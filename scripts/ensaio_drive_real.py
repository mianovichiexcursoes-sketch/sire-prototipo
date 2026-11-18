"""Ensaio REAL das fotos no Google Drive, isolado da demonstração pública.

Executar no computador da autora, depois de scripts/autorizacao_drive.py:

    .\\.venv\\Scripts\\python.exe scripts\\ensaio_drive_real.py

O que faz:
1. Pede a chave do Render com entrada oculta e lê, só em memória, as três
   credenciais do grupo sire-drive-oauth-* (nada é gravado em disco).
2. Usa o banco LOCAL configurado no .env (PostgreSQL do Windows), nunca o
   banco da demo. Cria agências, contas e excursões com prefixo único.
3. Envia uma imagem sintética (gerada aqui, sem pessoas) pelo fluxo real do
   SIRE e confere: visualização, rascunho restrito, isolamento entre agências,
   permissões do arquivo no Drive, persistência em um processo novo (reinício
   a frio) e remoção.
4. Apaga os dados de ensaio e o arquivo no Drive ao final, mesmo em falha.
5. Grava em evidencias/ apenas resultados (sem credenciais nem IDs de arquivo).
"""

import argparse
import hashlib
import io
import json
import os
import secrets
import subprocess
import sys
from datetime import date, datetime, time, timedelta
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

CHAVES = ("SIRE_DRIVE_CLIENT_ID", "SIRE_DRIVE_CLIENT_SECRET", "SIRE_DRIVE_REFRESH_TOKEN")
WORKSPACE = "tea-dbqsq4on74is73d4onpg"


# ---------------------------------------------------------------- credenciais
def _render(url, chave):
    req = Request(url, headers={"Authorization": f"Bearer {chave}", "Accept": "application/json"})
    with urlopen(req, timeout=20) as resposta:
        return json.load(resposta)


def carregar_credenciais():
    """Lê o grupo do Render para o ambiente DESTE processo (memória)."""
    from scripts.autorizacao_drive import USAR_JANELA, segredo

    USAR_JANELA[0] = True  # janela mascarada, com conferência do formato rnd_
    chave = segredo("RENDER_API_KEY")
    itens = _render(
        "https://api.render.com/v1/env-groups?" + urlencode({"ownerId": WORKSPACE, "limit": "100"}),
        chave,
    )
    grupos = [
        (i.get("envGroup", i) if isinstance(i, dict) else {}) for i in (itens or [])
    ]
    grupos = [g for g in grupos if str(g.get("name", "")).startswith("sire-drive-oauth-")]
    if len(grupos) != 1:
        raise SystemExit(f"Esperado 1 grupo sire-drive-oauth-*; encontrados {len(grupos)}.")
    detalhe = _render(f"https://api.render.com/v1/env-groups/{grupos[0]['id']}", chave)
    del chave
    valores = {v.get("key"): v.get("value") for v in detalhe.get("envVars") or []}
    detalhe.clear()
    if set(valores) != set(CHAVES) or not all(valores.values()):
        raise SystemExit("O grupo não contém as três credenciais preenchidas.")
    os.environ.update(valores)
    valores.clear()
    return grupos[0]["name"]


# ---------------------------------------------------------------- Django
def iniciar_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sire_project.settings")
    hosts = os.environ.get("SIRE_ALLOWED_HOSTS", "127.0.0.1,localhost")
    os.environ["SIRE_ALLOWED_HOSTS"] = hosts + ",testserver"
    import django

    django.setup()
    from django.db import connection

    if connection.vendor != "postgresql":
        print("Aviso: o ensaio está usando", connection.vendor, "(esperado PostgreSQL local).")
    return connection


def imagem_sintetica():
    """Faixas coloridas e texto; nenhuma pessoa ou dado real."""
    from PIL import Image, ImageDraw

    imagem = Image.new("RGB", (800, 600), "white")
    desenho = ImageDraw.Draw(imagem)
    cores = ["#97254e", "#e88aab", "#fce9f1", "#684957"]
    for i, cor in enumerate(cores):
        desenho.rectangle([0, i * 150, 800, (i + 1) * 150], fill=cor)
    desenho.text((40, 280), "SIRE - ENSAIO SINTETICO", fill="black")
    saida = io.BytesIO()
    imagem.save(saida, "PNG")
    saida.name = "ensaio.png"
    saida.seek(0)
    return saida


# ---------------------------------------------------------------- etapas
class Registro:
    def __init__(self):
        self.itens = []

    def __call__(self, nome, ok, detalhe=""):
        self.itens.append({"verificacao": nome, "conforme": bool(ok), "obtido": detalhe})
        print(("OK   " if ok else "FALHA"), nome, "-", detalhe)

    @property
    def tudo_ok(self):
        return all(i["conforme"] for i in self.itens)


def permissoes_drive(drive_id):
    """Metadados do arquivo no Drive: compartilhamento e permissões."""
    from sire import drive_fotos

    campos = "id,mimeType,shared,permissions(type,role)"
    return drive_fotos._json_request(
        f"{drive_fotos.API}/{drive_fotos._validar_drive_id(drive_id)}?fields={campos}",
        headers=drive_fotos._headers(),
    )


def existe_no_drive(drive_id):
    from sire import drive_fotos

    try:
        dados = drive_fotos._json_request(
            f"{drive_fotos.API}/{drive_id}?fields=id,trashed", headers=drive_fotos._headers()
        )
        return not dados.get("trashed", False)
    except drive_fotos.FalhaDrive as erro:
        causa = erro.__cause__
        if isinstance(causa, HTTPError) and causa.code == 404:
            return False
        raise


def fase_preparar(prefixo, estado_arquivo, registro):
    from django.contrib.auth.models import User
    from django.test import Client
    from sire.models import (
        Agencia, Excursao, FotoExcursao, PerfilUsuario, PontoEmbarque, StatusExcursao, TipoPerfil,
    )

    ag_a = Agencia.objects.create(nome=f"{prefixo} Agência A (fictícia)")
    ag_b = Agencia.objects.create(nome=f"{prefixo} Agência B (fictícia)")

    def conta(nome, tipo, agencia=None):
        usuario = User.objects.create_user(username=f"{prefixo}_{nome}", password=secrets.token_urlsafe(16))
        PerfilUsuario.objects.create(usuario=usuario, tipo=tipo, agencia=agencia)
        cliente = Client()
        cliente.force_login(usuario)
        return cliente

    agente_a = conta("agente_a", TipoPerfil.AGENTE, ag_a)
    agente_b = conta("agente_b", TipoPerfil.AGENTE, ag_b)
    passageiro = conta("passageiro", TipoPerfil.PASSAGEIRO)
    anonimo = Client()

    def excursao(titulo, status):
        e = Excursao.objects.create(
            titulo=f"{prefixo} {titulo}", destino="Destino fictício",
            data_saida=date.today() + timedelta(days=40), valor=100, capacidade=5,
            status=status, agencia=ag_a,
        )
        PontoEmbarque.objects.create(local="Terminal fictício", horario=time(7, 0), excursao=e)
        return e

    publicada = excursao("Publicada", StatusExcursao.PUBLICADA)
    rascunho = excursao("Rascunho", StatusExcursao.RASCUNHO)

    def enviar(cliente, exc):
        return cliente.post(f"/agente/excursoes/{exc.pk}/fotos/nova/", {"foto": imagem_sintetica()})

    # 1. Upload real pela agência dona
    enviar(agente_a, publicada)
    enviar(agente_a, rascunho)
    foto_pub = FotoExcursao.objects.filter(excursao=publicada).first()
    foto_ras = FotoExcursao.objects.filter(excursao=rascunho).first()
    registro("Upload pela agência dona (publicada e rascunho)", foto_pub and foto_ras,
             f"fotos gravadas: {int(bool(foto_pub)) + int(bool(foto_ras))} de 2")
    if not (foto_pub and foto_ras):
        return None

    # 2. Arquivo existe no Drive e é JPEG
    meta = permissoes_drive(foto_pub.drive_id)
    registro("Arquivo criado no Drive como JPEG", meta.get("mimeType") == "image/jpeg",
             meta.get("mimeType", "?"))

    # 3. Permissões: só a dona, sem link público
    tipos = sorted({p.get("type") for p in meta.get("permissions") or []})
    publico = any(p.get("type") in {"anyone", "domain"} for p in meta.get("permissions") or [])
    registro("Arquivo NÃO é público nem compartilhado",
             not publico and not meta.get("shared", False),
             f"shared={meta.get('shared')}; tipos de permissão={tipos}")

    # 4. Visualização pública da excursão publicada
    r = anonimo.get(f"/fotos/{foto_pub.pk}/imagem/")
    jpeg_ok = r.status_code == 200 and r.content[:3] == b"\xff\xd8\xff"
    registro("Visitante vê foto de excursão publicada", jpeg_ok,
             f"HTTP {r.status_code}; JPEG={r.content[:3] == b'\xff\xd8\xff'}; "
             f"Cache-Control={r.get('Cache-Control', '')}")
    registro("Resposta da foto sem cache reutilizável", "no-store" in r.get("Cache-Control", ""),
             r.get("Cache-Control", ""))
    registro("Página não expõe link direto ao Drive",
             "drive.google.com" not in anonimo.get(f"/excursao/{publicada.pk}/").content.decode()
             and "googleapis" not in anonimo.get(f"/excursao/{publicada.pk}/").content.decode(),
             "sem drive.google.com/googleapis no HTML")

    # 5. Rascunho restrito à agência dona
    codigos = {
        "visitante": anonimo.get(f"/fotos/{foto_ras.pk}/imagem/").status_code,
        "passageiro": passageiro.get(f"/fotos/{foto_ras.pk}/imagem/").status_code,
        "agente_outra_agencia": agente_b.get(f"/fotos/{foto_ras.pk}/imagem/").status_code,
        "agente_dona": agente_a.get(f"/fotos/{foto_ras.pk}/imagem/").status_code,
    }
    registro("Foto de rascunho só para a agência dona",
             codigos["agente_dona"] == 200 and all(
                 codigos[k] == 404 for k in ("visitante", "passageiro", "agente_outra_agencia")),
             json.dumps(codigos))

    # 6. Isolamento: agência B não envia nem remove fotos da A
    antes = FotoExcursao.objects.filter(excursao=publicada).count()
    rb = enviar(agente_b, publicada)
    depois = FotoExcursao.objects.filter(excursao=publicada).count()
    registro("Outra agência não envia foto", antes == depois and rb.status_code in (403, 404),
             f"HTTP {rb.status_code}; fotos {antes}->{depois}")
    rr = agente_b.post(f"/agente/excursoes/{publicada.pk}/fotos/{foto_pub.pk}/excluir/")
    ainda = FotoExcursao.objects.filter(pk=foto_pub.pk).exists() and existe_no_drive(foto_pub.drive_id)
    registro("Outra agência não remove foto", ainda and rr.status_code in (403, 404),
             f"HTTP {rr.status_code}; foto preservada no banco e no Drive: {ainda}")

    estado_arquivo.write_text(json.dumps({
        "prefixo": prefixo, "publicada": publicada.pk, "foto_pub": foto_pub.pk,
        "foto_ras": foto_ras.pk,
        "hash_drive_pub": hashlib.sha256(foto_pub.drive_id.encode()).hexdigest()[:12],
    }), encoding="utf-8")
    return True


def fase_reinicio(estado_arquivo, registro):
    """Processo novo: banco relido do disco e token obtido do zero."""
    from django.test import Client
    from sire.models import FotoExcursao

    estado = json.loads(estado_arquivo.read_text(encoding="utf-8"))
    foto = FotoExcursao.objects.filter(pk=estado["foto_pub"]).first()
    mesmo = foto and hashlib.sha256(foto.drive_id.encode()).hexdigest()[:12] == estado["hash_drive_pub"]
    r = Client().get(f"/fotos/{estado['foto_pub']}/imagem/")
    registro("Persistência após reinício (processo novo, cache vazio)",
             mesmo and r.status_code == 200 and r.content[:3] == b"\xff\xd8\xff",
             f"referência preservada: {bool(mesmo)}; HTTP {r.status_code}")


def fase_remover(prefixo, registro):
    """Remoção pela agência dona e limpeza total do ensaio."""
    from django.contrib.auth.models import User
    from django.test import Client
    from sire import drive_fotos
    from sire.models import Agencia, Excursao, FotoExcursao

    fotos = list(FotoExcursao.objects.filter(excursao__titulo__startswith=prefixo))
    dona = User.objects.filter(username=f"{prefixo}_agente_a").first()
    removidas_app = 0
    if dona and fotos:
        cliente = Client()
        cliente.force_login(dona)
        primeira = fotos[0]
        cliente.post(f"/agente/excursoes/{primeira.excursao_id}/fotos/{primeira.pk}/excluir/")
        removida = (not FotoExcursao.objects.filter(pk=primeira.pk).exists()
                    and not existe_no_drive(primeira.drive_id))
        registro("Remoção pela agência dona apaga banco e Drive", removida,
                 f"removida do banco e do Drive: {removida}")
        removidas_app = 1
        r = Client().get(f"/fotos/{primeira.pk}/imagem/")
        registro("Foto removida deixa de ser servida", r.status_code == 404, f"HTTP {r.status_code}")
    # Limpeza do restante (mesmo em falha): Drive primeiro, depois banco.
    orfaos = 0
    for foto in fotos[removidas_app:]:
        try:
            drive_fotos.excluir(foto.drive_id)
        except drive_fotos.FalhaDrive:
            orfaos += 1
    FotoExcursao.objects.filter(excursao__titulo__startswith=prefixo).delete()
    Excursao.objects.filter(titulo__startswith=prefixo).delete()
    User.objects.filter(username__startswith=prefixo).delete()
    Agencia.objects.filter(nome__startswith=prefixo).delete()
    registro("Limpeza do ensaio (Drive e banco)", orfaos == 0, f"arquivos não removidos: {orfaos}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--fase", choices=["reinicio"], help=argparse.SUPPRESS)
    parser.add_argument("--estado", help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.fase == "reinicio":  # processo filho
        iniciar_django()
        registro = Registro()
        fase_reinicio(Path(args.estado), registro)
        print("JSON:" + json.dumps(registro.itens, ensure_ascii=False))
        return 0

    grupo = carregar_credenciais()
    conexao = iniciar_django()
    with conexao.cursor() as cur:
        cur.execute("select current_database()" if conexao.vendor == "postgresql" else "select 'sqlite'")
        banco = cur.fetchone()[0]
    if banco in {"sire_demo"}:
        raise SystemExit("Banco da demonstração detectado; ensaio cancelado.")
    print(f"Credenciais do grupo {grupo} carregadas em memória. Banco local: {banco}.")

    prefixo = "ensaio_drive_" + secrets.token_hex(3)
    pasta = BASE_DIR / "evidencias" / (datetime.now().strftime("%Y-%m-%d_%H%M") + "_drive_real")
    pasta.mkdir(parents=True, exist_ok=True)
    estado = pasta / "estado-sem-segredos.json"
    registro = Registro()
    try:
        if fase_preparar(prefixo, estado, registro):
            filho = subprocess.run(
                [sys.executable, "-X", "utf8", __file__, "--fase", "reinicio", "--estado", str(estado)],
                cwd=BASE_DIR, capture_output=True, text=True, encoding="utf-8", timeout=180,
                env=os.environ.copy(),  # credenciais só no ambiente do processo filho
            )
            linhas = [l for l in filho.stdout.splitlines() if l.startswith("JSON:")]
            if linhas:
                for item in json.loads(linhas[-1][5:]):
                    registro(item["verificacao"], item["conforme"], item["obtido"])
            else:
                registro("Persistência após reinício (processo novo, cache vazio)", False,
                         f"processo filho terminou com código {filho.returncode}")
    finally:
        fase_remover(prefixo, registro)
        estado.unlink(missing_ok=True)
        for chave in CHAVES:
            os.environ.pop(chave, None)

    from django.conf import settings
    import django

    evidencia = {
        "executado_em": datetime.now().astimezone().isoformat(timespec="seconds"),
        "ambiente": {
            "local": "computador da autora (Windows)", "banco": banco,
            "python": sys.version.split()[0], "django": django.get_version(),
            "escopo_oauth": "https://www.googleapis.com/auth/drive.file",
            "grupo_render": grupo, "demo_publica_alterada": False,
        },
        "imagem": "sintética, gerada pelo script (faixas coloridas e texto)",
        "verificacoes": registro.itens,
        "resultado": "TODOS CONFORMES" if registro.tudo_ok else "HÁ FALHAS",
    }
    (pasta / "resultados.json").write_text(json.dumps(evidencia, ensure_ascii=False, indent=2), encoding="utf-8")
    print("RESULTADO:", evidencia["resultado"])
    print("Evidência:", pasta / "resultados.json")
    return 0 if registro.tudo_ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except HTTPError as erro:
        raise SystemExit(f"Falha HTTP {erro.code} ao consultar o Render. Nenhum segredo foi exibido.") from None
    except KeyboardInterrupt:
        raise SystemExit("Cancelado.") from None
