# Verificação independente de fontes — 19/11/2026, 14h55 BRT

## Escopo e resultado real
Nesta rodada foram reabertos diretamente por ID no Google Drive os sete documentos técnicos abaixo. O resultado é **verificação de leitura e proveniência**, não execução de teste nem aceite do tutorial. Nenhum arquivo de aplicação, migração, dado real, branch da demo ou ambiente Render foi alterado.

| Fonte oficial | ID | Revisão retornada pela API | Evidência de conteúdo |
|---|---|---|---|
| RN-01–RN-41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | AHj4eMQguVGb_4XDjpIILo1Ueu3oX74YzVU-Y3pjwZRW8SqamIbGe_xdMG_PkwTcvmpm8WSHhBiXi54l4ahoI6g3UbBVdUxMjmog4LuqsHs | RN-01 agente/agência, RN-03 isolamento, RN-04 privacidade, RN-05 perfis |
| Desenvolvimento/baseline | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | AHj4eMTd3MUuANlRTlg4m2XrvinNmjWa66sdQEiaLKJL47kzrBUbkgePcfhFjs6KpbfGSkqaZv6vvBYgZYtY1nhoDY7XVUqytJwfIG8EkGs | Histórico 2.1 e iteração técnica 2.6 |
| Guia implementação | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | AHj4eMQaNMjGn0nQytWmd1zCgC4eXduS5sJ-NYwLZOQtS5LvcMTDuZXWcdCg2KrDm02eDTrUv9zFLRxlOpMpmeAElRCdGivJKqIAUAmbgk4 | Django ORM, SQLite original e PostgreSQL incremental |
| UC01–UC14 | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | AHj4eMR9ieGd6kQkg8v57yrInG6V_mFxksUY7zZhppBjMPMHKLKqrFh-QgDIehKmhTKnOfxY13Rtx6xRB44A_q0U1uxqUr4Ji-CbBHxnT9Y | Atores Visitante, Passageiro e Agente |
| Requisitos v3.0 | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | AHj4eMTi8NviSAJ3x85wLTlG-5Oq8qM3pHYIzotUlXt5pUOO-KC2I8vyOz1-8LJLQigBx27FlqZzhcg2w3UdynaSzHMjImYxqEFHs1IAyxM | Distinção visão do produto / escopo do protótipo |
| Complemento CAT 0.2 | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | AHj4eMTSU0RTheqYeHkWD0Zq9snLQEYLwb6Ruu9Yf36JmWk-Y5D51wnT7_ujOKJXqaajTFULu9V5n2AjYtEH8jXtqVN0I_jRAhwRX2BWrEs | Fotos, ficha, limites e armazenamento persistente |
| Registro técnico | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | AHj4eMR_QOz9L1B-9E5roWp0mibyS37cGqh303DyLnFInxYRuajnk6JJyKMLIwShaLtDwLcvFz8klfgj_2rzYxFrf36gqDMRbfzsXga-U-8 | Rastreabilidade UC e ambiente efetivamente usado |

Revisão da API não é data de modificação. Esta rodada leu trechos de cada fonte, não auditou integralmente seus conteúdos.

## Estado de concorrência observado
Branches de tutorial já existentes: `feat/evo-uso-01-tutorial-20261118`, `fix/tutorial-mobile-viewport-20261119`, `fix/tutorial-fechar-acessibilidade-20261119`, `docs/gate-fontes-tutorial-20261119-1055`. A branch mobile já contém checklist mais recente informando PR #2 merged e PRs de tutorial concorrentes. Não editar templates ou JS compartilhados sem comparar commits e PRs atuais. Mudanças locais invisíveis do Claude não podem ser excluídas.

## Matriz de dependências / próxima ação
| Item | Estado | Evidência | Próxima ação |
|---|---|---|---|
| A ficha/fotos | integrado, aceite real pendente | registro de reconciliação no checklist da branch mobile | revisar CI e fotos reais antes de declarar concluído |
| B OAuth | bloqueado para ensaio real | nenhuma autorização Django comprovada nesta rodada | autora/operador configurar OAuth `drive.file` e segredos fora do repositório; retomar upload/exclusão/persistência somente depois |
| EVO-USO-01 | em execução concorrente | branches acima | comparar PRs, corrigir lacuna isolada e executar TUT sintéticos; avaliação humana pendente |
| C CPF | pendente de revisão | RN-04/05 e UC01 | definir finalidade/minimização, verificar PRs existentes e testar apenas CPFs sintéticos |
| D/E | pendente | não verificado nesta rodada | reconciliar branches e telas |
| F | pendente | nenhuma suíte reexecutada nesta rodada | testar SQLite/PostgreSQL e navegador em ambiente isolado |
| G | pendente | fontes técnicas consultadas | inventariar Drive, revisar monografia/IFSP/ABNT sem fabricar evidência |

**Rastreabilidade:** RN-03/04/05 → perfis e isolamento → testes de autorização pendentes → monografia pendente; UC01–UC14 → tutorial EVO-USO-01 → TUT/avaliação pendentes → apêndice acadêmico pendente; CAT 0.2 → ficha/fotos → CAT-VF e OAuth real pendentes → resultados pendentes.

**Limites:** Não houve leitura nesta unidade da monografia, modelo IFSP, regulamento e parecer; nenhuma mudança neles foi feita. Não houve execução de CI, deploy ou teste de navegador. A versão aprovada da demo permanece intocada.
