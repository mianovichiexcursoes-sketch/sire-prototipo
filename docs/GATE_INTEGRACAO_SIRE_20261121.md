# Gate de integração SIRE — 21/11/2026 (evidência documental)

## Estado observado diretamente
- PR #2: **merged**, fechada em 18/11, head histórico `faa5ba3d60b7f292be09676b13f39e9276eacafb`. Isto **não comprova** OAuth do aplicativo nem persistência de fotos em Render.
- PR #15: **open**, head `3f4549bfba35411b6e02918a8cfd6a1f6f4111d6`, atualização registrada 20/11. Tutorial implementado em branch própria, sem aceite humano confirmado.
- PR #20: **open**, head `63f341ab9769436c252c5cf71151a976ea9498ec`. Não mesclar alterações concorrentes em `base.html` sem comparar diffs.
- PR #14: plano documental de retorno do orientador; decisão vigente: **tutorial interativo, não vídeo**.
- Checklist em `feat/evo-uso-01-tutorial-20261118` ainda descreve A como 'em execução' apesar de #2 merged: corrigir status distinguindo **merge concluído** de **aceite funcional pendente**.

## Fontes consultadas nesta rodada
Leitura direta em 21/11/2026 via Google Docs, revisões identificadas pelo conector: RN `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`; baseline `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`; guia `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`; UC `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`; requisitos `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`; CAT `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`; registro `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`; monografia `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg`. A leitura não equivale a auditoria integral.

## Matriz de bloqueios e próximos passos
| Item | Status | Dependência e responsável | Evidência | Retomada |
|---|---|---|---|---|
| A — ficha/fotos | Merge realizado; aceite **pendente** | Persistência/isolamento/autorização e regressões reais; equipe técnica | PR #2 | Ensaiar em ambiente separado e anexar resultados reais |
| B — OAuth drive.file | **Bloqueado para integração real** | Consentimento OAuth do aplicativo e segredos protegidos no Render; autora/admin | Nenhuma confirmação de credenciais nesta rodada | Configuração segura confirmada, sem segredos no GitHub |
| EVO-USO-01 tutorial | **Em execução, avaliação pendente** | Reconciliar #15/#20; ensaio em navegador e retorno do orientador | PR #15 e #20 | Testes com perfis sintéticos e avaliação humana |
| C/D/E | **Pendentes de reconciliação** | Verificar PRs já existentes antes de nova implementação; agente técnico | Busca de PRs revelou múltiplas entregas independentes | Inventariar branches e identificar lacuna não trabalhada |
| F — regressões | **Pendente** | SQLite/PostgreSQL, autorização, fotos, celular, persistência pós-deploy | Sem nova execução conclusiva nesta rodada | Executar suíte e registrar logs verificáveis |
| G — auditoria global | **Pendente** | Inventário completo Drive, modelo IFSP, regulamento e revisão integral | Monografia original acessível; não auditada integralmente | Inventariar pasta e registrar divergências por documento |

## Preservação
Não foi alterado modelo, migration, template, demo, dado real ou monografia. Baseline ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem históricos. Este arquivo é evidência **documental**, não resultado de teste nem autorização de deploy.
