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


## Reconciliação independente — 20/11/2026, 14h55 (Brasília)

**Escopo desta unidade:** verificação de fontes e estado das integrações, sem alterar código, banco, migrations, demo ou artefatos de outro agente. Leitura direta nesta rodada dos IDs oficiais: regras RN-01–41, desenvolvimento ER-SIRE 2.1 (histórico 2.6), guia, UC01–UC14, requisitos v3.0, catálogo rev. 0.2 e registro técnico. Os documentos de monografia/IFSP e parecer permanecem **pendentes de releitura nesta unidade**, portanto não há aceite acadêmico.

| Item | Estado nesta unidade | Último commit/evidência verificada | Próxima ação e pré-requisito |
|---|---|---|---|
| A — ficha/fotos | CONCLUÍDO quanto ao **merge da PR #2**, não quanto ao aceite de fotos reais | PR #2 fechada e mesclada na branch `etapa/postgresql-windows`, HEAD histórico da PR `faa5ba3d60b7f292be09676b13f39e9276eacafb` | Revalidar upload/exclusão/persistência somente após OAuth próprio e ambiente de teste |
| B — Drive OAuth | BLOQUEADO para verificação real | Nenhuma autorização Django/Render ou prova de persistência verificada nesta unidade | Responsável: autora/operador da aplicação; pré-requisito: OAuth `drive.file` e segredos configurados com segurança; retomar após evidência sem revelar tokens |
| EVO-USO-01 — tutorial | EM EXECUÇÃO em outras branches, **não concluído por esta unidade** | PR #14 aberta, HEAD `f20106af511f5637787f2b450cd1468e53c25924`; PR #35 aberta, HEAD `bf917708f09d01befb8c7576dfc43d9d2a1e8158` | Conciliar árvore das PRs de tutorial, executar testes TUT e revisão humana antes de integrar; não editar templates concorrentes |
| C — CPF | PENDENTE | UC01, RN-04/05 consultados nesta rodada; nenhum teste/implementação novos | Implementar em branch independente com finalidade LGPD, somente CPF sintético, após comparar HEADs |
| D/E — UX e painéis | PENDENTE de reconciliação | RN-03–05, UC consultados; nenhum resultado novo alegado | Inspecionar alterações existentes antes de propor diff |
| F — regressão e aceite | PENDENTE | PR #24 e #28 estão mescladas; isto não equivale a repetir testes nesta unidade | Verificar CI, PostgreSQL/SQLite, browser e resultados efetivos por SHA, sem inferir aprovação |
| G — monografia/auditoria | PENDENTE | Fontes de requisitos consultadas, não auditoria integral | Inventariar pasta, ler monografia/modelo/parecer integralmente e registrar divergências |

**Dependências:** OAuth bloqueia somente ensaio real de Drive, não tutorial, CPF, UX ou documentação independente. Integração do tutorial depende de conciliar PRs #14/#35 e demais branches, regressões e revisão; a mera existência de PR não demonstra comportamento funcional. A demo permanece intocada. Não houve execução de testes, deploy, revisão do orientador ou alteração de documento acadêmico nesta unidade.

**Rastreabilidade do incremento de orientação:** EVO-USO-01 → `docs/PLANO_ESPIRAL_TUTORIAL_20261118.md` na PR #14 → implementação nas branches de tutorial (arquivos e testes ainda a reconciliar) → cenários TUT-01–09 a confirmar por execução → seção de nova volta da espiral na documentação, ainda não validada. A baseline UC01–UC14 e seis entidades permanece histórica.

**Próxima unidade independente concreta:** reconciliar código e testes do tutorial a partir das PRs abertas, registrar lacunas com SHA e executar cenários sintéticos em ambiente isolado. Se o código estiver ocupado por outro agente, avançar apêndice relacional/UC sem modificar os arquivos compartilhados.
