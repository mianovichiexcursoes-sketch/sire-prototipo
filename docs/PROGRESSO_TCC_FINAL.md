# PROGRESSO TCC FINAL — reconciliação de estado (18/11/2026, 18h55 BRT)

Este checklist é **um registro de estado verificável**, não aceite acadêmico nem declaração de deploy. Branch documental isolada derivada de `main`; não altera código, dados, migrations ou Render. O checklist histórico em `docs/progresso-tcc-final-20261117` está **desatualizado**: descreve PR #2 como aberta, mas consulta GitHub desta rodada a encontrou **mesclada**. Evitar copiar os status antigos como fatos atuais.

## Estado verificado e dependências

| ID | Status | Último commit / evidência | Bloqueio, responsável e próxima ação |
|---|---|---|---|
| A — ficha/fotos | **em execução (aceite real pendente)** | [PR #2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2) **merged**; branch histórica `etapa/ficha-fotos-sire` em `faa5ba3` | Reconciliar código integrado com PRs de segurança, verificar limites/autorizações e não inferir que Drive real funciona |
| B — OAuth Drive `drive.file` | **bloqueado para aceite real** | Nenhum teste OAuth Django/Render verificado nesta rodada | Pré-requisito: autorização própria do app, credenciais seguras e ambiente de ensaio; responsável: titular Google/Render; retomar com evidência de autorização e testes, nunca com segredo no GitHub/chat |
| C — CPF/LGPD | **pendente de conferência do incremento** | Branch `docs/evo-cpf-lgpd-20261117`, `6bf7df7` | Ler documentação e código mais recentes antes de migrar; apenas CPF sintético e mínimo necessário |
| D — UX de reserva | **pendente de aceite verificado** | Sem teste de navegador desta rodada | Comparar versão integrada e confirmar resumo/embarque/preço sem pagamento |
| E — painéis | **pendente de aceite verificado** | Sem teste de papéis desta rodada | Auditar consultas e RN-03–05 sem tocar em dados reais |
| F — CAT-VF/VF, PostgreSQL, responsividade, pós-deploy | **pendente de verificação integral** | Nenhuma suíte executada nesta rodada; resultados anteriores não foram reexecutados | Rodar CI e ensaios isolados; testes Drive real dependem de B; não publicar sem revisão |
| G — documentação/ABNT | **em execução** | [PR #28](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/28) **merged**; [PR #29](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/29) **open** em 18/11 | Reconciliar pacote acadêmico com documentos originais; revisar formatação, inventário integral, referências e validação humana |
| EVO-USO-01 — tutorial | **em execução / aceite humano pendente** | Branch `feat/evo-uso-01-tutorial-20261118` em `3f4549b`; branch de acessibilidade `fix/evo-uso-01-acessibilidade-20261118` em `63f341a`; [PR #14](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/14) | **Não reimplementar cegamente**: conferir integração e critérios TUT, testes teclado/mobile/primeiro acesso; decisão de 18/11 substitui vídeo por tutorial; solicitar avaliação do orientador via autora após verificação |
| FUT — assentos, pagamentos, cancelamentos | **pendente — fora do protótipo** | Requisitos 3.0 e RN-31–41 | Registrar somente como visão futura |

**Impacto do bloqueio B:** sem autorização OAuth própria e ensaio real não há comprovação de upload, exclusão, persistência de fotos após redeploy nem aceite dessa integração. Isso **não bloqueia** auditoria documental, UX, tutorial ou testes isolados. **Condição de retomada:** configuração segura comprovada e ambiente de teste com fotos sintéticas. Não há confirmação nova de OAuth nesta rodada.

## Fontes oficiais consultadas diretamente nesta rodada

- RN-01–RN-41: [regras](https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit), sobretudo RN-01–05 e RN-06–16.
- ER-SIRE 2.1 e histórico até versão documental 2.6: [desenvolvimento](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit).
- [Guia de implementação](https://docs.google.com/document/d/1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U/edit).
- [UC01–UC14](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit).
- [Requisitos versão 3.0](https://docs.google.com/document/d/1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM/edit).
- [Especificação complementar CAT, revisão 0.2](https://docs.google.com/document/d/1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is/edit).
- [Registro de implementação](https://docs.google.com/document/d/1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM/edit).
- [Plano do tutorial](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/docs/retorno-orientador-tutorial-20261118/docs/PLANO_ESPIRAL_TUTORIAL_20261118.md).

Leitura da monografia, modelo IFSP, regulamento e inventário integral **não realizada nesta rodada**; não afirmar auditoria global concluída. As datas editoriais são as declaradas nos documentos; a leitura não prova aprovação formal de cada revisão.

## Matriz mínima de rastreabilidade e lacunas

| Requisito | Código/migração a verificar | Teste/evidência | Documento acadêmico |
|---|---|---|---|
| ER-SIRE 2.1; UC01–UC14; seis entidades | `sire/models.py`, `sire/views.py`, migrations históricas | VF01–VF16: **não reexecutados** nesta rodada | Desenvolvimento 2.6, especificação UC, monografia |
| RN-01–05, RN-06–16 | views, forms, templates, autorização | CI/ensaio de isolamento e publicação **pendente de reconferência** | Regras e registro |
| CAT-RF e fotos | migration aditiva `0007`, `FotoExcursao`, storage | CAT-VF01–06, upload/exclusão real **pendentes de aceite** | Complementar 0.2 e registro |
| EVO-USO-01 | tutorial JS/templates em branches próprias | TUT teclado/foco/Escape/mobile/perfis **pendentes de reconferência** | Nova volta espiral, apêndice UC |
| RN-31–41 | **não implementar como baseline** | não aplicável ao protótipo | Trabalhos futuros |

## Próxima unidade independente

1. Conferir diffs da implementação EVO-USO-01 **já existente**, testes e estado de integração; corrigir apenas lacuna comprovada em branch própria, sem sobrescrever outro agente.
2. Reconciliar PR #29 com documentação e inventário da pasta do TCC; verificar leitura após qualquer edição.
3. Quando OAuth próprio estiver disponível, validar fotos reais; até lá manter B como bloqueado e executar trabalho independente.
4. Não mesclar esta branch documental automaticamente; comparar com a branch de checklist anterior e consolidar em uma única fonte de verdade antes do merge.

**Sem deploy, testes locais ou avaliação do orientador executados nesta rodada.**


## Rodada de reconciliação — 19/11/2026 (00h BRT)

**Unidade documental independente, sem modificação de aplicação.** Leitura direta por ID das fontes oficiais: RN-01–41, documentação de desenvolvimento (histórico 2.1–2.6), guia, UC01–UC14, requisitos v3.0, CAT rev. 0.2 e registro de implementação. O plano EVO-USO-01 foi lido na branch documental. Não se afirma auditoria integral das fontes restantes nesta rodada.

**Concorrência identificada:** [PR #15](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/15) já contém implementação inicial do tutorial, aberta e não mesclada; [PR #20](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/20) contém acessibilidade e depende da #15; [PR #21](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/21) contém testes Playwright sintéticos, sem confirmação de CI verde nesta consulta. [PR #31](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/31) contém critérios TUT; [PR #32](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/32) contém auditoria pontual acadêmica. Todas constavam abertas na consulta. **Não duplicar implementação** em templates compartilhados antes de reconciliar essas PRs.

| Item | Status nesta rodada | Último SHA/evidência | Dependência e próxima ação |
|---|---|---|---|
| EVO-USO-01 código | Em execução; não aceito | #15, SHA `3f4549bfba35411b6e02918a8cfd6a1f6f4111d6` | Reconciliar #20, revisar alvo ausente, foco, Escape e perfis; sem merge/deploy |
| EVO-USO-01 testes | Pendente de verificação | #21 (PR existente, CI não confirmado) | Conferir execução real Django/Playwright, desktop e celular; guardar logs e SHA |
| EVO-USO-01 avaliação | Bloqueado por verificação e avaliação humana | Feedback de 17/11 transcrito pela autora; não equivale a aceite | Após testes, autora solicita nova avaliação ao orientador; não contatar diretamente |
| G — auditoria global | Em execução | #32 (auditoria pontual aberta) | Inventariar pasta inteira, monografia, modelo IFSP e regulamento; não chamar auditoria pontual de global |
| B — Drive real | Bloqueado para aceite | Sem evidência de OAuth próprio Django/Render nesta rodada | Responsável titular da conta/Render; autorização segura e ensaio sintético são pré-requisitos; não bloqueia tutorial |

**Rastreabilidade EVO-USO-01:** fonte de mudança = feedback qualitativo de 17/11 + decisão da autora de 18/11; baseline UC01–UC14 e seis entidades permanecem históricas; incremento = #15/#20; critérios = #31; cenários = #21; evidência de navegador, regressão Django e avaliação humana = **pendentes**; atualização conclusiva da monografia = **pendente**. Não atribuir resultados de CI ou aceitação por inferência.

**Próxima unidade elegível:** conferir diferenças efetivas #15/#20/#21 e integrar critérios TUT à suíte isolada; se houver conflito de templates, trabalhar apenas em testes/documentação não conflitantes. Nenhuma alteração na demo Render, credenciais, dados ou migrations foi feita nesta rodada.


## Reconciliação incremental — 19/11/2026, 02h (Brasília)

**Fonte e integridade.** Foram relidos diretamente pelos IDs oficiais os sete documentos pertinentes: RN-01–41 (sem versão explícita), desenvolvimento (baseline ER-SIRE 2.1 e histórico posterior 2.6), guia, UC01–UC14, requisitos v3.0, CAT rev. 0.2 e registro técnico. Esta unidade é exclusivamente documental: **não executou testes, não alterou aplicação, não fez merge nem deploy**. Não substituir o histórico de seis entidades e UC01–UC14 por extensões.

**Correção de estado, com evidência GitHub:** [PR #2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2) está **merged** desde 18/11 14:05 UTC; [PR #24](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/24), [#28](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/28) e [#29](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/29) estão **merged**, não aberta a #29 como descrito no quadro anterior. PR #24 relata 13 aprovações, três ressalvas e um bloqueio em ensaios de 18/11, com 32 prints e 107 testes automáticos OK/3 ignorados; estes são **resultados declarados na PR**, não repetidos nesta rodada. Não extrapolar para aceite integral, OAuth, avaliação do orientador ou deploy novo.

| ID | Estado nesta consulta | Último SHA / evidência | Pré-requisito, responsável e próxima ação |
|---|---|---|---|
| A — ficha/fotos | Integrado; **aceite integral pendente** | #2 merge `72a488beb518b4dcca275970afb81892b97f3d4b` | Comparar implementação integrada, CAT-VF e ensaios reais antes de encerrar; não reabrir implementação histórica |
| B — OAuth/fotos reais | **Verificação insuficiente**, não declarar bloqueio absoluto sem reexaminar evidências | #24 relata fotos não reenviadas no ensaio final; registro anterior de Drive real citado na #28 | Operador Google/Render: verificar autorização própria do aplicativo, ensaio real de upload/exclusão e persistência após deploy com arquivos sintéticos; não expor tokens |
| EVO-USO-01 — tutorial | **Em execução**, não avaliado pelo orientador | [#15](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/15) SHA `3f4549b` aberta; [#20](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/20) SHA `63f341a` aberta e dependente de #15; [#21](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/21) SHA `f977ab8` aberta; [#33](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/33) SHA `8bd9670` aberta | Reconciliar #33 com #20 sobre #15; executar Playwright/Django e teste móvel/teclado. A ressalva do rodapé móvel em #24 continua sem evidência de correção aceita. Autora solicita avaliação ao orientador só após verificação |
| G — documentação e monografia | **Em execução**, auditoria global pendente | #29 merged; [#32](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/32) SHA `a43b7a2` aberta | Inventariar Drive completo, conferir monografia, IFSP, ABNT, apêndices, entrevistas e evidências; aprovação de título/avaliação depende da autora/orientador |
| Checklist persistente | **Em execução**, duplicidade de branches | [#30](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/30) branch atual; checklist histórico em branch separada | Reconciliar antes do merge, manter uma única fonte; evitar sobrescrever trabalhos simultâneos |

**Rastreabilidade EVO-USO-01:** feedback da autora (17–18/11) → extensão de uso separada da baseline → JS/templates na #15 e correções na #20/#33 → cenários sintéticos na #21 e critérios na #31 → resultados de navegador e Django ainda não reconferidos nesta rodada → seção metodológica/avaliação da monografia pendente. A aprovação humana é uma dependência distinta dos testes técnicos.

**Próxima unidade independente elegível:** revisar o diff da #33 contra #20 e adicionar testes de responsividade/teclado em branch de testes reconciliada; não tocar nos templates compartilhados até resolver precedência. Alternativamente inventariar documentos restantes da pasta TCC e elaborar relatório de divergências sem modificar a monografia. Nenhum item foi marcado concluído apenas com base em declaração de PR.


## Unidade documental — 19/11/2026, 02h57 (Brasília)

**Concluído nesta unidade:** descrição da [PR #14](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/14) corrigida para retirar a entrega de vídeo como requisito vigente e apontar tutorial interativo aprovado pela autora em 18/11. O texto original do plano permanece como histórico; nenhuma alteração de código ou da demo. Fonte da decisão: docs/PLANO_ESPIRAL_TUTORIAL_20261118.md, SHA de blob `929fd3414a401a04bf2b950bc734262e138cffe7` na branch docs/retorno-orientador-tutorial-20261118. Fontes oficiais relidas diretamente por IDs: RN, desenvolvimento, guia, UC, requisitos, CAT e registro técnico; versões identificadas: ER-SIRE 2.1 histórica, requisitos 3.0, CAT 0.2; demais versões não inferidas.

| Item | Estado | Evidência verificável | Bloqueio/dependência e próxima ação |
|---|---|---|---|
| EVO-USO-01 — alinhamento de escopo #14 | **Concluído (metadados)** | [PR #14](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/14), atualizada 19/11/2026 05:57 UTC; último HEAD da PR `f20106a` não alterado | Revisar coerência de documentos acadêmicos antes da entrega |
| EVO-USO-01 — aceite técnico | **Em execução** | PRs #15/#20/#21/#24/#33; ressalva de rodapé móvel da #24 | Dependência: conciliar diffs e executar testes de navegador e Django; responsável: desenvolvimento/revisão; retomar com HEAD reconciliado e evidência de testes |
| OAuth Drive/persistência após deploy | **Bloqueado para aceite real sem evidência atual suficiente** | PR #18 relata testes locais, mas não confirma deploy/persistência na demo | Dependência: configuração segura no Render e ensaio autorizado; responsável: titular do aplicativo/Render; retomar após comprovar acesso, sem publicar segredos |

**Testes nesta unidade:** não executados (edição documental). **Merge/deploy:** não realizados. **Próxima unidade independente:** inspeção e teste isolado da sobreposição móvel ou inventário de anexos acadêmicos, sem modificar templates concorrentes.


## Inspeção de concorrência — 19/11/2026, 05h58 (Brasília)

Leitura direta dos documentos oficiais por ID: regras RN-01–41 (sem versão explícita no texto inicial), desenvolvimento com baseline ER-SIRE 2.1 histórica, guia de implementação, especificação UC01–UC14, requisitos v3.0, catálogo/ficha rev. 0.2 e registro técnico. Os sete retornaram conteúdo legível. Esta unidade é de reconciliação documental, sem alteração do aplicativo, sem testes executados e sem deploy.

**Mapa verificável de sobreposição de PRs:** #15 (HEAD `3f4549b`) modifica `sire/static/sire/js/tutorial-uso.js` e `sire/templates/sire/base.html`; #20 (HEAD `63f341a`) modifica o **mesmo JS** e acrescenta correções de acessibilidade; #33 (HEAD `8bd9670`) também modifica o **mesmo JS** para Fechar. #21 (HEAD `f977ab8`) adiciona `tests/test_tutorial_browser.py` e workflow próprio, sem editar JS/template. Logo, **não é seguro mesclar #20 e #33 independentemente sobre #15** sem reconciliação explícita do arquivo comum. A PR #14 é documental e não implementa o tutorial. Evidência: listas de arquivos alterados nas PRs #15/#20/#21/#33 consultadas nesta data.

| Item | Status | Último commit consultado | Evidência e próxima ação |
|---|---|---|---|
| EVO-USO-01 — implementação | **Em execução** | #15 `3f4549b`, #20 `63f341a`, #33 `8bd9670` | Reconciliar alterações do JS em branch isolada, revisar base.html e executar testes TUT; sem afirmar aceite |
| EVO-USO-01 — testes browser | **Pendente de execução no HEAD integrado** | #21 `f977ab8` | Workflow e arquivo de teste existem na PR; executar contra código reconciliado, registrar resultado real e responsividade |
| A/B — fotos e Drive | **Bloqueado para aceite real** | #2 `faa5ba3` (HEAD histórico) | #2 encerrada/mesclada, mas ainda requer evidência de OAuth Django, fotos sintéticas, exclusão e persistência após deploy; responsável: titular Google/Render; retomar com credenciais somente em ambiente seguro |
| G — auditoria acadêmica | **Pendente de auditoria global** | #14 `f20106a`; #30 `1e401bf` antes desta edição | Inventariar pasta Drive inteira, confrontar monografia/modelo IFSP/UC e registrar divergências; não declarar revisão completa |

**Próxima ação independente:** comparar os patches de #15/#20/#33, preparar reconciliação isolada e validar os testes da #21; em paralelo, inventário documental sem alterar monografia antes da leitura integral. A demo Render e dados existentes não foram modificados.
