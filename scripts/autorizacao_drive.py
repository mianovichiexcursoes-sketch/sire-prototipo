"""Gera o refresh token OAuth para a conta Google dona das fotos do SIRE.

Execução local, apenas pelo responsável técnico; não envia credenciais ao Git.
Requer cliente OAuth do tipo Aplicativo para computador no Google Cloud.
"""
import base64
import hashlib
import json
import os
import secrets
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen


SCOPE = "https://www.googleapis.com/auth/drive.file"
PORT = 8766
REDIRECT = f"http://127.0.0.1:{PORT}/oauth/callback"


def main():
    client_id = os.environ.get("SIRE_DRIVE_CLIENT_ID", "")
    client_secret = os.environ.get("SIRE_DRIVE_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        raise SystemExit("Defina SIRE_DRIVE_CLIENT_ID e SIRE_DRIVE_CLIENT_SECRET antes de executar.")

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
            if query.path != "/oauth/callback" or params.get("state", [""])[0] != state:
                self.send_error(400, "Retorno inválido")
                return
            dados["code"] = params.get("code", [None])[0]
            dados["error"] = params.get("error", [None])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
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
        print("Se o navegador não abrir, use a URL abaixo:\n", endereco)
        webbrowser.open(endereco)
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
    if not tokens.get("refresh_token"):
        raise SystemExit("Nenhum refresh token foi fornecido. Revogue a autorização antiga e repita.")
    print("\nCopie somente para Secrets/Environment do Render; nunca para o GitHub:")
    print("SIRE_DRIVE_REFRESH_TOKEN=" + tokens["refresh_token"])
    print("\nMantenha este token confidencial. Não compartilhe prints desta tela.")


if __name__ == "__main__":
    main()
