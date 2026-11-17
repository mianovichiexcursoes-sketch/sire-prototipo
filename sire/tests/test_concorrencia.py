"""Reservas simultâneas: a capacidade não pode ser excedida (RN de disponibilidade).

Roda só no PostgreSQL, onde o bloqueio de linha (SELECT ... FOR UPDATE) é o
mecanismo em teste. No SQLite a serialização vem do modo IMMEDIATE e é
conferida por scripts/teste_concorrencia.py com um servidor real.
"""

import threading
from unittest import skipUnless

from django.db import connection, connections
from django.test import Client, TransactionTestCase

from sire.models import Reserva

from .base import AJUSTES, SENHA, criar_agencia, criar_excursao, criar_passageiro

RODADAS = 5


@skipUnless(connection.vendor == "postgresql", "exige PostgreSQL (bloqueio de linha)")
@AJUSTES
class ReservasSimultaneas(TransactionTestCase):
    def disputar(self, excursao, ponto, passageiros):
        """Dispara as reservas ao mesmo tempo e devolve as respostas."""
        clientes = []
        for passageiro in passageiros:
            cliente = Client()
            cliente.login(username=passageiro.username, password=SENHA)
            clientes.append(cliente)

        barreira = threading.Barrier(len(clientes))
        respostas = [None] * len(clientes)

        def tentar(indice, cliente):
            try:
                barreira.wait()
                respostas[indice] = cliente.post(
                    f"/excursao/{excursao.pk}/reservar/", {"ponto_embarque": ponto.pk}
                )
            finally:
                connections.close_all()

        tarefas = [
            threading.Thread(target=tentar, args=(i, c)) for i, c in enumerate(clientes)
        ]
        for tarefa in tarefas:
            tarefa.start()
        for tarefa in tarefas:
            tarefa.join()
        return respostas

    def conferir(self, capacidade, previas, disputantes):
        agencia = criar_agencia()
        passageiros = [criar_passageiro(f"p{i}") for i in range(previas + disputantes)]
        vagas = capacidade - previas
        for rodada in range(RODADAS):
            with self.subTest(rodada=rodada + 1):
                excursao, ponto = criar_excursao(agencia, f"Rodada {rodada}", capacidade)
                for passageiro in passageiros[:previas]:
                    Reserva.objects.create(
                        passageiro=passageiro, excursao=excursao, ponto_embarque=ponto
                    )
                respostas = self.disputar(excursao, ponto, passageiros[previas:])

                confirmadas = sum(r.status_code == 302 for r in respostas)
                recusadas = sum(
                    r.status_code == 200 and "Não há vagas" in r.content.decode()
                    for r in respostas
                )
                gravadas = Reserva.objects.filter(excursao=excursao).count()
                self.assertLessEqual(gravadas, capacidade, "capacidade excedida")
                self.assertEqual(gravadas, capacidade)
                self.assertEqual(confirmadas, vagas)
                self.assertEqual(recusadas, disputantes - vagas)

    def test_a_dois_passageiros_disputam_a_ultima_vaga(self):
        self.conferir(capacidade=2, previas=1, disputantes=2)

    def test_b_dez_passageiros_disputam_tres_vagas(self):
        self.conferir(capacidade=3, previas=0, disputantes=10)
