"""Extensões da conta: data de nascimento, aceite de privacidade, Minha conta,
troca de senha e botão de mostrar senha."""

from datetime import date, timedelta

from django.contrib.auth.models import User
from django.contrib.staticfiles import finders

from sire import recuperacao
from sire.models import PerfilUsuario, Reserva

from .base import (
    SENHA,
    CasoSire,
    criar_agencia,
    criar_agente,
    criar_excursao,
    criar_passageiro,
    dados_cadastro,
)

NOVA = "Outra-senha-forte-456"


class CadastroComNascimentoEAceite(CasoSire):
    def cadastrar(self, **alteracoes):
        return self.client.post("/cadastro/", dados_cadastro(**alteracoes))

    def existe(self):
        return User.objects.filter(username="novo").exists()

    def test_data_de_nascimento_e_gravada_no_perfil(self):
        self.cadastrar()
        perfil = PerfilUsuario.objects.get(usuario__username="novo")
        self.assertEqual(perfil.data_nascimento, date(1990, 5, 20))

    def test_data_de_nascimento_e_obrigatoria(self):
        self.cadastrar(data_nascimento="")
        self.assertFalse(self.existe())

    def test_data_no_futuro_e_recusada(self):
        amanha = (date.today() + timedelta(days=1)).isoformat()
        resposta = self.cadastrar(data_nascimento=amanha)
        self.assertContains(resposta, "não pode estar no futuro")
        self.assertFalse(self.existe())

    def test_data_implausivel_e_recusada(self):
        self.cadastrar(data_nascimento="1800-01-01")
        self.assertFalse(self.existe())

    def test_sem_aceite_do_aviso_de_privacidade_nao_cadastra(self):
        resposta = self.cadastrar(aceite=None)
        self.assertContains(resposta, "concordar com o aviso de privacidade")
        self.assertFalse(self.existe())

    def test_formulario_aponta_para_o_aviso_de_privacidade(self):
        self.assertContains(self.client.get("/cadastro/"), "/privacidade/")


class Privacidade(CasoSire):
    def test_aviso_e_publico_e_descreve_os_dados(self):
        resposta = self.client.get("/privacidade/")
        self.assertEqual(resposta.status_code, 200)
        for trecho in ("data de nascimento", "e-mail", "Estados Unidos", "demonstração"):
            with self.subTest(trecho):
                self.assertContains(resposta, trecho)

    def test_rodape_leva_ao_aviso(self):
        self.assertContains(self.client.get("/"), "/privacidade/")


class MinhaContaETrocaDeSenha(CasoSire):
    def setUp(self):
        super().setUp()
        self.maria = criar_passageiro("Maria", email="maria@example.com")
        self.entrar("Maria")

    def trocar(self, atual=SENHA, nova=NOVA, confirmacao=None):
        return self.client.post(
            "/minha-conta/senha/",
            {
                "old_password": atual,
                "new_password1": nova,
                "new_password2": confirmacao or nova,
            },
        )

    def test_minha_conta_exige_login(self):
        self.client.logout()
        for caminho in ("/minha-conta/", "/minha-conta/senha/"):
            self.assertEqual(self.client.get(caminho).status_code, 302)

    def test_minha_conta_mostra_os_proprios_dados(self):
        criar_passageiro("Outra", email="outra@example.com")
        resposta = self.client.get("/minha-conta/")
        self.assertContains(resposta, "maria@example.com")
        self.assertNotContains(resposta, "outra@example.com")

    def test_troca_de_senha_exige_a_senha_atual(self):
        self.trocar(atual="senha-errada")
        self.maria.refresh_from_db()
        self.assertTrue(self.maria.check_password(SENHA))

    def test_troca_de_senha_muda_a_senha_e_o_codigo(self):
        codigo_antigo = recuperacao.codigo_de(self.maria)
        resposta = self.trocar()
        self.assertRedirects(resposta, "/minha-conta/codigo/")
        self.maria.refresh_from_db()
        self.assertTrue(self.maria.check_password(NOVA))
        self.assertNotEqual(recuperacao.codigo_de(self.maria), codigo_antigo)
        # A sessão em uso continua válida depois da troca.
        self.assertEqual(self.client.get("/minha-conta/").status_code, 200)

    def test_senha_fraca_e_recusada(self):
        self.trocar(nova="123")
        self.maria.refresh_from_db()
        self.assertTrue(self.maria.check_password(SENHA))

    def test_conta_compartilhada_nao_troca_senha(self):
        criar_passageiro("demo_passageiro")
        self.client.logout()
        self.entrar("demo_passageiro")
        self.assertEqual(self.client.get("/minha-conta/senha/").status_code, 403)
        self.assertEqual(self.trocar().status_code, 403)


class NascimentoNaListaDoAgente(CasoSire):
    def test_agente_ve_nascimento_dos_passageiros_da_propria_excursao(self):
        agencia = criar_agencia()
        criar_agente("agente", agencia)
        excursao, ponto = criar_excursao(agencia)
        viajante = criar_passageiro("viajante")
        viajante.perfil.data_nascimento = date(1985, 3, 9)
        viajante.perfil.save()
        Reserva.objects.create(passageiro=viajante, excursao=excursao, ponto_embarque=ponto)
        self.entrar("agente")
        resposta = self.client.get(f"/agente/excursoes/{excursao.pk}/passageiros/")
        self.assertContains(resposta, "09/03/1985")


class MostrarSenha(CasoSire):
    def test_paginas_com_senha_carregam_o_script(self):
        for caminho in ("/login/", "/cadastro/", "/recuperar-acesso/"):
            with self.subTest(caminho):
                self.assertContains(self.client.get(caminho), "sire/js/mostrar-senha.js")

    def test_script_existe_e_nao_envia_o_formulario(self):
        caminho = finders.find("sire/js/mostrar-senha.js")
        self.assertIsNotNone(caminho)
        with open(caminho, encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        self.assertIn('botao.type = "button"', conteudo)
