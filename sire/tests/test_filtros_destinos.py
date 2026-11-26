"""Evolução da pesquisa; preserva os VF da baseline."""
from datetime import timedelta
from django.urls import reverse
from sire.destinos import padronizar_destino
from sire.models import TipoPacote
from .base import CasoSire, criar_agencia, criar_excursao, criar_agente, dados_excursao

class FiltrosDestinos(CasoSire):
    def setUp(self):
        super().setUp()
        self.agencia = criar_agencia()
        self.a, self.ponto = criar_excursao(self.agencia, titulo="Passeio de lancha")
        self.a.destino = "Capitolio MG"
        self.a.valor = 200
        self.a.data_retorno = self.a.data_saida + timedelta(days=2)
        self.a.save()
        self.b, _ = criar_excursao(self.agencia, titulo="Praia")
        self.b.destino = "Guarujá"
        self.b.valor = 100
        self.b.tipo_pacote = TipoPacote.BATE_VOLTA
        self.b.save()
        self.rascunho, ponto = criar_excursao(self.agencia, titulo="Segredo", publicada=False)
        self.rascunho.destino = "Destino secreto"
        self.rascunho.save()
        ponto.local = "Embarque secreto"
        ponto.save()

    def buscar(self, **dados):
        return self.client.get(reverse("sire:buscar_excursoes"), dados)

    def test_lista_preserva_legado_e_oculta_rascunhos(self):
        resposta = self.buscar()
        self.assertContains(resposta, "Capitólio - MG")
        self.assertNotContains(resposta, "Destino secreto")
        self.assertNotContains(resposta, "Embarque secreto")
        self.assertNotContains(resposta, "Segredo")

    def test_destino_padronizado_filtra_grafia_legada(self):
        resposta = self.buscar(destino_catalogo="Capitólio - MG")
        self.assertEqual(list(resposta.context["excursoes"]), [self.a])

    def test_busca_livre_antiga(self):
        self.assertEqual(list(self.buscar(destino="Capitolio").context["excursoes"]), [self.a])

    def test_filtros_combinados(self):
        resposta = self.buscar(destino_catalogo="Capitólio - MG",
                               embarque=self.ponto.local, palavra_chave="lancha",
                               duracao="2_3")
        self.assertEqual(list(resposta.context["excursoes"]), [self.a])

    def test_duracao_bate_volta_sem_retorno(self):
        self.assertEqual(list(self.buscar(duracao="1").context["excursoes"]), [self.b])

    def test_ordena_preco(self):
        self.assertEqual(list(self.buscar(ordem="preco").context["excursoes"]), [self.b, self.a])

    def test_destino_sem_viagens(self):
        self.assertFalse(self.buscar(destino_catalogo="Holambra - SP").context["excursoes"].exists())

    def test_filtro_invalido_nao_expoe_dados(self):
        resposta = self.buscar(embarque="Embarque secreto")
        self.assertTrue(resposta.context["filtros"].errors)
        self.assertFalse(resposta.context["excursoes"].exists())

    def test_padronizacao_sem_perder_destino_personalizado(self):
        self.assertEqual(padronizar_destino("capitolio"), "Capitólio - MG")
        self.assertEqual(padronizar_destino("Litoral fictício"), "Litoral fictício")
        agente = criar_agente("agente_destino", self.agencia)
        self.client.force_login(agente)
        resposta = self.client.post(reverse("sire:cadastrar_excursao"),
                                   dados_excursao(destino="capitolio"))
        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(self.agencia.excursao_set.filter(destino="Capitólio - MG").exists())
