"""Credenciais exclusivamente sintéticas; nenhuma chamada externa."""
import io
import json
from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import patch

from scripts import autorizacao_drive as oauth


class OAuthDriveTests(TestCase):
    def test_scope_exato(self):
        oauth.validar_tokens({'refresh_token': 'ficticio', 'scope': oauth.SCOPE})
        for scope in ['', 'https://www.googleapis.com/auth/drive', oauth.SCOPE + ' openid']:
            with self.subTest(scope=scope), self.assertRaises(ValueError):
                oauth.validar_tokens({'refresh_token': 'ficticio', 'scope': scope})

    def test_sem_refresh_token(self):
        with self.assertRaises(ValueError):
            oauth.validar_tokens({'scope': oauth.SCOPE})

    def test_id_invalido_nao_faz_rede(self):
        with patch.object(oauth, 'urlopen') as rede, self.assertRaises(ValueError):
            oauth.enviar_render('../outro', 'ficticio', {})
        rede.assert_not_called()

    def test_demo_protegida(self):
        for service in [
            {'name': 'sire-demo'}, {'name': 'sire-oauth-test', 'branch': 'main'},
            {'name': 'sire-oauth-test', 'branch': 'etapa/postgresql-windows'},
            {'name': 'outro'},
            {'name': 'sire-oauth-test', 'serviceDetails': {'url': 'https://sire-demo.onrender.com/'}},
        ]:
            with self.subTest(service=service), patch.object(oauth, 'urlopen') as rede:
                rede.return_value.__enter__.return_value = io.BytesIO(json.dumps(service).encode())
                with self.assertRaises(ValueError):
                    oauth.enviar_render('srv-ficticio', 'chave-ficticia', {'SIRE_DRIVE_CLIENT_ID': 'ficticio'})
                self.assertEqual(rede.call_count, 1)

    def test_env_individual_sem_saida(self):
        creds = dict(SIRE_DRIVE_CLIENT_ID='id-ficticio', SIRE_DRIVE_CLIENT_SECRET='segredo-ficticio', SIRE_DRIVE_REFRESH_TOKEN='token-ficticio')
        saida = io.StringIO()
        def responder(req, **kwargs):
            if req.get_method() == 'GET':
                return io.BytesIO(b'{"name":"sire-oauth-test","branch":"fix/oauth-seguro-20261117"}')
            return io.BytesIO(b'{"value":"resposta-ficticia-sensivel"}')
        with patch.object(oauth, 'urlopen', side_effect=responder) as rede, redirect_stdout(saida):
            oauth.enviar_render('srv-ficticio', 'api-ficticia', creds)
        self.assertEqual(saida.getvalue(), '')
        requests = [call.args[0] for call in rede.call_args_list][1:]
        self.assertEqual(len(requests), 3)
        for req, (key, value) in zip(requests, creds.items()):
            self.assertEqual(req.method, 'PUT')
            self.assertEqual(req.full_url, 'https://api.render.com/v1/services/srv-ficticio/env-vars/' + key)
            self.assertEqual(json.loads(req.data), {'value': value})
            self.assertEqual(req.get_header('Authorization'), 'Bearer api-ficticia')

    def test_sem_terminal_seguro_interrompe(self):
        with patch.dict(oauth.os.environ, {}, clear=True), patch.object(oauth, 'getpass', side_effect=oauth.GetPassWarning):
            with self.assertRaises(oauth.GetPassWarning):
                oauth.segredo('SIRE_DRIVE_CLIENT_SECRET')
