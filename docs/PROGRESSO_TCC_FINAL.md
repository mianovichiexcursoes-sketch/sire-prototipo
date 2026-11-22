# SIRE — Progresso final rastreável

Atualizado em 2026-11-17. Registro de planejamento e leitura de fontes; **não equivale a aceite funcional**. Branch de trabalho: `etapa/ficha-fotos-sire`; demo preservada em `etapa/postgresql-windows`. Não alterar baseline ER-SIRE 2.1, UC01–UC14 nem as seis entidades históricas.

## Fontes oficiais verificadas nesta rodada

Leitura direta pelo conector Google Drive em 17/11/2026, por ID exato (conteúdo acessível):

| Fonte | ID | Referência de versão/data identificada |
|---|---|---|
| Regras RN-01–RN-41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | documento de regras, versão não indicada no cabeçalho |
| Desenvolvimento / baseline | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | ER-SIRE 2.1; histórico posterior 2.6 |
| Guia do protótipo | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | guia com atualização PostgreSQL |
| Casos de uso | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | UC01–UC14 |
| Requisitos | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | versão 3.0 PFC2 |
| Complemento catálogo | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | revisão 0.2 |
| Registro técnico | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | registro desde 20/10/2026 |
| Monografia | 1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg | título: Projeto de Arquitetura de Software Aplicado ao Turismo Rodoviário |
| Modelo IFSP | 1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo | dezembro/2025 |
| Regulamento IFSP | 1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL | março/2026 |
| Pré-banca | 1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA | 23/10/2026 |
| Histórico de orientações | 1mpNI5u26q3NzVgXFeeMCHZgfWdxCgsG-WTangQWVRrE | histórico, não fonte normativa |

## Checklist de execução e dependências

| Etapa | Estado | Último commit / evidência | Próxima ação e dependência |
|---|---|---|---|
| A. PR #2 ficha, textos, fotos, migração 0007 | EM EXECUÇÃO | [PR #2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2); código e roteiro em `docs/INCREMENTO_FICHA_FOTOS_DRIVE.md`; testes desta rodada **não executados** | Conferir diffs, CI e testes em ambiente isolado, reconciliando com qualquer edição concorrente do Work; não mesclar |
| B. OAuth Drive e fotos reais | BLOQUEADO | Script `scripts/autorizacao_drive.py`; nenhum token nem upload real verificado nesta rodada | Pré-requisito: autorização OAuth própria do Django e três segredos no Render; responsável: autora/operador com acesso Google Cloud e Render. Impacto: impede ensaio real de upload, exclusão e persistência após deploy. Retomar após configuração e evidência de autenticação, sem publicar credenciais |
| C. CPF minimizado e sintético | PENDENTE | RN-04, RN-05 e UC01 lidos; sem implementação comprovada | Definir finalidade e política LGPD; implementar isoladamente após confirmar estado das branches do Work, com testes de dígitos verificadores e dados fictícios |
| D. UX de reserva | PENDENTE | UC de reserva e RN-17–30 como fontes | Melhorar resumo, embarque e confirmação sem simular pagamento; requer conciliação com branch ativa |
| E. Painéis | PENDENTE | RN-03–05 | Melhorar consultas existentes preservando perfis; requer conciliação com branch ativa |
| F. Verificação integral | PENDENTE | Nenhuma nova execução comprovada | Rodar SQLite/PostgreSQL, VF e CAT-VF, permissões, navegador; testes reais de Drive dependem de B |
| G. Auditoria documental global | PENDENTE | Fontes oficiais acessadas; pré-banca aponta divergência IA/Codex e título/escalabilidade | Inventariar pasta completa, auditar monografia e anexos, registrar divergências sem apagar histórico; validar título com orientador |

## Rastreabilidade incremental (a expandir)

| Regra / requisito | Implementação prevista | Verificação | Evidência | Monografia |
|---|---|---|---|---|
| RN-03–05, CAT-RF-02 | `sire/models.py`, `forms.py`, views/templates; migração 0007 | edição entre agências | pendente | seção de evolução |
| CAT-RF-03 | `FotoExcursao`, `drive_fotos.py`, galeria | 6 fotos, tipo/tamanho, exclusão, privacidade | código descrito; teste real pendente | evolução e riscos |
| UC01, RN-04–05, EVO-CPF (proposto) | formulário/modelo/migração aditiva a definir | CPF sintético válido/inválido, acesso por papel | pendente | LGPD e extensão |
| UC de reserva, RN-17–30 | views/templates existentes | capacidade, embarque, concorrência | pendente de regressão | resultados |

## Bloqueios e integridade

- Não há prova nesta rodada de CI verde, deploy, migração aplicada no Render, persistência de fotos ou teste real de OAuth. Não registrar esses resultados como concluídos.
- Não inferir inatividade do outro agente apenas pela ausência de revisão no GitHub; antes de editar código compartilhado, comparar HEAD, diffs e mudanças recentes.
- Conflito documental conhecido (pré-banca C1): texto histórico “não usar Codex” versus implementação assistida por IA. Preservar histórico, registrar correção transparente na documentação vigente após revisão acadêmica.
- PR #2 não possui revisões ou threads registradas na consulta desta rodada. A situação de checks e merge ainda requer consulta específica.

## Próxima unidade independente

Auditar diff e testes de A sem tocar na demo. Se outro agente estiver alterando A, iniciar documentação independente de propósito, retenção e minimização do CPF antes de mexer em modelos ou migrations. Nenhum merge ou deploy automático sem aceite verificável.

## Rodada de reconciliação — 17/11/2026, 10h56 (Brasília)

**Unidade executada:** auditoria documental independente, sem modificar código ou migrações e sem merge/deploy. As fontes originais RN-01–30, baseline ER-SIRE 2.1, guia, UC01–14, requisitos, complemento CAT revisão 0.2 e registro de implementação foram reabertas diretamente no Google Drive. A migração `0007_ficha_e_fotos_drive.py` foi inspecionada: adiciona `descricao`, `roteiro`, `inclusos` com default vazio e cria `FotoExcursao`, dependente de `0006_excursao_tipo_pacote`; é estruturalmente aditiva, **não prova migração aplicada**.

**Trabalho concorrente detectado:** a PR #2 agora lista `.github/workflows/fotos-regressao.yml`, `sire/test_fotos_regressao.py` e `docs/AUDITORIA_FOTOS_SEGURANCA_20261117.md`, que não estavam contemplados no resumo inicial. A auditoria desse outro trabalho declara correções de cache HTTP, bloqueio concorrente, checagem de agência, IDs de Drive e compensação de falha de gravação no commit `5850522c03a2bc87ae2a373b225155894194c0c4`, e aponta PR #4 (suíte) e PR #5 (correções). Evidências declaradas: [Actions fotos SQLite/PostgreSQL](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44080498422) e [Actions suíte geral](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44080498754). **Nesta rodada os logs brutos e status dessas execuções não foram conferidos independentemente; não tratar a declaração documental como nova execução.**

**Dependências/coordenação:** A permanece EM EXECUÇÃO, com código e testes em andamento por outro agente. Não editar `views.py`, `models.py`, migrações, templates nem a PR #2 enquanto não reconciliar PR #4/#5 e respectivos HEADs. B permanece BLOQUEADO pela autorização OAuth do aplicativo, com responsável autora/operador Google Cloud + Render; sem B não validar fotos reais ou persistência após deploy. C pode avançar de modo independente apenas em especificação de finalidade, minimização e política de acesso do CPF (RN-04/05 e UC01), sem coletar CPF real; implementação requer checagem de branches ativas. D/E seguem independentes de B, sujeitos a reconciliação de código. F parcialmente possível com Drive simulado; aceite real dependente de B. G mantém auditoria global pendente.

**Próxima ação verificável:** comparar HEAD, status de CI e conteúdo das PRs #2/#4/#5; consolidar matriz CAT-RF-02/03/04 → migração 0007 / views / testes FOTO → evidências; só então revisar lacunas sem duplicar alterações. Em paralelo, preparar especificação EVO-CPF/LGPD em documento separado e sintético. **Nenhum teste, merge, deploy ou aprovação humana foi executado nesta rodada.**


## Reconciliação documental — 20/11/2026, 03h56 (America/Sao_Paulo)

**Unidade independente versionada:** atualização do checklist histórico após leitura direta das sete fontes oficiais por IDs exatos no Google Drive e inspeção do README da branch de demonstração. Nenhum código, migration, template, dado real ou configuração do Render foi alterado. Não houve execução de teste, CI, deploy ou avaliação do orientador nesta unidade.

**Fontes reabertas nesta unidade:** RN-01–RN-41 (ID `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`), desenvolvimento/baseline (ID `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`), guia (ID `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`), UC01–14 (ID `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`), requisitos v3.0 (ID `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`), catálogo rev. 0.2 (ID `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`) e registro técnico (ID `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`). Revisões retornadas pelo conector nesta consulta; datas de última edição não foram verificadas.

**Divergência de estado identificada:** este checklist, atualizado originalmente em 17/11, descreve A como em execução e B como bloqueado, mas o README da branch `etapa/postgresql-windows` relata integração na PR #18, ensaio OAuth real em PostgreSQL local em 18/11, PRs #24/#28 e relatório de aceite. Portanto, os estados anteriores são **históricos, não a situação atual confirmada**. A verificação de deploy, persistência pós-redeploy no Render, CPF, aceite humano e avaliação do orientador continua pendente. Não reinterpretar teste local OAuth como comprovação de persistência no Render.

| Item | Estado desta unidade | Evidência disponível | Próxima ação / dependência |
|---|---|---|---|
| A. Ficha e fotos | INTEGRADO SEGUNDO README; ACEITE PARCIAL | README na branch de demo cita PR #18, migration 0007 e PR #28 | Verificar PRs/SHAs e cenários CAT-VF, sem alterar arquivos concorrentes |
| B. OAuth Drive | LOCAL RELATADO; RENDER NÃO VERIFICADO | README aponta `docs/OAUTH_EXECUCAO_REAL_2026-11-18.md` | Testar upload, exclusão e persistência após redeploy no ambiente autorizado; depende de credenciais seguras e janela de teste |
| C. CPF | PENDENTE DE RECONCILIAÇÃO | Baseline UC01 e RN-04/05 verificadas; README não o declara implementado | Inspecionar branches de evolução antes de alterar modelos; só dados sintéticos |
| D/E. UX e painéis | PENDENTE DE RECONCILIAÇÃO | README e fontes oficiais, sem teste desta unidade | Conferir funcionalidades efetivas, papéis e regressões |
| EVO-USO-01 | IMPLEMENTADO SEGUNDO README; AVALIAÇÃO HUMANA PENDENTE | README cita tutorial contextual, PR #18, ressalva móvel e ausência de avaliação do orientador | Conferir testes de teclado, foco, Escape e responsividade; solicitar nova tentativa via autora após revisão |
| F. Verificação | PARCIAL RELATADA, NÃO REEXECUTADA | README cita 32 capturas, PR #24 e PR #28, três ressalvas e um bloqueio | Validar logs, cenários faltantes e evidência pós-deploy |
| G. Auditoria global | PENDENTE | Fontes acadêmicas da baseline verificadas; monografia completa não relida nesta unidade | Inventariar pasta TCC JULIA — SIRE e auditar monografia e anexos com modelo IFSP |

**Rastreabilidade desta unidade:** RN-03/04/05 → permissões entre agências e dados pessoais → cenários de autorização ainda a reconferir → README/PR #28 → seção de segurança e limites da monografia; UC01–UC14 → `sire/views.py`, formulários e templates (mapeamento histórico no registro técnico) → VF01–VF16 → relatório de aceite citado pelo README → apêndice UC; EVO-USO-01 → `tutorial-uso.js` segundo README → TUT-01–06 → PR #18 e PR #28 → iteração da espiral a avaliar. Esses vínculos não equivalem a execução de testes nesta unidade.

**Concorrência:** há branches específicas `feat/evo-uso-01-tutorial-20261118`, `fix/tutorial-mobile-viewport-20261119` e `docs/auditoria-integracao-tutorial-20261120-0304`; este commit altera somente o checklist em branch própria. Antes de integrar, comparar com a versão mais recente do checklist e reconciliar com o outro agente. A demo permanece intacta.

**Próxima unidade:** inspecionar o estado atual das PRs #18/#24/#28 e a auditoria móvel, reconciliar o checklist com evidências reais, sem reimplementar tutorial ou OAuth local já relatados. Bloqueio externo: avaliação pelo orientador depende de revisão humana e comunicação autorizada pela autora.


## Verificação incremental — 21/11/2026 (20h56 Brasília)

**Fontes efetivamente relidas por ID:** regras RN-01–41, baseline de desenvolvimento 2.1 (histórico até 2.6), guia de implementação, UC01–UC14, requisitos v3.0, catálogo revisão 0.2 e registro técnico. Não foi realizada nesta unidade leitura integral da monografia nem do modelo IFSP. Esta nota não equivale a auditoria global.

**Achado verificável de código:** na branch de demo `etapa/postgresql-windows`, `sire/templates/sire/base.html` já inclui `sire/js/tutorial-uso.js` e atributo de perfil `data-sire-role`. O arquivo `sire/static/sire/js/tutorial-uso.js` já implementa passos por perfil, botão Como usar, orientação sem envio de formulários, indicação de que reserva não é pagamento e tratamento de indisponibilidade de armazenamento via try/catch. Portanto **não reimplementar tutorial** sem conciliar esta versão e as branches `feat/evo-uso-01-tutorial-20261118`, `fix/tutorial-mobile-viewport-20261119` e `test/tutorial-storage-indisponivel-20261120`. A presença do código não comprova funcionamento em navegador, acessibilidade, aceite humano ou deploy recente.

**EVO-USO-01 — EM VERIFICAÇÃO:** fonte: feedback da autora de 18/11; implementação inspecionada: `base.html` e `tutorial-uso.js` na branch de demo; cenário pendente: abrir primeiro acesso por Visitante/Passageiro/Agente, navegar Anterior/Próximo/Pular/Fechar, Escape, foco e celular, sem disparar POST; evidência atual: inspeção estática do código; monografia: quadrantes da nova volta da espiral ainda sem avaliação humana comprovada. Próxima ação: confrontar o código com testes e PRs integradas, executar navegador em ambiente isolado e documentar resultado real.

**Dependências reavaliadas:** OAuth do aplicativo não é dependência do tutorial; testes reais de persistência de fotos pós-redeploy continuam condicionados a autorização/ambiente verificáveis. A avaliação de uso depende do orientador, por intermédio da autora. Não houve testes executados, merge, deploy, alteração de dados, revisão do orientador ou atualização da monografia nesta unidade. A próxima rodada deve priorizar evidência de execução dos cenários TUT sem repetir implementação já existente.


## Auditoria incremental de código — 22/11/2026, 20h (Brasília)

**Fontes oficiais lidas nesta unidade por ID exato:** RN-01–41, Desenvolvimento SIRE (baseline ER-SIRE 2.1), Guia do Protótipo, UC01–UC14, Requisitos v3.0, CAT revisão 0.2 e Registro de Implementação. Não equivale a leitura integral da monografia ou auditoria ABNT. Preservar seis entidades e UC históricos; EVO-USO-01 é extensão separada.

**Comparação reprodutível de blobs GitHub** de `sire/static/sire/js/tutorial-uso.js` (leitura, sem execução):

| Ref | SHA do blob | Evidência estática | Estado |
|---|---|---|---|
| `etapa/postgresql-windows` | `aac1a7b4e13f5a401d75eb6887cd9c191a2d0776` | Já contém tutorial por perfil, Escape, foco, `getClientRects`, local/sessionStorage protegidos; não contém ação textual `Fechar` | Implementado parcialmente; aceite navegador pendente |
| `fix/tutorial-mobile-viewport-20261119` | `baab4e37fb0f110076455cd502f832d1f75bed57` | Em relação ao JS da demo, acrescenta `max-height:min(45dvh,22rem)`, botão `data-action=fechar` e tratamento de fechar | Correção candidata; não integrar sem reconciliar HEAD/template |
| `feat/evo-uso-01-tutorial-20261118` | `41039cd9f6d464cd746e70ee33656d97f26f4946` | Implementação alternativa com `Anterior` e `Fechar`, mas sem `getClientRects` e sem sessionStorage textual | Linhagem divergente; não aplicar por substituição integral |

**Verificação negativa limitada:** nenhuma das três versões contém as sequências literais `submit(`, `requestSubmit(` ou `click(` no JS lido. Isto **não** demonstra ausência de submissão por todos os caminhos, nem valida comportamento em navegador. O botão `Voltar` na versão mobile atende à navegação anterior em termos de rótulo, sujeito a teste funcional.

**EVO-USO-01 — EM EXECUÇÃO:** primeiro reconciliar o JS da demo com as correções pontuais da versão mobile e verificar `base.html`/outras PRs; executar testes de teclado, Escape, Fechar, Voltar, Próximo, Pular, foco, 320/375px, perfis e ausência de POST com dados sintéticos. OAuth próprio do Django **não é dependência** desses testes. Responsável pelo aceite humano: autora/orientador após evidências. Sem teste, CI, merge, deploy ou aprovação realizados nesta unidade.

**B — BLOQUEADO para teste real de Drive:** falta evidência de OAuth `drive.file` próprio do aplicativo e configuração segura no Render; impacto: upload/exclusão/persistência pós-deploy não podem ser aceitos; responsável: titular do aplicativo/Render; retomar após autorização verificável, sem divulgar segredos. Continuar tarefas independentes de tutorial/documentação.

**Próxima ação independente:** criar patch mínimo em branch isolada a partir do HEAD mais recente da demo, após conferir PRs e template; testar antes de propor integração. Checklist nesta branch documental, não na demo; reconciliar com PRs #66/#70 antes de merge.


## Verificação de dependências e artefatos — 22/11/2026, 20h56 (Brasília)

**Leitura direta nesta rodada:** sete fontes oficiais por ID exato: RN-01–RN-41 (documento `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`), baseline ER-SIRE 2.1 (`19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`), guia (`1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`), UC01–UC14 (`1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`), requisitos v3.0 (`1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`), CAT rev. 0.2 (`1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`) e registro (`1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`). Acesso ao conteúdo confirmado; datas de modificação não consultadas. Monografia e regulamento IFSP não auditados nesta unidade.

**Correção factual importante:** `docs/PROGRESSO_TCC_FINAL.md` **existe** na branch da demo `etapa/postgresql-windows` (blob `ddab6696c56fd072a8e5c3486698ef87947881f6`), e também nesta branch documental (blob anterior `0305228cfb42b3fc343b9a98416597317cf93c80`). Ausência na `main` não significa ausência na demo. Reconciliar ambos antes de publicar qualquer checklist único.

**Arquivos e HEAD de conteúdo lidos nesta rodada:** `sire/static/sire/js/tutorial-uso.js` na demo: blob `aac1a7b4e13f5a401d75eb6887cd9c191a2d0776`; na branch `fix/tutorial-mobile-viewport-20261119`: blob `baab4e37fb0f110076455cd502f832d1f75bed57`. `sire/templates/sire/base.html` é idêntico nas duas branches, blob `7dfff230ebb346a007cdf2e65533c9bc4e84c483`. Assim, **a divergência inspecionada se concentra no JavaScript**, não no template base dessas duas refs. Isto não exclui alterações concorrentes posteriores nem prova testes.

| ID | Estado | Evidência / último commit | Pré-requisito e próxima ação |
|---|---|---|---|
| EVO-USO-01 | EM EXECUÇÃO; verificação pendente | Blobs JS `aac1a7b` / `baab4e3`, template `7dfff23`; nenhum teste nesta rodada | Reconciliar com PRs #33/#35/#64, criar patch mínimo em branch isolada e testar TUT teclado, Escape, foco, perfis, 320/375px e ausência de POST |
| B OAuth e persistência de fotos | BLOQUEADO para aceite Render | Sem evidência nova de OAuth Django autorizado no Render; relato histórico de ensaio local não substitui prova pós-deploy | Responsável: titular do aplicativo/Render; retomar após autorização segura e janela de teste; não divulgar credenciais |
| F Testes integrados | PENDENTE | Não houve execução nesta rodada | Preparar ambiente isolado e dados sintéticos, verificar SQLite/PostgreSQL e testes de navegador |
| G Auditoria acadêmica | PENDENTE | Fontes técnicas relidas, sem monografia integral | Inventariar pasta, comparar modelo IFSP e documentos após integração técnica |

**Critérios verificáveis para a próxima unidade:** registrar SHA de branch antes/depois, diff pontual do JS, comandos de teste e saída real; nenhuma submissão automática, nenhum dado pessoal real, nenhum merge/deploy antes da revisão. Não reabrir implementação alternativa completa se o patch móvel já resolver a diferença. A demo não foi modificada nesta unidade.
