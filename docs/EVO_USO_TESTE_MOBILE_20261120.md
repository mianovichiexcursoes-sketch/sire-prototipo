# EVO-USO-01 — unidade de teste estático (20/11/2026)

**Estado: EM EXECUÇÃO; não é aceite funcional.** Base: PR #39 (HEAD 11e8146), que deriva da PR #35 e #33. Commit desta unidade: `3ef30c8cd7b8632ceb6382c8e08d7fbc4c8f3582`.

| Item | Status | Evidência | Próxima ação |
|---|---|---|---|
| TUT-mobile — contrato de CSS e controles | EM EXECUÇÃO | `tests/test_tutorial_contract.py`, commit acima; dois testes estáticos adicionados | Executar suíte no SHA integrado, validar 320px e 375×812 no Chromium real |
| TUT perfis, foco, Escape e ausência de submissão | PENDENTE DE REGRESSÃO | PRs #15/#20/#21/#33/#35/#39, não equivalem a integração aprovada | Conciliar branches, executar TUT-01–09 e Django/SQLite/PostgreSQL |
| B. OAuth drive.file próprio | BLOQUEADO | Sem confirmação de credenciais do aplicativo/Render ou autorização nesta rodada | Autora/operador Google Cloud e Render autorizar; só então ensaio real de fotos |
| Auditoria acadêmica global | PENDENTE | Fontes RN, ER-SIRE, guia, UC, requisitos, CAT consultadas diretamente por ID nesta rodada | Inventariar pasta, confrontar monografia e apêndices, validar com orientador |

**Limitação de execução:** tentativa de `git clone` no ambiente isolado falhou por DNS (`Could not resolve host: github.com`). Portanto nenhum teste desta unidade foi executado ou aprovado. Os testes adicionados verificam apenas texto-fonte, não renderização real, acessibilidade efetiva nem segurança do backend.

**Fontes oficiais consultadas:** RN (1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0); ER-SIRE (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8); UC (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY); requisitos (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM); guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U); CAT (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is). Baseline ER-SIRE 2.1, UC01–UC14 e seis entidades preservadas.

**Dependências:** nenhuma mudança em produção, migração, CPF, fotos ou templates. Não mesclar/publicar esta branch sem CI e revisão humana.