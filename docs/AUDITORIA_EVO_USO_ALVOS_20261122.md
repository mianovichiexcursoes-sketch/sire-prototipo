# EVO-USO-01 — auditoria estática de alvos e perfis (22/11/2026)

**Tipo:** análise de código; NÃO é teste executado, aceite, deploy ou merge. Base isolada: `etapa/postgresql-windows`. Não altera código concorrente.

## Fontes oficiais consultadas diretamente
- RN-01–41: documento `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`, revisão `AHj4eMQguVGb_4XDjpIILo1Ueu3oX74YzVU-Y3pjwZRW8SqamIbGe_xdMG_PkwTcvmpm8WSHhBiXi54l4ahoI6g3UbBVdUxMjmog4LuqsHs`.
- Baseline ER-SIRE 2.1: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`.
- Guia: `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`.
- UC01–UC14: `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`.
- Requisitos: `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`.
- Complemento CAT: `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`.
- Registro técnico: `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`.

## Achados verificáveis na leitura do código remoto
1. Na branch `feat/evo-uso-01-tutorial-20261118`, blob `41039cd9f6d464cd746e70ee33656d97f26f4946`, o array não-agente inclui **Criar conta** para passageiro autenticado. A PR #64 propõe correção; não declarar corrigido na base ou na demo sem reconciliação.
2. Na mesma implementação, `findTarget` pesquisa texto parcial em `a,button,h1,h2,nav a` sem verificar visibilidade, e pode destacar elemento oculto ou homônimo. Critério TUT: selecionar somente alvo visível, habilitado e pertencente ao contexto, com fallback não bloqueante.
3. Na branch `fix/tutorial-fechar-acessibilidade-20261119`, blob `2ecc2a352c00d9d36ebc4e17355a7f51dcaa5530`, a seleção usa `getClientRects().length` e texto exato, reduzindo ambiguidade, mas a efetividade depende de integração e teste no DOM real. Não presumir que esta branch já esteja na PR principal.

## Cenários pendentes (não executados)
| Critério | Pré-condição | Procedimento | Evidência exigida |
|---|---|---|---|
| TUT-PERFIL | passageiro sintético autenticado | abrir Como usar | não orientar novo cadastro; screenshot e resultado Playwright |
| TUT-ALVO | dois controles homônimos, um oculto | percorrer guia | apenas alvo visível recebe destaque; log e captura |
| TUT-VAZIO | nenhuma excursão/vaga | abrir e concluir guia | nenhuma reserva ou POST; captura e rede |
| TUT-TECLADO | teclado apenas | anterior/próximo/Escape/fechar | foco previsível e restaurado; log |
| TUT-MOBILE | viewport 375 px | percorrer passos | alvo não encoberto; captura |

## Dependências e próxima ação
**Em execução, sem aceite:** reconciliar HEAD/diffs das PRs #15/#20/#33/#35/#64 antes de editar o JS/template compartilhado. Responsável: integração técnica. **Bloqueado para integração:** testes Django e navegador em HEAD consolidado e revisão humana. **OAuth do aplicativo:** necessário para fotos reais, não para tutorial. Preservar ER-SIRE 2.1, seis entidades e UC01–UC14; não implantar nem criar dados reais. Esta auditoria deve ser referenciada no checklist canônico `docs/PROGRESSO_TCC_FINAL.md` após reconciliação com PRs #66/#70, sem sobrescrevê-las.
