"""Carregador do portfólio: cria, publica, não duplica e não mexe no que existe."""

import json
from datetime import date
from io import StringIO
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase, override_settings

from sire import drive_fotos
from sire.management.commands.carregar_portfolio import DADOS
from sire.models import Agencia, Excursao, FotoExcursao, PerfilUsuario, StatusExcursao

ITENS = json.loads(DADOS.read_text(encoding="utf-8"))
DRIVE = dict(
    SIRE_DRIVE_CLIENT_ID="ficticio",
    SIRE_DRIVE_CLIENT_SECRET="ficticio",
    SIRE_DRIVE_REFRESH_TOKEN="ficticio",
)


def rodar():
    saida = StringIO()
    call_command("carregar_portfolio", stdout=saida)
    return saida.getvalue()


class CarregarPortfolio(TestCase):
    def test_tres_agencias_com_agente_e_excursoes_publicadas(self):
        rodar()
        futuras = [i for i in ITENS["excursoes"] if date.fromisoformat(i["saida"]) >= date.today()]
        self.assertEqual(Agencia.objects.count(), 3)
        self.assertEqual(PerfilUsuario.objects.filter(tipo="AGENTE").count(), 3)
        self.assertEqual(Excursao.objects.count(), len(futuras))
        self.assertFalse(Excursao.objects.exclude(status=StatusExcursao.PUBLICADA).exists())
        for excursao in Excursao.objects.all():
            with self.subTest(excursao.titulo):
                self.assertTrue(excursao.pontos_embarque.exists())
                self.assertTrue(excursao.descricao and excursao.inclusos and excursao.roteiro)

    def test_segunda_execucao_nao_duplica_nem_altera(self):
        rodar()
        primeira = Excursao.objects.order_by("id").first()
        primeira.valor = 1
        primeira.save()
        total = Excursao.objects.count()
        rodar()
        self.assertEqual(Excursao.objects.count(), total)
        primeira.refresh_from_db()
        self.assertEqual(primeira.valor, 1)

    def test_fotos_existem_no_repositorio(self):
        pasta = DADOS.parent / "fotos"
        for item in ITENS["excursoes"]:
            for nome in item["fotos"]:
                with self.subTest(nome):
                    self.assertTrue((pasta / nome).is_file())

    @override_settings(**DRIVE)
    def test_envia_fotos_uma_vez_quando_drive_configurado(self):
        ids = iter(f"id{n}" for n in range(1000))
        with patch.object(drive_fotos, "enviar", side_effect=lambda *_: next(ids)) as enviar:
            rodar()
            esperadas = sum(len(i["fotos"]) for i in ITENS["excursoes"]
                            if date.fromisoformat(i["saida"]) >= date.today())
            self.assertEqual(FotoExcursao.objects.count(), esperadas)
            rodar()
            self.assertEqual(enviar.call_count, esperadas)

    def test_sem_drive_carrega_sem_fotos(self):
        texto = rodar()
        self.assertEqual(FotoExcursao.objects.count(), 0)
        self.assertIn("0 fotos enviadas", texto)
