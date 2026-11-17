"""Recuperação de senha (extensão fora da baseline): por código e por e-mail."""

import re

from django.contrib.auth.models import User
from django.core import mail
from django.db import connection
from django.test import override_settings

from sire import recuperacao

from .base import SENHA, CasoSire, criar_passageiro, dados_cadastro

PADRAO = re.compile(r"[A-Z2-7]{5}-[A-Z2-7]{5}-[A-Z2-7]{5}-[A-Z2-7]{5}")
NOVA = "Outra-senha-forte-456"


class CodigoDeRecuperacao(CasoSire):
    def setUp(self):
        super().setUp()
        self.maria = criar_passageiro("Maria", email="maria@example.com")
        self.codigo = recuperacao.codigo_de(self.maria)

    def recuperar(self, usuario, codigo, nova=NOVA, confirmacao=None, ip="10.0.0.1"):
        return self.client.post(
            "/recuperar-acesso/",
            {
                "username": usuario,
                "codigo": codigo,
                "new_password1": nova,
                "new_password2": confirmacao or nova,
            },
            REMOTE_ADDR=ip,
        )

    def senha_atual_e(self, senha):
        self.maria.refresh_from_db()
        return self.maria.check_password(senha)

    def test_cadastro_mostra_o_codigo_da_conta(self):
        resposta = self.client.post("/cadastro/", dados_cadastro())
        encontrado = PADRAO.search(resposta.content.decode())
        self.assertIsNotNone(encontrado)
        self.assertTrue(recuperacao.confere(User.objects.get(username="novo"), encontrado.group()))

    def test_codigo_nao_e_gravado_no_banco_nem_na_sessao(self):
        with connection.cursor() as cursor:
            for tabela in connection.introspection.table_names():
                cursor.execute(f'SELECT * FROM "{tabela}"')
                for linha in cursor.fetchall():
                    for valor in linha:
                        self.assertNotIn(self.codigo, str(valor))
        self.assertEqual(list(self.client.session.keys()), [])

    def test_conta_autenticada_consulta_o_proprio_codigo(self):
        self.assertEqual(self.client.get("/minha-conta/codigo/").status_code, 302)
        self.entrar("Maria")
        self.assertContains(self.client.get("/minha-conta/codigo/"), self.codigo)

    def test_recuperacao_valida_troca_a_senha_e_o_codigo(self):
        # Usuário em maiúsculas e código em minúsculas, sem hífens.
        resposta = self.recuperar("MARIA", self.codigo.replace("-", "").lower())
        self.assertContains(resposta, "Senha redefinida")
        self.assertTrue(self.senha_atual_e(NOVA))
        novo = recuperacao.codigo_de(self.maria)
        self.assertNotEqual(novo, self.codigo)
        self.assertContains(resposta, novo)
        # O código antigo deixa de valer.
        self.recuperar("Maria", self.codigo, "Terceira-senha-789", ip="10.0.0.2")
        self.assertTrue(self.senha_atual_e(NOVA))

    def test_troca_de_senha_encerra_sessoes_abertas(self):
        self.entrar("Maria")
        outro_navegador = self.client_class()
        outro_navegador.post(
            "/recuperar-acesso/",
            {"username": "Maria", "codigo": self.codigo, "new_password1": NOVA, "new_password2": NOVA},
        )
        self.assertEqual(self.client.get("/minhas-reservas/").status_code, 302)

    def test_tentativas_invalidas_nao_trocam_a_senha(self):
        casos = {
            "código errado": ("Maria", "AAAAA-BBBBB-CCCCC-DDDDD", NOVA, None),
            "usuário inexistente": ("ninguem", self.codigo, NOVA, None),
            "confirmação diferente": ("Maria", self.codigo, NOVA, "Diferente-000"),
            "senha fraca": ("Maria", self.codigo, "123", None),
        }
        for indice, (rotulo, caso) in enumerate(casos.items()):
            with self.subTest(rotulo):
                resposta = self.recuperar(*caso, ip=f"10.0.1.{indice}")
                self.assertEqual(resposta.status_code, 200)
                self.assertTrue(self.senha_atual_e(SENHA))

    def test_mensagem_nao_revela_se_o_usuario_existe(self):
        erro = "Usuário ou código de recuperação inválidos"
        self.assertContains(self.recuperar("Maria", "AAAAA-BBBBB-CCCCC-DDDDD"), erro)
        self.assertContains(self.recuperar("ninguem", self.codigo, ip="10.0.0.3"), erro)

    def test_limite_de_tentativas_bloqueia_ate_o_codigo_certo(self):
        for _ in range(5):
            self.recuperar("Maria", "AAAAA-AAAAA-AAAAA-AAAAA")
        resposta = self.recuperar("Maria", self.codigo)
        self.assertContains(resposta, "Muitas tentativas")
        self.assertTrue(self.senha_atual_e(SENHA))

    def test_contas_compartilhadas_da_banca_ficam_fora(self):
        demo = criar_passageiro("demo_passageiro")
        self.recuperar("demo_passageiro", recuperacao.codigo_de(demo), ip="10.0.0.4")
        demo.refresh_from_db()
        self.assertTrue(demo.check_password(SENHA))
        self.entrar("demo_passageiro")
        pagina = self.client.get("/minha-conta/codigo/").content.decode()
        self.assertIsNone(PADRAO.search(pagina))

    def test_codigo_de_uma_conta_nao_abre_outra(self):
        outra = criar_passageiro("Joana")
        self.recuperar("Joana", self.codigo, ip="10.0.0.5")
        outra.refresh_from_db()
        self.assertTrue(outra.check_password(SENHA))


class CadastroComEmail(CasoSire):
    def cadastrar(self, usuario, email):
        return self.client.post("/cadastro/", dados_cadastro(usuario, email))

    def test_email_e_obrigatorio(self):
        self.cadastrar("sem_email", "")
        self.assertFalse(User.objects.filter(username="sem_email").exists())

    def test_email_e_gravado_em_minusculas_e_nao_se_repete(self):
        self.cadastrar("pessoa", "Pessoa@Example.com")
        self.assertEqual(User.objects.get(username="pessoa").email, "pessoa@example.com")
        self.cadastrar("outra", "PESSOA@example.com")
        self.assertFalse(User.objects.filter(username="outra").exists())


@override_settings(SIRE_RESET_DOMAIN="sire.exemplo.test")
class RecuperacaoPorEmail(CasoSire):
    """Opção secundária; depende de provedor de e-mail configurado."""

    def setUp(self):
        super().setUp()
        self.pessoa = criar_passageiro("pessoa", email="pessoa@example.com")

    def pedir(self, email, ip="10.0.2.1"):
        return self.client.post("/recuperar-senha/", {"email": email}, REMOTE_ADDR=ip)

    def test_link_redefine_a_senha_e_nao_pode_ser_reutilizado(self):
        self.pedir("PESSOA@EXAMPLE.COM")
        self.assertEqual(len(mail.outbox), 1)
        caminho = re.search(
            r"https://sire\.exemplo\.test(/redefinir-senha/\S+)", mail.outbox[0].body
        ).group(1)
        formulario = self.client.get(caminho, follow=True).redirect_chain[-1][0]
        self.client.post(formulario, {"new_password1": NOVA, "new_password2": NOVA})
        self.pessoa.refresh_from_db()
        self.assertTrue(self.pessoa.check_password(NOVA))
        reutilizado = self.client_class().get(caminho, follow=True)
        self.assertNotContains(reutilizado, "new_password1")

    def test_resposta_e_a_mesma_para_email_inexistente(self):
        existente = self.pedir("pessoa@example.com")
        inexistente = self.pedir("ninguem@example.com", ip="10.0.2.2")
        self.assertEqual((existente.status_code, existente.url), (inexistente.status_code, inexistente.url))
        self.assertEqual(len(mail.outbox), 1)

    def test_contas_compartilhadas_nao_recebem_link(self):
        criar_passageiro("demo_passageiro", email="demo@example.com")
        self.pedir("demo@example.com")
        self.assertEqual(len(mail.outbox), 0)

    def test_limite_de_pedidos_por_email(self):
        for _ in range(6):
            self.pedir("pessoa@example.com", ip="10.0.2.9")
        self.assertEqual(len(mail.outbox), 3)


class RecuperacaoPorEmailDesativada(CasoSire):
    def test_sem_provedor_configurado_o_envio_fica_indisponivel(self):
        resposta = self.client.post("/recuperar-senha/", {"email": "alguem@example.com"})
        self.assertContains(resposta, "não está disponível")
        self.assertEqual(len(mail.outbox), 0)

    def test_esqueci_minha_senha_leva_ao_codigo(self):
        self.assertContains(self.client.get("/login/"), "/recuperar-acesso/")
