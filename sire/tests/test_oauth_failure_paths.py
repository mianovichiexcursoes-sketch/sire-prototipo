"""Regressões isoladas para falhas parciais de configuração OAuth.

Não usa rede, credenciais reais ou serviço Render. Executar:
python -m unittest sire.tests.test_oauth_failure_paths -v
"""
import io
import json
from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import patch
from urllib.error import HTTPError

from scripts import autorizacao_drive as oauth


class OAuthFailurePathsTests(TestCase):
    def test_falha_no_segundo_put_interrompe_sem_expor_segredos(self):
        valores = {
            "SIRE_DRIVE_CLIENT_ID": "id-sintetico",
            "SIRE_DRIVE_CLIENT_SECRET": "segredo-sintetico",
            "SIRE_DRIVE_REFRESH_TOKEN": "refresh-sintetico",
        }
        chamadas = []

        def responder(req, **kwargs):
            chamadas.append(req)
            if req.get_method() == "GET":
                return io.BytesIO(json.dumps({
                    "name": "sire-oauth-test-isolado",
                    "branch": "test/oauth-falha-parcial-20261117",
                }).encode())
            if len([r for r in chamadas if r.get_method() == "PUT"]) == 2:
                raise HTTPError(req.full_url, 503, "indisponivel", {}, None)
            return io.BytesIO(b'{}')

        saida = io.StringIO()
        with patch.object(oauth, "urlopen", side_effect=responder), redirect_stdout(saida):
            with self.assertRaises(HTTPError):
                oauth.enviar_render("srv-sintetico", "api-sintetica", valores)
        self.assertEqual([r.get_method() for r in chamadas], ["GET", "PUT", "PUT"])
        self.assertEqual(saida.getvalue(), "")
        for segredo in valores.values():
            self.assertNotIn(segredo, saida.getvalue())

    def test_servico_sem_nome_de_ensaio_nao_recebe_put(self):
        chamadas = []

        def responder(req, **kwargs):
            chamadas.append(req)
            return io.BytesIO(b'{"name":"servico-desconhecido","branch":"outra"}')

        with patch.object(oauth, "urlopen", side_effect=responder):
            with self.assertRaises(ValueError):
                oauth.enviar_render("srv-sintetico", "api-sintetica", {
                    "SIRE_DRIVE_CLIENT_ID": "id-sintetico"
                })
        self.assertEqual(len(chamadas), 1)
        self.assertEqual(chamadas[0].get_method(), "GET")
