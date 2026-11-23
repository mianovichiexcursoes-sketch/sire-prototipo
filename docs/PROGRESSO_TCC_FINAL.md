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

## Rodada 23/11/2026 — reconciliação executável EVO-USO-01

- **Status: EM EXECUÇÃO, NÃO VALIDADO.** Branch isolada `fix/evo-uso-consolidacao-20261123`, commit `fac3a2e74e10c469d5810d9e4deacb61965efa37`; base: `etapa/postgresql-windows`, blob inicial do JS `aac1a7b4e13f5a401d75eb6887cd9c191a2d0776`.
- **Fontes reabertas por ID** em 23/11/2026: RN (mod. 28/09), baseline (18/11), guia (12/11), UC (22/10), requisitos v3 (23/10), CAT rev. 0.2 (18/11), registro (18/11). Preservados ER-SIRE 2.1, UC01–UC14 e seis entidades.
- **Mudança real:** consolidado botão Fechar da PR #33, CSS móvel da #35 e navegação Tab/Shift+Tab inspirada na #20, preservando o tutorial contextual por perfil já presente na demo. A PR #64 resolve um problema do tutorial antigo, mas a base atual já separa o perfil passageiro; não aplicar patch duplicado. Nenhuma alteração de models, migrations, dados ou deploy.
- **Verificação realizada:** inspeção estática dos marcadores de Fechar, 45dvh, Tab, ramo passageiro e ausência de chamada literal `.submit(` no JS alterado. **Isto NÃO é teste de navegador, Django, CI, acessibilidade, autorização ou prova de ausência de qualquer POST.**
- **Próxima ação:** executar TUT-01–12 em Chromium (320×568, 375×812 e desktop) com perfis sintéticos; foco inicial, Tab/Shift+Tab, Escape, Fechar/Pular, retorno de foco, storage indisponível, tela sem vagas, sem submissão, navegação entre páginas; rodar Django SQLite/PostgreSQL e conferir checks no SHA da PR. Rever sobreposição do painel e regressões antes de merge. Responsável: execução técnica/revisor.
- **BLOQUEADO — OAuth real:** falta evidência de autorização `drive.file` do aplicativo Django e credenciais seguras no Render; responsável autora/operador Cloud/Render; impacto exclusivo na integração real de fotos, exclusão e persistência após deploy. Retomar quando ambiente isolado estiver configurado e auditável; não impede TUT.
- **BLOQUEADO — aceite do orientador:** exige versão testada e avaliação humana; responsável autora/orientador. Nenhum aceite inferido.
- **Rastreabilidade:** EVO-USO-01 / TUT-01–12 → `sire/static/sire/js/tutorial-uso.js` → testes de navegador pendentes → seção de evolução/avaliação da espiral pendente. RN-03–05 e UC01–14 preservados; extensão sem nova entidade ou caso de uso histórico.

## Reconciliação de estado confirmada — 23/11/2026 (rodada atual)

- **A / PR #2 — CONCLUÍDA quanto ao merge histórico, NÃO quanto ao aceite funcional:** consulta direta ao GitHub confirmou `closed/merged` em 18/11/2026, merge SHA `72a488beb518b4dcca275970afb81892b97f3d4b`, base `etapa/postgresql-windows`. Corrigir qualquer referência anterior a “PR #2 aberta”. A descrição da PR registra explicitamente ausência de teste funcional real no Render e dependência OAuth `drive.file`. Próxima ação: confrontar os testes posteriores de fotos com a versão efetivamente implantada, sem presumir deploy.
- **EVO-USO-01 / PR #77 — EM EXECUÇÃO:** HEAD consultado `f5bfd6a1a95dd3e5e55156497bf3243d40c63e54`, branch `fix/evo-uso-consolidacao-20261123`; a descrição da PR relaciona três execuções GitHub Actions como `completed/success`, mas **os jobs/logs individuais não foram inspecionados nesta rodada**. Não converter a informação da descrição em aceite TUT-01–12, prova visual, SQLite/PostgreSQL executados, revisão humana ou deploy. Próxima ação: verificar jobs e artefatos no HEAD, mapear cada cenário e executar revisão visual em 320/375 px e desktop.
- **B / OAuth — BLOQUEADO:** pré-requisito: consentimento `drive.file` próprio do aplicativo e configuração segura no Render; responsável: titular da conta Google Cloud/Render; evidência: descrição da PR #2 ainda registra a dependência, sem comprovação de configuração nesta rodada. Impacto: aceite de envio/exclusão/persistência reais de fotos. Condição de retomada: autorização e ambiente de teste verificáveis, sem expor segredos.
- **C / CPF — PENDENTE de decisão de finalidade e minimização:** PR #76 contém proposta documental, não autorização para coletar CPF. Responsável: autora; condição: definir necessidade, finalidade, base legal, retenção e acessos antes de migration ou coleta. Ensaios somente sintéticos.
- **G / auditoria final — PENDENTE:** leitura integral, inventário de pasta e confronto com monografia e modelo IFSP ainda não concluídos; não declarar TCC finalizado.

**Evidências de referência:** [PR #2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2), [PR #77](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/77), [PR #76](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/76). Fontes oficiais reabertas nesta rodada pelos sete IDs exatos: RN-01–41, documentação baseline, guia, UC01–14, requisitos, CAT e registro. Sem alteração de demo, migrações ou dados reais.


## Verificação independente de logs e artefato — 23/11/2026, 12h35 BRT

- **EVO-USO-01 — EM EXECUÇÃO, teste automatizado parcial confirmado.** No job Playwright/Chromium `137574612817` do [run #45139772375](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/45139772375), o log bruto confirma aplicação de migrações `sire.0001`–`0007` em SQLite temporário, execução de `python scripts/teste_tutorial_navegador.py` e saída `37 verificações aprovadas`. Um `curl` inicial recusado precedeu a subida do servidor e não impediu o job de concluir.
- **Evidência arquivada:** [artifact evidencia-tutorial #14800618896](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/45139772375/artifacts/14800618896), 166668 bytes, digest SHA256 `2497563be21d421c7bbb283297e2e7cb939771473c1456f75e3f311d46cb879f`, válido segundo metadata até 21/02/2027. O log confirma três arquivos enviados; **conteúdo visual não inspecionado**.
- **Limite:** `37 verificações` é contagem agregada do script, não prova individual de TUT-01–12, foco, 320/375 px ou aceite visual; não comprova PostgreSQL neste job, OAuth Drive real, merge ou deploy. SHA da execução: `f5bfd6a1a95dd3e5e55156497bf3243d40c63e54`, anterior ao HEAD da PR #77 observado nesta rodada (`8903e8b79e24712b9768b8fb5f606a1a7b952a75`); **reexecutar para HEAD atual**.
- **Próxima ação:** inspecionar `scripts/teste_tutorial_navegador.py` e os três arquivos do artifact, mapear asserts a TUT-01–12, rodar no HEAD atual, revisar capturas e responsividade manualmente. Não integrar/publicar antes disso e do aceite da autora.
