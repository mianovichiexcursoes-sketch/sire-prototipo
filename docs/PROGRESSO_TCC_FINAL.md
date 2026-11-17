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
