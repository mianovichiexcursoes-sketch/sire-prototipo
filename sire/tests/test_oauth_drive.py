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

    def test_grupo_sem_vinculo_nem_credenciais_extras(self):
        creds = dict(SIRE_DRIVE_CLIENT_ID='id-ficticio', SIRE_DRIVE_CLIENT_SECRET='segredo-ficticio', SIRE_DRIVE_REFRESH_TOKEN='token-ficticio')
        def responder(req, **kwargs):
            if req.get_method() == 'GET':
                return io.BytesIO(b'{"name":"SIRE.","id":"tea-ficticio"}')
            resposta = io.BytesIO(b'{"envVars":[{"value":"segredo-ficticio"}]}')
            resposta.status = 201
            return resposta
        saida = io.StringIO()
        with patch.object(oauth, 'urlopen', side_effect=responder) as rede, redirect_stdout(saida):
            nome = oauth.enviar_grupo_render('tea-ficticio', 'api-ficticia', creds)
        self.assertTrue(nome.startswith('sire-drive-oauth-'))
        self.assertEqual(saida.getvalue(), '')
        self.assertEqual(rede.call_count, 2)
        req = rede.call_args.args[0]
        self.assertEqual(req.full_url, 'https://api.render.com/v1/env-groups')
        self.assertEqual(req.get_method(), 'POST')
        body = json.loads(req.data)
        self.assertEqual(body['serviceIds'], [])
        self.assertEqual(body['secretFiles'], [])
        self.assertEqual(body['ownerId'], 'tea-ficticio')
        self.assertEqual({v['key']: v['value'] for v in body['envVars']}, creds)
        self.assertNotIn('api-ficticia', req.data.decode())

    def test_workspace_errado_impede_gravacao(self):
        for workspace in [{'name': 'Outro', 'id': 'tea-ficticio'}, {'name': 'SIRE.', 'id': 'tea-outro'}]:
            with self.subTest(workspace=workspace), patch.object(oauth, 'urlopen') as rede:
                rede.return_value.__enter__.return_value = io.BytesIO(json.dumps(workspace).encode())
                with self.assertRaises(ValueError):
                    oauth.enviar_grupo_render('tea-ficticio', 'ficticio', {k: 'ficticio' for k in oauth.CHAVES_DRIVE})
                self.assertEqual(rede.call_count, 1)

    def _rede_grupos(self, grupos, detalhe=None):
        def responder(req, **kwargs):
            if '/env-groups?' in req.full_url:
                return io.BytesIO(json.dumps([{'envGroup': g, 'cursor': 'c'} for g in grupos]).encode())
            return io.BytesIO(json.dumps(detalhe or {}).encode())
        return patch.object(oauth, 'urlopen', side_effect=responder)

    def test_lista_somente_grupos_do_drive(self):
        grupos = [{'id': 'evg-a', 'name': 'sire-drive-oauth-1a2b'}, {'id': 'evg-b', 'name': 'outro'}]
        with self._rede_grupos(grupos):
            self.assertEqual(oauth.grupos_drive_existentes('tea-ficticio', 'k'), ['sire-drive-oauth-1a2b'])

    def test_conferir_grupo_sem_expor_valores(self):
        detalhe = {'envVars': [{'key': k, 'value': 'segredo-ficticio'} for k in oauth.CHAVES_DRIVE]}
        saida = io.StringIO()
        with self._rede_grupos([{'id': 'evg-abc', 'name': 'sire-drive-oauth-x', 'serviceLinks': []}], detalhe), redirect_stdout(saida):
            self.assertEqual(oauth.conferir_grupo('tea-ficticio', 'k', 'sire-drive-oauth-x'), ('evg-abc', True))
        self.assertEqual(saida.getvalue(), '')

    def test_conferir_grupo_recusa_vinculo_chave_extra_ou_vazia(self):
        cheio = [{'key': k, 'value': 'v'} for k in oauth.CHAVES_DRIVE]
        casos = {
            'vinculado': ([{'id': 'evg-a', 'name': 'g', 'serviceLinks': [{'id': 'srv-x'}]}], {'envVars': cheio}),
            'chave extra': ([{'id': 'evg-a', 'name': 'g'}], {'envVars': cheio + [{'key': 'RENDER_API_KEY', 'value': 'v'}]}),
            'valor vazio': ([{'id': 'evg-a', 'name': 'g'}], {'envVars': cheio[:2] + [{'key': cheio[2]['key'], 'value': ''}]}),
            'ausente': ([{'id': 'evg-a', 'name': 'outro'}], {}),
        }
        for rotulo, (grupos, detalhe) in casos.items():
            with self.subTest(rotulo), self._rede_grupos(grupos, detalhe), self.assertRaises(ValueError):
                oauth.conferir_grupo('tea-ficticio', 'k', 'g')

    def test_formato_recusa_valor_trocado_sem_exibir(self):
        # Ex.: o NOME da chave colado no lugar da chave do Render.
        casos = {
            'RENDER_API_KEY': ('sire-drive-temporaria', 'rnd_' + 'A' * 24),
            'SIRE_DRIVE_CLIENT_ID': ('GOCSPX-ficticio', '123-abc.apps.googleusercontent.com'),
            'SIRE_DRIVE_CLIENT_SECRET': ('123-abc.apps.googleusercontent.com', 'GOCSPX-' + 'b' * 20),
        }
        for nome, (errado, certo) in casos.items():
            with self.subTest(nome), patch.dict(oauth.os.environ, {}, clear=True):
                with patch.object(oauth, 'getpass', return_value=errado):
                    with self.assertRaises(ValueError) as erro:
                        oauth.segredo(nome)
                    self.assertNotIn(errado, str(erro.exception))
                with patch.object(oauth, 'getpass', return_value=' ' + certo + ' '):
                    self.assertEqual(oauth.segredo(nome), certo)

    def test_renovacao_le_cliente_do_grupo_sem_exibir(self):
        detalhe = {'envVars': [{'key': k, 'value': k.lower() + '-ficticio'} for k in oauth.CHAVES_DRIVE]}
        saida = io.StringIO()
        with self._rede_grupos([{'id': 'evg-abc', 'name': 'sire-drive-oauth-x'}], detalhe), redirect_stdout(saida):
            grupo_id, nome, valores = oauth.ler_grupo_drive('tea-ficticio', 'k')
        self.assertEqual((grupo_id, nome), ('evg-abc', 'sire-drive-oauth-x'))
        self.assertEqual(valores['SIRE_DRIVE_CLIENT_ID'], 'sire_drive_client_id-ficticio')
        self.assertEqual(saida.getvalue(), '')

    def test_renovacao_recusa_grupo_vinculado_ou_ambiguo(self):
        cheio = {'envVars': [{'key': k, 'value': 'v'} for k in oauth.CHAVES_DRIVE]}
        casos = {
            'vinculado': [{'id': 'evg-a', 'name': 'sire-drive-oauth-a', 'serviceLinks': [{'id': 'srv-x'}]}],
            'dois grupos': [{'id': 'evg-a', 'name': 'sire-drive-oauth-a'}, {'id': 'evg-b', 'name': 'sire-drive-oauth-b'}],
            'nenhum': [{'id': 'evg-a', 'name': 'outro'}],
        }
        for rotulo, grupos in casos.items():
            with self.subTest(rotulo), self._rede_grupos(grupos, cheio), self.assertRaises(ValueError):
                oauth.ler_grupo_drive('tea-ficticio', 'k')

    def test_renovacao_troca_somente_o_refresh_token(self):
        with patch.object(oauth, 'urlopen', return_value=io.BytesIO(b'{"value":"x"}')) as rede:
            oauth.atualizar_token_grupo('evg-abc', 'k', 'novo-token-ficticio')
        req = rede.call_args.args[0]
        self.assertEqual(req.get_method(), 'PUT')
        self.assertEqual(req.full_url, 'https://api.render.com/v1/env-groups/evg-abc/env-vars/SIRE_DRIVE_REFRESH_TOKEN')
        self.assertEqual(json.loads(req.data), {'value': 'novo-token-ficticio'})
        with patch.object(oauth, 'urlopen') as rede, self.assertRaises(ValueError):
            oauth.atualizar_token_grupo('../outro', 'k', 'x')
        rede.assert_not_called()

    def test_grupo_rejeita_segredos_extras_antes_da_rede(self):
        creds = {k: 'ficticio' for k in oauth.CHAVES_DRIVE}
        creds['RENDER_API_KEY'] = 'ficticio'
        with patch.object(oauth, 'urlopen') as rede, self.assertRaises(ValueError):
            oauth.enviar_grupo_render('tea-ficticio', 'ficticio', creds)
        rede.assert_not_called()
