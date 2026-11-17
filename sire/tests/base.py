"""Apoio comum aos testes: dados fictícios e configuração mais rápida."""

from datetime import date, time, timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.cache import cache
from django.test import TestCase, override_settings

from sire.models import (
    Agencia,
    Excursao,
    PerfilUsuario,
    PontoEmbarque,
    Reserva,
    StatusExcursao,
    TipoPerfil,
)

SENHA = "Senha-de-teste-123"

# Hash rápido só durante os testes; a aplicação usa o padrão do Django.
AJUSTES = override_settings(
    PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"],
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
)


def criar_agencia(nome="Agência A"):
    return Agencia.objects.create(nome=nome)


def criar_agente(usuario, agencia, senha=SENHA):
    conta = User.objects.create_user(username=usuario, password=senha)
    PerfilUsuario.objects.create(usuario=conta, tipo=TipoPerfil.AGENTE, agencia=agencia)
    return conta


def criar_passageiro(usuario, senha=SENHA, email=""):
    conta = User.objects.create_user(username=usuario, password=senha, email=email)
    PerfilUsuario.objects.create(usuario=conta, tipo=TipoPerfil.PASSAGEIRO)
    return conta


def criar_excursao(agencia, titulo="Excursão", capacidade=2, publicada=True, embarque=True):
    excursao = Excursao.objects.create(
        titulo=titulo,
        destino="Destino fictício",
        data_saida=date.today() + timedelta(days=30),
        valor=Decimal("100.00"),
        capacidade=capacidade,
        status=StatusExcursao.PUBLICADA if publicada else StatusExcursao.RASCUNHO,
        agencia=agencia,
    )
    ponto = None
    if embarque:
        ponto = PontoEmbarque.objects.create(
            local="Terminal fictício", horario=time(7, 0), excursao=excursao
        )
    return excursao, ponto


def dados_excursao(**alteracoes):
    dados = {
        "titulo": "Passeio fictício",
        "destino": "Litoral",
        "data_saida": (date.today() + timedelta(days=20)).isoformat(),
        "data_retorno": "",
        "valor": "150.00",
        "capacidade": "10",
    }
    dados.update(alteracoes)
    return dados


def dados_cadastro(usuario="novo", email="novo@example.com", **alteracoes):
    """Formulário público de cadastro preenchido de forma válida."""
    dados = {
        "username": usuario,
        "first_name": "Nome",
        "last_name": "Sobrenome",
        "email": email,
        "data_nascimento": "1990-05-20",
        "password1": SENHA,
        "password2": SENHA,
        "aceite": "on",
    }
    dados.update(alteracoes)
    return {chave: valor for chave, valor in dados.items() if valor is not None}


def reservas_de(excursao):
    return Reserva.objects.filter(excursao=excursao).count()


@AJUSTES
class CasoSire(TestCase):
    """Base dos testes: limpa os contadores de tentativas a cada teste."""

    def setUp(self):
        cache.clear()

    def entrar(self, usuario, senha=SENHA):
        self.assertTrue(self.client.login(username=usuario, password=senha))
