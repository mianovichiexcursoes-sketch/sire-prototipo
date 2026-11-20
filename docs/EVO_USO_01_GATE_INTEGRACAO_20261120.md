# EVO-USO-01 — gate de integração independente (20/11/2026)

> Documento incremental de auditoria, **não substitui** o checklist canônico `docs/PROGRESSO_TCC_FINAL.md` mantido nas PRs #15/#20/#21. Nenhuma integração, teste, deploy ou aceite é reivindicado aqui.

## Fontes oficiais lidas diretamente nesta rodada

- RN-01–RN-41: Google Doc `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`, modificado em 28/09/2026. RN-03/04/05 exigem isolamento de agência, proteção de dados e perfis; RN-06–09 condicionam publicação e embarque; RN-17–21 condicionam reserva e capacidade.
- Documentação de desenvolvimento ER-SIRE 2.1: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`, modificado em 18/11/2026; baseline histórica preservada.
- Guia de implementação: `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`, modificado em 12/11/2026.
- Casos UC01–UC14: `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`, modificado em 22/10/2026.
- Requisitos v3: `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`, modificado em 23/10/2026.
- Complemento CAT: `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`, modificado em 18/11/2026.
- Registro técnico: `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`, modificado em 18/11/2026.
- Monografia principal: `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg`, modificado em 18/11/2026; somente leitura de trecho pertinente, **não auditada integralmente**.

## Inventário verificado por API GitHub

| PR | Estado em 20/11 | HEAD | Base | Risco/dependência |
|---|---|---|---|---|
| #2 | merged | faa5ba3 | etapa/postgresql-windows | Merge **não** comprova OAuth nem persistência de fotos |
| #14 | open, draft | f20106a | etapa/postgresql-windows | Retorno do orientador, documentação |
| #15 | open | 3f4549b | etapa/postgresql-windows | Tutorial inicial, JS/template/checklist |
| #20 | open | 63f341a | #15 | Acessibilidade, JS/checklist |
| #21 | open | f977ab8 | #20 | Testes browser e workflow |
| #33 | open | 8bd9670 | etapa/postgresql-windows | Handler Fechar, JS concorrente |
| #35 | open | bf91770 | #33 | Ajuste móvel, JS concorrente |
| #39 | open | 11e8146 | #35 | Contrato estático, depende de #35 |
| #41 | open | 9c3b4aa | #15 | Auditoria documental |

**Conflito confirmado pela descrição e inventário de patches da PR #14:** #15/#20/#33/#35 alteram o mesmo `sire/static/sire/js/tutorial-uso.js`; #15/#20/#21 alteram checklist. Não aplicar patches cegamente. A possível atividade local de Claude não é visível via GitHub.

## Matriz de dependências e próximo passo

| Item | Estado | Pré-requisito | Evidência atual | Próxima ação |
|---|---|---|---|---|
| EVO-USO-01 tutorial | em execução, não integrado | reconciliar HEADs #15→#20→#21 e #33→#35→#39 em branch isolada | PRs e SHAs acima | comparar patches, resolver JS manualmente, preservar sem POST automático |
| TUT-01–09 / regressões UC | pendente | árvore de integração revisada | não há execução nova nesta rodada | executar suíte Django + navegador real em 320px e 375×812; registrar saída e SHA |
| CAT-RF-03 fotos Drive | bloqueado para aceite real | OAuth próprio drive.file e credenciais seguras do aplicativo no Render | #2 merged; especificação CAT | autora configura fora do chat; testar upload/exclusão e persistência pós-deploy |
| Revisão acadêmica e avaliação | pendente | integração testada + avaliação humana | docs oficiais lidos parcialmente | anexar modelo relacional e UC01–14; avaliação posterior pela autora/orientador |

**Impacto do bloqueio OAuth:** somente integração de fotos e seus testes reais; não bloqueia tutorial, CPF sintético, UX ou documentação independente. **Responsável:** titular do projeto Google/Render. **Retomada:** credenciais configuradas por canal seguro e autorização comprovada, sem inserir segredos no repositório.

**Próxima unidade executável:** criar branch de integração a partir de #21 e comparar explicitamente #33/#35/#39 antes de incorporar mudanças. Verificar foco, Escape, Fechar/Pular, alvos ausentes, storage indisponível, perfis e não envio de formulários. Não tocar na demo antes de CI e avaliação.

**Histórico:** 20/11/2026 03h (America/Sao_Paulo): leitura direta das fontes e PRs; somente este artefato documental versionado, sem execução de testes, deploy ou edição de monografia.
