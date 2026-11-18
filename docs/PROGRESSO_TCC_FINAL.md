# PROGRESSO TCC FINAL — EVO-USO-01 (18/11/2026)

Este checklist acompanha a branch isolada feat/evo-uso-01-tutorial-20261118. A linha documental principal e outras PRs não foram alteradas. Histórico ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem preservados.

| Item | Estado | Último commit | Evidência | Próxima ação |
|---|---|---|---|---|
| A — PR #2, ficha e fotos | Em execução em PR independente | faa5ba3 (referência histórica) | PR #2; CI 44097899889 | Revisão e testes reais de fotos após OAuth |
| B — OAuth drive.file | Bloqueado: autorização própria do app/ambiente de ensaio não confirmados | 2a354a7 (PR #9) | PR #9 e CI 44145474063 (somente fotos simuladas) | Autora configura ambiente isolado, sem divulgar segredos |
| C — CPF/LGPD | Pendente, branch independente | — | — | Revisar estado da PR dedicada e testes sintéticos |
| D — UX de reserva | Pendente | — | — | Implementar após reconciliação das branches |
| E — Painéis | Pendente | — | — | Verificar consultas e permissões existentes |
| F — CAT/VF regressão | Pendente parcialmente | faa5ba3 | CI 44097899889 | Validar cenários afetados, PostgreSQL e navegador |
| G — documentação e auditoria global | Pendente | — | Documentos oficiais abaixo | Inventariar pasta e auditar monografia integral |
| EVO-USO-01 — tutorial | Em execução, NÃO validado | 9f2f923 (auditoria); 91fcede / 6f1045a (implementação) | docs/EVO_USO_01_AUDITORIA_QA_20261118.md; JS e base.html | Conciliar PR #15; corrigir A01–A05 em branch técnica; testar TUT-01–06 em navegador |
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

## Rodada 18/11/2026 — auditoria EVO-USO-01
- **Concluído:** revisão estática dos arquivos da PR #15 e matriz de verificação TUT-01–06, registrada em `docs/EVO_USO_01_AUDITORIA_QA_20261118.md` (commit `9f2f923`). Nenhum teste de navegador executado nesta rodada.
- **Achados a reproduzir:** roteiros idênticos para visitante/passageiro, seleção ambígua de alvos, foco/teclado, destaque que altera posicionamento, ausência de retomada entre páginas. São riscos de inspeção, não falhas confirmadas em produção.
- **Bloqueios:** OAuth real — credenciais/autorização do aplicativo e ambiente isolado não confirmados; responsável autora; retomar somente com autorização segura. Testes de navegador — ambiente e execução ainda não comprovados; responsável equipe técnica; retomar após conciliação do HEAD e preparação de perfis sintéticos. Avaliação orientador — requer versão testada e encaminhamento pela autora.
- **Próxima unidade independente:** correções isoladas TUT-A01–A05 após conferir HEAD/PR #15; alternativamente modelo relacional e apêndice UC01–14 se conflito técnico impedir edição.
