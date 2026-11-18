# SIRE — Evidência adicional de CI da PR #9 (18/11/2026)

## Fonte e escopo
Consulta direta ao endpoint GitHub Actions `GET /repos/mianovichiexcursoes-sketch/sire-prototipo/actions/runs?branch=fix/oauth-grupo-render-20261117&per_page=20` em 18/11/2026. Branch da PR #9: `fix/oauth-grupo-render-20261117`; commit examinado: `2a354a75f01401f49db639fa6e52752fe7a2d60c`.

## Evidência nova
O endpoint retornou **3 execuções** de workflow para a branch, incluindo a execução `44145474063`, intitulada “SIRE - regressao de fotos (SQLite e PostgreSQL)”, com `status=completed` e `conclusion=success`, evento `pull_request`, `head_sha=2a354a75f01401f49db639fa6e52752fe7a2d60c`, iniciada em 17/11/2026 às 18:13:20 UTC e encerrada às 18:13:49 UTC. Evidência: https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44145474063 .

**Limite:** este sucesso de workflow não prova que os nove testes específicos de `sire/tests/test_oauth_drive.py` tenham sido executados, nem que OAuth real, callback, consentimento negado, upload ou persistência no Drive funcionem. Não foi inspecionado o log de jobs desse run nesta entrega. Os testes de OAuth específicos continuam sem comprovação de execução independente.

## Divergência reconciliada
O relatório anterior dizia que uma consulta por SHA não retornou execuções. Essa consulta tinha escopo limitado. A consulta por branch encontrou ao menos um run bem-sucedido no SHA correto; o relato anterior não deve ser apagado, apenas complementado. **Não há fundamento para afirmar ausência de CI na PR #9.**

## Gate e dependências
Fontes oficiais lidas diretamente nesta rodada por seus IDs: regras RN-01–RN-41, baseline ER-SIRE 2.1, guia, UC01–UC14, requisitos v3.0, especificação complementar rev.0.2, registro de implementação, monografia, modelo e regulamento IFSP, parecer pré-banca e histórico PROMPS. A alteração aqui é exclusivamente documental. OAuth real continua bloqueado por autorização do aplicativo e ambiente isolado; responsável: autora/operador do Google Cloud e Render; retomar somente após autorização segura. Não alterar demo, não publicar segredos.

## Próxima ação
Abrir jobs da execução 44145474063, confirmar nomes e resultados por job, e executar separadamente os nove testes OAuth em ambiente isolado com saída e SHA registrados. Para o callback, criar cenários sintéticos de `error=access_denied`, state inválido, timeout e callback bem-sucedido; conciliar antes com a PR #9. Não mesclar nem publicar sem regressão completa.
