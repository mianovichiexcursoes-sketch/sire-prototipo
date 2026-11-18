# SIRE — Evidência integral dos logs CI da PR #9 (18/11/2026)

## Escopo e proveniência
Revisão independente da execução [44145474063](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44145474063), associada ao commit `2a354a75f01401f49db639fa6e52752fe7a2d60c` da [PR #9](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/9). Logs obtidos diretamente dos jobs GitHub Actions, sem executar novos testes, sem alterar código ou demo. Fontes normativas lidas por IDs originais no Drive em 18/11/2026: RN-01–RN-41, baseline ER-SIRE 2.1, guia, UC01–UC14, requisitos 3.0, complemento CAT 0.2 e registro de implementação; monografia, modelo IFSP, regulamento, parecer e histórico também consultados. Não houve atualização acadêmica original.

## Comandos e resultados observados nos logs
| Job / ID | Comandos observados | Resultado literal | Limitação |
|---|---|---|---|
| `fotos-sqlite` / 134259294641 | `python manage.py check`; `python manage.py makemigrations --check --dry-run`; `python manage.py test sire.test_fotos_regressao --verbosity 2` | `Ran 17 tests in 0.864s`; `OK (skipped=1)`; `Applying sire.0007_ficha_e_fotos_drive... OK` | 16 aprovados, 1 ignorado por depender de row-lock PostgreSQL; migração em banco descartável |
| `fotos-postgresql` / 134259295337 | `python manage.py check`; `python manage.py makemigrations --check --dry-run`; `python manage.py test sire.test_fotos_regressao --verbosity 2` | `Ran 17 tests in 1.252s`; `OK`; `Applying sire.0007_ficha_e_fotos_drive... OK` | 17 aprovados em banco descartável; Drive simulado |

**Cobertura observável:** isolamento entre agências (RN-03), cache de rascunho/publicação, limite de seis fotos, falha de exclusão remota, requisição GET sem exclusão, IDs inválidos, concorrência em PostgreSQL. Esses são nomes/cenários presentes nos logs, não ensaios manuais.

**Não comprovado:** os nove testes `sire/tests/test_oauth_drive.py` (o comando de CI só chama `sire.test_fotos_regressao`), callback HTTP com `error=access_denied`, timeout, consentimento Google real `drive.file`, Environment Group efetivamente criado, upload/exclusão/persistência real após deploy, testes completos VF/CAT e navegação responsiva. Nenhuma credencial foi lida ou gravada.

## Matriz de rastreabilidade desta evidência
| Requisito / extensão | Arquivo/artefato | Cenário verificado | Evidência | Monografia |
|---|---|---|---|---|
| RN-03; CAT-RF-03 | `sire.test_fotos_regressao`, `sire.0007_ficha_e_fotos_drive` | Isolamento e autorização de fotos | Logs dos dois jobs acima | Resultados do incremento, **ainda não atualizados** |
| CAT-RF-03; CAT-VF fotos | `sire.test_fotos_regressao` | Cache, 7ª foto, exclusão e concorrência | Logs acima; PostgreSQL executou teste de row-lock | Resultados/limitações, **pendente** |
| EVO-OAUTH | `sire/tests/test_oauth_drive.py` na PR #9 | Nove testes específicos, callback e timeout | **Não executados por estes jobs** | Não declarar validação OAuth |

## Bloqueios, responsáveis e condição de retomada
- **OAuth real — BLOQUEADO:** falta evidência de consentimento próprio `drive.file` e ambiente isolado Render; responsável autora/operador autorizado; impede aceite de fotos reais e deploy, não impede testes sintéticos locais. Retomar somente com autorização e configuração segura verificadas, sem segredos no GitHub.
- **Callback OAuth — PENDENTE:** lacuna identificada por inspeção na PR #9; responsável mantenedor/revisor dessa PR; requer conciliação e testes sintéticos de negativa/timeout em branch isolada.
- **Integração — EM REVISÃO:** PRs concorrentes abertas; responsável revisor/Work; requer conciliação de HEADs e regressão antes de merge.
- **CPF — BLOQUEADO para coleta:** finalidade, necessidade e base legal dependem de validação da autora; documentação pode prosseguir sem dados reais.
- **Auditoria acadêmica — PENDENTE:** inventário completo e verificação da monografia ainda não executados.

Próxima unidade independente: adicionar testes sintéticos do callback sem modificar a branch PR #9, após verificar seus HEADs e a ausência de alterações concorrentes. Sem merge, deploy, migração de produção ou edição de documentos históricos nesta rodada.
