"""Carrega no catálogo as saídas de dezembro/2026 e janeiro/2027 (portfólio).

Pode ser executado várias vezes: agências, agentes e excursões são localizados
pelo nome/título e nada que já exista é alterado ou apagado. Saídas com data
já passada não são criadas. As fotos vão para o Google Drive pelo mesmo
caminho do envio pela tela (drive_fotos), só quando a excursão ainda não tem
foto e o Drive está configurado. Falha no Drive não interrompe o carregamento.

As senhas dos agentes vêm de SIRE_DEMO_SENHA (a mesma das contas de
demonstração). Sem essa variável, os agentes ficam sem senha utilizável.
Não acrescenta campos, tabelas ou regras.
"""

import json
import os
from datetime import date, time
from decimal import Decimal
from pathlib import Path

from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction

from sire import drive_fotos
from sire.models import (
    Agencia,
    Excursao,
    FotoExcursao,
    PerfilUsuario,
    PontoEmbarque,
    StatusExcursao,
    TipoPerfil,
)

PASTA = Path(__file__).resolve().parents[2] / "portfolio"
DADOS = PASTA / "dez2026_jan2027.json"


class Command(BaseCommand):
    help = "Carrega as excursões de dezembro e janeiro no catálogo (portfólio)."

    def handle(self, *args, **options):
        dados = json.loads(DADOS.read_text(encoding="utf-8"))
        agencias = self._agencias(dados["agencias"])

        criadas = existentes = passadas = 0
        novas_fotos = 0
        for item in dados["excursoes"]:
            saida = date.fromisoformat(item["saida"])
            if saida < date.today():
                passadas += 1
                continue
            excursao, criada = self._excursao(agencias[item["agencia"]], item, saida)
            criadas += criada
            existentes += not criada
            novas_fotos += self._fotos(excursao, item.get("fotos", []))

        self.stdout.write(
            self.style.SUCCESS(
                f"Portfólio: {criadas} excursões criadas, {existentes} já existiam, "
                f"{passadas} ignoradas por data passada, {novas_fotos} fotos enviadas."
            )
        )

    @transaction.atomic
    def _agencias(self, lista):
        senha = os.environ.get("SIRE_DEMO_SENHA", "")
        resultado = {}
        for a in lista:
            agencia, _ = Agencia.objects.get_or_create(nome=a["nome"])
            conta, criada = User.objects.get_or_create(
                username=a["agente"],
                defaults={"first_name": a["agente_nome"], "last_name": "(portfólio)"},
            )
            if criada:
                conta.is_staff = False
                conta.is_superuser = False
                if senha:
                    conta.set_password(senha)
                else:
                    conta.set_unusable_password()
                conta.save()
            PerfilUsuario.objects.get_or_create(
                usuario=conta, defaults={"tipo": TipoPerfil.AGENTE, "agencia": agencia}
            )
            resultado[a["chave"]] = agencia
        return resultado

    @transaction.atomic
    def _excursao(self, agencia, item, saida):
        excursao = Excursao.objects.filter(titulo=item["titulo"], agencia=agencia).first()
        if excursao:
            return excursao, False
        excursao = Excursao(
            titulo=item["titulo"],
            destino=item["destino"],
            tipo_pacote=item.get("tipo") or None,
            descricao=item.get("descricao", ""),
            roteiro=item.get("roteiro", ""),
            inclusos=item.get("inclusos", ""),
            data_saida=saida,
            data_retorno=date.fromisoformat(item["retorno"]) if item.get("retorno") else None,
            valor=Decimal(item["valor"]),
            capacidade=item["capacidade"],
            agencia=agencia,
        )
        excursao.full_clean()
        excursao.save()
        for local, horario in item["embarques"]:
            hora, minuto = (int(p) for p in horario.split(":"))
            PontoEmbarque.objects.create(
                excursao=excursao, local=local, horario=time(hora, minuto)
            )
        # Mesma regra da tela: só publica com dados válidos e embarque.
        if excursao.pode_publicar():
            excursao.status = StatusExcursao.PUBLICADA
            excursao.save(update_fields=["status"])
        return excursao, True

    def _fotos(self, excursao, nomes):
        if not nomes or excursao.fotos.exists() or not drive_fotos.configurado():
            return 0
        enviadas = 0
        for nome in nomes[: drive_fotos.LIMITE_FOTOS]:
            caminho = PASTA / "fotos" / nome
            try:
                with caminho.open("rb") as bruto:
                    jpeg = drive_fotos.preparar_jpeg(File(bruto, name=nome))
                drive_id = drive_fotos.enviar(excursao.id, jpeg)
                FotoExcursao.objects.create(excursao=excursao, drive_id=drive_id)
                enviadas += 1
            except (OSError, ValueError, drive_fotos.FalhaDrive) as erro:
                self.stdout.write(
                    self.style.WARNING(f"Foto {nome} não enviada ({excursao.titulo}): {erro}")
                )
                break
        return enviadas
