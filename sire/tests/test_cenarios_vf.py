"""Cenários de verificação funcional VF01–VF16 da baseline ER-SIRE 2.1.

Cada teste corresponde a um cenário de docs/VERIFICACAO.md e confere a
resposta HTTP e os dados persistidos.
"""

from django.contrib.auth.models import User

from sire.models import Excursao, PerfilUsuario, PontoEmbarque, Reserva, StatusExcursao

from .base import (
    SENHA,
    CasoSire,
    criar_agencia,
    criar_agente,
    criar_excursao,
    criar_passageiro,
    dados_excursao,
    reservas_de,
)


class CadastroEAutenticacao(CasoSire):
    def cadastrar(self, usuario="novo", email="novo@example.com"):
        return self.client.post(
            "/cadastro/",
            {
                "username": usuario,
                "first_name": "Nome",
                "last_name": "Sobrenome",
                "email": email,
                "password1": SENHA,
                "password2": SENHA,
            },
        )

    def test_vf01_cadastro_publico_cria_passageiro_sem_agencia(self):
        resposta = self.cadastrar()
        self.assertEqual(resposta.status_code, 200)
        perfil = PerfilUsuario.objects.get(usuario__username="novo")
        self.assertEqual(perfil.tipo, "PASSAGEIRO")
        self.assertIsNone(perfil.agencia)

    def test_vf02_identificador_repetido_e_recusado(self):
        self.cadastrar()
        self.cadastrar(email="outro@example.com")
        self.assertEqual(User.objects.filter(username="novo").count(), 1)

    def test_vf03_login_e_acesso_por_perfil(self):
        agencia = criar_agencia()
        criar_agente("agente", agencia)
        criar_passageiro("passageiro")

        self.entrar("passageiro")
        self.assertEqual(self.client.get("/minhas-reservas/").status_code, 200)
        self.assertEqual(self.client.get("/agente/excursoes/").status_code, 403)
        self.client.logout()

        self.entrar("agente")
        self.assertEqual(self.client.get("/agente/excursoes/").status_code, 200)
        self.assertEqual(self.client.get("/minhas-reservas/").status_code, 403)

    def test_vf03_paginas_privadas_exigem_login(self):
        for caminho in ("/minhas-reservas/", "/agente/excursoes/"):
            resposta = self.client.get(caminho)
            self.assertEqual(resposta.status_code, 302)
            self.assertIn("/login/", resposta.url)


class GestaoDeExcursoes(CasoSire):
    def setUp(self):
        super().setUp()
        self.agencia = criar_agencia("Agência A")
        self.outra = criar_agencia("Agência B")
        criar_agente("agente_a", self.agencia)
        criar_agente("agente_b", self.outra)
        self.entrar("agente_a")

    def test_vf04_excursao_nasce_rascunho_na_agencia_do_agente(self):
        # Tentativa de forjar agência e status pelo formulário.
        dados = dados_excursao(agencia=self.outra.pk, status="PUBLICADA")
        self.client.post("/agente/excursoes/nova/", dados)
        excursao = Excursao.objects.get(titulo="Passeio fictício")
        self.assertEqual(excursao.status, StatusExcursao.RASCUNHO)
        self.assertEqual(excursao.agencia, self.agencia)

    def test_vf05_nao_edita_excursao_de_outra_agencia(self):
        alheia, _ = criar_excursao(self.outra, "Da agência B")
        resposta = self.client.post(
            f"/agente/excursoes/{alheia.pk}/editar/", dados_excursao(titulo="Invadida")
        )
        self.assertEqual(resposta.status_code, 404)
        alheia.refresh_from_db()
        self.assertEqual(alheia.titulo, "Da agência B")

    def test_vf06_cadastra_ponto_de_embarque_na_excursao_da_url(self):
        excursao, _ = criar_excursao(self.agencia, publicada=False, embarque=False)
        alheia, _ = criar_excursao(self.outra, "Da agência B")
        self.client.post(
            f"/agente/excursoes/{excursao.pk}/embarques/novo/",
            {"local": "Terminal A", "horario": "06:30", "excursao": alheia.pk},
        )
        ponto = PontoEmbarque.objects.get(local="Terminal A")
        self.assertEqual(ponto.excursao, excursao)

    def test_vf07_nao_publica_sem_ponto_de_embarque(self):
        excursao, _ = criar_excursao(self.agencia, publicada=False, embarque=False)
        self.client.post(f"/agente/excursoes/{excursao.pk}/publicar/")
        excursao.refresh_from_db()
        self.assertEqual(excursao.status, StatusExcursao.RASCUNHO)

    def test_vf08_publica_excursao_valida(self):
        excursao, _ = criar_excursao(self.agencia, publicada=False)
        self.client.post(f"/agente/excursoes/{excursao.pk}/publicar/")
        excursao.refresh_from_db()
        self.assertEqual(excursao.status, StatusExcursao.PUBLICADA)

    def test_passageiro_nao_publica_excursao(self):
        excursao, _ = criar_excursao(self.agencia, publicada=False)
        criar_passageiro("passageiro")
        self.client.logout()
        self.entrar("passageiro")
        resposta = self.client.post(f"/agente/excursoes/{excursao.pk}/publicar/")
        self.assertEqual(resposta.status_code, 403)

    def test_uc07_e3_capacidade_nao_fica_abaixo_das_reservas(self):
        excursao, ponto = criar_excursao(self.agencia, capacidade=2)
        for nome in ("p1", "p2"):
            Reserva.objects.create(
                passageiro=criar_passageiro(nome), excursao=excursao, ponto_embarque=ponto
            )
        self.client.post(
            f"/agente/excursoes/{excursao.pk}/editar/",
            dados_excursao(titulo=excursao.titulo, capacidade="1"),
        )
        excursao.refresh_from_db()
        self.assertEqual(excursao.capacidade, 2)


class CatalogoEDetalhes(CasoSire):
    def setUp(self):
        super().setUp()
        self.agencia = criar_agencia()
        self.publicada, self.ponto = criar_excursao(self.agencia, "Praia publicada")
        self.rascunho, _ = criar_excursao(self.agencia, "Serra rascunho", publicada=False)

    def test_vf09_catalogo_mostra_so_publicadas(self):
        pagina = self.client.get("/").content.decode()
        self.assertIn("Praia publicada", pagina)
        self.assertNotIn("Serra rascunho", pagina)

    def test_vf09_pesquisa_por_destino(self):
        self.publicada.destino = "Ubatuba"
        self.publicada.save()
        self.assertIn("Praia publicada", self.client.get("/buscar/?destino=ubat").content.decode())
        self.assertNotIn(
            "Praia publicada", self.client.get("/buscar/?destino=inexistente").content.decode()
        )

    def test_vf09_detalhe_de_rascunho_nao_existe_para_o_publico(self):
        self.assertEqual(self.client.get(f"/excursao/{self.rascunho.pk}/").status_code, 404)

    def test_vf10_detalhe_mostra_disponibilidade_calculada(self):
        Reserva.objects.create(
            passageiro=criar_passageiro("p1"), excursao=self.publicada, ponto_embarque=self.ponto
        )
        resposta = self.client.get(f"/excursao/{self.publicada.pk}/")
        self.assertEqual(resposta.context["excursao"].calcular_disponibilidade(), 1)
        self.assertContains(resposta, "Vagas disponíveis")


class Reservas(CasoSire):
    def setUp(self):
        super().setUp()
        self.agencia = criar_agencia("Agência A")
        self.excursao, self.ponto = criar_excursao(self.agencia, capacidade=2)
        self.p1 = criar_passageiro("p1")
        self.p2 = criar_passageiro("p2")
        self.entrar("p1")

    def reservar(self, excursao=None, ponto=None):
        excursao = excursao or self.excursao
        ponto = ponto or self.ponto
        return self.client.post(
            f"/excursao/{excursao.pk}/reservar/", {"ponto_embarque": ponto.pk}
        )

    def test_vf11_reserva_com_embarque_valido(self):
        resposta = self.reservar()
        self.assertRedirects(resposta, "/minhas-reservas/")
        reserva = Reserva.objects.get()
        self.assertEqual(
            (reserva.passageiro, reserva.excursao, reserva.ponto_embarque),
            (self.p1, self.excursao, self.ponto),
        )
        self.assertEqual(self.excursao.calcular_disponibilidade(), 1)

    def test_vf12_embarque_de_outra_excursao_e_recusado(self):
        _, ponto_alheio = criar_excursao(self.agencia, "Outra")
        resposta = self.reservar(ponto=ponto_alheio)
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(reservas_de(self.excursao), 0)

    def test_vf13_excursao_lotada_recusa_sem_erro_500(self):
        for passageiro in (self.p1, self.p2):
            Reserva.objects.create(
                passageiro=passageiro, excursao=self.excursao, ponto_embarque=self.ponto
            )
        resposta = self.reservar()
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Não há vagas disponíveis")
        self.assertEqual(reservas_de(self.excursao), 2)

    def test_vf14_passageiro_ve_so_as_proprias_reservas(self):
        outra, ponto_outra = criar_excursao(self.agencia, "Excursão do p2")
        Reserva.objects.create(passageiro=self.p1, excursao=self.excursao, ponto_embarque=self.ponto)
        Reserva.objects.create(passageiro=self.p2, excursao=outra, ponto_embarque=ponto_outra)
        pagina = self.client.get("/minhas-reservas/").content.decode()
        self.assertIn(self.excursao.titulo, pagina)
        self.assertNotIn("Excursão do p2", pagina)

    def test_agente_nao_reserva(self):
        criar_agente("agente", self.agencia)
        self.client.logout()
        self.entrar("agente")
        self.assertEqual(self.reservar().status_code, 403)
        self.assertEqual(reservas_de(self.excursao), 0)

    def test_excursao_em_rascunho_nao_aceita_reserva(self):
        rascunho, ponto = criar_excursao(self.agencia, "Rascunho", publicada=False)
        self.assertEqual(self.reservar(rascunho, ponto).status_code, 404)
        self.assertEqual(reservas_de(rascunho), 0)

    def test_baseline_nao_limita_reservas_por_passageiro(self):
        # ER-SIRE 2.1: não há regra de uma reserva por passageiro por excursão.
        self.reservar()
        self.reservar()
        self.assertEqual(Reserva.objects.filter(passageiro=self.p1).count(), 2)


class ConsultasDoAgente(CasoSire):
    def setUp(self):
        super().setUp()
        self.agencia = criar_agencia("Agência A")
        self.outra = criar_agencia("Agência B")
        criar_agente("agente_a", self.agencia)
        self.excursao, ponto = criar_excursao(self.agencia, "Da agência A")
        self.alheia, _ = criar_excursao(self.outra, "Da agência B")
        self.passageiro = criar_passageiro("viajante")
        Reserva.objects.create(
            passageiro=self.passageiro, excursao=self.excursao, ponto_embarque=ponto
        )
        self.entrar("agente_a")

    def test_vf15_reservas_da_propria_agencia_e_bloqueio_da_alheia(self):
        resposta = self.client.get(f"/agente/excursoes/{self.excursao.pk}/reservas/")
        self.assertContains(resposta, "viajante")
        alheia = self.client.get(f"/agente/excursoes/{self.alheia.pk}/reservas/")
        self.assertEqual(alheia.status_code, 404)

    def test_vf16_passageiros_da_excursao(self):
        resposta = self.client.get(f"/agente/excursoes/{self.excursao.pk}/passageiros/")
        self.assertContains(resposta, "viajante")
        alheia = self.client.get(f"/agente/excursoes/{self.alheia.pk}/passageiros/")
        self.assertEqual(alheia.status_code, 404)

    def test_agente_lista_so_excursoes_da_propria_agencia(self):
        pagina = self.client.get("/agente/excursoes/").content.decode()
        self.assertIn("Da agência A", pagina)
        self.assertNotIn("Da agência B", pagina)
