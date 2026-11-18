# OAuth do Google Drive — execução real de 18/11/2026

Execução assistida por IA (Claude Code), no computador Windows da autora, sobre
a PR #9 (`fix/oauth-grupo-render-20261117`), na branch separada
`fix/oauth-execucao-real-20261118`. Sem merge, sem deploy e sem alteração da
demonstração pública. A baseline ER-SIRE 2.1 e o fluxo de reservas não mudam.

## 1. Acessos efetivamente usados

| Recurso | Como | Observação |
| --- | --- | --- |
| Terminal | PowerShell do computador da autora | navegador e retorno local (127.0.0.1:8766) na mesma máquina |
| Google Cloud | navegador do app, conta da agência logada pela autora | — |
| Render | painel, com login da autora; API com chave temporária restrita | — |
| GitHub | `git push` com a credencial já salva | sem `gh` nem token |

## 2. Conferência do Google Cloud (antes de criar)

O registro anterior indicava projeto, API, consentimento e cliente já criados.
Na conta logada, o projeto **SIRE TCC** (`sire-tcc`) existia, mas:

- a Google Drive API estava **desativada**;
- a tela de consentimento **não estava configurada**;
- **não havia cliente OAuth** no projeto nem no outro projeto da conta.

Com autorização da autora, foram criados (sem duplicatas):

| Item | Valor |
| --- | --- |
| Google Drive API | Ativada |
| App | SIRE — Fotos de excursões, público **externo**, status **Testando** |
| Usuária de teste | conta da agência (1 de 100) |
| Escopos | somente `https://www.googleapis.com/auth/drive.file` (não confidencial) |
| Cliente | SIRE — Autorização do Drive, tipo **App para computador** |

O aceite da política de dados do Google e o clique em "Criar" do cliente foram
feitos pela autora. A chave secreta não foi lida pela IA nem baixada em arquivo.

## 3. Correções no script antes da execução

- Para se já existir grupo `sire-drive-oauth-*` (evita duplicata ao repetir).
- Relê o grupo criado e confere exatamente as 3 chaves preenchidas e nenhum
  serviço vinculado, sem imprimir valores.
- Segredos pedidos em **janela local mascarada** (•••), com contador de
  caracteres e conferência de formato antes do uso (`rnd_`, `…apps.googleusercontent.com`,
  `GOCSPX-`). `--sem-janela` mantém a entrada pelo terminal, com a mesma conferência.
- `sire/drive_fotos.py`: parâmetro `pageSize` (era `page_size`, inexistente na API v3).

### Incidente na primeira tentativa

A entrada oculta do terminal não dava retorno visual. O nome da chave do
Render foi enviado no lugar da chave (HTTP 401, nada gravado) e, em seguida, a
chave foi colada no prompt do PowerShell, ficando visível na tela e no
histórico. Medidas: troca da entrada por janela mascarada com conferência de
formato (commit `11786b9`) e **revogação da chave exposta**, feita no painel
do Render em 18/11/2026 após o ensaio, com autorização da autora.

## 4. Autorização e gravação no Render (real)

Saída do script, sem valores:

```
Workspace SIRE. confirmado; nenhum grupo anterior do Drive encontrado.
Autorização do Google recebida com escopo drive.file.
CONCLUIDO: grupo criado no Render: sire-drive-oauth-36a0572f (evg-dbuq4kom7kps73d5trfg)
Conferido: exatamente 3 chaves preenchidas e nenhum serviço vinculado.
A demonstração pública não foi alterada.
```

Conferência independente no painel do Render: grupo com 3 variáveis, 0 arquivos
secretos, "You haven't linked this environment group to any services"; o
serviço `sire-demo` não tem grupo vinculado nem variáveis `SIRE_DRIVE_*`. A
chave da API do Render não integra o grupo. Chave usada com permissões
restritas: leitura do workspace e leitura/escrita de Environment groups.

## 5. Ensaio real das fotos

`scripts/ensaio_drive_real.py`, 18/11/2026 10:09 (-03:00): Python 3.14.8,
Django 6.1.2, PostgreSQL 18 **local** (banco `sire` do computador da autora,
nunca o da demo), credenciais lidas do grupo do Render só em memória, imagem
sintética gerada pelo script (faixas coloridas e texto, sem pessoas).
Evidência: [`evidencias/2026-11-18_1008_drive_real/resultados.json`](../evidencias/2026-11-18_1008_drive_real/resultados.json).

| # | Verificação | Resultado |
| --- | --- | --- |
| 1 | Upload pela agência dona (publicada e rascunho) | Conforme (2 de 2) |
| 2 | Arquivo criado no Drive como JPEG | Conforme |
| 3 | Arquivo não público nem compartilhado | Conforme (`shared=False`, só permissão `user`) |
| 4 | Visitante vê foto de excursão publicada | Conforme (HTTP 200, JPEG) |
| 5 | Resposta sem cache reutilizável | Conforme (`no-store`) |
| 6 | Página não expõe link direto ao Drive | Conforme |
| 7 | Foto de rascunho só para a agência dona | Conforme (visitante, passageiro e outra agência: 404; dona: 200) |
| 8 | Outra agência não envia foto | Conforme (404, contagem inalterada) |
| 9 | Outra agência não remove foto | Conforme (404, foto preservada no banco e no Drive) |
| 10 | Persistência após reinício (processo novo, cache vazio, token obtido do zero) | Conforme |
| 11 | Remoção pela agência dona apaga banco e Drive | Conforme |
| 12 | Foto removida deixa de ser servida | Conforme (404) |
| 13 | Limpeza do ensaio | Conforme (0 arquivos restantes) |

**Resultado: 13 de 13 conformes.** As linhas `Not Found` no terminal são os
registros esperados das tentativas negadas.

Ficou no Drive da agência apenas a pasta vazia `SIRE - Fotos de excursões`,
criada pelo aplicativo.

## 6. O que NÃO foi comprovado

- Persistência após **reinício/redeploy no Render**: não há ambiente de ensaio
  persistente isolado. O plano gratuito permite um único PostgreSQL por
  workspace, já usado pela demo; nenhum recurso pago foi criado. O teste 10
  comprova a persistência após reinício **do processo local**, com o banco local.
- Integração das fotos na demonstração pública: o grupo não foi vinculado e a
  galeria (PR #2) não está publicada.
- Concorrência de uploads simultâneos contra o Drive real (coberta só por
  testes com Drive simulado).

## 7. Pendências e riscos

1. ~~Revogar no Render a chave de API usada~~ — **feito** em 18/11/2026: o
   painel mostra "No provisioned API keys"; o grupo segue presente e válido.
2. ~~Validade do token (modo Testando)~~ — **resolvido** em 18/11/2026: ver
   seção 8.
3. Ambiente persistente isolado para o teste de redeploy: menor alternativa
   viável sem custo é um serviço web gratuito de ensaio, vinculado ao grupo,
   usando um PostgreSQL externo gratuito (não o da demo); depende de decisão.
4. Revisar e integrar a cadeia de PRs (#2, #5, #7, #9 e esta) antes de
   qualquer publicação das fotos.

## 8. Publicação do app e renovação do token (18/11/2026, 10:30)

Para evitar a expiração de 7 dias dos tokens emitidos em modo Testando:

1. **Branding:** página inicial `https://sire-demo.onrender.com/`, política de
   privacidade `https://sire-demo.onrender.com/privacidade/` e domínio
   autorizado `sire-demo.onrender.com`. Sem logotipo.
2. **Publicação:** status alterado de "Testando" para **"Em produção"**, com
   autorização da autora. Com 1 domínio, sem logotipo e somente o escopo não
   confidencial `drive.file`, o Google não exigiu verificação.
3. **Renovação:** novo modo `scripts/autorizacao_drive.py --renovar-token
   WORKSPACE_ID` (commit `f76ffb2`). Lê o ID e a chave secreta do cliente do
   grupo do Render só em memória (o Google não volta a exibir a chave
   secreta), faz nova autorização e troca apenas `SIRE_DRIVE_REFRESH_TOKEN`.
   Saída:

   ```
   Workspace SIRE. confirmado; cliente lido do grupo sire-drive-oauth-36a0572f.
   Autorização do Google recebida com escopo drive.file.
   CONCLUIDO: token renovado no grupo sire-drive-oauth-36a0572f (evg-dbuq4kom7kps73d5trfg)
   Conferido: 3 chaves preenchidas e nenhum serviço vinculado.
   ```

   Uma primeira tentativa recebeu HTTP 401 porque a chave nova do Render
   ainda não tinha sido gerada (foi colada a chave antiga, já revogada);
   nada foi alterado.
4. **Ensaio repetido com o token novo:** 18/11/2026 10:32, **13 de 13
   conformes** — [`evidencias/2026-11-18_1032_drive_real/resultados.json`](../evidencias/2026-11-18_1032_drive_real/resultados.json).
5. **Chave temporária do Render** (`sire-drive-renovacao`, permissões
   restritas) revogada logo depois; o painel mostra "No provisioned API keys".

Aviso de privacidade: atualizado nesta branch com a seção "Fotos das
excursões" (Drive da responsável, acesso restrito a arquivos do próprio SIRE,
sem link público, visibilidade só após publicação, remoção de metadados e
vedação de fotos com pessoas identificáveis). A demonstração pública ainda
exibe a versão anterior até a integração da cadeia de PRs. Teste
`sire/tests/test_privacidade_fotos.py` comprova que o JPEG enviado ao Drive
não carrega EXIF nem coordenadas GPS do original.
