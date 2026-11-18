# SIRE — Auditoria de cobertura e CI da PR #9 (18/11/2026)

**Natureza:** verificação independente de código e metadados; não constitui execução de testes, autorização OAuth, aceite, merge ou deploy. Branch examinada: `fix/oauth-grupo-render-20261117`; commit identificado `2a354a75f01401f49db639fa6e52752fe7a2d60c` ([commit](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/commit/2a354a75f01401f49db639fa6e52752fe7a2d60c)).

## Gate de fontes

Lidos diretamente pelo conector Google Drive, por IDs exatos, em 18/11/2026: regras RN-01–41, desenvolvimento ER-SIRE 2.1, guia de implementação, UC01–UC14, requisitos, complemento CAT revisão 0.2 e registro de implementação. Esta leitura pontual não equivale à auditoria integral da monografia. Preservar baseline, seis entidades e 14 UC históricos; OAuth é incremento separado.

## Evidências observadas

- `sire/tests/test_oauth_drive.py` na branch da PR #9 contém **nove métodos** de `unittest.TestCase`; três exercitam especificamente criação de Environment Group sem vínculo, rejeição de workspace divergente e recusa de credenciais extras. São **testes com mocks**, não chamadas reais ao Google ou Render.
- `.github/workflows/testes.yml` configura `python manage.py test --verbosity 2` em SQLite e PostgreSQL para eventos push/PR. Isso descreve o gatilho previsto, não demonstra que um workflow tenha sido executado.
- Consulta `fetch_commit_workflow_runs` para o SHA acima retornou **lista vazia**. A API consultada limita-se à primeira página e a runs com evento pull_request; portanto, **CI NÃO CONFIRMADO** para este SHA, e a lista vazia não comprova ausência de outros runs.
- O guia `docs/OAUTH_GRUPO_RENDER.md` declara nove testes locais aprovados, mas não fornece nesta verificação logs brutos com versão Python e SHA; classificar como **resultado declarado pelo autor, não reproduzido nesta rodada**.
- O código inspecionado cria grupo sem `serviceIds` e `secretFiles` e valida o workspace por nome e ID; não prova provisionamento real, autorização `drive.file`, durabilidade de fotos nem atomicidade após falha de rede.

## Matriz de rastreabilidade incremental

| EVO / requisito | Código | Teste | Evidência | Situação | Monografia |
|---|---|---|---|---|---|
| EVO-OAUTH-01: escopo mínimo `drive.file` | `scripts/autorizacao_drive.py` | `test_scope_exato`, `test_sem_refresh_token` | arquivo da branch lido; sem execução independente | PENDENTE aceite | seção de evolução OAuth |
| EVO-OAUTH-02: não afetar demo | `conferir_workspace`, `enviar_grupo_render` | `test_grupo_sem_vinculo_nem_credenciais_extras`, `test_workspace_errado_impede_gravacao` | mocks lidos; CI não confirmado | PENDENTE ensaio real isolado | riscos/controles |
| EVO-OAUTH-03: não transmitir segredos extras | `CHAVES_DRIVE` | `test_grupo_rejeita_segredos_extras_antes_da_rede` | inspeção estática | PENDENTE regressão | LGPD/segurança |

## Dependências e retomada

**B — BLOQUEADO (integração real):** falta evidência de consentimento OAuth próprio do aplicativo, grupo criado no workspace correto e serviço/banco de ensaio isolados. Responsável: autora/operador autorizado Google Cloud/Render. Impacto: bloqueia upload, exclusão, persistência pós-deploy e aceite real. Retomar após autorização e infraestrutura comprovadas sem revelar segredos.

**F — PENDENTE (testes):** executar os nove testes na branch/commit exatos, arquivar saída e versão Python; conferir GitHub Actions por URL de run/commit, não inferir aprovação por configuração YAML. Reexecutar se HEAD mudar. Testes independentes da branch `test/oauth-falha-parcial-20261117` cobrem o caminho antigo de PUT sequencial, **não** validam o modo de grupo da PR #9.

**A — EM REVISÃO:** não integrar PRs #2/#7/#9/#10 sem conciliar HEAD, bases e atividade do Work. **C — BLOQUEADO** para coleta de CPF até finalidade/necessidade LGPD aprovadas. **D/E/G — PENDENTES.** Nenhum dado real, migração, merge ou deploy foi alterado nesta auditoria.
