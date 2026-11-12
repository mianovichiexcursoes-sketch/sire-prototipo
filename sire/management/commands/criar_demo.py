"""Dados fictícios da demonstração para a banca. Pode ser executado várias vezes.

Cria uma agência, um agente, um passageiro e três excursões fictícias. As duas
contas são comuns: sem acesso ao Admin e sem privilégio de superusuário. A senha
vem da variável de ambiente SIRE_DEMO_SENHA e não é gravada em arquivo.
Não acrescenta campos, tabelas ou regras: usa somente os models da baseline.
"""

import os
from datetime import date, time, timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from sire.models import (
    Agencia,
    Excursao,
    PerfilUsuario,
    PontoEmbarque,
    StatusExcursao,
    TipoPerfil,
)

AGENCIA = "Agência Demonstração (fictícia)"
AGENTE = "demo_agente"
PASSAGEIRO = "demo_passageiro"

PUBLICADA, RASCUNHO = StatusExcursao.PUBLICADA, StatusExcursao.RASCUNHO

# título, destino, dias até a saída, valor, capacidade, status
EXCURSOES = [
    ("Praia fictícia — bate e volta", "Litoral Demonstração", 20, "180.00", 40, PUBLICADA),
    ("Serra fictícia — fim de semana", "Serra Demonstração", 35, "420.00", 2, PUBLICADA),
    ("Parque fictício — em preparação", "Parque Demonstração", 50, "250.00", 30, RASCUNHO),
]


class Command(BaseCommand):
    help = "Cria os dados fictícios da demonstração (agência, contas e excursões)."

    @transaction.atomic
    def handle(self, *args, **options):
        senha = os.environ.get("SIRE_DEMO_SENHA", "")
        if not senha:
            self.stdout.write(
                self.style.WARNING(
                    "SIRE_DEMO_SENHA não definida: nenhum dado de demonstração criado."
                )
            )
            return

        agencia, _ = Agencia.objects.get_or_create(nome=AGENCIA)

        for usuario, tipo, nome in (
            (AGENTE, TipoPerfil.AGENTE, "Agente"),
            (PASSAGEIRO, TipoPerfil.PASSAGEIRO, "Passageiro"),
        ):
            conta, _ = User.objects.get_or_create(
                username=usuario,
                defaults={"first_name": nome, "last_name": "Demonstração"},
            )
            conta.is_staff = False
            conta.is_superuser = False
            conta.set_password(senha)
            conta.save()
            PerfilUsuario.objects.get_or_create(
                usuario=conta,
                defaults={
                    "tipo": tipo,
                    "agencia": agencia if tipo == TipoPerfil.AGENTE else None,
                },
            )

        for titulo, destino, dias, valor, capacidade, status in EXCURSOES:
            excursao, criada = Excursao.objects.get_or_create(
                titulo=titulo,
                agencia=agencia,
                defaults={
                    "destino": destino,
                    "data_saida": date.today() + timedelta(days=dias),
                    "valor": Decimal(valor),
                    "capacidade": capacidade,
                    "status": status,
                },
            )
            if criada:
                PontoEmbarque.objects.create(
                    local="Terminal Rodoviário (fictício)",
                    horario=time(6, 0),
                    excursao=excursao,
                )
                PontoEmbarque.objects.create(
                    local="Praça Central (fictícia)", horario=time(6, 30), excursao=excursao
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Demonstração pronta: contas {AGENTE} e {PASSAGEIRO}, "
                f"{Excursao.objects.filter(agencia=agencia).count()} excursões fictícias."
            )
        )
