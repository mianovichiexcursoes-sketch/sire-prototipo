"""Aviso de privacidade das fotos e remoção de metadados antes do envio ao Drive."""

import io

from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

from sire import drive_fotos

from .base import CasoSire


def jpeg_com_localizacao():
    """JPEG sintético com EXIF de câmera e coordenadas GPS (fictícias)."""
    imagem = Image.new("RGB", (64, 48), "#97254e")
    exif = Image.Exif()
    exif[0x010F] = "Camera Ficticia"  # Make
    exif[0x0132] = "2026:11:18 10:00:00"  # DateTime
    gps = exif.get_ifd(0x8825)
    gps[1] = "S"
    gps[2] = (21.0, 8.0, 0.0)
    gps[3] = "W"
    gps[4] = (47.0, 59.0, 0.0)
    saida = io.BytesIO()
    imagem.save(saida, "JPEG", exif=exif)
    return saida.getvalue()


class MetadadosRemovidos(CasoSire):
    def test_original_tem_localizacao(self):
        with Image.open(io.BytesIO(jpeg_com_localizacao())) as foto:
            self.assertTrue(foto.getexif().get_ifd(0x8825))

    def test_jpeg_enviado_ao_drive_nao_tem_exif_nem_localizacao(self):
        arquivo = SimpleUploadedFile("praia.jpg", jpeg_com_localizacao(), "image/jpeg")
        dados = drive_fotos.preparar_jpeg(arquivo)
        with Image.open(io.BytesIO(dados)) as foto:
            exif = foto.getexif()
            self.assertEqual(len(exif), 0)
            self.assertFalse(exif.get_ifd(0x8825))
        self.assertNotIn(b"Camera Ficticia", dados)


class AvisoDasFotos(CasoSire):
    def test_aviso_explica_o_armazenamento_das_fotos(self):
        resposta = self.client.get("/privacidade/")
        for trecho in (
            "Fotos das excursões",
            "Google Drive",
            "só tem acesso aos arquivos que ele",
            "não ficam públicas",
            "enquanto ela é rascunho",
            "localização",
            "passageiros ou outras pessoas",
        ):
            with self.subTest(trecho):
                self.assertContains(resposta, trecho)
