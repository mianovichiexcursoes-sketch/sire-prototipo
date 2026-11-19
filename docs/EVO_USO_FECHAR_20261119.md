# Registro independente EVO-USO-01 — 19/11/2026

## Proveniência
Fontes originais consultadas diretamente por ID nesta execução: RN-01–41 `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`; baseline e documentação 2.6 `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`; guia `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`; UC01–14 `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`; requisitos `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`; CAT `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`; registro `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`. Versões: baseline ER-SIRE 2.1 histórica; CAT revisão 0.2; documento de desenvolvimento histórico até 2.6. Não altera UC01–UC14 nem seis entidades.

## Unidade de progresso
| Item | Status | Commit/evidência | Próxima ação |
|---|---|---|---|
| TUT — botão explícito Fechar | IMPLEMENTADO, NÃO VERIFICADO | `990524a88a8b6104497e280ccf6796f362660a33`; `sire/static/sire/js/tutorial-uso.js` | Executar testes de teclado, Escape, Fechar, Pular e foco, incluindo celular; revisar PR antes de integrar |
| TUT — sobreposição do rodapé no celular | PENDENTE | PR #24 relata ressalva em navegador | Corrigir e repetir teste real em viewport móvel; não alegar correção pelo botão Fechar |
| TUT — avaliação do orientador | BLOQUEADO | Feedback de 17/11 transcrito pela autora; sem novo aceite | Responsável: autora e orientador. Pré-requisito: versão revisada e testada; retomar após demonstração autorizada |
| B — OAuth próprio do aplicativo | BLOQUEADO para teste de integração real | A conexão ChatGPT Drive não autoriza o Django | Responsável: operadora Google Cloud/Render. Configurar OAuth drive.file e segredos apenas no ambiente seguro; testar upload/exclusão/persistência após deploy |
| F — regressão e CI | PENDENTE | PR #24 relata 107 OK/3 ignorados em versão anterior; não repetidos nesta unidade | Rodar suíte no SHA desta PR, SQLite/PostgreSQL e testes de navegador |
| G — auditoria acadêmica global | PENDENTE | PR #32 contém auditoria pontual, não global | Inventariar Drive e conciliar monografia, modelo, apêndice, normas e evidências |

## Rastreabilidade e limites
EVO-USO-01 / TUT (usabilidade, sem novo UC histórico) → `tutorial-uso.js` → cenário: abrir tutorial, usar Fechar, observar retorno do foco ao botão Como usar, verificar que nenhum POST ocorre → **evidência de execução pendente** → seção de evolução/avaliação da espiral na monografia **pendente**. RN-03–05: orientação por perfil existente; nenhum dado pessoal persistido nesta alteração. Nenhum banco, migration, formulário, API, deploy, merge, pagamento ou dado real foi alterado.

O checklist histórico `docs/PROGRESSO_TCC_FINAL.md` na branch demo está datado de 17/11 e contém estados superados; reconciliar em PR específica antes de sobrescrever, porque PRs #30/#31 e outros agentes já editaram esse arquivo. Esta unidade usa registro próprio para não causar perda de trabalho concorrente.
