"""Regressão isolada de fotos — extensão CAT-RF-03, RN-03/04/05/11.

Executar: python manage.py test sire.test_fotos_regressao
Todos os usuários, IDs e bytes são sintéticos. Drive é sempre mockado.
Testes intencionalmente detectam o problema atual de cache público (FOTO-05);
NÃO interpretar falha como aprovação ou como resultado já executado.
"""
from datetime import date
from decimal import Decimal
from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase, TransactionTestCase
from django.urls import reverse

from .models import Agencia, Excursao, FotoExcursao, PerfilUsuario, StatusExcursao, TipoPerfil


class FotoPermissoesRegressao(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.agencia_a = Agencia.objects.create(nome="Agência A sintética")
        cls.agencia_b = Agencia.objects.create(nome="Agência B sintética")
        cls.agente_a = User.objects.create_user("agente_foto_a", password="senha-sintetica")
        cls.agente_b = User.objects.create_user("agente_foto_b", password="senha-sintetica")
        PerfilUsuario.objects.create(
            usuario=cls.agente_a, tipo=TipoPerfil.AGENTE, agencia=cls.agencia_a
        )
        PerfilUsuario.objects.create(
            usuario=cls.agente_b, tipo=TipoPerfil.AGENTE, agencia=cls.agencia_b
        )
        cls.excursao = Excursao.objects.create(
            titulo="Excursão fictícia", destino="Cidade sintética",
            data_saida=date(2027, 3, 1), valor=Decimal("100.00"),
            capacidade=10, agencia=cls.agencia_a, status=StatusExcursao.RASCUNHO,
        )
        cls.foto = FotoExcursao.objects.create(
            excursao=cls.excursao, drive_id="drive-ficticio-foto-1"
        )

    def _imagem(self):
        return reverse("sire:imagem_excursao", args=[self.foto.pk])

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.baixar", return_value=b"jpeg-ficticio")
    def test_foto_02_visitante_nao_ve_rascunho(self, baixar, configurado):
        resposta = self.client.get(self._imagem())
        self.assertEqual(resposta.status_code, 404)
        baixar.assert_not_called()

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.baixar", return_value=b"jpeg-ficticio")
    def test_foto_03_agente_alheio_nao_ve_rascunho(self, baixar, configurado):
        self.client.force_login(self.agente_b)
        resposta = self.client.get(self._imagem())
        self.assertEqual(resposta.status_code, 404)
        baixar.assert_not_called()

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.baixar", return_value=b"jpeg-ficticio")
    def test_foto_04_agente_proprio_ve_rascunho_sem_cache(self, baixar, configurado):
        self.client.force_login(self.agente_a)
        resposta = self.client.get(self._imagem())
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta["Content-Type"], "image/jpeg")
        self.assertIn("no-store", resposta["Cache-Control"])
        self.assertEqual(resposta["X-Content-Type-Options"], "nosniff")

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.baixar", return_value=b"jpeg-ficticio")
    def test_foto_05_despublicacao_nao_deixa_cache_publico(self, baixar, configurado):
        """Imagem publicada não pode permanecer em cache após despublicação."""
        self.excursao.status = StatusExcursao.PUBLICADA
        self.excursao.save(update_fields=["status"])
        primeira = self.client.get(self._imagem())
        self.assertEqual(primeira.status_code, 200)
        self.assertIn("no-store", primeira["Cache-Control"])
        self.assertNotIn("public", primeira["Cache-Control"])
        self.assertEqual(primeira["Pragma"], "no-cache")
        self.assertEqual(primeira["Expires"], "0")
        self.excursao.status = StatusExcursao.RASCUNHO
        self.excursao.save(update_fields=["status"])
        segunda = self.client.get(self._imagem())
        self.assertEqual(segunda.status_code, 404)

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.enviar")
    def test_foto_07_setima_foto_recusada_sem_upload(self, enviar, configurado):
        for indice in range(2, 7):
            FotoExcursao.objects.create(
                excursao=self.excursao, drive_id=f"drive-ficticio-foto-{indice}"
            )
        self.client.force_login(self.agente_a)
        url = reverse("sire:adicionar_foto", args=[self.excursao.pk])
        resposta = self.client.post(url, data={})
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(self.excursao.fotos.count(), 6)
        enviar.assert_not_called()

    @patch("sire.views.drive_fotos.excluir")
    def test_foto_09_agente_alheio_nao_remove_foto(self, excluir):
        """RN-03: URL direta de exclusão não autoriza outra agência."""
        self.client.force_login(self.agente_b)
        url = reverse("sire:remover_foto", args=[self.excursao.pk, self.foto.pk])
        resposta = self.client.post(url)
        self.assertEqual(resposta.status_code, 404)
        self.assertTrue(FotoExcursao.objects.filter(pk=self.foto.pk).exists())
        excluir.assert_not_called()

    @patch("sire.views.drive_fotos.excluir")
    def test_foto_10_falha_drive_preserva_referencia(self, excluir):
        """CAT-RF-03: erro de exclusão remota não pode apagar referência local."""
        from . import drive_fotos
        excluir.side_effect = drive_fotos.FalhaDrive("falha sintética")
        self.client.force_login(self.agente_a)
        url = reverse("sire:remover_foto", args=[self.excursao.pk, self.foto.pk])
        resposta = self.client.post(url)
        self.assertEqual(resposta.status_code, 302)
        self.assertTrue(FotoExcursao.objects.filter(pk=self.foto.pk).exists())
        excluir.assert_called_once_with("drive-ficticio-foto-1")

    @patch("sire.views.drive_fotos.configurado", return_value=False)
    @patch("sire.views.drive_fotos.baixar")
    def test_foto_06_drive_nao_configurado_falha_fechado(self, baixar, configurado):
        """CAT-RF-03: ausência de credenciais não expõe bytes nem IDs remotos."""
        self.excursao.status = StatusExcursao.PUBLICADA
        self.excursao.save(update_fields=["status"])
        resposta = self.client.get(self._imagem())
        self.assertEqual(resposta.status_code, 404)
        baixar.assert_not_called()

    @patch("sire.views.drive_fotos.excluir")
    def test_foto_11_exclusao_exige_post(self, excluir):
        """Uma navegação GET não deve remover foto nem acionar o Drive."""
        self.client.force_login(self.agente_a)
        url = reverse("sire:remover_foto", args=[self.excursao.pk, self.foto.pk])
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 405)
        self.assertTrue(FotoExcursao.objects.filter(pk=self.foto.pk).exists())
        excluir.assert_not_called()

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.baixar", return_value=b"jpeg-ficticio")
    def test_foto_01_visitante_ve_foto_publicada(self, baixar, configurado):
        """CAT-RF-03: foto publicada pode ser consultada sem login."""
        self.excursao.status = StatusExcursao.PUBLICADA
        self.excursao.save(update_fields=["status"])
        resposta = self.client.get(self._imagem())
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta["Content-Type"], "image/jpeg")
        self.assertEqual(resposta["X-Content-Type-Options"], "nosniff")
        baixar.assert_called_once_with("drive-ficticio-foto-1")

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.baixar")
    def test_foto_12_referencia_excluida_nao_dispara_download(self, baixar, configurado):
        """Referência ausente não deve permitir acesso a bytes remotos."""
        self.excursao.status = StatusExcursao.PUBLICADA
        self.excursao.save(update_fields=["status"])
        url = self._imagem()
        self.foto.delete()
        resposta = self.client.get(url)
        self.assertEqual(resposta.status_code, 404)
        baixar.assert_not_called()

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.preparar_jpeg", return_value=b"jpeg-sintetico")
    @patch("sire.views.drive_fotos.enviar", return_value="drive-sintetico-2")
    def test_foto_13_upload_adquire_lock_antes_de_gravar(self, enviar, preparar, configurado):
        """Regressão estrutural: bloquear a excursão antes da contagem e gravação."""
        from unittest.mock import patch as mock_patch
        from django.core.files.uploadedfile import SimpleUploadedFile

        self.client.force_login(self.agente_a)
        original = Excursao.objects.select_for_update
        with mock_patch.object(Excursao.objects, "select_for_update", wraps=original) as lock:
            resposta = self.client.post(
                reverse("sire:adicionar_foto", args=[self.excursao.pk]),
                {"foto": SimpleUploadedFile("teste.jpg", b"x", content_type="image/jpeg")},
            )
        self.assertEqual(resposta.status_code, 302)
        lock.assert_called_once_with()
        enviar.assert_called_once()
        self.assertEqual(self.excursao.fotos.count(), 2)

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.preparar_jpeg", return_value=b"jpeg-sintetico")
    @patch("sire.views.drive_fotos.enviar", return_value="drive-sintetico-7")
    def test_foto_14_limite_recusado_antes_do_drive(self, enviar, preparar, configurado):
        from django.core.files.uploadedfile import SimpleUploadedFile

        for numero in range(2, 7):
            FotoExcursao.objects.create(excursao=self.excursao, drive_id=f"drive-sintetico-{numero}")
        self.client.force_login(self.agente_a)
        resposta = self.client.post(
            reverse("sire:adicionar_foto", args=[self.excursao.pk]),
            {"foto": SimpleUploadedFile("teste.jpg", b"x", content_type="image/jpeg")},
        )
        self.assertEqual(resposta.status_code, 302)
        self.assertEqual(self.excursao.fotos.count(), 6)
        enviar.assert_not_called()

    @patch("sire.views.drive_fotos.configurado", return_value=True)
    @patch("sire.views.drive_fotos.preparar_jpeg")
    @patch("sire.views.drive_fotos.enviar")
    def test_foto_15_upload_alheio_nega_antes_de_processar(self, enviar, preparar, configurado):
        """RN-03: nem mesmo formulário inválido revela ou processa outra agência."""
        self.client.force_login(self.agente_b)
        resposta = self.client.post(reverse("sire:adicionar_foto", args=[self.excursao.pk]), data={})
        self.assertEqual(resposta.status_code, 404)
        preparar.assert_not_called()
        enviar.assert_not_called()


class FotoConcorrenciaPostgreSQL(TransactionTestCase):
    """CAT-RF-03: dois agentes enviando simultaneamente à mesma excursão."""

    def setUp(self):
        self.agencia = Agencia.objects.create(nome="Agência sintética para concorrência")
        self.usuario = User.objects.create_user("agente_concorrencia", password="senha-sintetica")
        PerfilUsuario.objects.create(
            usuario=self.usuario, tipo=TipoPerfil.AGENTE, agencia=self.agencia
        )
        self.excursao = Excursao.objects.create(
            titulo="Teste concorrência", destino="Destino fictício",
            data_saida=date(2027, 4, 1), valor=Decimal("100.00"),
            capacidade=20, agencia=self.agencia, status=StatusExcursao.RASCUNHO,
        )
        for n in range(5):
            FotoExcursao.objects.create(excursao=self.excursao, drive_id=f"pre-{n}")

    def test_foto_16_dois_uploads_mesma_vaga_nao_criam_setima(self):
        import itertools
        import threading
        import time
        from concurrent.futures import ThreadPoolExecutor
        from django.core.files.uploadedfile import SimpleUploadedFile
        from django.db import connection, connections
        from django.test import Client

        if connection.vendor != "postgresql":
            self.skipTest("Concorrência de row-lock só é verificável em PostgreSQL.")

        pronto = threading.Barrier(2)
        proximo = itertools.count(1)
        ids_lock = threading.Lock()

        def enviar_falso(*args, **kwargs):
            with ids_lock:
                identificador = next(proximo)
            # Sem SELECT FOR UPDATE, duas requisições enxergariam 5 fotos
            # durante esse intervalo e ambas concluiriam o envio.
            time.sleep(0.2)
            return f"upload-concorrente-{identificador}"

        def requisicao(numero):
            cliente = Client()
            try:
                cliente.force_login(self.usuario)
                pronto.wait(timeout=15)
                return cliente.post(
                    reverse("sire:adicionar_foto", args=[self.excursao.pk]),
                    {"foto": SimpleUploadedFile(
                        f"imagem-{numero}.jpg", b"x", content_type="image/jpeg"
                    )},
                ).status_code
            finally:
                connections.close_all()

        with patch("sire.views.drive_fotos.configurado", return_value=True), \
             patch("sire.views.drive_fotos.preparar_jpeg", return_value=b"jpeg-sintetico"), \
             patch("sire.views.drive_fotos.enviar", side_effect=enviar_falso) as envio:
            with ThreadPoolExecutor(max_workers=2) as pool:
                respostas = list(pool.map(requisicao, (1, 2)))

        self.assertEqual(respostas, [302, 302])
        self.assertEqual(FotoExcursao.objects.filter(excursao=self.excursao).count(), 6)
        self.assertEqual(envio.call_count, 1)
