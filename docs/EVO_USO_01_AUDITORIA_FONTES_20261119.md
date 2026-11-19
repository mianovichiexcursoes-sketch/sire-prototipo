# EVO-USO-01 — verificação documental independente (19/11/2026)

## Escopo e fontes efetivamente reabertas
Leitura direta dos documentos originais no Google Drive em 19/11/2026, sem assumir que o texto do prompt substitui a fonte:

| Documento | ID | Modificado no Drive (UTC) | Observação verificada |
|---|---|---|---|
| RN-01–41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | 2026-09-28 19:43 | RN-03 isolamento entre agências; RN-04 proteção de passageiro; RN-05 perfis |
| Desenvolvimento | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | 2026-11-18 22:36 | ER-SIRE 2.1 é baseline histórica; há versões posteriores documentadas |
| Guia | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | 2026-11-12 13:17 | protótipo Django, templates e PostgreSQL como evolução |
| Casos de uso | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | 2026-10-22 21:15 | UC01–UC14 e atores Visitante, Passageiro, Agente |
| Requisitos | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | 2026-10-23 10:54 | documento versão 3.0 PFC2 |
| Complemento CAT | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | 2026-11-18 14:07 | revisão 0.2; ficha/fotos como incremento |
| Registro técnico | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | 2026-11-18 22:34 | diferencia ambiente Work SQLite e evolução PostgreSQL |

## Decisão e dependências
- Tutorial EVO-USO-01: há implementação na branch feat/evo-uso-01-tutorial-20261118 e correções isoladas posteriores em fix/tutorial-fechar-acessibilidade-20261119 e fix/tutorial-mobile-viewport-20261119. **Não reimplementar** nem sobrescrever templates compartilhados; primeiro reconciliar diferenças e evidências de navegador.
- OAuth drive.file: bloqueado para ensaio REAL até autorização do aplicativo Django e configuração segura no Render pela autora/operador. A conexão do ChatGPT não é autorização do aplicativo. Não bloqueia tutorial local nem documentação.
- Revisão humana: avaliação do orientador permanece pendente; nenhuma evidência de aceite foi produzida aqui.
- Não houve execução de testes, merge ou deploy nesta unidade documental; demo preservada.

## Matriz de rastreabilidade e verificações ainda necessárias
| Identificador | Fonte | Código/artefato a conciliar | Cenário de verificação | Evidência | Monografia |
|---|---|---|---|---|---|
| EVO-USO-01/TUT-01–05 | retorno do orientador 17/11, decisão da autora 18/11; UC01–14 | base.html; tutorial-uso.js; branches de correção | Visitante/Passageiro/Agente, primeiro acesso, Como usar, foco, Escape, pular, alvos ausentes, celular | pendente de teste reproduzível | evolução espiral, resultados e limitações |
| RN-03–05 | RN oficiais | views e permissões existentes | agente não acessa outra agência; passageiro não vê dados alheios | pendente nesta unidade | verificação funcional |
| CAT-RF / migração 0007 | complemento revisão 0.2 | PR #2 | textos, até seis fotos, validação, exclusão e persistência | pendente de ensaio real OAuth | evolução do catálogo |
| DOC-01 | ER-SIRE 2.1, UC01–14 | documento do projeto, modelo relacional e apêndice | comparar entidades e UC com código, sem renumerar baseline | pendente | apêndices |

## Próxima ação
Conferir HEAD e diff das duas branches de correção do tutorial contra feat/evo-uso-01, identificar lacuna específica ainda não corrigida, executar teste local/sintético e só então preparar integração revisável. Manter bloqueio OAuth separado. Este registro não substitui auditoria integral da monografia nem avaliação humana.
