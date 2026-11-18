# SIRE — Revisão independente do callback OAuth (18/11/2026)

**Natureza:** auditoria estática; nenhum teste executado, nenhuma credencial real, nenhum deploy. Fonte de código: PR #9, HEAD `2a354a75f01401f49db639fa6e52752fe7a2d60c`; arquivos `scripts/autorizacao_drive.py` (blob `05fb2a307323612610e08f77363140ab943b09c3`), `sire/tests/test_oauth_drive.py` (blob `fa11260fbe8e5be12e831e8cc25822eec7b573ee`) e workflow `.github/workflows/testes.yml` (blob `fe10edac118b89a0ccd81c34853d42368cfdb5a5`). Consulta ao status combinado do commit retornou lista vazia; **não demonstra aprovação nem reprovação de CI**. Tentativa local de acessar GitHub por git falhou com `Could not resolve host: github.com`, portanto testes não foram reproduzidos.

## Gate documental

Lidos diretamente por IDs exatos no Drive nesta rodada: RN-01–41, baseline ER-SIRE 2.1, guia, UC01–14, ERS 3.0, CAT revisão 0.2, registro de implementação, monografia principal, modelo IFSP, parecer de pré-banca e histórico PROMPS TCC. A auditoria integral da monografia não foi realizada. Regulamento PDF não foi relido nesta rodada. Preservar a baseline e registrar OAuth como extensão.

## Achados reproduzíveis por inspeção

1. **Callback com parâmetro `error`:** `Callback.do_GET` registra `dados["error"]` mas sempre responde HTTP 200 e escreve "Autorizacao concluida" quando state e caminho são válidos. Em seguida `main` interrompe corretamente se `dados["error"]` existir. **Impacto:** mensagem enganosa no navegador, não emissão comprovada de token. **Correção proposta:** responder mensagem neutra de falha e HTTP 400 quando `error` existir, sem expor dados.
2. **Ausência de testes diretos do callback:** os nove métodos existentes cobrem escopo, token, Render e grupo, mas não exercitam `Callback.do_GET`, state incorreto, `error=access_denied`, code duplicado ou timeout. **Impacto:** falta evidência automatizada da fronteira OAuth. **Próxima ação:** testes com HTTPServer local e mocks, sem credenciais reais.
3. **Status CI indeterminado:** status combinado sem entradas e consulta anterior de runs por SHA vazia. Workflow configurado para push/PR, porém configuração não comprova execução. **Próxima ação:** obter URL de run com SHA, conclusão e logs ou reproduzir testes em checkout verificado.

## Matriz incremental

| EVO | Código | Teste atual | Evidência | Status | Monografia |
|---|---|---|---|---|---|
| EVO-OAUTH-CB-01, resposta correta ao consentimento negado | `scripts/autorizacao_drive.py: Callback.do_GET` | inexistente entre os nove testes examinados | código PR #9, HEAD acima | PENDENTE teste/correção | evolução de segurança OAuth |
| EVO-OAUTH-CB-02, rejeição de state/callback inválidos | mesmo | inexistente entre os nove testes examinados | condição de rejeição visível, sem execução | PENDENTE teste | avaliação de riscos |
| EVO-OAUTH-RENDER-01, grupo sem vínculo | `enviar_grupo_render` | mock presente | inspeção estática | BLOQUEADO para aceite real | limitações |

## Dependências e proteção

**B BLOQUEADO:** autorização Google `drive.file` e ambiente Render isolado sem comprovação; responsável autora/operador autorizado; retomar após consentimento e infraestrutura verificáveis sem divulgar segredos. **F PENDENTE:** executar callback e nove testes da PR #9 em ambiente com checkout/CI; responsável implementação/revisor. **A EM REVISÃO:** PRs #2/#7/#8/#9/#10 abertas; não modificar branch ativa do Work, nem mesclar/deploy. **C BLOQUEADO:** finalidade/necessidade CPF ainda dependem de validação. **D/E/G PENDENTES.** Nenhuma alteração no sistema ou na demo.
