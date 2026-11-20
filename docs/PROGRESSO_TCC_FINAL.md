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


## Reconciliação independente — 20/11/2026 (rodada 11)

**Unidade versionada:** mapa verificável das cadeias de PRs e gates, sem alterar código nem a demo. Fontes oficiais RN, baseline, guia, UC, requisitos, CAT e registro técnico reabertas pelos IDs exatos no Google Drive nesta rodada; versões identificadas no quadro acima, sem alegar que seus textos foram alterados. O checklist desta branch é uma proposta isolada; conciliar com PR #30 antes de integração para evitar sobrescrever registros concorrentes.

| Item | Status | HEAD observado / evidência | Dependência e próxima ação |
|---|---|---|---|
| A — ficha e fotos | BLOQUEADO PARA ACEITE REAL | PR #2 merged em 18/11, merge `72a488b`; implementação não equivale a ensaio real | OAuth próprio drive.file e configuração segura; responsável autora/operador Google Cloud e Render; retomar upload, exclusão e persistência real somente após credenciais configuradas e ensaio autorizado |
| EVO-USO-01 tutorial — cadeia principal | EM EXECUÇÃO, NÃO INTEGRADA | PR #15 `3f4549b` → PR #20 `63f341a` → PR #21 `f977ab8` (bases encadeadas, abertas) | Comparar patches e testes desta árvore antes de propor integração; preservar dados sintéticos e papéis |
| EVO-USO-01 — correções paralelas | EM EXECUÇÃO, NÃO INTEGRADA | PR #33 `8bd9670` → #35 `bf91770` → #39 `11e8146` (bases encadeadas, abertas) | Reconciliar alterações em tutorial-uso.js e CSS com cadeia #15/#20/#21; evitar aplicar commits em duplicidade |
| Documentação e checklist | EM EXECUÇÃO | PR #14 `f20106a`, #30 `70818b6`, #41 `9c3b4aa`, todas abertas | Eleger versão canônica do checklist e resolver divergências antes de merge; esta atualização não substitui a PR #30 |
| TUT verificação | PENDENTE | Nenhuma execução de testes de navegador ou Django foi realizada nesta rodada | Executar testes e registrar saída/commit da árvore efetivamente integrada; validar 320px, 375×812, Escape, Fechar, Pular, perfis e ausência de submit involuntário |
| Avaliação da autora/orientador | BLOQUEADO | Nenhum aceite verificado nesta rodada | Pré-requisitos: árvore integrada testada e versão de avaliação aprovada; responsável autora/orientador; retomar após revisão humana |
| Auditoria acadêmica global | PENDENTE | Baseline ER-SIRE 2.1, seis entidades e UC01–UC14 preservados como referências históricas | Inventariar todos os arquivos e conferir monografia/ABNT com fontes originais, sem fabricar VF/CAT-VF |

**Conflito concreto:** cadeias #15/#20/#21 e #33/#35/#39 partem de bases distintas e alteram arquivos compartilhados. Não se deve afirmar que a soma das PRs está pronta, nem publicar a demo. **Último commit desta unidade:** consultar o SHA do commit que adicionou esta seção na branch `docs/rodada11-dependencias-20261120`; o próprio commit GitHub é a evidência, não um teste funcional. **Próxima ação independente:** comparar o JS final de cada cadeia e produzir reconciliação testável numa branch separada após conferência dos HEADs mais recentes.
