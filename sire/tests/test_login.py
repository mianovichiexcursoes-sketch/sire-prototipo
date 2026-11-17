"""UC02 refinado: login sem distinção de maiúsculas no nome de usuário."""

from django.contrib.auth.models import User

from .base import SENHA, CasoSire, criar_passageiro


class LoginSemDistincaoDeMaiusculas(CasoSire):
    def setUp(self):
        super().setUp()
        criar_passageiro("demo_passageiro")

    def tentar(self, usuario, senha=SENHA):
        resposta = self.client.post("/login/", {"username": usuario, "password": senha})
        identificador = self.client.session.get("_auth_user_id")
        conta = User.objects.get(pk=identificador).username if identificador else None
        self.client.logout()
        return resposta, conta

    def test_tres_grafias_entram_na_mesma_conta(self):
        for grafia in ("demo_passageiro", "DEMO_PASSAGEIRO", "Demo_Passageiro"):
            with self.subTest(grafia=grafia):
                resposta, conta = self.tentar(grafia)
                self.assertEqual(resposta.status_code, 302)
                self.assertEqual(conta, "demo_passageiro")

    def test_senha_errada_e_recusada_com_mensagem_unica(self):
        resposta, conta = self.tentar("DEMO_PASSAGEIRO", "senha-errada")
        self.assertIsNone(conta)
        self.assertContains(resposta, "Usuário ou senha inválidos")

    def test_senha_continua_distinguindo_maiusculas(self):
        _, conta = self.tentar("demo_passageiro", SENHA.upper())
        self.assertIsNone(conta)

    def test_usuario_inexistente_recebe_a_mesma_mensagem(self):
        resposta, conta = self.tentar("nao_existe")
        self.assertIsNone(conta)
        self.assertContains(resposta, "Usuário ou senha inválidos")

    def test_nomes_iguais_em_grafias_diferentes_exigem_grafia_exata(self):
        criar_passageiro("Ana", "Senha-da-Ana-123")
        criar_passageiro("ana", "Senha-da-ana-456")
        self.assertEqual(self.tentar("Ana", "Senha-da-Ana-123")[1], "Ana")
        self.assertEqual(self.tentar("ana", "Senha-da-ana-456")[1], "ana")
        # Grafia ambígua não é resolvida; senha de uma conta não abre a outra.
        self.assertIsNone(self.tentar("ANA", "Senha-da-Ana-123")[1])
        self.assertIsNone(self.tentar("ana", "Senha-da-Ana-123")[1])
