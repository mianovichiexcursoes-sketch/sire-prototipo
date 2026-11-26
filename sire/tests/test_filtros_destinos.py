"""Evolução da pesquisa; preserva os VF da baseline."""
from datetime import timedelta
from django.urls import reverse
from sire.destinos import padronizar_destino
from sire.models import CategoriaViagem, TipoPacote
from .base import CasoSire, criar_agencia, criar_excursao, criar_agente, dados_excursao

class FiltrosDestinos(CasoSire):
    def setUp(self):
        super().setUp()
        self.agencia = criar_agencia()
        self.a, self.ponto = criar_excursao(self.agencia, titulo="Passeio de lancha")
        self.a.destino = "Capitolio MG"
        self.a.valor = 200
        self.a.categoria = CategoriaViagem.CACHOEIRA
        self.a.tipo_pacote = TipoPacote.COM_HOSPEDAGEM
        self.a.data_retorno = self.a.data_saida + timedelta(days=2)
        self.a.save()
        self.b, _ = criar_excursao(self.agencia, titulo="Praia")
        self.b.destino = "Guarujá"
        self.b.valor = 100
        self.b.categoria = CategoriaViagem.PRAIA
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
                               tipo_pacote=TipoPacote.COM_HOSPEDAGEM)
        self.assertEqual(list(resposta.context["excursoes"]), [self.a])

    def test_tipo_bate_volta_ou_hospedagem(self):
        self.assertEqual(list(self.buscar(tipo_pacote=TipoPacote.BATE_VOLTA).context["excursoes"]), [self.b])
        self.assertEqual(list(self.buscar(tipo_pacote=TipoPacote.COM_HOSPEDAGEM).context["excursoes"]), [self.a])
        self.assertNotIn("duracao", self.buscar().context["filtros"].fields)

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

    def test_categoria_e_preco_combinados(self):
        self.assertEqual(list(self.buscar(categoria="PRAIA", preco_min="100", preco_max="100").context["excursoes"]), [self.b])
        self.assertFalse(self.buscar(categoria="PRAIA", preco_min="101").context["excursoes"].exists())
        self.assertEqual(list(self.buscar(preco_max="150").context["excursoes"]), [self.b])
        self.assertFalse(self.buscar(preco_max="0").context["excursoes"].exists())

    def test_preco_invalido_e_categoria_invalida(self):
        for dados in ({"preco_min":"200","preco_max":"100"}, {"preco_min":"-1"}, {"categoria":"INVALIDA"}):
            resposta = self.buscar(**dados)
            self.assertTrue(resposta.context["filtros"].errors)
            self.assertFalse(resposta.context["excursoes"].exists())

    def test_categoria_opcional_e_sem_expor_rascunhos(self):
        self.rascunho.categoria = CategoriaViagem.PRAIA
        self.rascunho.save()
        self.assertEqual(list(self.buscar(categoria="PRAIA").context["excursoes"]), [self.b])
        self.a.categoria = ""
        self.a.save()
        self.assertIn(self.a, list(self.buscar().context["excursoes"]))

    def test_agente_define_categoria(self):
        agente = criar_agente("agente_categoria", self.agencia)
        self.client.force_login(agente)
        resposta = self.client.post(reverse("sire:cadastrar_excursao"), dados_excursao(destino="Guarujá", categoria="PRAIA"))
        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(self.agencia.excursao_set.filter(destino="Guarujá - SP", categoria="PRAIA").exists())
