# EVO-USO-01 — gate de integração observado em 20/11/2026

Registro pontual, não aceite funcional. Fontes oficiais abertas diretamente no Drive nesta rodada: RN-01–RN-41 (ID 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0), desenvolvimento ER-SIRE 2.1 (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8), guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U), UC01–UC14 (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY), requisitos v3 (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM), CAT revisão 0.2 (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is), registro (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM). O conteúdo foi consultado para identificar a baseline; não há aprovação de alterações de escopo.

## Estado confirmado pela API GitHub

| PR | Estado | HEAD observado | Base | Dependência |
|---|---|---|---|---|
| #2 | merged | faa5ba3d60b7f292be09676b13f39e9276eacafb | etapa/postgresql-windows | OAuth real ainda não demonstrado |
| #14 | open/draft | f20106af511f5637787f2b450cd1468e53c25924 | etapa/postgresql-windows | documentação, não tutorial funcional |
| #15 | open | 3f4549bfba35411b6e02918a8cfd6a1f6f4111d6 | etapa/postgresql-windows | implementação inicial |
| #20 | open | 63f341ab9769436c252c5cf71151a976ea9498ec | feat/evo-uso-01-tutorial-20261118 | depende de #15 |
| #21 | open | f977ab8e33173fc21ee8b29d5eb03ab8d74c8ed4 | fix/evo-uso-01-acessibilidade-20261118 | depende de #20 |
| #33 | open | 8bd96705e19afc0b5d0a89671270ae8232bbf175 | etapa/postgresql-windows | Fechar em ramo paralelo |
| #35 | open | bf917708f09d01befb8c7576dfc43d9d2a1e8158 | fix/tutorial-fechar-acessibilidade-20261119 | ajuste móvel paralelo |
| #39 | open | 11e8146b795cf4b9152548f66770cebf0b3ac82f | fix/tutorial-mobile-viewport-20261119 | contrato estático paralelo |

## Dependências e condição de retomada

- **EVO-USO-01 — EM EXECUÇÃO:** a integração depende de conciliar a cadeia #15 → #20 → #21 com #33/#35/#39, comparando diffs do mesmo JS e templates. Responsável: integração técnica; retomar com árvore isolada e verificação dos handlers Fechar/Pular/Escape.
- **EVO-USO-01 — VERIFICAÇÃO PENDENTE:** CI de PR individual não demonstra árvore integrada. Rodar Django e navegador real (320px, 375×812, teclado, foco, alvos ausentes, perfis, localStorage desabilitado e ausência de submit involuntário), guardar URL de execução e SHA exato.
- **OAuth Drive — BLOQUEADO PARA FOTOS REAIS:** pré-requisito: autorização do aplicativo Django com escopo drive.file e segredos configurados em ambiente seguro pela autora/operador. Não há evidência nesta rodada de autorização nem persistência real. Não bloqueia tutorial isolado.
- **Avaliação do orientador — PENDENTE:** somente após integração e testes; a autora deve autorizar contato e coletar feedback real.
- **A–G / documentação — PENDENTE:** manter checklist canônico em docs/PROGRESSO_TCC_FINAL.md; este registro é anexo de evidência e não o substitui. Não reescrever baseline, seis entidades nem UC01–UC14.

## Próxima unidade independente

Construir integração isolada a partir do HEAD confirmado da base, revisar patches conflitantes antes de tocar em arquivos compartilhados, executar testes locais e registrar saída bruta. Nenhum teste, merge, deploy, alteração de modelo ou migração foi executado nesta rodada. Esta auditoria não comprova ausência de alterações locais do Claude.
