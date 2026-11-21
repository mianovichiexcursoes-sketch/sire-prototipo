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


## Gate de fontes — 19/11/2026, 17h55 (Brasília)

**Unidade executada:** leitura direta via Google Docs API dos sete documentos oficiais, pelos IDs exatos, antes de qualquer alteração de código. Registro de revisões retornadas pela API (identificadores técnicos, não datas de aprovação):

| Documento | ID abreviado | Revisão consultada | Evidência/escopo |
|---|---|---|---|
| RN-01–41 | 1REAmrici | AHj4eMQguVGb | RN-01–05: vínculo, isolamento e privacidade; RN-06–16: excursões; RN-17 em diante: reservas |
| Desenvolvimento/baseline | 19U5JhTH | AHj4eMTd3MUu | Histórico ER-SIRE 2.1 e evolução 2.6; não reescrever baseline |
| Guia de implementação | 1QzjUnox | AHj4eMQaNMjG | Django ORM, seis entidades e SQLite original, PostgreSQL como incremento |
| UC01–UC14 | 1h5T8l9 | AHj4eMR9ieG | Atores Visitante, Passageiro e Agente; UC01/UC02 conferidos |
| Requisitos | 1RTgG9f | AHj4eMTi8Nvi | v3.0: distinção entre visão de produto e escopo de protótipo |
| CAT/ficha | 1EKm59rE | AHj4eMTSU0RT | rev. 0.2: extensão opcional, filtro, fotos e migração aditiva |
| Registro técnico | 1g3MnJfh | AHj4eMR_QOz9 | Rastreabilidade UC01–14 e verificações HTTP históricas |

**Observação de integridade:** prefixos de revisão acima servem somente como índice de consulta; a revisão completa é obtida novamente na API para comparar alterações. Nesta unidade não houve teste Django, Chromium, CI novo, merge nem deploy. Os documentos restantes da auditoria global ainda não foram relidos nesta unidade; portanto não se declara gate integral da monografia satisfeito.

**Conflito e dependências reavaliados:** PR #14 continua documental, draft, HEAD `f20106af511f5637787f2b450cd1468e53c25924` e lista expressamente #15/#20/#21/#33/#35 como incrementos não integrados. Checklist não existe em `main`; esta branch é fonte candidata e requer reconciliação antes de torná-la canônica. Não tocar no JS compartilhado enquanto os HEADs concorrentes não forem conciliados. OAuth `drive.file` não é pré-requisito para tutorial, mas é para aceite real da integração de fotos. Responsável pelo OAuth: titular Google/Render; condição de retomada: configuração autorizada e evidência de ensaio sintético persistente.

**Status da unidade:** concluído somente o registro verificável de fontes/dependências. **Próxima ação:** comparar patches do tutorial, reconciliar em branch isolada e executar TUT com evidência; em paralelo inventariar documentos restantes e anexos da pasta TCC. Não confundir registro documental com entrega funcional.


## Reconciliação incremental — 20/11/2026, 22h57 BRT

**Unidade efetivamente executada:** consulta direta aos sete documentos oficiais por seus IDs exatos no Google Drive e aos metadados das PRs #2, #14, #15, #30 e #39 no GitHub; atualização deste checklist sem modificar modelos, migrations, templates, demo ou dados. Os documentos consultados foram: RN-01–41 (ID 1REAmrici...), desenvolvimento ER-SIRE (19U5JhTH..., histórico 2.6 de 12/11), guia (1QzjUnox...), UC01–UC14 (1h5T8l9...), requisitos 3.0 (1RTgG9f...), CAT rev. 0.2 (1EKm59rE...) e registro de implementação (1g3MnJfh...). A consulta textual não fornece revisão documental nova confirmada nesta rodada; não inferir versão além das indicadas nos próprios textos.

| Item | Status nesta rodada | Último SHA observado / evidência | Dependência e próxima ação |
|---|---|---|---|
| A — PR #2 | **concluído somente merge histórico; aceite de fotos pendente** | PR #2 merged, HEAD histórico `faa5ba3d60b7f292be09676b13f39e9276eacafb` | Não declarar persistência real sem OAuth e teste pós-deploy |
| EVO-USO-01 implementação | **em execução, integração pendente** | PR #15 aberta, HEAD `3f4549bfba35411b6e02918a8cfd6a1f6f4111d6`; PR #39 aberta, HEAD `11e8146b795cf4b9152548f66770cebf0b3ac82f`; PR #14 aberta documental | Comparar patches/HEADs de #15/#20/#21/#33/#35/#39 e preparar branch de integração isolada; executar TUT-01–09 e testes de navegador antes de merge |
| Checklist canônico | **em execução, ainda fora da branch base** | PR #30 aberta, HEAD anterior `70818b6ea174f703222705a5f2fcfa2bd44bef9e` | Reconciliar o checklist antes de integrar; este registro é histórico incremental, não substitui os estados de outras PRs |
| B — OAuth Drive | **bloqueado para ensaio real** | Nenhuma autorização Django `drive.file` ou ensaio Render confirmados nesta rodada | Responsável: titular Google/Render; exige autorização própria do app e configuração segura; então testar upload, exclusão e persistência após deploy com fotos sintéticas |
| F — aceite/regressão | **pendente** | Não houve execução de Django, PostgreSQL, CI ou navegador nesta unidade | Executar apenas em branch integrada e ambiente isolado; preservar demo |
| G — auditoria acadêmica global | **pendente** | Leitura de sete fontes técnicas; não houve leitura integral da monografia, modelo IFSP, regulamento e inventário completo da pasta nesta unidade | Completar fontes e inventário; conferir título com orientador, sem reescrever baseline ou fabricar evidências |

**Rastreabilidade desta unidade:** RN-03–05 → autorização entre agências e privacidade → testes de acesso cruzado pendentes → seção de requisitos/segurança; UC01–UC14 → rotas e telas do guia/registro histórico → VF01–VF16 históricos, não reexecutados → apêndice de casos de uso; CAT-RF-03 → fotos/migração aditiva → CAT-VF de upload/exclusão e pós-deploy pendentes → seção de incrementos; EVO-USO-01 → PRs #15/#39 e demais patches → TUT-01–09 pendentes → nova volta da espiral, avaliação humana pendente.

**Limitação explícita:** trabalho desta unidade é uma atualização rastreável de estado, não implementação nova do tutorial, execução de testes, aprovação, merge nem deploy. A concorrência exige comparação efetiva de patches antes de editar código compartilhado. Próxima unidade independente: reconciliar implementação e testes do tutorial numa branch isolada, sem depender do OAuth.


## Auditoria documental pontual — 21/11/2026, 04h (BRT)

**Entrega verificável desta rodada:** leitura direta por IDs exatos dos sete documentos técnicos obrigatórios, da monografia principal, do modelo de relatório PFC (dezembro/2025), do parecer de pré-banca (23/10/2026) e do histórico PROMPS TCC. Esta leitura **não equivale** a inventário integral da pasta, revisão ABNT conclusiva ou aprovação. Não houve alteração nos documentos-fonte.

**Divergência confirmada de título:** a monografia principal (ID `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg`) inicia com título “PROJETO DE ARQUITETURA DE SOFTWARE APLICADO AO TURISMO RODOVIÁRIO” e subtítulo “ENGENHARIA DE REQUISITOS PARA PLATAFORMAS DE LOGÍSTICA DE LAZER”; o modelo PFC (ID `1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo`) apresenta “Projeto de Arquitetura de Software Aplicado ao Turismo Rodoviário: Engenharia de Requisitos para Plataformas **Escaláveis** de Logística de Lazer”. O parecer de pré-banca (ID `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA`) já aponta risco de alegação de escalabilidade não comprovada. **Status: bloqueado para harmonização do título**; responsável: autora/orientador; pré-requisito: confirmar título oficial; condição de retomada: confirmação documentada. Não modificar capas nem atribuir resultados de escalabilidade.

**Rastreabilidade:** requisito acadêmico de consistência de título → capas/folhas de rosto dos dois documentos acima → comparação textual efetivamente feita nesta rodada → evidência: links pelos IDs → seções pré-textuais da monografia. EVO-USO-01 permanece **em execução**: PRs #15/#20/#21/#33/#35/#39 ainda exigem reconciliação de JS, template e CSS, testes TUT-01–09 e avaliação humana. OAuth próprio continua **bloqueado** para aceite real de fotos, sem impedir tutorial. PR #30 é draft; não considerar checklist integrado à branch principal.

**Próxima ação independente:** conciliar os HEADs do tutorial em branch isolada, executar Django/Chromium e regressões; para a auditoria, inventariar a pasta inteira e cotejar regulamento PFC com a monografia, preservando títulos até manifestação do orientador. Nenhum teste, merge ou deploy realizado nesta unidade.


## Verificação independente — 21/11/2026, 09h BRT

**Fontes efetivamente abertas por ID nesta rodada:** regras RN-01–41, documentação de desenvolvimento (133.468 caracteres), guia (15.633), casos UC01–UC14 (18.934), requisitos v3.0 (36.473), complemento CAT rev. 0.2 (17.590), registro de implementação (48.074), monografia principal (101.657), modelo IFSP (84.437), parecer de pré-banca (16.962) e histórico PROMPS TCC (30.920). Esses números representam extensão do texto retornado pelo conector, **não** validação de todas as páginas, formatação, anexos ou referências. Regulamento PFC em PDF ainda requer leitura específica. Fontes por URL e IDs constam no enunciado e seções anteriores deste checklist; datas editoriais não equivalem a aprovação.

**Correção factual A:** PR #2 consta **closed/merged** em 18/11/2026 às 14:05 UTC, merge SHA `72a488beb518b4dcca275970afb81892b97f3d4b`, HEAD da PR `faa5ba3d60b7f292be09676b13f39e9276eacafb`. Portanto **não** descrevê-la como aguardando merge. A descrição da própria PR mantém pendente a autorização OAuth própria do Django/Render e ensaios reais de fotos, sem afirmar deploy.

**EVO-USO-01:** PR #14 segue aberta/draft, HEAD `f20106af511f5637787f2b450cd1468e53c25924`, com dependências explícitas #15/#20/#21/#33/#35/#39 e conflitos sobre `tutorial-uso.js`. O JS lido na branch #15 possui ações Anterior/Próximo/Pular, Escape, destaque e oferta inicial, mas **não comprova** integração de Fechar separado, responsividade, fluxo entre páginas, testes executados ou aceite. Próxima ação executável: construir árvore integrada em branch isolada a partir de ancestry real, verificar JS/template e executar Django + Chromium; não sobrescrever branches concorrentes.

**Matriz e dependências atualizadas:**

| Item | Status | Evidência / último SHA conhecido | Próxima ação e condição de aceite |
|---|---|---|---|
| A / CAT | Em execução (merge feito; aceite pendente) | PR #2 merge `72a488b` | CAT-VF01–06, permissões, migração 0007 e persistência real após deploy; OAuth necessário somente para operações Drive |
| B / Drive | Bloqueado para ensaio OAuth real, estado de credenciais não confirmado | PR #2 descreve configuração pendente | Titular Google/Render autorizar aplicativo `drive.file` e configurar segredos fora do Git; ensaiar upload/exclusão sintéticos |
| EVO-USO-01 | Em execução, **não verificado** | PR #14 `f20106a`; JS da #15 SHA blob `41039cd` | Reconciliar #15/#20/#21/#33/#35/#39, testes TUT e avaliação da autora/orientador |
| G / auditoria global | Em execução, **não concluída** | Leitura textual direta das 11 fontes nesta rodada | Ler regulamento PDF, inventariar pasta completa, revisar monografia integral e confirmar alterações após salvar |

**Entrega desta rodada:** atualização documental de rastreabilidade em branch já existente, sem alterar migrations, templates, dados ou demo. **Não executados:** suíte Django, Playwright/Chromium, deploy, upload real, merge ou avaliação humana. **Próxima rodada:** priorizar integração/testes do tutorial, sem produzir novo checklist paralelo. A ausência de acesso a arquivos locais não deve ser confundida com ausência de código no GitHub.
