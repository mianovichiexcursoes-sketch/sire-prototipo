# PROGRESSO TCC FINAL — EVO-USO-01 (18/11/2026)

Este checklist acompanha a branch isolada feat/evo-uso-01-tutorial-20261118. A linha documental principal e outras PRs não foram alteradas. Histórico ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem preservados.

| Item | Estado | Último commit | Evidência | Próxima ação |
|---|---|---|---|---|
| A — PR #2, ficha e fotos | PR fechada; integração não verificada | faa5ba3 (referência histórica) | PR #2; CI 44097899889 | Revisão e testes reais de fotos após OAuth |
| B — OAuth drive.file | Bloqueado: autorização própria do app/ambiente de ensaio não confirmados | 2a354a7 (PR #9) | PR #9 e CI 44145474063 (somente fotos simuladas) | Autora configura ambiente isolado, sem divulgar segredos |
| C — CPF/LGPD | Pendente, branch independente | — | — | Revisar estado da PR dedicada e testes sintéticos |
| D — UX de reserva | Pendente | — | — | Implementar após reconciliação das branches |
| E — Painéis | Pendente | — | — | Verificar consultas e permissões existentes |
| F — CAT/VF regressão | Pendente parcialmente | faa5ba3 | CI 44097899889 | Validar cenários afetados, PostgreSQL e navegador |
| G — documentação e auditoria global | Pendente | — | Documentos oficiais abaixo | Inventariar pasta e auditar monografia integral |
| EVO-USO-01 — tutorial | Suíte Chromium proposta; execução não confirmada | a9de631 / 22afb069 | tests/test_tutorial_browser.py; .github/workflows/evo-uso-01-browser.yml | Verificar CI do SHA e corrigir falhas; validar Django e navegador móvel antes de merge |
| EVO-USO-01 — modelo e UC no projeto | Pendente | — | PR #14, plano espiral | Consolidar apêndice e PDF após conferir diagramas |

## Gate de fontes
Lidas em 18/11/2026 por ID: RN-01–41 (1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0); baseline (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8); guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U); UC (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY); requisitos (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM); CAT (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is); registro (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM). Datas de modificação não aferidas nesta rodada. Plano e retorno do orientador lidos na branch docs/retorno-orientador-tutorial-20261118.

## Dependências e riscos
- OAuth: bloqueio de integração REAL de fotos; não bloqueia tutorial. Responsável pela autorização: autora. Retomar após confirmação de credenciais seguras e ambiente separado.
- Concorrência: outros agentes podem ter alterações locais invisíveis. Branch isolada parte de etapa/postgresql-windows; integração deve conciliar base.html antes de merge.
- Tutorial: não envia formulários, não muda papel nem armazena dados pessoais; usa localStorage com somente versão/perfil/estado. Precisa testar foco, teclado, Escape, ausência de alvos, celular, convite e regressão. A implementação não equivale a aceite.
- Avaliação: orientador ainda não reavaliou; não declarar aprovação nem métricas.
- Modelo: apêndice UC01–UC14 e modelo relacional legível pendentes; não renumerar baseline.

## Rastreabilidade
EVO-USO-01 / TUT-01 a TUT-05 -> base.html + tutorial-uso.js -> ensaios de navegador pendentes -> seção metodologia/avaliação da monografia pendente. TUT-06 depende de regressão de reservas e autorização entre agências. DOC-01 depende de conferência do diagrama e apêndice. AVAL-01 depende de retorno humano.

## Rodada 18/11/2026 — correções isoladas
- PR #15 inspecionada no SHA 3f4549b; PR #19 documental no SHA 19b2f08; PR #2 consultada e encontrada fechada, sem inferir merge.
- Fonte RN lida via Drive fetch (a leitura Docs retornou 429); baseline lida via fetch; guia, UC, requisitos, CAT e registro via get_document_text. Versões originais não modificadas.
- TUT-A01/A02/A03/A04/A05: correções propostas em branch independente, sem testes de navegador; responsável pela conciliação: revisão técnica. Retomar merge somente após regressão, revisão do template e aceite.
- OAuth real: bloqueado por autorização Django drive.file e ambiente isolado não confirmados; responsável: autora/operador da conta. Evidência: nenhuma autorização real demonstrada. Não impede TUT.

## Rodada 18/11/2026 — suíte Chromium TUT-01–06 isolada
- **Em execução, NÃO aprovada:** branch `test/evo-uso-01-browser-20261118`, commits `22afb069` (testes Playwright) e `a9de631` (workflow de CI). Testes verificam convite, acesso permanente, roteiro passageiro/agente, Escape e foco, storage indisponível e ausência de submissão de formulário; usam HTML e formulário sintéticos, não dados reais.
- **Pré-requisito da verificação:** runner GitHub Actions com Playwright 1.56.0 e Chromium; o código do tutorial é lido do mesmo SHA pelo teste. A execução local completa não ocorreu: repositório inacessível via DNS no ambiente local. Workflow recém-criado ainda requer comprovação de job/log, portanto TUT-01–06 seguem **pendentes de resultado**.
- **Limitação:** harness isolado não demonstra integração Django, permissões reais, responsividade no Render, acessibilidade por leitor de tela nem aceite do orientador. Não mesclar PR #15/#20 sem CI, regressão e conciliação do template.
- **Próxima ação concreta:** verificar job do workflow no SHA `a9de631`; corrigir falhas reais, ampliar viewport móvel/Tab, conciliar PR #20; depois testar em aplicação Django isolada. OAuth real permanece bloqueado por autorização do aplicativo/ambiente Render de ensaio (responsável: autora), mas não impede testes de tutorial.
