# Conciliação documental FOTO-05 — 18/11/2026

## Procedência
Fontes oficiais consultadas por IDs exatos nesta rodada: RN-01–41, baseline de desenvolvimento ER-SIRE 2.1, guia, UC01–UC14, ERS 3.0, especificação complementar CAT revisão 0.2 e registro de implementação. PR #2 HEAD `faa5ba3d60b7f292be09676b13f39e9276eacafb`, aberta/draft na consulta. PRs #7/#8/#9 também abertas/draft. Não houve ensaio novo.

## Divergência demonstrada
Em `sire/test_fotos_regressao.py` (blob `1167f09930d063dbe0cb71cf8b97cf85d7a8e203`), o cabeçalho diz que os testes "detectam o problema atual de cache público (FOTO-05)". Entretanto `sire/views.py` (blob `6c27af99a42bb9a366aa6b3d2be3c53f6363b74f`) define `Cache-Control: private, no-store, no-cache, max-age=0, must-revalidate`, `Pragma: no-cache` e `Expires: 0` na resposta da foto. `docs/AUDITORIA_FOTOS_SEGURANCA_20261117.md` registra FOTO-05 como correção implementada, não como falha aberta. Os testes FOTO-04/05 afirmam `no-store` e ausência de `public`.

**Conclusão restrita:** o cabeçalho é historicamente desatualizado em relação ao código do HEAD examinado; não há evidência de falha atual de cache HTTP nessa comparação estática. A execução CI do HEAD, já documentada em `docs/AUDITORIA_CI_PR2_20261118.md`, não substitui ensaio real de navegador/CDN ou Drive. Não declarar eliminação de cópias salvas anteriormente.

## Próxima ação sem colisão
Corrigir apenas o cabeçalho do teste na branch da PR #2 **após** conciliação com o agente que a mantém, usando redação sugerida: "Testes de regressão de cache FOTO-05 verificam a política no-store; o defeito de cache público foi identificado historicamente e corrigido no incremento, sujeito a validação integrada." Não modificar aqui o arquivo de teste ou o HEAD da PR #2. Repetir testes por SHA se houver novo commit. Verificar autorização e despublicação em ensaio isolado após OAuth próprio; nunca na demo aprovada.

## Rastreabilidade e estado
CAT-RF-03 / RN-03, RN-04, RN-05, RN-11 → `sire/views.py`, `sire/test_fotos_regressao.py` → FOTO-04/FOTO-05 → CI PR #2 (simulada) → evolução do protótipo (monografia ainda não auditada). Baseline de seis entidades e UC01–UC14 não alterada. **Status:** divergência textual CONCLUÍDA como diagnóstico; correção do comentário PENDENTE (responsável mantenedor da PR #2); OAuth/aceite real BLOQUEADO (responsável autora/operador Google Cloud e Render; retomar após autorização drive.file e serviço isolado). Sem migração, merge, deploy, teste novo ou edição acadêmica.
