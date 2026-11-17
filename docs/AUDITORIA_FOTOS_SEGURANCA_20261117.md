# SIRE — Auditoria de segurança das fotos (17/11/2026)

**Status do incremento:** correções de segurança implementadas e aprovadas em CI **com Drive simulado**. **Não publicadas na demo**. **Aceite de integração real pendente** de OAuth Drive e validação pós-deploy.

## Referências oficiais efetivamente consultadas nesta revisão

- Regras de negócio **RN-03**, **RN-04**, **RN-05**, **RN-06**, **RN-11**, **RN-14**: documento Google ID `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`, reaberto em 17/11/2026.
- Extensão de catálogo **CAT-RF-03/04**, **CAT-VF-03/04/06**: documento Google ID `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`, revisão 0.2, reaberta em 17/11/2026.
- **UC05/06/07**: documento Google ID `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`, reaberto em 17/11/2026.
- Requisitos SIRE v3.0, guia de implementação e registro de rastreabilidade também foram reabertos em 17/11/2026.
- A baseline ER-SIRE 2.1, UC01–UC14 e seis entidades históricas permanecem preservadas; `FotoExcursao` é incremento posterior.

## Problemas encontrados e correções realizadas

| ID | Risco anterior | Correção | Verificação |
| --- | --- | --- | --- |
| FOTO-05 | Imagem publicada recebia `Cache-Control: public, max-age=3600`, podendo permanecer em navegador/CDN após despublicação | `Cache-Control: private, no-store, no-cache, max-age=0, must-revalidate`, `Pragma: no-cache`, `Expires: 0`; autorização consultada antes de acessar bytes | FOTO-04/05/01 e CI |
| FOTO-07/16 | Duas requisições observavam 5 fotos e podiam produzir 7 arquivos | `transaction.atomic` e bloqueio da linha `Excursao.objects.select_for_update()` antes da contagem e gravação, mantendo conferência final dentro do bloqueio | FOTO-13/14 e **FOTO-16** com duas conexões PostgreSQL reais |
| FOTO-15 | Upload de agência alheia poderia ser validado/processado antes da consulta de posse | `get_object_or_404` por agência antes de validar arquivo; rejeição antecipada quando já há 6 fotos, com recontagem dentro do lock | FOTO-15/14 |
| FOTO-18 | IDs de arquivo do banco eram interpolados em URL autenticada da API Drive sem validação explícita | IDs opacos aceitam apenas letras, números, `-` e `_` (1–128 chars); rejeitar path, query e fragment | FOTO-18 |
| FOTO-17 | Falha ao criar referência no banco poderia deixar arquivo remoto órfão | Compensação chama `drive_fotos.excluir` no erro do banco; registra erro neutro se a compensação falhar | FOTO-17 |
| FOTO-02/03/09/10/11/12 | Exposição de rascunho, exclusão por outra agência, falhas de Drive, remoção por GET | Restrições existentes preservadas e verificadas em regressão | Casos correspondentes |

Os JPEGs continuam sendo servidos somente por rota do Django: não são publicados como links públicos do Drive. O servidor já impunha validação de JPG/PNG/WebP, limite de 5 MB de entrada, 20 milhões de pixels, otimização e limite de 2 MB da saída, com `Content-Type: image/jpeg` e `X-Content-Type-Options: nosniff`.

## Evidências de CI — versão desta revisão

- Commit da correção e dos testes: `5850522c03a2bc87ae2a373b225155894194c0c4`.
- Fotos SQLite + PostgreSQL: https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44080498422 — **success**.
  - PostgreSQL: **17 testes, 17 aprovados**, incluindo duas requisições concorrentes disputando a sexta foto.
  - SQLite: **17 coletados, 16 aprovados, 1 ignorado por projeto** (FOTO-16 depende de row lock PostgreSQL).
- Suíte geral: https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44080498754 — **success**.
- A branch de desenvolvimento da ficha permanece em PR #2, a suíte original em PR #4, e este conjunto (testes + correções) em PR #5; não alterar a branch da PR #2 sem coordenação.

## Restrições e pendências para aceite operacional

1. **Integração**: responsável pela PR #2 revisar e integrar as alterações da PR #5; evitar duplicar commits da PR #4. Nenhum merge/deploy autorizado apenas por CI.
2. **OAuth real**: proprietário da conta Google deve configurar credenciais OAuth exclusivas do aplicativo e escopo `drive.file` em Secrets do Render. **Não copiar tokens do conector ChatGPT nem expor credenciais.**
3. **Teste de ponta a ponta**: usar excursão e fotos sintéticas, verificar envio real, rejeição de arquivo inválido, acesso de rascunho só pela agência, despublicação, exclusão, limite de 6 e persistência depois de redeploy.
4. **Limitação residual documentada**: a compensação não resolve falhas em que o processo morre entre a confirmação remota de upload e a gravação da referência; para produção, considerar um processo de reconciliação de órfãos/outbox. O controle de concorrência segura uma transação enquanto o Drive responde, podendo afetar latência; medir na validação real.
5. **Cache interno**: bytes podem permanecer no cache privado do servidor por até 1 hora, mas a rota consulta estado da excursão e permissão antes de consultá-los; URL da imagem removida retorna 404. A política `no-store` impede cache HTTP normal no cliente/CDN, mas não retira cópias já salvas manualmente.
6. **Release**: manter demo `etapa/postgresql-windows` e banco existentes inalterados até cumprir testes de integração, revisar plano de rollback e confirmar migração aditiva `0007_ficha_e_fotos_drive`.

**Rastreabilidade:** RN-03/05/11 + CAT-RF-03/04 → `sire/views.py`, `sire/drive_fotos.py`, `sire/test_fotos_regressao.py` → FOTO-01…18 presentes na suíte (numeração identificadora não implica que todos os números intermediários existam) → logs GitHub Actions → documentação desta revisão. **A monografia só deve declarar aceite operacional depois da validação real.**
