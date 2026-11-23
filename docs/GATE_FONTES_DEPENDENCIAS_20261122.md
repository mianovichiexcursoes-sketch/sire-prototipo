# SIRE — Gate de fontes e dependências (22/11/2026)

Registro incremental, sem alterar a baseline ER-SIRE 2.1, as seis entidades históricas ou UC01–UC14. **Não representa aceite, teste, merge ou deploy.**

## Leitura direta das fontes nesta rodada

| Documento | ID | Verificação |
|---|---|---|
| Regras RN-01–RN-41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | texto recuperado, 7.805 caracteres; RN-01 vinculação, RN-02 agência responsável, RN-03 isolamento, RN-04 proteção de passageiro |
| Baseline/documentação | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | texto recuperado, 133.468 caracteres; histórico 2.1 preservado |
| Guia de implementação | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | texto recuperado, 15.633 caracteres; SQLite original, PostgreSQL evolução |
| Casos de uso | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | texto recuperado, 18.934 caracteres; UC01–UC14 históricos |
| Requisitos | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | texto recuperado, 36.473 caracteres; versão 3.0, distinguir visão/protótipo |
| Catálogo/ficha | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | texto recuperado, 17.590 caracteres; revisão 0.2 |
| Registro técnico | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | texto recuperado, 48.074 caracteres; baseline e execução histórica |

Contagens são extensão de texto retornado pelo conector, não versão documental nem auditoria integral. Datas de última edição não verificadas. A monografia e modelo IFSP não foram relidos nesta unidade; edição acadêmica permanece vedada até leitura.

## Estado e próxima ação

| Item | Status | Último commit confirmado nesta unidade | Evidência | Dependência e próxima ação |
|---|---|---|---|---|
| A fotos PR #2 | Em execução por branches/PRs paralelas | não aferido | PR #2 e branches existentes | conferir diffs/CI atuais antes de editar; não publicar |
| B OAuth Drive | Bloqueado para ensaio real | não aferido | falta confirmação de autorização do aplicativo | responsável autora/operador; retomar após OAuth drive.file e ambiente seguro comprovados |
| C CPF | Pendente | não aferido | RN-04 e UC01 lidos | especificar finalidade, minimização e testes sintéticos em branch isolada |
| D UX reserva | Pendente | não aferido | baseline/UC lidos | reconciliar templates antes de editar |
| E painéis | Pendente | não aferido | RN-03 lida | verificar papéis e consultas existentes |
| F regressão | Pendente | não aferido | sem execução nesta rodada | SQLite/PostgreSQL, navegador e fotos reais após dependências |
| G auditoria monografia | Pendente | não aferido | fontes técnicas lidas | inventariar Drive, ler monografia/IFSP, registrar divergências |
| EVO-USO-01 tutorial | Em execução em branch independente | 91fcede/6f1045a (registro histórico, não revalidado) | feat/evo-uso-01-tutorial-20261118 e plano aprovado | reconciliar código, verificar teclado/mobile/foco e avaliação humana |

**Concorrência:** existem branches feat/evo-uso-01-tutorial-20261118, fix/tutorial-fechar-acessibilidade-20261119, fix/tutorial-mobile-viewport-20261119, test/tutorial-storage-indisponivel-20261120. Não sobrescrever arquivos compartilhados sem comparar HEAD/diff. O checklist não foi localizado na branch padrão (404); há versões em branches de trabalho, exigindo consolidação em PR revisada.

**Rastreabilidade:** EVO-USO-01 → tutorial-uso.js/base.html → testes TUT ainda não revalidados nesta rodada → seção espiral/avaliação pendente. CAT-RF-02/03 → migration 0007/views/fotos → testes CAT-VF e OAuth real pendentes → seção de evolução pendente. RN-03/04 → autorização e proteção de dados → regressões entre agências pendentes → seção de segurança pendente.
