# SIRE — Progresso final rastreável

Atualizado em 2026-11-22 (reconciliação documental; histórico anterior preservado). Registro de planejamento e leitura de fontes; **não equivale a aceite funcional**. Branch de trabalho: `etapa/ficha-fotos-sire`; demo preservada em `etapa/postgresql-windows`. Não alterar baseline ER-SIRE 2.1, UC01–UC14 nem as seis entidades históricas.

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
| A. PR #2 ficha, textos, fotos, migração 0007 | CÓDIGO MESCLADO; ACEITE PENDENTE | [PR #2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2); código e roteiro em `docs/INCREMENTO_FICHA_FOTOS_DRIVE.md`; testes desta rodada **não executados** | PR #2 mesclada em 18/11; conferir CI e testes de upload/persistência, sem inferir deploy |
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

## Reconciliação de 22/11/2026 — evidência consultada diretamente

- **A:** PR #2 está `closed`, `merged=true` (consulta GitHub 22/11). Código integrado não equivale a validação de fotos no Render. Último commit específico do merge: consultar histórico antes de registrar SHA; nenhuma execução nova nesta rodada.
- **EVO-USO-01:** PRs #15, #20, #64 e #65 estão `open`, `draft=true`, `merged=false` na consulta de 22/11. #65 teve atualização em 22/11 às 01:57 UTC; possível concorrência recente. Não integrar ou alterar JS/templates compartilhados antes de reconciliar diffs. Evidência: links `/pull/15`, `/pull/20`, `/pull/64`, `/pull/65` do repositório.
- **B BLOQUEADO:** falta evidência de OAuth `drive.file` concedido ao aplicativo Django e configuração segura no Render. Responsável: autora/operador Google Cloud e Render. Impacto: não declarar upload, exclusão e persistência real de fotos aceitos. Retomar com autorização e testes rastreáveis, sem divulgar segredos.
- **F PENDENTE:** testes de SQLite/PostgreSQL, navegador, teclado, mobile e TUT ainda não executados nesta reconciliação; testes e deploy não presumidos a partir de PRs.
- **G PENDENTE:** apêndice UC01–14, modelo legível, inventário integral da pasta e auditoria ABNT continuam sem aceite verificado.
- **Próxima ação independente:** reconciliar a cadeia de PRs do tutorial e executar ensaios sintéticos em ambiente isolado; em paralelo, inventariar documentos acadêmicos sem reescrever baseline. Não criar PRs documentais repetidas para a mesma matriz.

### Gate de fontes desta reconciliação
Leitura direta em 22/11/2026: RN-01–41, baseline/documentação de desenvolvimento, guia, UC01–14, requisitos v3.0, complemento CAT rev.0.2 e registro técnico, todos pelos IDs da tabela inicial. Não foi feita revisão integral da monografia nesta rodada. Preservados ER-SIRE 2.1, seis entidades e UC01–14.

### Matriz mínima de dependências
| Item | Código/artefato | Cenário | Evidência desta rodada | Seção acadêmica |
|---|---|---|---|---|
| EVO-USO-01 / UC01–14 | PRs #15/#20/#64; JS e templates a reconciliar | TUT-01–10 por perfil, teclado e ausência de submissão | PRs abertas; testes não executados | metodologia espiral e avaliação pendentes |
| CAT / RN-03–05 | PR #2, migração 0007 e fotos | permissões entre agências, 6 fotos, persistência pós-deploy | merge verificado; OAuth e teste real não verificados | evolução separada da baseline |
| G / DOC-01 | documentação ER-SIRE e especificação UC | modelo e apêndice legíveis no PDF | fontes lidas; PDF não validado | apêndices e rastreabilidade pendentes |

## Evidência documental nova — mapeamento UC → tutorial (22/11/2026)

Fonte primária consultada diretamente pelo ID `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY` (Especificação de Casos de Uso – SIRE). Os títulos abaixo são os títulos efetivos do documento, não casos de uso novos. **Status: mapeamento documental concluído; implementação e testes TUT ainda pendentes.**

| Perfil/etapa orientada | UC histórico confirmado | Alvo/ação a conferir no tutorial | Gate de verificação |
|---|---|---|---|
| Visitante: catálogo e busca | UC03 Consultar catálogo; UC04 Pesquisar excursões | catálogo, pesquisa e filtros sem disparo automático | TUT navegador, alvo presente/ausente |
| Visitante: detalhes | UC05 Consultar detalhes da excursão | ficha da excursão sem criar reserva | TUT navegação e ausência de submissão |
| Visitante: criar acesso | UC01 Cadastrar passageiro; UC02 Autenticar usuário | instrução de cadastro apenas ao visitante; autenticação conforme perfil | regressão da PR #64, TUT-02 |
| Passageiro: reserva e embarque | UC10 Realizar reserva; UC11 Selecionar ponto de embarque | explicar escolha de embarque e confirmação, sem submissão pelo tutorial | teste com dados sintéticos, sem vagas e sem pagamento |
| Passageiro: acompanhar | UC12 Consultar minhas reservas | consulta apenas do próprio passageiro | teste de autorização |
| Agente: excursões | UC06 Cadastrar excursão; UC07 Editar excursão | criação/edição sem salvar ou publicar automaticamente | teste de perfil e ausência de POST |
| Agente: embarque e publicação | UC08 Cadastrar ponto de embarque; UC09 Publicar excursão | apontar campos e ação manual de publicação | teste de não publicação involuntária |
| Agente: consultas | UC13 Consultar reservas da excursão; UC14 Consultar passageiros da excursão | consultas restritas à agência | RN-03, teste entre agências |

**Dependências explícitas:** o tutorial não depende do OAuth Drive; validação real de fotos depende de OAuth próprio `drive.file`, armazenamento e ensaio pós-deploy. A matriz acima não comprova testes TUT, autorização entre agências nem aceite do orientador. **Próxima ação:** reconciliar os HEADs de #15/#20/#33/#35/#64, executar testes de navegador/teclado/mobile e Django em branch isolada; registrar SHA e saídas antes de integrar. Nenhum merge/deploy foi realizado nesta unidade.
