"""Gera o refresh token OAuth para a conta Google dona das fotos do SIRE.

Execução local, apenas pelo responsável técnico; não envia credenciais ao Git.
Requer cliente OAuth do tipo Aplicativo para computador no Google Cloud.
"""
import base64
import hashlib
import json
import os
import secrets
import re
import time
import warnings
from getpass import getpass, GetPassWarning
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen


SCOPE = "https://www.googleapis.com/auth/drive.file"
PORT = 8766
REDIRECT = f"http://127.0.0.1:{PORT}/oauth/callback"


def segredo(nome):
    """Não usar fallback de getpass que possa ecoar a entrada."""
    valor = os.environ.get(nome, "")
    if valor:
        return valor
    with warnings.catch_warnings():
        warnings.simplefilter("error", GetPassWarning)
        return getpass(f"{nome} (entrada oculta): ")


def validar_tokens(tokens):
    if not isinstance(tokens, dict) or not tokens.get("refresh_token"):
        raise ValueError("Autorização sem refresh token; nenhuma credencial enviada ao Render.")
    if set(tokens.get("scope", "").split()) != {SCOPE}:
        raise ValueError("Escopo concedido diferente de drive.file; operação interrompida.")


def enviar_render(service_id, api_key, credenciais):
    """Altera somente três chaves; não consulta nem substitui os demais segredos.

    O ID deve pertencer a um serviço de ensaio, nunca à demonstração pública.
    Respostas e exceções do provedor não são impressas.
    """
    if not re.fullmatch(r"srv-[a-z0-9]+", service_id):
        raise ValueError("ID de serviço de ensaio inválido.")
    base = f"https://api.render.com/v1/services/{service_id}"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    with urlopen(Request(base, headers=headers), timeout=20) as resposta:
        servico = json.load(resposta)
    # Defesa adicional: nenhum destino público atual pode receber esta configuração.
    if (servico.get("name") == "sire-demo"
            or servico.get("branch") in {"main", "etapa/postgresql-windows"}
            or servico.get("serviceDetails", {}).get("url", "").rstrip("/")
            == "https://sire-demo.onrender.com"):
        raise ValueError("A versão pública está protegida; use um serviço de ensaio isolado.")
    if not servico.get("name", "").startswith("sire-oauth-test"):
        raise ValueError("O serviço de ensaio deve ter nome iniciado por sire-oauth-test.")
    for chave, valor in credenciais.items():
        requisicao = Request(
            f"{base}/env-vars/{chave}", method="PUT", headers=headers,
            data=json.dumps({"value": valor}).encode(),
        )
        with urlopen(requisicao, timeout=20) as resposta:
            resposta.read()  # Pode conter segredo; nunca imprimir ou gravar.


def main():
    client_id = segredo("SIRE_DRIVE_CLIENT_ID")
    client_secret = segredo("SIRE_DRIVE_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise SystemExit("Defina SIRE_DRIVE_CLIENT_ID e SIRE_DRIVE_CLIENT_SECRET antes de executar.")

    service_id = os.environ.get("SIRE_DRIVE_RENDER_SERVICE_ID", "")
    if not re.fullmatch(r"srv-[a-z0-9]+", service_id):
        raise SystemExit("Defina SIRE_DRIVE_RENDER_SERVICE_ID para o serviço de ensaio isolado.")
    api_key = segredo("RENDER_API_KEY")
    if not api_key:
        raise SystemExit("Credencial do Render ausente.")

    state = secrets.token_urlsafe(24)
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
    dados = {"code": None, "error": None}

    class Callback(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            return  # Não registrar o código de autorização em logs.

        def do_GET(self):
            query = urlparse(self.path)
            params = parse_qs(query.query)
            if query.path != "/oauth/callback" or params.get("state", []) != [state]:
                self.send_error(400, "Retorno inválido")
                return
            if len(params.get("code", [])) > 1 or len(params.get("error", [])) > 1:
                self.send_error(400)
                return
            dados["code"] = params.get("code", [None])[0]
            dados["error"] = params.get("error", [None])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Referrer-Policy", "no-referrer")
            self.end_headers()
            self.wfile.write(b"<h2>Autorizacao concluida. Volte ao terminal do SIRE.</h2>")

    parametros = {
        "client_id": client_id, "redirect_uri": REDIRECT, "response_type": "code",
        "scope": SCOPE, "access_type": "offline", "prompt": "consent",
        "state": state, "code_challenge": challenge, "code_challenge_method": "S256",
    }
    endereco = "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode(parametros)
    with HTTPServer(("127.0.0.1", PORT), Callback) as servidor:
        servidor.timeout = 180
        print("Autorize somente a conta Google que guardará as fotos do SIRE.")
        if not webbrowser.open(endereco):
            raise SystemExit("Não foi possível abrir o navegador local; autorização interrompida.")
        prazo = time.monotonic() + 180
        while not dados["code"] and not dados["error"] and time.monotonic() < prazo:
            servidor.timeout = max(0.1, prazo - time.monotonic())
            servidor.handle_request()
    if not dados["code"] or dados["error"]:
        raise SystemExit("Autorização não concluída. Verifique a conta e tente novamente.")
    requisicao = Request(
        "https://oauth2.googleapis.com/token",
        data=urlencode({
            "code": dados["code"], "client_id": client_id, "client_secret": client_secret,
            "redirect_uri": REDIRECT, "grant_type": "authorization_code",
            "code_verifier": verifier,
        }).encode(),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urlopen(requisicao, timeout=20) as resposta:
        tokens = json.load(resposta)
    validar_tokens(tokens)
    enviar_render(service_id, api_key, {
        "SIRE_DRIVE_CLIENT_ID": client_id,
        "SIRE_DRIVE_CLIENT_SECRET": client_secret,
        "SIRE_DRIVE_REFRESH_TOKEN": tokens["refresh_token"],
    })
    print("Credenciais encaminhadas ao ambiente de ensaio do Render, sem exibir valores.")
    print("Nenhum deploy solicitado. Testes reais e revisão ainda são necessários.")


if __name__ == "__main__":
    try:
        main()
    except (Exception, KeyboardInterrupt):
        raise SystemExit("Fluxo interrompido com segurança. Configuração pode estar parcial; confira as chaves no Render sem revelar valores.") from None
