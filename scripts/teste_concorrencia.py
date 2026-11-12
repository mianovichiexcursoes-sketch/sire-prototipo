"""Ensaio de reservas simultâneas do SIRE por HTTP real.

Sobe um servidor Django local, autentica passageiros fictícios e dispara os
POSTs de reserva ao mesmo tempo (threading.Barrier). Depois confere no banco
quantas reservas foram gravadas. Usa o banco configurado no ambiente/.env.

Uso (na pasta do manage.py, com a venv):
    python scripts/teste_concorrencia.py
    python scripts/teste_concorrencia.py --rodadas 20 --porta 8013

Cenário A — última vaga: capacidade 2, uma reserva prévia, dois passageiros
disputam a vaga restante. Esperado: 1 reserva gravada e 1 recusa por lotação.
Cenário B — disputa ampla: capacidade 3, dez passageiros simultâneos.
Esperado: 3 reservas gravadas e 7 recusas por lotação.

Os dados criados usam um prefixo único e são removidos ao final. Senhas são
aleatórias e não são gravadas em arquivo.
"""

import argparse
import json
import os
import secrets
import socket
import subprocess
import sys
import threading
import time
from datetime import date, datetime, time as hora, timedelta
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sire_project.settings")

import django  # noqa: E402

django.setup()

from django.contrib.auth.models import User  # noqa: E402
from django.db import connection  # noqa: E402

from sire.models import (  # noqa: E402
    Agencia,
    Excursao,
    PerfilUsuario,
    PontoEmbarque,
    Reserva,
    StatusExcursao,
    TipoPerfil,
)

MSG_LOTADA = "Não há vagas disponíveis"
MSG_OCUPADO = "O banco está ocupado"


class Sessao:
    """Navegador mínimo: cookies de sessão e token CSRF, como um usuário real."""

    def __init__(self, base):
        self.base = base
        self.cookies = CookieJar()
        self.abrir = build_opener(HTTPCookieProcessor(self.cookies))

    def _csrf(self):
        return next(c.value for c in self.cookies if c.name == "csrftoken")

    def get(self, caminho):
        with self.abrir.open(self.base + caminho, timeout=60) as resp:
            return resp.status, resp.geturl(), resp.read().decode("utf-8")

    def post(self, caminho, dados):
        corpo = urlencode({**dados, "csrfmiddlewaretoken": self._csrf()}).encode()
        req = Request(self.base + caminho, data=corpo)
        req.add_header("Referer", self.base + caminho)
        with self.abrir.open(req, timeout=60) as resp:
            return resp.status, resp.geturl(), resp.read().decode("utf-8")


def esperar_porta(porta, limite=40):
    fim = time.time() + limite
    while time.time() < fim:
        with socket.socket() as s:
            s.settimeout(0.5)
            if s.connect_ex(("127.0.0.1", porta)) == 0:
                return
        time.sleep(0.3)
    raise RuntimeError("O servidor Django não respondeu na porta %d." % porta)


def criar_excursao(agencia, prefixo, nome, capacidade):
    excursao = Excursao.objects.create(
        titulo=f"{prefixo} {nome}",
        destino="Destino fictício",
        data_saida=date.today() + timedelta(days=30),
        valor=100,
        capacidade=capacidade,
        status=StatusExcursao.PUBLICADA,
        agencia=agencia,
    )
    ponto = PontoEmbarque.objects.create(
        local="Terminal fictício", horario=hora(7, 0), excursao=excursao
    )
    return excursao, ponto


def reservar(sessao, excursao, ponto):
    return sessao.post(
        f"/excursao/{excursao.pk}/reservar/", {"ponto_embarque": ponto.pk}
    )


def classificar(url_final, corpo):
    if url_final.rstrip("/").endswith("minhas-reservas"):
        return "RESERVA_GRAVADA"
    if MSG_LOTADA in corpo:
        return "RECUSADA_LOTACAO"
    if MSG_OCUPADO in corpo:
        return "RECUSADA_BANCO_OCUPADO"
    return "OUTRO"


def disputar(participantes, excursao, ponto):
    """Dispara os POSTs juntos e devolve o que cada passageiro observou."""
    barreira = threading.Barrier(len(participantes))
    saida = [None] * len(participantes)

    def tentar(i, usuario, sessao):
        barreira.wait()
        inicio = time.perf_counter()
        try:
            http, url, corpo = reservar(sessao, excursao, ponto)
            resultado = classificar(url, corpo)
        except Exception as erro:  # registrado como evidência, não escondido
            http, resultado = None, f"ERRO: {erro!r}"
        saida[i] = {
            "passageiro": usuario,
            "http": http,
            "resultado": resultado,
            "inicio_ms": round(inicio * 1000, 2),
            "fim_ms": round(time.perf_counter() * 1000, 2),
        }

    threads = [
        threading.Thread(target=tentar, args=(i, u, s))
        for i, (u, s) in enumerate(participantes)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    base = min(r["inicio_ms"] for r in saida)
    for r in saida:
        r["inicio_ms"] = round(r["inicio_ms"] - base, 2)
        r["fim_ms"] = round(r["fim_ms"] - base, 2)
    return saida


def rodada(nome, n, agencia, prefixo, sessoes, capacidade, previas, disputantes):
    excursao, ponto = criar_excursao(agencia, prefixo, f"{nome} {n}", capacidade)
    for usuario, sessao in sessoes[:previas]:
        _, url, corpo = reservar(sessao, excursao, ponto)
        assert classificar(url, corpo) == "RESERVA_GRAVADA", "reserva prévia falhou"
    vagas_antes = capacidade - previas
    tentativas = disputar(
        sessoes[previas : previas + disputantes], excursao, ponto
    )
    gravadas_bd = Reserva.objects.filter(excursao=excursao).count()
    confirmadas = sum(t["resultado"] == "RESERVA_GRAVADA" for t in tentativas)
    lotadas = sum(t["resultado"] == "RECUSADA_LOTACAO" for t in tentativas)
    conforme = (
        gravadas_bd == capacidade
        and confirmadas == vagas_antes
        and lotadas == disputantes - vagas_antes
    )
    return {
        "cenario": nome,
        "rodada": n,
        "capacidade": capacidade,
        "reservas_previas": previas,
        "vagas_antes_da_disputa": vagas_antes,
        "passageiros_simultaneos": disputantes,
        "confirmadas_http": confirmadas,
        "recusadas_por_lotacao_http": lotadas,
        "reservas_no_banco": gravadas_bd,
        "excedeu_capacidade": gravadas_bd > capacidade,
        "conforme": conforme,
        "tentativas": tentativas,
    }


def limpar(prefixo):
    Reserva.objects.filter(excursao__titulo__startswith=prefixo).delete()
    Excursao.objects.filter(titulo__startswith=prefixo).delete()
    User.objects.filter(username__startswith=prefixo).delete()
    Agencia.objects.filter(nome__startswith=prefixo).delete()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--rodadas", type=int, default=20, help="rodadas do cenário A")
    parser.add_argument("--rodadas-b", type=int, default=5, help="rodadas do cenário B")
    parser.add_argument("--porta", type=int, default=8013)
    parser.add_argument("--saida", default="", help="arquivo JSON de evidência")
    args = parser.parse_args()

    banco = connection.vendor
    with connection.cursor() as cur:
        cur.execute(
            "select version()" if banco == "postgresql" else "select sqlite_version()"
        )
        versao_banco = cur.fetchone()[0]
    saida = Path(
        args.saida or BASE_DIR / "docs" / f"resultados-concorrencia-{banco}.json"
    )

    prefixo = "conc_" + secrets.token_hex(3)
    base = f"http://127.0.0.1:{args.porta}"
    servidor = subprocess.Popen(
        [
            sys.executable,
            str(BASE_DIR / "manage.py"),
            "runserver",
            f"127.0.0.1:{args.porta}",
            "--noreload",
        ],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    rodadas = []
    try:
        esperar_porta(args.porta)
        agencia = Agencia.objects.create(nome=f"{prefixo} Agência fictícia")
        sessoes = []
        for i in range(10):
            usuario, senha = f"{prefixo}_p{i:02d}", secrets.token_urlsafe(16)
            conta = User.objects.create_user(username=usuario, password=senha)
            PerfilUsuario.objects.create(usuario=conta, tipo=TipoPerfil.PASSAGEIRO)
            sessao = Sessao(base)
            sessao.get("/login/")
            _, url, _ = sessao.post("/login/", {"username": usuario, "password": senha})
            assert "/login" not in url, "login do passageiro fictício falhou"
            sessoes.append((usuario, sessao))

        for n in range(1, args.rodadas + 1):
            rodadas.append(
                rodada("A-ultima-vaga", n, agencia, prefixo, sessoes, 2, 1, 2)
            )
        for n in range(1, args.rodadas_b + 1):
            rodadas.append(
                rodada("B-disputa-ampla", n, agencia, prefixo, sessoes, 3, 0, 10)
            )
    finally:
        servidor.terminate()
        servidor.wait(timeout=15)
        limpar(prefixo)

    resumo = {}
    for r in rodadas:
        c = resumo.setdefault(
            r["cenario"],
            {"rodadas": 0, "conformes": 0, "rodadas_com_excesso": 0, "outros": 0},
        )
        c["rodadas"] += 1
        c["conformes"] += r["conforme"]
        c["rodadas_com_excesso"] += r["excedeu_capacidade"]
        c["outros"] += sum(
            t["resultado"] not in ("RESERVA_GRAVADA", "RECUSADA_LOTACAO")
            for t in r["tentativas"]
        )

    evidencia = {
        "executado_em": datetime.now().astimezone().isoformat(timespec="seconds"),
        "ambiente": {
            "sistema": sys.platform,
            "python": sys.version.split()[0],
            "django": django.get_version(),
            "banco": banco,
            "versao_banco": versao_banco,
            "servidor": "manage.py runserver --noreload (multithread)",
        },
        "metodo": (
            "POSTs HTTP reais com sessão e CSRF, liberados juntos por "
            "threading.Barrier; contagem final lida do banco pelo ORM."
        ),
        "resumo": resumo,
        "rodadas": rodadas,
    }
    saida.write_text(
        json.dumps(evidencia, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"Banco: {banco} — {versao_banco}")
    for nome, c in resumo.items():
        print(
            f"{nome}: {c['conformes']}/{c['rodadas']} rodadas conformes; "
            f"rodadas com excesso de capacidade: {c['rodadas_com_excesso']}; "
            f"respostas fora do esperado: {c['outros']}"
        )
    print(f"Evidência: {saida}")
    return 0 if all(r["conforme"] for r in rodadas) else 1


if __name__ == "__main__":
    sys.exit(main())
