"""Gera o refresh token OAuth para a conta Google dona das fotos do SIRE.

Execução local, apenas pelo responsável técnico; não envia credenciais ao Git.
Requer cliente OAuth do tipo Aplicativo para computador no Google Cloud.
"""
import argparse
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
from urllib.error import HTTPError


SCOPE = "https://www.googleapis.com/auth/drive.file"
PORT = 8766
REDIRECT = f"http://127.0.0.1:{PORT}/oauth/callback"


# Formato esperado de cada segredo: confere se o valor colado é o certo
# (por exemplo, o NOME da chave no lugar da chave) sem nunca exibi-lo.
FORMATOS = {
    "RENDER_API_KEY": (r"rnd_[A-Za-z0-9]{16,}", "a chave do Render começa com rnd_"),
    "SIRE_DRIVE_CLIENT_ID": (
        r"[0-9]+-[a-z0-9]+\.apps\.googleusercontent\.com",
        "o ID do cliente termina com .apps.googleusercontent.com",
    ),
    "SIRE_DRIVE_CLIENT_SECRET": (r"GOCSPX-[A-Za-z0-9_-]{10,}", "a chave secreta começa com GOCSPX-"),
}
DESCRICOES = {
    "RENDER_API_KEY": "Chave de API do Render (começa com rnd_)",
    "SIRE_DRIVE_CLIENT_ID": "ID do cliente OAuth do Google (termina com .apps.googleusercontent.com)",
    "SIRE_DRIVE_CLIENT_SECRET": "Chave secreta do cliente OAuth do Google (começa com GOCSPX-)",
}
USAR_JANELA = [False]  # ligado por main(); os testes usam só o terminal


def _janela_segredo(nome):
    """Campo mascarado (•) em uma janela local: a pessoa vê que colou algo,
    e quantos caracteres, sem que o valor apareça na tela, no terminal ou em logs."""
    import tkinter as tk

    resultado = {"valor": None}
    raiz = tk.Tk()
    raiz.title("SIRE — " + nome)
    raiz.attributes("-topmost", True)
    raiz.resizable(False, False)
    tk.Label(raiz, text=DESCRICOES.get(nome, nome), font=("Segoe UI", 11, "bold"),
             padx=16, pady=(12)).pack(anchor="w")
    tk.Label(raiz, text="Cole com Ctrl+V. O valor fica oculto (•••).",
             padx=16).pack(anchor="w")
    campo = tk.Entry(raiz, show="•", width=52, font=("Consolas", 12))
    campo.pack(padx=16, pady=8)
    aviso = tk.Label(raiz, text="0 caracteres", fg="#684957", padx=16)
    aviso.pack(anchor="w")

    def mudou(_evento=None):
        aviso.config(text=f"{len(campo.get().strip())} caracteres", fg="#684957")

    def confirmar(_evento=None):
        valor = campo.get().strip()
        padrao, dica = FORMATOS.get(nome, (r".+", ""))
        if not re.fullmatch(padrao, valor):
            aviso.config(text="Formato inesperado: " + dica + ". Confira e cole de novo.",
                         fg="#9d2424")
            campo.delete(0, "end")
            return
        resultado["valor"] = valor
        raiz.destroy()

    campo.bind("<KeyRelease>", mudou)
    campo.bind("<Return>", confirmar)
    tk.Button(raiz, text="Confirmar", command=confirmar, padx=12).pack(pady=(4, 14))
    raiz.protocol("WM_DELETE_WINDOW", raiz.destroy)
    raiz.after(200, lambda: (raiz.lift(), raiz.focus_force(), campo.focus_set()))
    raiz.mainloop()
    if not resultado["valor"]:
        raise KeyboardInterrupt
    return resultado["valor"]


def segredo(nome):
    """Não usar fallback de getpass que possa ecoar a entrada."""
    valor = os.environ.get(nome, "")
    if valor:
        return valor
    if USAR_JANELA[0]:
        try:
            print(f"Abrindo janela para {nome}...")
            return _janela_segredo(nome)
        except ImportError:
            pass  # sem interface gráfica: segue para a entrada oculta do terminal
    with warnings.catch_warnings():
        warnings.simplefilter("error", GetPassWarning)
        valor = getpass(f"{nome} (entrada oculta): ").strip()
    padrao, dica = FORMATOS.get(nome, (r".+", ""))
    if valor and not re.fullmatch(padrao, valor):
        raise ValueError(f"O valor de {nome} não tem o formato esperado ({dica}).")
    return valor


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


CHAVES_DRIVE = {"SIRE_DRIVE_CLIENT_ID", "SIRE_DRIVE_CLIENT_SECRET", "SIRE_DRIVE_REFRESH_TOKEN"}


def conferir_workspace(owner_id, api_key):
    if not re.fullmatch(r"tea-[a-z0-9]+", owner_id):
        raise ValueError("Identificador do workspace inválido.")
    req = Request(f"https://api.render.com/v1/owners/{owner_id}",
                  headers={"Authorization": f"Bearer {api_key}"})
    with urlopen(req, timeout=20) as resposta:
        workspace = json.load(resposta)
    if workspace.get("id") != owner_id or workspace.get("name") != "SIRE.":
        raise ValueError("O workspace não corresponde ao SIRE confirmado.")


def enviar_grupo_render(owner_id, api_key, credenciais):
    """Cria grupo novo sem vínculo; não altera serviço, banco ou deploy."""
    if set(credenciais) != CHAVES_DRIVE or not all(credenciais.values()):
        raise ValueError("Conjunto de credenciais incompleto.")
    conferir_workspace(owner_id, api_key)
    nome = "sire-drive-oauth-" + secrets.token_hex(4)
    req = Request("https://api.render.com/v1/env-groups", method="POST",
                  headers={"Authorization": f"Bearer {api_key}",
                           "Content-Type": "application/json"},
                  data=json.dumps({
                      "name": nome, "ownerId": owner_id,
                      "envVars": [{"key": k, "value": v} for k, v in credenciais.items()],
                      "serviceIds": [], "secretFiles": [],
                  }).encode())
    with urlopen(req, timeout=20) as resposta:
        if resposta.status != 201:
            raise ValueError("Render não confirmou a criação do grupo.")
        # A resposta pode conter segredos. Não imprimir nem gravar.
        corpo = resposta.read()
    try:
        criado = json.loads(corpo) if corpo else {}
    except ValueError:
        criado = {}
    if criado.get("serviceLinks"):
        raise ValueError("O grupo foi criado vinculado a um serviço; verifique o painel.")
    return nome


PREFIXO_GRUPO = "sire-drive-oauth-"


def _listar_grupos(owner_id, api_key):
    """Lista os grupos do workspace (somente nomes, IDs e vínculos)."""
    req = Request(
        "https://api.render.com/v1/env-groups?" + urlencode({"ownerId": owner_id, "limit": "100"}),
        headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
    )
    with urlopen(req, timeout=20) as resposta:
        itens = json.load(resposta)
    grupos = []
    for item in itens if isinstance(itens, list) else []:
        grupo = item.get("envGroup", item) if isinstance(item, dict) else {}
        grupos.append({
            "id": grupo.get("id", ""),
            "name": grupo.get("name", ""),
            "serviceLinks": grupo.get("serviceLinks") or [],
        })
    return grupos


def grupos_drive_existentes(owner_id, api_key):
    """Nomes dos grupos de credenciais do Drive já criados (evita duplicatas)."""
    return [g["name"] for g in _listar_grupos(owner_id, api_key)
            if g["name"].startswith(PREFIXO_GRUPO)]


def conferir_grupo(owner_id, api_key, nome):
    """Relê o grupo criado e confere chaves e vínculos sem expor valores.

    Devolve o ID (não secreto). Os valores das variáveis são descartados.
    """
    candidatos = [g for g in _listar_grupos(owner_id, api_key) if g["name"] == nome]
    if len(candidatos) != 1:
        raise ValueError("O grupo criado não foi encontrado de forma única no Render.")
    grupo_id = candidatos[0]["id"]
    if not re.fullmatch(r"evg-[a-z0-9]+", grupo_id):
        raise ValueError("Identificador de grupo inesperado.")
    req = Request(f"https://api.render.com/v1/env-groups/{grupo_id}",
                  headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"})
    with urlopen(req, timeout=20) as resposta:
        grupo = json.load(resposta)
    chaves = {v.get("key") for v in grupo.get("envVars") or []}
    vazias = [v.get("key") for v in grupo.get("envVars") or [] if not v.get("value")]
    grupo.clear()  # descarta os valores lidos
    if grupo_id and chaves and chaves != CHAVES_DRIVE:
        raise ValueError("O grupo não contém exatamente as três chaves do Drive.")
    if vazias:
        raise ValueError("Há chave sem valor no grupo criado.")
    if candidatos[0]["serviceLinks"]:
        raise ValueError("O grupo está vinculado a um serviço; desvincule no painel.")
    return grupo_id, bool(chaves)


def main():
    parser = argparse.ArgumentParser(description="Autorizar Drive e guardar credenciais no Render sem exibi-las.")
    parser.add_argument("--grupo-render", metavar="WORKSPACE_ID",
                        help="Criar grupo separado, sem vincular a nenhum serviço.")
    parser.add_argument("--permitir-novo-grupo", action="store_true",
                        help="Criar outro grupo mesmo que já exista um sire-drive-oauth-*.")
    parser.add_argument("--sem-janela", action="store_true",
                        help="Pedir os segredos no terminal em vez de janela mascarada.")
    args = parser.parse_args()
    USAR_JANELA[0] = not args.sem_janela
    service_id = ""
    ETAPA[0] = "1/3 (Render)"
    print("Etapa 1/3: validar o destino seguro no Render.")
    if not args.grupo_render:
        service_id = os.environ.get("SIRE_DRIVE_RENDER_SERVICE_ID", "")
        if not re.fullmatch(r"srv-[a-z0-9]+", service_id):
            raise SystemExit("Defina SIRE_DRIVE_RENDER_SERVICE_ID ou use --grupo-render WORKSPACE_ID.")
    api_key = segredo("RENDER_API_KEY")
    if not api_key:
        raise SystemExit("Credencial do Render ausente.")
    if args.grupo_render:
        conferir_workspace(args.grupo_render, api_key)
        existentes = grupos_drive_existentes(args.grupo_render, api_key)
        if existentes and not args.permitir_novo_grupo:
            raise SystemExit(
                "Já existe grupo de credenciais do Drive no Render: "
                + ", ".join(existentes)
                + ". Nada foi alterado. Confira no painel antes de repetir; para criar "
                "outro mesmo assim, use --permitir-novo-grupo."
            )
        print("Workspace SIRE. confirmado; nenhum grupo anterior do Drive encontrado.")
    ETAPA[0] = "2/3 (Google)"
    print("Etapa 2/3: informar o cliente OAuth e autorizar no Google.")

    client_id = segredo("SIRE_DRIVE_CLIENT_ID")
    client_secret = segredo("SIRE_DRIVE_CLIENT_SECRET")
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
    credenciais = {
        "SIRE_DRIVE_CLIENT_ID": client_id,
        "SIRE_DRIVE_CLIENT_SECRET": client_secret,
        "SIRE_DRIVE_REFRESH_TOKEN": tokens["refresh_token"],
    }
    ETAPA[0] = "3/3 (gravação no Render)"
    print("Autorização do Google recebida com escopo drive.file.")
    print("Etapa 3/3: guardar credenciais no Render sem exibir valores.")
    if args.grupo_render:
        nome = enviar_grupo_render(args.grupo_render, api_key, credenciais)
        credenciais.clear()
        ETAPA[0] = "3/3 (conferência do grupo)"
        grupo_id, chaves_lidas = conferir_grupo(args.grupo_render, api_key, nome)
        print("CONCLUIDO: grupo criado no Render: " + nome + " (" + grupo_id + ")")
        if chaves_lidas:
            print("Conferido: exatamente 3 chaves preenchidas e nenhum serviço vinculado.")
        else:
            print("Conferido: grupo existe e não tem serviço vinculado; a chave do Render "
                  "não permitiu ler a lista de variáveis.")
        print("A demonstração pública não foi alterada.")
    else:
        enviar_render(service_id, api_key, credenciais)
        print("CONCLUIDO: credenciais encaminhadas ao serviço de ensaio do Render.")
    print("Nenhum deploy solicitado. Testes reais e revisão ainda são necessários.")



ETAPA = ["inicial"]


if __name__ == "__main__":
    try:
        main()
    except HTTPError as erro:
        raise SystemExit(
            f"Falha HTTP {erro.code} na etapa {ETAPA[0]}. Nenhum segredo foi exibido. "
            "Informe somente esta linha."
        ) from None
    except ValueError as erro:
        # Mensagens de ValueError deste script são escritas aqui e não contêm segredos.
        raise SystemExit(f"Interrompido na etapa {ETAPA[0]}: {erro}") from None
    except KeyboardInterrupt:
        raise SystemExit(f"Cancelado na etapa {ETAPA[0]}. Nada mais foi enviado.") from None
    except Exception as erro:
        # Apenas o tipo do erro: a mensagem de bibliotecas pode conter dados sensíveis.
        raise SystemExit(
            f"Fluxo interrompido na etapa {ETAPA[0]} ({type(erro).__name__}). "
            "Nenhum segredo foi exibido. Se a etapa for 3/3, confira o painel do Render "
            "antes de repetir."
        ) from None
