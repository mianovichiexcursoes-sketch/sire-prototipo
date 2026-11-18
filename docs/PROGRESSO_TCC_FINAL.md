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


## Rodada de verificação independente — 17/11/2026, 12h03–12h (Brasília)

**Fontes:** reabertos pelos IDs originais os 11 Google Docs oficiais/históricos e o regulamento IFSP em PDF. Referências e revisões são aquelas listadas acima; o conteúdo foi consultado, sem edição de monografia.

**Reconciliação GitHub:** PR #2 HEAD `faa5ba3d60b7f292be09676b13f39e9276eacafb`; PR #7 (OAuth seguro) HEAD `0a7f77cee3785bf755ccfe4927c6014a0d1063e7`, ainda aberta em draft. PRs #3 e #6 também abertas, documentação concorrente. PRs #4/#5 não aparecem entre abertas (histórico requer consulta própria antes de integrar). Três execuções GitHub Actions para HEAD da PR #2 concluídas com `success`: [geral 44097900342](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097900342), [fotos SQLite/PostgreSQL 44097899889](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097899889), [geral 44097890889](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097890889). **Status de workflow conferido via API, não equivale a teste real de Drive nem deploy.**

**Entrega isolada desta rodada:** [EVO_CPF_LGPD_PROPOSTA.md](EVO_CPF_LGPD_PROPOSTA.md), commit `6d4e8f67376b4d9b48cd0c14b7ef154107390231`, branch `docs/evo-cpf-lgpd-20261117`. Documento especifica finalidade a validar, minimização, acessos RN-04/05, gates de proteção, critérios sintéticos e rastreabilidade; nenhum CPF, modelo ou migration foi alterado. C = **EM EXECUÇÃO (especificação proposta; implementação bloqueada por aprovação de finalidade/necessidade e reconciliação de código)**.

**B permanece BLOQUEADO:** OAuth real do aplicativo e credenciais de ensaio não comprovados; responsável autora/operador Google Cloud/Render; impacto nos testes reais de foto e persistência; retomar apenas com autorização segura e ambiente de ensaio. A = EM EXECUÇÃO, com CI verde no HEAD observado, mas ainda depende de revisão e testes reais. D/E/F/G pendentes.

**Próxima ação:** abrir detalhes das execuções CI e diffs PR #2/#7, conferir cadeia de PRs fechadas, revisar proposta EVO-CPF antes de qualquer implementação, sem tocar na demo. Não houve merge, deploy, OAuth real ou testes locais nesta rodada.


## Reconciliação independente — 17/11/2026, 13h04 (Brasília)

**Fontes verificadas nesta rodada diretamente por ID:** regras RN-01–41, baseline de desenvolvimento, guia de implementação, casos de uso UC01–UC14, ERS 3.0, complemento CAT revisão 0.2 e registro de implementação (IDs na tabela de fontes acima). Não houve edição desses originais. Os demais documentos da auditoria global continuam pendentes de releitura integral nesta etapa.

**Estado observado pelo conector GitHub:** PR #2 aberta/draft, HEAD `faa5ba3d60b7f292be09676b13f39e9276eacafb`; PR #4 **merged** (HEAD de origem `aa3820fead0d07587847b094929aa7d66b52c3f2`) e PR #5 **merged** (HEAD de origem `1b6675ed838644dd987cb7e780c8dfba3e53c2ba`) na branch `etapa/ficha-fotos-sire`; PR #6 aberta/draft com base na branch de segurança; PR #7 aberta/draft, base `fix/fotos-cache-lock-20261117`, HEAD `0a7f77cee3785bf755ccfe4927c6014a0d1063e7`; PR #8 aberta/draft, base `etapa/ficha-fotos-sire`, HEAD observado antes deste registro `461eeeec3c8f22716aeaf4e0e53337de45d6b106`. **PR #7 não deve ser presumida integrada à PR #2**: sua base é branch intermediária, embora a PR #5 tenha sido mesclada; reconciliar ancestralidade e diffs antes de retarget ou merge. Ausência de merge na PR #7 não significa ausência de seu código na demo, que exige conferência separada.

**Entrega desta rodada:** inventário verificável da cadeia de PRs e risco de base divergente, sem editar modelos, migrações, templates, código OAuth ou ambiente. O item A segue EM EXECUÇÃO (PR #2 draft, revisão final pendente). O item B segue BLOQUEADO (OAuth real e credenciais seguras não comprovados; responsável autora/operador Google Cloud/Render; condição para retomar: autorização do aplicativo e serviço isolado). C segue EM EXECUÇÃO apenas na documentação, aguardando aprovação da finalidade/necessidade LGPD antes de codificar. D/E/F/G pendentes. A conclusão de CI anterior não prova fotos reais, deploy ou aceite.

**Próxima unidade independente:** inspecionar patches e jobs de CI das PRs #2/#5/#7; comparar bases e HEADs atuais e propor reconciliação segura; não alterar a demo. Se código estiver em edição concorrente, continuar matriz de rastreabilidade e auditoria documental independente. Nenhum teste novo, merge, deploy ou autorização Google foi executado nesta rodada.


## Auditoria de evidências — 17/11/2026, 14h (Brasília)

**Gate documental:** reabertos por IDs exatos todos os 12 arquivos exigidos (11 documentos Google e regulamento PFC PDF), incluindo RN-01–41, baseline ER-SIRE 2.1, guia, UC01–14, ERS 3.0, CAT rev. 0.2, registro, monografia, modelo IFSP, pré-banca e histórico. Metadados de modificação recuperados pelo Drive: regras 28/09/2026; baseline 16/11; guia 12/11; UC 22/10; ERS 23/10; CAT e registro 17/11; monografia 17/11; modelo 30/06; regulamento 28/09; parecer 23/10; histórico 28/09. Leitura de cabeçalhos e trechos pertinentes nesta rodada; **não é auditoria integral da monografia**.

**CI auditado por jobs da execução 44097899889, commit da PR #2 `faa5ba3d60b7f292be09676b13f39e9276eacafb`:** jobs `fotos-sqlite` e `fotos-postgresql` com status `completed/success`; etapas `Verificar configuracao Django`, `Verificar migracoes pendentes`, `Executar regressao de fotos com Drive simulado`, `Conferir configuracao e migrations` e `Testar fotos e concorrencia real em PostgreSQL descartavel` reportaram `success`. [Execução verificável](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097899889). Também retornaram `completed/success` as execuções 44097900342 do mesmo SHA. **Isto não comprova OAuth, Drive real, Render, persistência pós-deploy, testes visuais nem contagens detalhadas além das que os jobs explicitam.**

**Reconciliação sem escrita concorrente:** PR #2 descreve a ficha e migração 0007; PR #5 descreve segurança de fotos e regressão simulada, já integrada segundo reconciliação anterior; PR #7 continua com proposta de OAuth protegido, incluindo fluxo administrativo que não imprime token e bloqueio explícito da demo, mas sua base intermediária exige verificação antes de merge; PR #8 é documentação independente. Descrições das PRs não são prova de aplicação. Evitou-se modificar código, migrações, templates, OAuth ou branch da demo.

**Estados e dependências atualizados:** A = EM EXECUÇÃO (CI simulado confirmado, revisão humana e integração ainda pendentes); B = BLOQUEADO (responsável autora/operador Google Cloud/Render; falta OAuth próprio e segredos seguros no ambiente de ensaio; condição: autorização e ensaio isolado; impede fotos reais e pós-deploy); C = EM EXECUÇÃO DOCUMENTAL / BLOQUEADO PARA CÓDIGO (responsável autora/revisão LGPD; falta confirmar necessidade, finalidade e base legal antes de coleta); D/E = PENDENTE (trabalho de UX/painéis exige reconciliação do Work); F = PARCIAL (CI de fotos simulado passou; aceite completo pendente); G = PENDENTE (inventário integral e monografia não auditados).

**Próxima unidade:** inspecionar diferenças de base e HEAD da PR #7 e sua interação com PR #2 sem retarget automático; depois preparar matriz de cobertura de VF/CAT e lacunas de testes em documento isolado. Não publicar sem evidência de OAuth e revisão. Nenhum merge, deploy, teste local ou alteração de documentos originais nesta rodada.


## Auditoria de ancestralidade OAuth — 17/11/2026, 14h55 (Brasília)

**Fontes oficiais reabertas:** todos os 12 itens da tabela de fontes por ID exato, incluindo RN-01–41, UC01–14, baseline, CAT 0.2, monografia, modelo e regulamento IFSP. Consulta documental não equivale a revisão integral da monografia. Não houve edição dos documentos originais.

**Evidência nova e verificável:** comparação GitHub `etapa/ficha-fotos-sire...fix/oauth-seguro-20261117` (https://github.com/mianovichiexcursoes-sketch/sire-prototipo/compare/etapa/ficha-fotos-sire...fix/oauth-seguro-20261117) retornou **diverged**, 2 commits à frente e 3 atrás; merge-base `1b6675ed838644dd987cb7e780c8dfba3e53c2ba`, HEAD observado da ficha `faa5ba3d60b7f292be09676b13f39e9276eacafb`. A diferença específica do OAuth tem quatro arquivos: `scripts/autorizacao_drive.py`, `sire/tests/test_oauth_drive.py`, `docs/OAUTH_EXECUCAO_2026-11-17.md` e `docs/INCREMENTO_FICHA_FOTOS_DRIVE.md`. **Não fazer merge direto, nem mudar a base da PR #7 automaticamente**: primeiro verificar se os três commits da ficha já incluem outras mudanças do Work e repetir CI após reconciliação.

**Bloqueio B refinado:** relatório [OAuth de 17/11](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/fix/oauth-seguro-20261117/docs/OAUTH_EXECUCAO_2026-11-17.md) registra Google Cloud Console inacessível naquele ensaio, sem autorização OAuth real. Registra também que o workspace Render SIRE foi confirmado, mas somente `sire-demo` e `sire-demo-db` free existem, sem banco persistente isolado de ensaio. Responsáveis: titular Google/operador do ambiente; pré-requisitos: Console acessível, consentimento drive.file e infraestrutura isolada. Impacto: bloqueia upload, exclusão e persistência real pós-redeploy; **não bloqueia** revisão documental, UX independente e testes simulados. Retomar com autorização e banco isolado, sem utilizar o banco da demo, cobrar ou expor segredos.

**Conflito acadêmico adicional constatado:** monografia principal apresenta subtítulo “Engenharia de Requisitos para Plataformas de Logística de Lazer”, enquanto o modelo IFSP consultado contém “Plataformas Escaláveis de Logística de Lazer”. Não alterar título sem confirmação do orientador; registrar divergência na auditoria final. O parecer de pré-banca já alerta para alegação de escalabilidade não comprovada.

**Status após a unidade:** A EM EXECUÇÃO, com CI simulado previamente verificado; B BLOQUEADO para ensaio real; C EM EXECUÇÃO documental e BLOQUEADO para coleta por finalidade/base legal; D/E PENDENTES; F PARCIAL; G PENDENTE. Nenhum teste novo executado, merge, deploy, mudança de modelo ou alteração da demo nesta unidade. **Próxima unidade independente:** mapear casos VF01–16 e CAT-VF01–06 para os testes existentes e lacunas, sem tocar nas branches de código do Work. Após reconciliar HEADs, avaliar cherry-pick isolado dos dois commits OAuth em branch nova e CI, sem promover à demo.


## Entrega independente — 17/11/2026, 15h55 (Brasília)

**Commit verificável:** `c5b8adf36c5cfa56581bc928b36ae189fbb8cd12` — [matriz de verificação pendente](MATRIZ_VERIFICACAO_PENDENTE_20261117.md), na branch documental da PR #8. Leitura direta dos 12 documentos-fonte por ID original nesta rodada; a matriz relaciona VF01–VF16 e CAT-VF01–06 aos UC, RN, arquivos, evidências requeridas e dependências. É uma **entrega documental**, não execução de testes nem aceite.

**Status F:** EM EXECUÇÃO DOCUMENTAL (matriz criada); testes reais continuam PENDENTES. CI com Drive simulado anteriormente verificado não comprova Drive real. **B:** BLOQUEADO — falta OAuth próprio e segredos em ensaio isolado; responsável autora/operador Google Cloud/Render; impacto: fotos reais, exclusão e persistência pós-deploy; retomar com autorização segura comprovada. **A:** EM EXECUÇÃO por outro agente; evitar alterações concorrentes. **C:** proposta LGPD em revisão, sem código ou CPF real. **D/E/G:** pendentes.

**Próxima ação:** conferir correspondência linha a linha da matriz com descrições oficiais dos VF, inspecionar estado atual das PRs #2/#7/#8 e executar testes independentes somente após reconciliação de HEAD e ambiente; preservar demo. Nenhum merge, deploy, migração ou teste novo foi executado.


## Conciliação histórica VF — 17/11/2026, 17h04 (Brasília)

**Entrega verificável:** commit `61a551d575a7d78b82b492181904cc5ec5f41178`, [matriz VF/CAT atualizada](MATRIZ_VERIFICACAO_PENDENTE_20261117.md). Os 12 documentos-fonte exigidos foram reabertos diretamente pelos IDs originais nesta rodada; para a conciliação foram examinadas as seções 5 e 10.2 do registro técnico, além de RN-01–41, UC01–14 e guia. A matriz agora separa os 16 **resultados históricos declarados** dos ensaios HTTP/ORM em SQLite de 22/10/2026 dos **testes ainda pendentes** sobre o código atual. Nenhum VF foi reexecutado nesta rodada; os arquivos `VFxx.json` e `execucao-2026-10-22.json` citados no registro ainda precisam ser localizados e conferidos.

**Estado F:** EM EXECUÇÃO documental (conciliação histórica), **não concluído**. Último commit de evidência documental: `61a551d`. Próxima ação: recuperar artefatos JSON históricos e comparar com o commit da baseline, depois planejar regressão em ambiente isolado para SQLite/PostgreSQL e CAT-VF. **Estado B:** BLOQUEADO para ensaio real de Drive; pré-requisitos OAuth próprio `drive.file`, segredos seguros e ambiente de ensaio ainda não comprovados; responsável autora/operador com acesso Google Cloud/Render; retomar somente após confirmação independente. **Estado A:** EM EXECUÇÃO na PR #2 sob coordenação com outro agente; não editar código compartilhado. **Estado C:** proposta documental, aprovação da finalidade LGPD pendente. D/E/G permanecem pendentes.

**Limite:** nenhuma mudança de código, migração, CI, PR base, merge ou deploy foi realizada; demo mantida intacta. O sucesso histórico não substitui aceite da versão atual.


## Recuperação de evidência histórica VF — 17/11/2026, 18h (Brasília)

**Entrega documental verificada:** localizados na branch preservada `etapa/postgresql-windows` os arquivos [`docs/resultados-http.json`](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/etapa/postgresql-windows/docs/resultados-http.json) (blob `e3323f54f39a995dc479f39bcb384dfc0a599a5e`) e [`docs/VERIFICACAO.md`](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/etapa/postgresql-windows/docs/VERIFICACAO.md) (blob `89be19913a761b5ee4b826ad0b5be558a17566c9`). O JSON contém registros identificados VF01 a VF16, além de B1 e EXTRA; o relatório explica o método HTTP/ORM local, dados fictícios e a inexistência de suíte automatizada naquela execução. Os 16 identificadores foram conferidos na leitura do JSON; o registro de 20/10/2026 é histórico, **não** novo teste nem prova de aprovação da versão atual.

**Limite da recuperação:** a árvore Git recursiva da branch `etapa/postgresql-windows` foi consultada; nela **não** constam arquivos individuais `VFxx.json` nem `execucao-2026-10-22.json`. Busca nominal no Google Drive por `VF01.json` e `execucao-2026-10-22` retornou somente o documento que os menciona, não os arquivos. Portanto, o JSON agregado encontrado é evidência histórica concreta, mas **não** substitui os arquivos individuais ainda não recuperados nem permite atribuir a ele a data 22/10 sem confirmação adicional. Não concluir que os arquivos individuais não existam no ZIP histórico; esse pacote ainda requer inventário específico.

**Fontes oficiais consultadas nesta rodada:** RN-01–41, baseline ER-SIRE, guia, UC01–14, requisitos, CAT, registro de implementação, monografia, modelo IFSP, parecer e PROMPS TCC foram lidos diretamente por IDs exatos no Drive; o regulamento PDF requer conferência específica na auditoria final. Nenhum documento original foi editado.

**Estado F:** EM EXECUÇÃO, recuperação parcial de evidência histórica concluída nesta unidade; testes atuais SQLite/PostgreSQL, CAT e navegador continuam pendentes. **Próxima ação:** conferir conteúdo e origem do ZIP histórico `sire-prototipo-completo.zip` na pasta Drive, recuperar se possível os arquivos individuais, comparar baseline/commit e só então planejar reexecução isolada. **B:** BLOQUEADO para Drive real até OAuth `drive.file` e ambiente isolado; **A:** PR #2 sob revisão concorrente; **C:** LGPD aguardando aprovação da finalidade. Nenhum merge, deploy, alteração da demo ou teste novo.


## Recuperação integral das evidências VF — 17/11/2026, 18h55 (Brasília)

**Fontes oficiais consultadas nesta rodada:** leitura direta por ID dos 12 documentos de referência (incluindo RN-01–41, ER-SIRE 2.1, guia, UC01–14, requisitos, CAT, registro técnico, monografia, modelo e regulamento IFSP, parecer e histórico PROMPS). Leitura não equivale a revisão integral acadêmica. PRs #2, #7 e #8 consultadas: abertas; não houve alteração de código concorrente.

**Descoberta e conferência real:** na pasta principal TCC JULIA — SIRE do Drive foram localizados os dois arquivos originais `SIRE_evidencias_HTTP_2026-10-22.zip` (ID `1wLIkHrDzFXD9ZUTIR1JcsQwaA4ESb2RI`) e `sire-prototipo-completo.zip` (ID `1hJUKt00jgT5MTUvG2V7c3CM9WYCAALiZ`). Os ZIPs foram obtidos e abertos localmente somente para leitura. O ZIP de evidências contém 20 entradas: `VF01.json`–`VF16.json`, `VF12-primeira-conferencia.json`, `execucao-2026-10-22.json`, `registro-detalhado.txt` e `SHA256.json`. A verificação de integridade ZIP retornou nenhum membro corrompido; **19/19 hashes SHA-256 do manifesto coincidiram**. Os 16 JSONs finais identificam VF01–VF16 e registram `situacao=conforme`; o registro inicial `VF12-primeira-conferencia.json` registra `não conforme`, posteriormente acompanhado por `VF12.json` com `conforme`. Preservar AMBAS as versões como histórico, sem ocultar a falha inicial. O JSON agregado `execucao-2026-10-22.json` contém 16 resultados, informa SQLite isolado e registra que o navegador remoto não conseguiu acessar o servidor local (`ERR_CONNECTION_REFUSED`), logo **não comprova verificação visual**.

**Localização verificável:** [ZIP original de evidências](https://drive.google.com/file/d/1wLIkHrDzFXD9ZUTIR1JcsQwaA4ESb2RI/view) e [ZIP do protótipo](https://drive.google.com/file/d/1hJUKt00jgT5MTUvG2V7c3CM9WYCAALiZ/view). Evidências são HISTÓRICAS, não testes executados hoje, não equivalem a aprovação da versão atual, não comprovam PostgreSQL atual, Google Drive real nem deploy. Nenhum dado real foi alterado e os conteúdos pessoais dos fixtures não foram copiados ao checklist.

**Estado F:** recuperação de artefatos históricos CONCLUÍDA; regressão atual e CAT-VF01–06 PENDENTES. **Estado B:** BLOQUEADO para Drive real por autorização OAuth própria `drive.file` e ambiente isolado, responsabilidade da autora/operador Google Cloud/Render; condição de retomada: autorização e infraestrutura de ensaio sem tocar na demo. **Estado A:** PR #2 ainda aberta; evitar sobrescrever Work. **Estado C:** finalidade/base legal do CPF aguardam aprovação antes de coleta. **Próxima unidade independente:** cruzar `VFxx.json` e `execucao-2026-10-22.json` com a matriz de rastreabilidade, documentando inclusive a falha inicial VF12; depois avaliar regressão local em branch isolada. Nenhum merge, deploy, migração ou teste novo do sistema nesta rodada.


## Rodada 17/11/2026, 19h55 (Brasília) — confronto VF histórico

**Entrega:** matriz `docs/MATRIZ_VERIFICACAO_PENDENTE_20261117.md` ampliada no commit `ffc09409e89f0c9876dac5b8b0478fb4db69af3f`, com confronto por grupos de VF01–VF16 contra `docs/resultados-http.json` da baseline e registro explícito da primeira falha VF12, da posterior conformidade e dos limites de evidência. Os 12 documentos oficiais/históricos exigidos foram abertos diretamente por IDs nesta rodada. O pacote ZIP foi verificado na rodada anterior, não reexecutado nem reaberto individualmente nesta.

**Estado/dependências:** F EM EXECUÇÃO documental, confronto agregado CONCLUÍDO; regressão atual SQLite/PostgreSQL e CAT-VF PENDENTES. A PR #2 exige conciliação com trabalho concorrente antes de edição de código; B BLOQUEADO para Drive real por OAuth próprio e ambiente isolado (responsável: autora/operador autorizado; retomar após autorização e infraestrutura de ensaio); C BLOQUEADO para coleta de CPF até finalidade/base legal aprovada; D/E/G PENDENTES. **Próxima ação:** inspecionar VF12 inicial/final e localizar a alteração causal no histórico; não inferir correção só pelo resultado final. Nenhum merge, deploy, migração ou teste novo nesta rodada.


## Rodada 17/11/2026, 20h59 (Brasília) — causa VF12 esclarecida

**Entrega verificada:** [análise causal VF12](ANALISE_CAUSAL_VF12_20261117.md), commit `44162f7ce979610ca12df6ceb77edd31b90c880f`. Leitura direta das fontes oficiais pelos 12 IDs, incluindo seção 10.3 do registro técnico original. **Achado:** a primeira não conformidade VF12 resultou da frase esperada incorreta no verificador ("Escolha uma opção válida") em comparação à mensagem real do Django ("Faça uma escolha válida. Sua escolha não é uma das disponíveis."). A reserva indevida foi rejeitada; a quantidade não mudou. O registro primário afirma que **não houve correção de código ou commit causal**. Preservar a evidência inicial e final, sem inventar defeito corrigido. Comparação direta dos dois JSON individuais permanece PENDENTE, pois não foram reabertos nesta rodada.

**F:** análise causal documental VF12 CONCLUÍDA; comparação de JSON e regressão atual PENDENTES. **A:** PR #2 e branches em trabalho concorrente; não tocar em código. **B:** BLOQUEADO para Drive real por OAuth próprio `drive.file` e ambiente de ensaio isolado (responsável: autora/operador Google Cloud/Render; retomar quando comprovados). **C:** coleta CPF BLOQUEADA até finalidade/base legal aprovadas. **D/E/G:** pendentes. **Próxima ação:** comparação individual dos JSON e depois regressão isolada; preservar demo. Nenhum teste novo, merge, migração ou deploy.


## Rodada 17/11/2026, 22h — revisão independente do patch OAuth PR #7

**Gate documental:** os 12 documentos-fonte exigidos foram acessados diretamente por ID nesta rodada, incluindo RN, ER-SIRE 2.1, guia, UC, requisitos, catálogo, registro técnico, monografia, modelo/regulamento IFSP, parecer e histórico. Esta leitura pontual não constitui auditoria acadêmica integral.

**Evidência técnica efetivamente examinada:** patches da [PR #7](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/7) para `scripts/autorizacao_drive.py` e `sire/tests/test_oauth_drive.py`, via API GitHub. Os testes adicionados usam mocks e valores sintéticos; **não foram executados nesta rodada**. A consulta de PRs abertas via busca retornou lista vazia, insuficiente para inferir que as PRs foram encerradas; conferir estados individualmente antes de integrar.

**Achados de revisão, não falhas reproduzidas:** (1) `enviar_render` faz três PUTs sequenciais de variáveis; se a segunda/terceira requisição falhar, configuração parcial é possível e o próprio tratamento final alerta disso; requer plano de recuperação/checagem sem revelar segredos. (2) A proteção da demo usa nome, branch e URL reportados pelo Render; verificar identidade do serviço/ambiente e permissões da chave antes de uso real. (3) O callback local aceita apenas `state` exato e limita parâmetros repetidos, mas testes mostrados não exercitam callback, timeout, interrupção e erros HTTP. (4) A função de envio tem teste mockado de três PUTs, não comprova compatibilidade com API real do Render nem OAuth concedido. (5) Nenhum teste aqui demonstra upload, exclusão, persistência pós-deploy ou isolamento entre agências.

**Ação e responsáveis:** B permanece **BLOQUEADO** para teste real até OAuth `drive.file` do aplicativo, serviço de ensaio isolado, autorização da autora e revisão de permissões (autora/operador Google Cloud/Render). A revisão de patch é **CONCLUÍDA** documentalmente; revisão de integração, execução de testes e verificação do contrato API são **PENDENTES** (desenvolvimento/revisor). Não mesclar PR #7 na demo sem reconciliação de bases, testes e aceite. F permanece **EM EXECUÇÃO**; comparação dos JSON individuais de VF12 ainda **PENDENTE** (ZIP histórico localizado, mas não reextraído nesta rodada). Próxima unidade independente: inspecionar os JSON individuais VF12 ou elaborar teste isolado para falha parcial de PUT e callback, após reconciliar branches e fontes pertinentes.

**Limites:** nenhum commit de código, teste novo, merge, deploy, migração, edição da monografia ou acesso a credenciais. A baseline ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem intactos.


## Rodada 17/11/2026, 22h56 (Brasília) — testes isolados de falha OAuth

**Gate documental:** RN-01–41, baseline ER-SIRE 2.1, guia, UC01–14, requisitos, especificação CAT, registro técnico, monografia, modelo IFSP, parecer e histórico PROMPS foram lidos diretamente por seus IDs originais no Google Drive. O regulamento PDF não foi reexaminado nesta rodada. A leitura não equivale à auditoria final.

**Entrega de código independente:** criada a branch [test/oauth-falha-parcial-20261117](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/tree/test/oauth-falha-parcial-20261117) a partir de `fix/oauth-seguro-20261117`, sem modificar a branch da PR #7. Commit [ae98bf1](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/commit/ae98bf17204c274566a358f2e82ac26805ec71e1) adicionou `sire/tests/test_oauth_failure_paths.py` com dois testes de unidade sintéticos: falha HTTP 503 no segundo PUT deve interromper o terceiro PUT e não imprimir segredos; serviço de nome não autorizado deve ser rejeitado antes de qualquer PUT. Os testes caracterizam riscos, **não corrigem atomicidade** nem comprovam API Render real.

**Execução:** tentativa de clonar a branch para executar `python -m unittest sire.tests.test_oauth_failure_paths -v` no ambiente isolado falhou antes da execução: `Could not resolve host: github.com`. **Resultado dos testes: NÃO EXECUTADOS; não marcar aprovação.** O arquivo foi versionado pela integração GitHub, commit confirmado. Antes de integrar, executar suíte na branch isolada e revisar asserções/compatibilidade com o script atual. Nenhum CI novo foi afirmado.

**Dependências:** B BLOQUEADO para autorização real Google OAuth `drive.file`, ambiente Render isolado e teste real de fotos; responsável autora/operador autorizado, retomar após autorização e ambiente confirmado. A PR #7 permanece sujeita a conciliação de base e revisão humana; os novos testes não foram inseridos na PR existente para evitar sobrescrever Work. F EM EXECUÇÃO, testes atuais SQLite/PostgreSQL e CAT pendentes. A PR #2 exige revisão antes de merge; C exige finalidade/base legal LGPD; D/E/G pendentes. Busca GitHub de PRs abertas retornou lista vazia, resultado inconclusivo: verificar PRs individualmente antes de operações de integração.

**Próxima ação:** executar os testes isolados via CI/ambiente com acesso à branch, registrar resultado e, se aprovados, propor incorporação à PR #7 após conciliação. Alternativa independente: confrontar JSONs individuais de VF12. **Sem merge, deploy, migração, alteração da demo, credenciais reais ou dados empresariais.**


## Rodada 17/11/2026, 23h55 (Brasília) — PR #9 e dependências OAuth

**Gate:** leitura direta dos 12 documentos oficiais/históricos pelos IDs exatos, incluindo regulamento PFC PDF. Não equivale à auditoria integral da monografia.

**Entrega documental CONCLUÍDA:** [revisão independente da PR #9 e dos testes isolados](REVISAO_DEPENDENCIAS_OAUTH_PR9_20261117.md), commit `9266aaf8a01ee27621f369672cbf8334d1c8a105`. PR #2 aberta/draft HEAD `faa5ba3`; PR #7 aberta/draft HEAD `0a7f77c`; PR #9 aberta/draft HEAD `2a354a7`, com Environment Group desvinculado. Branch `test/oauth-falha-parcial-20261117` foi lida: dois testes cobrem caminho antigo de PUT sequencial, não o novo modo de grupo. Não atribuir a PR #9 cobertura que não foi executada nesta rodada.

**B BLOQUEADO:** OAuth real drive.file e grupo Render não comprovados, responsável autora/operador autorizado; condição de retomada: consentimento e grupo verificado sem segredos, seguidos de serviço de ensaio isolado. **A EM REVISÃO:** PR #2 e cadeia #7/#9 ainda requerem reconciliação sem sobrescrever Work. **F PENDENTE:** testes da branch isolada ainda não executados/CI não confirmado; próxima ação é executar com SHA e saída preservados. **C BLOQUEADO** para coleta até finalidade/base legal; D/E/G pendentes. Nenhum merge, deploy, migração, teste novo ou alteração da demo.


## Rodada 18/11/2026 — conferência estática independente PR #2

**Entrega CONCLUÍDA:** [revisão PR #2](REVISAO_PR2_EVIDENCIAS_20261118.md), commit `eb6a411635665b35ce93afe83e82d45ad4e6f3ed`. Documentos oficiais RN, baseline, guia, UC, requisitos, CAT e registro lidos diretamente pelos IDs originais. Demais fontes acadêmicas não relidas nesta rodada; gate para alteração acadêmica integral permanece aberto.

**Evidência verificável:** PR #2 aberta/draft HEAD `faa5ba3d60b7f292be09676b13f39e9276eacafb`; migração `0007_ficha_e_fotos_drive.py` depende da 0006, acrescenta três campos textuais opcionais e a tabela `FotoExcursao` sem remover colunas. O teste de fotos usa mocks e tem cabeçalho possivelmente desatualizado sobre cache público. São observações estáticas, **não testes executados**. PR #7 aberta/draft HEAD `0a7f77c`, PR #9 aberta/draft HEAD `2a354a7`; PR #8 permanece aberta/draft.

**A EM REVISÃO:** reconciliar branches e revisar implementação/CI sem sobrescrever Work (responsável: revisor/autor da integração; retomar após diff e testes por SHA). **B BLOQUEADO:** falta confirmação de OAuth próprio `drive.file` e ambiente isolado (responsável: autora/operador Google/Render; retomar após consentimento/ambiente); não realizar upload/exclusão/persistência real nem deploy. **C BLOQUEADO:** finalidade/base legal CPF não aprovadas. **F PENDENTE:** execução SQLite/PostgreSQL, CAT-VF e testes visuais. **D/E/G PENDENTES.** Próxima ação independente: verificar status/logs dos workflows do HEAD exato da PR #2 e avaliar divergência de documentação, sem alterar demo. Nenhum teste novo, merge, migração aplicada, deploy ou monografia editada.


## Rodada de auditoria CI — 18/11/2026 (01h55, Brasília)

**Unidade concluída:** leitura dos logs reais de GitHub Actions da PR #2 no HEAD `faa5ba3d60b7f292be09676b13f39e9276eacafb`. Evidência versionada em [AUDITORIA_CI_PR2_20261118.md](AUDITORIA_CI_PR2_20261118.md), commit `56ed670178a859bcfdf99dd478f5284569e00177`. As 12 fontes oficiais/históricas foram novamente acessadas por seus IDs originais nesta rodada; nenhuma versão histórica foi alterada.

| Item | Status | Evidência | Próxima ação |
|---|---|---|---|
| A-CI-PR2: verificar logs SQLite/PostgreSQL no HEAD da PR #2 | **CONCLUÍDO** | Runs [44097899889](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097899889) e [44097900342](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097900342): fotos 17/17 PostgreSQL e 16/17 SQLite (1 skip); suíte 84/84 PostgreSQL e 81/84 SQLite (3 skips), sem falhas | Reexecutar se o HEAD mudar; revisar comentários de cache e conciliar PRs |
| B-OAUTH real | **BLOQUEADO** | CI usa Drive simulado, não comprova token real | Pré-requisito: autorização própria `drive.file`, credenciais seguras e ambiente isolado; responsável: autora/operador Google Cloud e Render; retomar após confirmação verificável |
| F-aceite integrado | **PENDENTE** | CI não cobre navegador, deploy e persistência real | Executar testes em ensaio sem afetar demo após B e conciliação |
| G-monografia | **PENDENTE** | Fontes consultadas, mas auditoria integral ainda não realizada | Inventário e confronto documental com evidências verificáveis |

**Limites:** os logs demonstram migração 0007 apenas nos bancos descartáveis de CI. Não houve nesta rodada merge, deploy, migração na demo, teste OAuth real nem execução local. PRs #2, #7, #8 e #9 consultadas abertas em draft; PR #8 apresentou atualização em 18/11/2026 04:01 UTC, portanto não editar arquivos compartilhados sem nova reconciliação.


## Rodada 18/11/2026, 04h (Brasília) — cobertura e CI da PR #9

**CONCLUÍDO (auditoria independente):** [AUDITORIA_COBERTURA_CI_PR9_20261118.md](AUDITORIA_COBERTURA_CI_PR9_20261118.md), commit `e84d17b65b999db68386c80192331d90441563d6`. Reabertos por ID os sete documentos oficiais pertinentes (RN, baseline, guia, UC, requisitos, CAT e registro), sem editar originais. Inspecionados `sire/tests/test_oauth_drive.py`, `.github/workflows/testes.yml` e `docs/OAUTH_GRUPO_RENDER.md` na branch `fix/oauth-grupo-render-20261117`, commit `2a354a75f01401f49db639fa6e52752fe7a2d60c`. Foram encontrados nove métodos de teste, incluindo três do Environment Group, com mocks. Consulta de runs por SHA retornou lista vazia (busca limitada a pull_request/primeira página): **CI não confirmado**, não equivale a falha nem a sucesso. A afirmação documental de nove testes locais aprovados não foi reproduzida nesta rodada.

**B BLOQUEADO:** OAuth real `drive.file`, grupo Render efetivamente criado e ambiente isolado ainda sem evidência; responsável autora/operador autorizado; retomar com consentimento e infraestrutura verificados sem segredos. **F PENDENTE:** executar testes da PR #9 por SHA e guardar logs; avaliar callback, falhas HTTP e regressão; testes antigos de PUT não cobrem novo grupo. **A EM REVISÃO:** conciliar PRs/branches com Work antes de editar código ou integrar. **C BLOQUEADO:** finalidade/necessidade CPF ainda não aprovadas. **D/E/G PENDENTES.** Próxima ação independente: localizar runs da PR #9 por outros meios/commit exato ou executar testes isolados; comparar JSONs históricos VF12. Nenhum merge, deploy, migração ou teste novo foi executado.
