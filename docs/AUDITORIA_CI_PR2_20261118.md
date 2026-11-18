# Auditoria de CI da PR #2 — 18/11/2026

## Escopo e procedência
Leitura direta das fontes oficiais SIRE (12 documentos pelos IDs originais), da PR #2 e dos logs do GitHub Actions. **Não é nova execução local**, nem aceite da integração real Google Drive. Branch da PR: `etapa/ficha-fotos-sire`; HEAD verificado: `faa5ba3d60b7f292be09676b13f39e9276eacafb`. PR #2 aberta em draft na consulta.

## Evidências de CI vinculadas ao HEAD
| Run / URL | Job | Resultado observado no log |
|---|---|---|
| [44097899889](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097899889) | fotos-sqlite (job 134089794220) | 17 testes, OK, 1 skipped (row-lock PostgreSQL) |
| Mesmo run | fotos-postgresql (job 134089794860) | 17 testes, OK, sem skip |
| [44097900342](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097900342) | suíte PostgreSQL (job 134089798323) | 84 testes, OK |
| Mesmo run | suíte SQLite (job 134089798680) | 84 testes, OK, 3 skipped (concorrência exclusiva PostgreSQL) |

Ambos os workflows retornaram `completed/success`. Os quatro logs registram `Applying sire.0007_ficha_e_fotos_drive... OK` em bancos de teste descartáveis, e `System check identified no issues (0 silenced)`. **Não implica migração aplicada na demo ou produção**.

## Limites e próximos gates
- Os testes de fotos usam Drive simulado: não verificam OAuth `drive.file` real, persistência pós-deploy, exclusão remota ou permissões reais da conta Google.
- Os skips em SQLite são esperados para testes de row-lock, mas devem permanecer explícitos na documentação.
- A divergência entre comentário histórico sobre cache público e a implementação deve ser conferida diretamente nos testes e views antes de declarar a correção encerrada.
- A CI atesta o HEAD específico acima, não alterações posteriores, PRs #7/#8/#9 nem eventual merge.
- Não há evidência nesta auditoria de testes de navegador responsivo, nem de aceite humano.
- Próximo: reconciliar PRs #2/#7/#8/#9 e validar comportamento de fotos em ambiente isolado com OAuth próprio, mantendo a demo preservada.

## Rastreabilidade
CAT-RF-02/03 e migração 0007 → `sire.0007_ficha_e_fotos_drive` e testes de fotos → runs acima → capítulo de evolução da espiral (a atualizar somente após auditoria acadêmica). Baseline ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem históricos; `FotoExcursao` é extensão.
