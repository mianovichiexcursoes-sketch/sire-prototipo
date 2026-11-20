# SIRE — inventário de leitura direta das fontes (20/11/2026)

**Escopo desta unidade:** inventário de acesso por ID exato e bloqueios de rastreabilidade, sem modificar baseline, código, checklist concorrente, monografia ou demo. A leitura direta foi feita via integração Google Drive; tamanho abaixo é de caracteres extraídos, não tamanho oficial de arquivo. Data de modificação da fonte não foi verificada nesta unidade. **Não constitui auditoria integral nem aceite.**

| Fonte | ID exato | Texto acessível | Extensão extraída | Observação verificável |
|---|---|---|---:|---|
| Regras RN-01–RN-41 | `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` | sim | 7.805 | RN-03 restringe administração à agência vinculada; RN-04 protege dados pessoais |
| Baseline desenvolvimento | `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8` | sim | 133.468 | histórico 2.1 em 05/10/2026; versões posteriores preservadas |
| Guia de implementação | `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U` | sim | 15.633 | SQLite original e PostgreSQL como terceira iteração técnica |
| UC01–UC14 | `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY` | sim | 18.934 | atores Visitante, Passageiro, Agente |
| Requisitos | `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM` | sim | 36.473 | versão 3.0 — PFC2; delimitar protótipo/visão |
| Extensão catálogo/ficha | `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is` | sim | 17.590 | revisão 0.2, extensão CAT sem renumerar baseline |
| Registro técnico | `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM` | sim | 48.074 | registra ambiente original Python 3.12.14 / Django 6.1.2 / SQLite 3.53.1 |
| Monografia | `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg` | sim | 101.657 | título e orientador presentes; revisão integral pendente |
| Modelo IFSP dez/2025 | `1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo` | sim | 84.437 | modelo acessível; revisão ABNT pendente |
| Parecer pré-banca | `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA` | sim | 16.962 | alerta sobre inconsistências, UML e autoria assistida |
| PROMPS TCC (histórico) | `1mpNI5u26q3NzVgXFeeMCHZgfWdxCgsG-WTangQWVRrE` | sim | 30.920 | histórico não normativo; verificar atualidade |

## Conciliação e próximos gates

- **Em execução por outras PRs:** #15 (tutorial), #21/#42 (testes), #30/#43 (checklist), #44 (título). Não editar arquivos dessas PRs em paralelo sem reconciliação. PR #2 foi reportada como mesclada em #30, mas esta unidade não revalidou o merge pelo endpoint próprio.
- **Bloqueado — OAuth Drive próprio:** não há nesta unidade evidência de consentimento do aplicativo Django, escopo `drive.file`, credenciais seguras no Render ou persistência pós-deploy. Responsável: autora/administrador do projeto Google; condição de retomada: autorização verificável e testes com fotos sintéticas. Não impede tutorial local.
- **Pendente — tutorial EVO-USO-01:** reconciliar branches e templates, executar testes Django/Chromium e inspeção responsiva, obter avaliação real do orientador; não publicar automaticamente.
- **Pendente — auditoria global:** inventariar pasta completa do Drive, confrontar versões e documentos, revisar integralmente monografia e registrar divergências sem reescrever históricos.
- **Próxima unidade independente:** consultar regulamento IFSP pelo ID `1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL`, inventariar árvore da pasta central e comparar lista com este inventário; preservar checklist canônico na PR #30/#43.

## Rastreabilidade mínima desta unidade

`RN-03/RN-04, UC01–UC14, ER-SIRE 2.1, CAT` → documentos oficiais acima → **somente inventário documental**, sem alteração em models/migrations/templates → **nenhum teste executado nesta unidade** → seções da monografia ainda **não auditadas**. Nenhum resultado de CI, deploy, PostgreSQL, OAuth, teste manual ou aceite é inferido da mera acessibilidade das fontes.
