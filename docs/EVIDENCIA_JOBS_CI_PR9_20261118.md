# Evidência independente — jobs do CI da PR #9 (18/11/2026)

## Escopo e fontes

Inspeção dos jobs e logs da execução GitHub Actions [44145474063](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44145474063), associada no registro anterior ao commit `2a354a75` da PR #9. Consulta feita em 18/11/2026, aproximadamente 07h (Brasília). A execução ocorreu em 17/11/2026 às 18h13 UTC. Fontes oficiais relidas por ID: regras RN-01–RN-41, baseline, guia, UC01–UC14, requisitos, especificação complementar, registro, monografia, modelo IFSP, parecer de pré-banca e histórico PROMPS. O regulamento PDF não foi reaberto nesta rodada. Esta inspeção não altera documentos históricos nem a demo.

## Evidência observada

| Job | ID | Conclusão | Comando de teste observado | Resultado observado |
|---|---|---|---|---|
| fotos-sqlite | [134259294641](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44145474063/job/134259294641) | success | `python manage.py test sire.test_fotos_regressao --verbosity 2` | 17 testes encontrados; 17 executados, 1 ignorado (concorrência com row-lock exige PostgreSQL); migração `sire.0007_ficha_e_fotos_drive` aplicada no banco descartável |
| fotos-postgresql | [134259295337](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44145474063/job/134259295337) | success | `python manage.py test sire.test_fotos_regressao --verbosity 2` | 17 testes encontrados; 17 executados; cenário de concorrência FOTO-16 aprovado; migração `sire.0007_ficha_e_fotos_drive` aplicada no banco descartável |

Os logs exibem `No changes detected` antes dos testes. A conclusão de ambos os jobs foi `success`. O job SQLite exibiu `OK (skipped=1)`; o PostgreSQL terminou com sucesso e o teste FOTO-16 foi `ok`.

**Limite fundamental:** nenhum desses dois jobs invocou `sire.tests.test_oauth_drive`. A execução **não prova** os nove testes OAuth da PR #9, callback de consentimento negado, timeout, credenciais reais, criação efetiva do Environment Group, nem upload/exclusão/persistência real no Google Drive. Drive simulado não equivale a OAuth do aplicativo.

## Rastreabilidade e dependências

| Requisito/artefato | Código ou cenário | Evidência | Estado | Próxima ação |
|---|---|---|---|---|
| RN-03–05 / CAT-FOTO | `sire.test_fotos_regressao` (permissões e cache) | Jobs acima | Concluído apenas para regressão automatizada com mocks | Testes de navegador e revisão humana |
| EVO-FOTO / migração 0007 | `sire.0007_ficha_e_fotos_drive` | Logs de ambos os jobs | Concluído somente em bancos descartáveis | Não aplicar à demo sem aceite integrado |
| EVO-OAUTH / escopo `drive.file` | `sire.tests.test_oauth_drive` | Ausente nos comandos dos jobs | Pendente de execução independente | Rodar suíte em ambiente isolado e registrar SHA/saída |
| EVO-OAUTH / integração real | Consentimento próprio, callback, Render isolado | Não evidenciado | Bloqueado: autorização própria e configuração segura não comprovadas; responsável autora/operador Google Cloud e Render | Retomar quando consentimento e ambiente isolado forem confirmados sem compartilhar segredos |
| CAT-VF / VF01–VF16 | Casos de aceite e regressão completa | Não abrangidos por esta execução | Pendente | Executar em versão reconciliada, com dados sintéticos |
| Monografia / resultados | Seção de verificação | Este relatório | Pendente de harmonização | Distinguir testes automatizados com mocks de validação real; não inventar evidências |

Nenhum teste novo foi disparado nesta rodada; foram **lidos logs de uma execução histórica**. Nenhum merge, deploy, alteração de dados ou migração de produção foi realizado. A PR #9 segue rascunho. Preservar baseline ER-SIRE 2.1, UC01–UC14 e seis entidades históricas; evolução de fotos é separada.
