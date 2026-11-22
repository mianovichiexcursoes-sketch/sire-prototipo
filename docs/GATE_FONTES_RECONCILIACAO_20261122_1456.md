# Gate de fontes e reconciliação — 22/11/2026, 14h56 BRT

Unidade documental isolada. **Não é teste, aceite, merge ou deploy.** Preserva a baseline ER-SIRE 2.1, seis entidades e UC01–UC14.

## Fontes originais lidas diretamente nesta rodada

| Fonte | ID Drive | Evidência de conteúdo |
|---|---|---|
| RN-01–41 | `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` | RN-01 vínculo agente/agência; RN-03 isolamento; RN-04 privacidade; RN-05 perfis |
| Documentação baseline | `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8` | histórico ER-SIRE 2.1; versões posteriores separadas |
| Guia de implementação | `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U` | SQLite original, PostgreSQL como iteração técnica |
| Casos de uso | `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY` | Visitante, Passageiro e Agente; UC01–UC14 |
| Requisitos | `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM` | versão 3.0, visão ampliada versus protótipo |
| Catálogo/ficha | `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is` | revisão 0.2; CAT separado da baseline |
| Registro técnico | `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM` | histórico de implementação e verificação, não reexecução atual |

Data de leitura: 22/11/2026. **Data de modificação de cada fonte não aferida** nesta unidade; obter metadados antes de alegar versão final. Monografia, IFSP, parecer e PROMPS ainda exigem leitura para alterações acadêmicas.

## Estado GitHub confirmado por consulta de PR (22/11)

| Item | Status | SHA verificável | Próxima ação |
|---|---|---|---|
| A / PR #2 | **concluído somente o merge** na branch `etapa/postgresql-windows` | `72a488beb518b4dcca275970afb81892b97f3d4b` | conferir HEAD/CI e deploy; não equivale a fotos reais |
| EVO-USO / PR #15 | **em execução, aberta** | `3f4549bfba35411b6e02918a8cfd6a1f6f4111d6` | reconciliar diffs #20/#33/#35/#64 antes de tocar templates |
| EVO-USO / PRs #20, #33, #35, #64 | **em execução, abertas** | #20 `63f341a`; #33 `8bd9670`; #35 `bf91770`; #64 `1f8741a` | testes e comparação das alterações concorrentes |
| Checklist / PRs #66 e #70 | **em execução, abertas** | #66 `cc3df3e`; #70 `dd3c02b` | escolher checklist canônico e reconciliar, sem sobrescrever |
| OAuth próprio Django `drive.file` | **bloqueado para aceite** | sem prova nesta rodada de autorização/credenciais do aplicativo | titular Google/Render autorizar/configurar fora do chat; depois testar com arquivos sintéticos |
| Testes integrados SQLite/PostgreSQL/browser | **pendente** | não executados nesta rodada | rodar no HEAD reconciliado e guardar logs reais |
| Auditoria global/monografia | **pendente** | fontes acadêmicas não lidas integralmente nesta rodada | inventariar pasta, ler originais, revisar com evidências |

**Dependências:** OAuth bloqueia apenas integração real de fotos e aceite relacionado; não bloqueia tutorial, documentação, CPF sintético ou UX. PRs concorrentes bloqueiam alteração segura de templates compartilhados até reconciliação. Não há evidência de que trabalho local invisível de outro agente tenha sido incorporado.

## Rastreabilidade mínima desta unidade

RN-03/RN-04/RN-05 → isolamento por perfil e proteção de passageiro → testes de acesso cruzado entre agências **pendentes** → seção de segurança/limitações da monografia **pendente**.

UC01–UC14 + EVO-USO-01 → tutorial por perfil sem envio automático de formulário → PR #15 e correções dependentes, teste teclado/mobile **pendente** → apêndice textual UC e avaliação espiral **pendentes**.

CAT revisão 0.2 → ficha/fotos e migration 0007 → PR #2 mesclada, teste remoto de fotos **pendente** → resultados CAT-VF e limitações **pendentes**.

## Próxima rodada

1. Reconciliar PRs #15/#20/#33/#35/#64 e checklists #66/#70, sem merge automático.
2. Testar tutorial no código reconciliado com dados sintéticos e salvar logs.
3. Consultar CI e Render; não declarar deploy sem confirmação.
4. Manter checklist único após revisão; esta nota é evidência auxiliar, não substitui o checklist canônico.
