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
