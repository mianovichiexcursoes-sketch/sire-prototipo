"""Arquivo que não é foto (ex.: vídeo) ou grande demais: aviso claro, nada enviado."""

from unittest.mock import patch

from django.contrib.staticfiles import finders
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings

from sire import drive_fotos
from sire.models import FotoExcursao

from .base import CasoSire, criar_agencia, criar_agente, criar_excursao

DRIVE = dict(
    SIRE_DRIVE_CLIENT_ID="ficticio",
    SIRE_DRIVE_CLIENT_SECRET="ficticio",
    SIRE_DRIVE_REFRESH_TOKEN="ficticio",
)


@override_settings(**DRIVE)
class ArquivoRecusado(CasoSire):
    def setUp(self):
        super().setUp()
        agencia = criar_agencia()
        criar_agente("agente", agencia)
        self.excursao, _ = criar_excursao(agencia, publicada=False)
        self.entrar("agente")
        self.url = f"/agente/excursoes/{self.excursao.pk}/fotos/nova/"

    def mensagens(self, resposta):
        return [str(m) for m in resposta.context["messages"]]

    def test_campo_so_oferece_imagens_e_carrega_o_aviso(self):
        pagina = self.client.get(f"/agente/excursoes/{self.excursao.pk}/editar/").content.decode()
        self.assertIn('accept="image/jpeg,image/png,image/webp"', pagina)
        self.assertIn('data-limite-bytes="5242880"', pagina)
        self.assertIn("sire/js/fotos-upload.js", pagina)

    def test_script_avisa_video_e_tamanho_antes_de_enviar(self):
        caminho = finders.find("sire/js/fotos-upload.js")
        self.assertIsNotNone(caminho)
        with open(caminho, encoding="utf-8") as arquivo:
            js = arquivo.read()
        for trecho in ("window.alert", "evento.preventDefault()", "um vídeo", "Enviando foto"):
            with self.subTest(trecho):
                self.assertIn(trecho, js)

    def test_video_pequeno_e_recusado_sem_chamar_o_drive(self):
        video = SimpleUploadedFile("passeio.mp4", b"\x00\x00\x00\x18ftypmp42" + b"0" * 2048, "video/mp4")
        with patch.object(drive_fotos, "enviar") as enviar:
            resposta = self.client.post(self.url, {"foto": video}, follow=True)
        enviar.assert_not_called()
        self.assertEqual(FotoExcursao.objects.count(), 0)
        self.assertTrue(any("JPG, PNG ou WebP" in m for m in self.mensagens(resposta)))

    def test_arquivo_grande_e_recusado_pelo_tamanho(self):
        grande = SimpleUploadedFile("filme.mp4", b"0" * (6 * 1024 * 1024), "video/mp4")
        with patch.object(drive_fotos, "enviar") as enviar, \
                patch.object(drive_fotos, "preparar_jpeg") as preparar:
            resposta = self.client.post(self.url, {"foto": grande}, follow=True)
        enviar.assert_not_called()
        preparar.assert_not_called()
        self.assertEqual(FotoExcursao.objects.count(), 0)
        texto = " ".join(self.mensagens(resposta))
        self.assertIn("Arquivo grande demais para foto", texto)
        self.assertIn("vídeos não são aceitos", texto)
