# PROGRESSO TCC FINAL — controle de integração (23/11/2026)

> Registro independente em branch documental. **Não equivale a aceite, merge ou deploy.** Antes de integrar, reconciliar com os checklists e PRs concorrentes. Fonte: leitura direta de documentos Google Drive pelos IDs oficiais em 23/11/2026; a data de modificação dos arquivos não foi verificada nesta rodada.

## Baseline preservada
ER-SIRE 2.1; seis entidades históricas; UC01–UC14. Novas funcionalidades são EVO/CAT separadas, não reescrita retroativa.

## Status e dependências
| Item | Status | Último commit/evidência | Próxima ação / dependência |
|---|---|---|---|
| A — ficha/fotos PR #2 | em execução (aceite pendente) | PR #2 consultada em 23/11: **merged=true**; não prova deploy nem testes completos | Reconciliar merge, migration 0007, permissões, limites de fotos, testes e persistência antes de aceitar |
| B — OAuth drive.file | bloqueado para integração real | Autorização própria Django e credenciais seguras no Render **não verificadas** nesta rodada | Responsável: autora/admin Google Cloud/Render; confirmar OAuth do aplicativo, variáveis seguras e ensaio controlado; não usar token do ChatGPT |
| C — CPF | pendente | Documento ER consultado; testes/implementação não auditados nesta rodada | Verificar PRs concorrentes e finalidade LGPD antes de modificar modelo |
| D — UX de reserva | pendente | Sem verificação de aceite | Conferir fluxos atuais, separar reserva de pagamento |
| E — painéis | pendente | Sem verificação de aceite | Verificar consultas e isolamento de papéis |
| F — testes | pendente | Não houve execução de suíte nesta rodada | SQLite/PostgreSQL, CAT-VF01–06, VF01–16, mobile, autorização e persistência; registrar logs reais |
| G — auditoria acadêmica | pendente | Baseline, guia, UC, ER, RN, CAT e registro consultados via Drive em 23/11 | Inventariar pasta completa, conferir monografia e IFSP antes de editar |
| EVO-USO-01 — tutorial | em execução (aceite pendente) | PR #14 aberta, plano de espiral lido; outras PRs de tutorial encontradas abertas | Reconciliar alterações concorrentes; testes de foco, teclado, 320/375, alvo ausente e perfis; solicitar avaliação humana somente após verificação |

## Gate de fontes (leitura direta em 23/11/2026)
- RN-01–41: `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` — acessível; conteúdo obtido.
- Baseline: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8` — acessível; conteúdo obtido.
- Guia: `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U` — acessível.
- UC01–UC14: `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY` — acessível.
- ER: `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM` — acessível.
- CAT: `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is` — acessível.
- Registro: `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM` — acessível.
- Monografia, modelo IFSP, regulamento, pré-banca e PROMPS: **não consultados nesta rodada**; leitura obrigatória antes de revisão acadêmica.

## Rastreabilidade mínima para completar
| ID | Código/migration | Cenário | Evidência | Monografia |
|---|---|---|---|---|
| UC01–UC14 / ER-SIRE 2.1 | conferir contra main | VF01–16 | pendente | apêndice UC e modelo relacional |
| CAT / EVO ficha | PR #2 / conferir 0007 | CAT-VF01–06 | pendente | evolução separada |
| EVO-USO-01 | conferir PRs de tutorial | TUT, acessibilidade, mobile | pendente | nova volta espiral sem renumerar histórico |
| EVO-CPF | conferir PRs CPF | DV sintético, proteção e minimização | pendente | extensão e LGPD |

## Registro da rodada
Leituras: 7 documentos oficiais, PR #2 e PR #14, plano do tutorial. PR #2 já está mesclada; evitar repetir implementação. Checklist canônico ausente em `main` (404 na leitura). Esta branch introduz controle sem tocar na demo, migrations ou templates. Nenhum teste, deploy, OAuth, revisão integral ou aceite humano foi executado/afirmado. **Próxima unidade:** reconciliar PRs de tutorial e checklists existentes, selecionar código independente sem conflito, verificar com testes reais e atualizar este controle. Antes de merge deste arquivo, comparar com outros controles em PRs abertas para evitar duplicidade.
