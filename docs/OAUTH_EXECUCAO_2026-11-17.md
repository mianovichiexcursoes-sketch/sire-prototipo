# OAuth Drive — execução de 17/11/2026

Implementação assistida por IA. Alteração isolada sobre `fix/fotos-cache-lock-20261117`, sem merge ou deploy. Não altera modelo de dados, baseline ER-SIRE 2.1 ou regras de reserva.

## Fontes lidas nesta execução

- Documento oficial complementar CAT, revisão 0.2 e seção 8: https://docs.google.com/document/d/1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is/edit
- Regras de negócio RN-01–41: https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit
- README, documentação do incremento, progresso executivo da branch documental e código das fotos/OAuth.
- OAuth desktop/PKCE: https://developers.google.com/identity/protocols/oauth2/native-app
- Atualização individual de variável: https://api-docs.render.com/reference/update-env-var
- Segredos Render: https://render.com/docs/configure-environment-variables.md

## Problema corrigido

O script anterior imprimia o refresh token no terminal. Agora solicita entradas ocultas, recusa terminal sem ocultação, valida o escopo retornado como exatamente drive.file e encaminha as credenciais diretamente por HTTPS para três campos de ambiente no Render. Não imprime token, segredo, código ou URL de autorização e não escreve arquivos com credenciais. Mantém PKCE S256 e state, recusa parâmetros duplicados e tolera requisições inválidas até o prazo de 180 segundos. Resposta callback sem cache/referrer. Erros do provedor são substituídos por mensagem genérica na entrada CLI.

O serviço alvo deve ser de ensaio, com nome iniciado por sire-oauth-test. Nome sire-demo, URL pública atual e branches main/etapa/postgresql-windows são recusados. Atualizações são individuais; demais variáveis não são lidas/substituídas. Falha de rede pode deixar configuração parcial. Não há rollback automático. O script não solicita deploy. Exige navegador local no mesmo computador do callback; não executar esperando que o callback do navegador remoto chegue ao shell local.

## Evidências desta rodada

Python 3.12, ambiente virtual descartável, SQLite de teste; credenciais exclusivamente fictícias e rede simulada nos testes novos.

- `python manage.py test --noinput`: 90 testes, 87 aprovados, 3 pulados (concorrência PostgreSQL), OK.
- Seis testes novos: escopo exato/rejeição ampliada, ausência de refresh token, ID de serviço inválido sem rede, bloqueio de destinos públicos, PUT individual sem saída sensível, recusa de entrada sem ocultação.
- Testes de fotos herdados verificam upload/exibição/remoção e isolamento da aplicação com Drive simulado. Não comprovam permissões ou armazenamento do Google real.
- `python manage.py check`: sem problemas.
- `python manage.py makemigrations --check --dry-run`: sem alterações.
- `git diff --check`: sem erros.

## Bloqueios observados, não inferidos

1. Google Cloud Console em https://console.cloud.google.com/ retornou página “Site Unavailable / Unable to access this site.” A mesma resposta persistiu após uma recarga. Não chegou à tela de login. Não há evidência de bloqueio por robô, nem motivo para afirmar indisponibilidade global. Não foi possível criar projeto, ativar API ou configurar consentimento/cliente.
2. **Resolvido após confirmação da autora:** workspace “SIRE.” autorizado e consultado. Inventário: somente serviço sire-demo e banco sire-demo-db, plano free, PostgreSQL 18, Oregon. Serviço live no commit 7c53134264953908e8884bb588dd123d1d4cb972, branch etapa/postgresql-windows; nenhum serviço ou segredo foi alterado.
3. Não houve autorização real da conta Google, obtenção de token, configuração de credenciais no Render, upload remoto, inspeção de permissões Drive, exclusão remota ou teste de persistência após redeploy.

## Continuidade

Workspace confirmado; recuperar acesso ao Console, preparar projeto/API/consentimento apenas drive.file e cliente desktop. Solicitar participação da titular no login/consentimento quando a página estiver disponível. Criar ou identificar serviço e banco descartáveis de ensaio, sem banco da demo. Autorizar e configurar segredos por canal protegido. Ensaiar imagem sintética: upload, galeria pública somente após publicação, rascunho restrito à agência, remoção, ausência de compartilhamento público no Drive e persistência após redeploy. Revisar cadeia de PRs antes de qualquer promoção. Tokens de aplicativo externo em Testing podem expirar em sete dias: verificar o estado de publicação antes do aceite de persistência duradoura.

## Continuidade após confirmação do workspace

- Google Cloud Console novamente indisponível antes do login; não foi solicitada senha nem consentimento fora do Google.
- CI da PR #7, commit `9b2879ce6cf8639bbae94c133c00641347da7afd`: [suíte SQLite/PostgreSQL](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44084972576) e [regressão fotos](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44084972698) concluídas com sucesso. Job PostgreSQL, incluindo concorrência, confirmado separadamente. Isso não valida Drive real.
- PR #7 sem conflito com sua base no momento da consulta; continua em rascunho, sem merge.
- Não há ambiente de ensaio Render. A documentação atual permite apenas um PostgreSQL free ativo por workspace; a vaga já está ocupada pela demo. Referência consultada: https://render.com/docs/free.md (Single-instance limit).
- Não criar SQLite efêmero como prova de persistência, não compartilhar o banco da demo, não contratar plano pago automaticamente. O ensaio persistente precisa de banco isolado externo já disponível ou decisão explícita de infraestrutura. Nenhuma cobrança ou recurso novo criado.
- Bloqueios restantes: acesso ao Google Cloud/OAuth e infraestrutura persistente isolada para teste de redeploy. Nenhuma credencial real foi obtida ou armazenada nesta rodada.
