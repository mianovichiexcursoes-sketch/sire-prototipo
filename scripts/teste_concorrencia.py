"""Ensaio de reservas simultâneas e reexecução dos VF afetados, por HTTP real.

Sobe um servidor Django local, autentica usuários fictícios e dispara os POSTs
de reserva ao mesmo tempo (threading.Barrier). Depois de cada rodada compara as
respostas HTTP com as reservas gravadas no banco. Usa o banco do ambiente/.env.

Uso (na pasta do manage.py, com a venv):
    python scripts/teste_concorrencia.py
    python scripts/teste_concorrencia.py --rodadas 5 --porta 8013

Teste A — 2 passageiros distintos disputam 1 vaga: 1 persistida, 1 recusa.
Teste B — 10 passageiros distintos disputam 3 vagas: 3 persistidas, 7 recusas.
Teste C — o mesmo passageiro, em 2 sessões, com 5 vagas: sem erro e sem exceder
          a capacidade. A baseline ER-SIRE 2.1 não limita a uma reserva por
          passageiro por excursão; portanto o esperado são 2 reservas.
Verificações funcionais: VF10, VF11, VF12, VF13, UC07-E3 e autorização.

Os dados criados usam um prefixo único e são removidos ao final. Senhas são
aleatórias e não são gravadas em arquivo.
"""

import argparse
import json
import os
import re
import secrets
import socket
import subprocess
import sys
import threading
import time
from datetime import date, datetime, time as hora, timedelta
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sire_project.settings")

import django  # noqa: E402

django.setup()

from django.contrib.auth.models import User  # noqa: E402
from django.db import connection  # noqa: E402
from django.db.models import Count  # noqa: E402

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

    def _enviar(self, req):
        try:
            with self.abrir.open(req, timeout=60) as resp:
                return resp.status, resp.geturl(), resp.read().decode("utf-8")
        except HTTPError as erro:  # 403, 404 e 500 também são respostas a registrar
            return erro.code, erro.url, erro.read().decode("utf-8", "replace")

    def get(self, caminho):
        return self._enviar(Request(self.base + caminho))

    def post(self, caminho, dados):
        corpo = urlencode({**dados, "csrfmiddlewaretoken": self._csrf()}).encode()
        req = Request(self.base + caminho, data=corpo)
        req.add_header("Referer", self.base + caminho)
        return self._enviar(req)


def esperar_porta(porta, limite=40):
    fim = time.time() + limite
    while time.time() < fim:
        with socket.socket() as s:
            s.settimeout(0.5)
            if s.connect_ex(("127.0.0.1", porta)) == 0:
                return
        time.sleep(0.3)
    raise RuntimeError("O servidor Django não respondeu na porta %d." % porta)


def entrar(base, usuario, senha):
    sessao = Sessao(base)
    sessao.get("/login/")
    _, url, _ = sessao.post("/login/", {"username": usuario, "password": senha})
    assert "/login" not in url, f"login de {usuario} falhou"
    return sessao


def criar_excursao(agencia, prefixo, nome, capacidade, status=StatusExcursao.PUBLICADA):
    excursao = Excursao.objects.create(
        titulo=f"{prefixo} {nome}",
        destino="Destino fictício",
        data_saida=date.today() + timedelta(days=30),
        valor=100,
        capacidade=capacidade,
        status=status,
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


def classificar(http, url_final, corpo):
    if http == 200 and url_final.rstrip("/").endswith("minhas-reservas"):
        return "RESERVA_GRAVADA"
    if http == 200 and MSG_LOTADA in corpo:
        return "RECUSADA_LOTACAO"
    if http == 200 and MSG_OCUPADO in corpo:
        return "RECUSADA_BANCO_OCUPADO"
    return f"OUTRO_HTTP_{http}"


def disputar(participantes, excursao, ponto):
    """Dispara os POSTs juntos e devolve o que cada sessão observou."""
    barreira = threading.Barrier(len(participantes))
    saida = [None] * len(participantes)

    def tentar(i, usuario, sessao):
        barreira.wait()
        inicio = time.perf_counter()
        try:
            http, url, corpo = reservar(sessao, excursao, ponto)
            resultado = classificar(http, url, corpo)
        except Exception as erro:  # registrado como evidência, não escondido
            http, resultado = None, f"ERRO: {erro!r}"
        saida[i] = {
            "passageiro": usuario,
            "http": http,
            "resultado": resultado,
            "inicio_ms": inicio * 1000,
            "fim_ms": time.perf_counter() * 1000,
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


def rodada(teste, n, agencia, prefixo, capacidade, previas, participantes):
    """Uma rodada: reservas prévias sequenciais e depois a disputa simultânea."""
    excursao, ponto = criar_excursao(agencia, prefixo, f"{teste} {n}", capacidade)
    for _, sessao in previas:
        http, url, corpo = reservar(sessao, excursao, ponto)
        assert classificar(http, url, corpo) == "RESERVA_GRAVADA", "prévia falhou"
    vagas_ini = capacidade - len(previas)
    esperadas = min(vagas_ini, len(participantes))

    tentativas = disputar(participantes, excursao, ponto)

    persistidas = Reserva.objects.filter(excursao=excursao).count()
    confirmadas = sum(t["resultado"] == "RESERVA_GRAVADA" for t in tentativas)
    recusas = sum(t["resultado"] == "RECUSADA_LOTACAO" for t in tentativas)
    erros = len(tentativas) - confirmadas - recusas
    repetidas = (
        Reserva.objects.filter(excursao=excursao)
        .values("passageiro")
        .annotate(q=Count("id"))
        .filter(q__gt=1)
    )
    conforme = (
        erros == 0
        and persistidas <= capacidade
        and confirmadas == esperadas
        and recusas == len(participantes) - esperadas
        and persistidas == len(previas) + confirmadas
    )
    return {
        "teste": teste,
        "rodada": n,
        "capacidade": capacidade,
        "reservas_previas": len(previas),
        "sessoes_simultaneas": len(participantes),
        "vagas_inicio": vagas_ini,
        "vagas_fim": capacidade - persistidas,
        "confirmacoes_http": confirmadas,
        "recusas_por_lotacao_http": recusas,
        "persistidas_na_disputa": persistidas - len(previas),
        "reservas_no_banco": persistidas,
        "passageiros_com_mais_de_uma_reserva": sum(r["q"] - 1 for r in repetidas),
        "erros": erros,
        "excedeu_capacidade": persistidas > capacidade,
        "duracao_ms": max(t["fim_ms"] for t in tentativas),
        "conforme": conforme,
        "tentativas": tentativas,
    }


def verificacoes_funcionais(agencia, prefixo, passageiros, s_agente):
    """Reexecuta, no banco em uso, os cenários afetados pela mudança."""
    (u1, s1), (u2, s2) = passageiros[0], passageiros[1]
    itens = []

    def registrar(nome, esperado, obtido, ok):
        itens.append(
            {"verificacao": nome, "esperado": esperado, "obtido": obtido, "conforme": ok}
        )

    exc, ponto = criar_excursao(agencia, prefixo, "VF", 2)
    outra, ponto_outra = criar_excursao(agencia, prefixo, "VF outra", 2)

    # VF11 — reserva confirmada com vínculos corretos
    http, url, corpo = reservar(s1, exc, ponto)
    r = Reserva.objects.filter(excursao=exc).select_related("passageiro").first()
    ok = (
        classificar(http, url, corpo) == "RESERVA_GRAVADA"
        and r is not None
        and r.passageiro.username == u1
        and r.ponto_embarque_id == ponto.pk
    )
    registrar(
        "VF11",
        "Reserva confirmada com vínculos corretos",
        f"http {http}; reservas: {Reserva.objects.filter(excursao=exc).count()}; "
        f"passageiro, excursão e embarque corretos: {ok}",
        ok,
    )

    # VF10 — disponibilidade exibida 2 − 1 = 1
    http, _, corpo = s1.get(f"/excursao/{exc.pk}/")
    m = re.search(r"Vagas disponíveis\s*</dt>\s*<dd>\s*(\d+)", corpo)
    exibida = int(m.group(1)) if m else None
    registrar(
        "VF10",
        "Disponibilidade exibida 2 − 1 = 1",
        f"http {http}; vagas exibidas: {exibida}",
        http == 200 and exibida == 1,
    )

    # VF12 — embarque de outra excursão rejeitado
    antes = Reserva.objects.filter(excursao=exc).count()
    http, url, corpo = reservar(s2, exc, ponto_outra)
    depois = Reserva.objects.filter(excursao=exc).count()
    recusou = classificar(http, url, corpo) != "RESERVA_GRAVADA"
    registrar(
        "VF12",
        "Embarque de outra excursão rejeitado; total inalterado",
        f"http {http}; rejeitado: {recusou}; reservas {antes} → {depois}",
        http == 200 and recusou and antes == depois,
    )

    # VF13 — excursão lotada
    reservar(s2, exc, ponto)  # ocupa a segunda vaga
    antes = Reserva.objects.filter(excursao=exc).count()
    http, url, corpo = reservar(s1, exc, ponto)
    depois = Reserva.objects.filter(excursao=exc).count()
    registrar(
        "VF13",
        "Excursão lotada: mensagem, sem nova reserva, sem HTTP 500",
        f"http {http}; mensagem de lotação: {MSG_LOTADA in corpo}; "
        f"reservas {antes} → {depois} (capacidade 2)",
        http == 200 and MSG_LOTADA in corpo and antes == depois == 2,
    )

    # UC07-E3 — reduzir capacidade abaixo das reservas existentes
    s_agente.get(f"/agente/excursoes/{exc.pk}/editar/")
    http, _, corpo = s_agente.post(
        f"/agente/excursoes/{exc.pk}/editar/",
        {
            "titulo": exc.titulo,
            "destino": exc.destino,
            "data_saida": exc.data_saida.isoformat(),
            "data_retorno": "",
            "valor": "100.00",
            "capacidade": "1",
        },
    )
    exc.refresh_from_db()
    registrar(
        "UC07-E3",
        "Capacidade 2 → 1 com 2 reservas: recusada",
        f"http {http}; capacidade após a tentativa: {exc.capacidade}; "
        f"mensagem de erro: {'Capacidade não pode ser menor' in corpo}",
        http == 200 and exc.capacidade == 2,
    )

    # Autorização da reserva
    http_agente, _, _ = reservar(s_agente, outra, ponto_outra)
    rasc, ponto_rasc = criar_excursao(
        agencia, prefixo, "VF rascunho", 2, StatusExcursao.RASCUNHO
    )
    http_rasc, _, _ = reservar(s1, rasc, ponto_rasc)
    sem_reserva = (
        Reserva.objects.filter(excursao__in=[outra, rasc]).count() == 0
    )
    registrar(
        "Autorização da reserva",
        "Agente: HTTP 403; RASCUNHO: HTTP 404",
        f"agente: HTTP {http_agente}; rascunho: HTTP {http_rasc}; "
        f"nenhuma reserva criada: {sem_reserva}",
        http_agente == 403 and http_rasc == 404 and sem_reserva,
    )
    return itens


def limpar(prefixo):
    Reserva.objects.filter(excursao__titulo__startswith=prefixo).delete()
    Excursao.objects.filter(titulo__startswith=prefixo).delete()
    User.objects.filter(username__startswith=prefixo).delete()
    Agencia.objects.filter(nome__startswith=prefixo).delete()


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--rodadas", type=int, default=5, help="rodadas por teste")
    parser.add_argument("--porta", type=int, default=8013)
    parser.add_argument("--saida", default="", help="arquivo JSON de evidência")
    args = parser.parse_args()

    banco = connection.vendor
    cfg = connection.settings_dict
    with connection.cursor() as cur:
        cur.execute(
            "select version()" if banco == "postgresql" else "select sqlite_version()"
        )
        versao_banco = cur.fetchone()[0]
        isolamento = None
        if banco == "postgresql":
            cur.execute("show transaction_isolation")
            isolamento = cur.fetchone()[0]
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
    rodadas, funcionais = [], []
    try:
        esperar_porta(args.porta)
        agencia = Agencia.objects.create(nome=f"{prefixo} Agência fictícia")

        passageiros, senhas = [], {}
        for i in range(10):
            usuario, senha = f"{prefixo}_p{i:02d}", secrets.token_urlsafe(16)
            conta = User.objects.create_user(username=usuario, password=senha)
            PerfilUsuario.objects.create(usuario=conta, tipo=TipoPerfil.PASSAGEIRO)
            senhas[usuario] = senha
            passageiros.append((usuario, entrar(base, usuario, senha)))

        agente, senha_agente = f"{prefixo}_agente", secrets.token_urlsafe(16)
        conta = User.objects.create_user(username=agente, password=senha_agente)
        PerfilUsuario.objects.create(
            usuario=conta, tipo=TipoPerfil.AGENTE, agencia=agencia
        )
        s_agente = entrar(base, agente, senha_agente)

        # Teste C: o MESMO passageiro em duas sessões (dois navegadores).
        u0 = passageiros[0][0]
        mesmo = [passageiros[0], (u0, entrar(base, u0, senhas[u0]))]

        for n in range(1, args.rodadas + 1):
            rodadas.append(
                rodada("A", n, agencia, prefixo, 2, passageiros[:1], passageiros[1:3])
            )
        for n in range(1, args.rodadas + 1):
            rodadas.append(rodada("B", n, agencia, prefixo, 3, [], passageiros))
        for n in range(1, args.rodadas + 1):
            rodadas.append(rodada("C", n, agencia, prefixo, 5, [], mesmo))

        funcionais = verificacoes_funcionais(agencia, prefixo, passageiros, s_agente)
    finally:
        servidor.terminate()
        servidor.wait(timeout=15)
        limpar(prefixo)

    resumo = {}
    for r in rodadas:
        c = resumo.setdefault(
            r["teste"],
            {
                "rodadas": 0,
                "conformes": 0,
                "vagas_inicio_fim": [],
                "confirmacoes": [],
                "recusas": [],
                "persistidas": [],
                "passageiros_com_mais_de_uma_reserva": [],
                "erros": 0,
                "rodadas_com_excesso": 0,
                "duracao_ms": [],
            },
        )
        c["rodadas"] += 1
        c["conformes"] += r["conforme"]
        c["vagas_inicio_fim"].append(f"{r['vagas_inicio']}→{r['vagas_fim']}")
        c["confirmacoes"].append(r["confirmacoes_http"])
        c["recusas"].append(r["recusas_por_lotacao_http"])
        c["persistidas"].append(r["persistidas_na_disputa"])
        c["passageiros_com_mais_de_uma_reserva"].append(
            r["passageiros_com_mais_de_uma_reserva"]
        )
        c["erros"] += r["erros"]
        c["rodadas_com_excesso"] += r["excedeu_capacidade"]
        c["duracao_ms"].append(round(r["duracao_ms"]))

    evidencia = {
        "executado_em": datetime.now().astimezone().isoformat(timespec="seconds"),
        "ambiente": {
            "sistema": sys.platform,
            "python": sys.version.split()[0],
            "django": django.get_version(),
            "banco": banco,
            "versao_banco": versao_banco,
            "isolamento": isolamento,
            "nome_do_banco": str(cfg.get("NAME")) if banco == "postgresql" else "sqlite",
            "usuario_do_banco": cfg.get("USER") or None,
            "host": cfg.get("HOST") or None,
            "servidor": "manage.py runserver --noreload (multithread)",
        },
        "metodo": (
            "POSTs HTTP reais com sessão e CSRF, liberados juntos por "
            "threading.Barrier; contagem final lida do banco pelo ORM."
        ),
        "resumo": resumo,
        "verificacoes_funcionais": funcionais,
        "rodadas": rodadas,
    }
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(
        json.dumps(evidencia, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"Banco: {banco} — {versao_banco}")
    if banco == "postgresql":
        print(
            f"Conexão: banco {cfg['NAME']}, usuário {cfg['USER']}, "
            f"host {cfg['HOST']}:{cfg['PORT']}, isolamento {isolamento}"
        )
    for nome, c in resumo.items():
        print(
            f"Teste {nome}: {c['conformes']}/{c['rodadas']} conformes | "
            f"vagas {', '.join(c['vagas_inicio_fim'])} | "
            f"confirmações {c['confirmacoes']} | recusas {c['recusas']} | "
            f"persistidas {c['persistidas']} | "
            f"mais de uma reserva do mesmo passageiro {c['passageiros_com_mais_de_uma_reserva']} | "
            f"erros {c['erros']} | excesso {c['rodadas_com_excesso']} | "
            f"duração ms {c['duracao_ms']}"
        )
    for f in funcionais:
        print(
            f"{f['verificacao']}: {'CONFORME' if f['conforme'] else 'NÃO CONFORME'} "
            f"— {f['obtido']}"
        )
    print(f"Evidência: {saida}")
    tudo_ok = all(r["conforme"] for r in rodadas) and all(
        f["conforme"] for f in funcionais
    )
    return 0 if tudo_ok else 1


if __name__ == "__main__":
    sys.exit(main())
