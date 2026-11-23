# PROGRESSO TCC FINAL — auditoria de fontes e dependências

Atualizado em 23/11/2026. **Registro de auditoria documental; não constitui teste, implementação, merge ou deploy.** Branch isolada para não sobrescrever alterações de outros agentes. Baseline ER-SIRE 2.1 preservada (seis entidades e UC01–UC14). Extensões têm IDs separados.

## Fontes originais lidas nesta rodada (Google Drive, IDs exatos)

| Fonte | ID | Verificação | Versão/data visível |
|---|---|---|---|
| Regras RN01–41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | leitura de texto confirmada | sem revisão indicada no cabeçalho |
| Desenvolvimento/baseline | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | leitura confirmada | histórico 2.1 (05/10/2026), revisões posteriores |
| Guia de implementação | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | leitura confirmada | menciona terceira iteração técnica |
| UC01–UC14 | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | leitura confirmada | baseline ER-SIRE 2.1 |
| Requisitos | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | leitura confirmada | versão 3.0/PFC2 |
| Catálogo/ficha | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | leitura confirmada | revisão 0.2 |
| Registro técnico | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | leitura confirmada | registro iniciado 20/10/2026 |

**Limite:** leitura nesta rodada confirmou conteúdo introdutório e escopo dos sete documentos, não revisão integral de todas as seções. Monografia, modelo IFSP, regulamento, parecer e PROMPS TCC ainda requerem leitura específica antes de qualquer alteração acadêmica. Não alegar gate integral concluído.

## Checklist rastreável

| ID | Status | Último commit / evidência | Dependência / próxima ação |
|---|---|---|---|
| A ficha/fotos PR #2 | Pendente | PR #2 (link no pedido) | Inspecionar diff, CI, migration 0007 e permissões; sem merge |
| B OAuth drive.file | Bloqueado para integração real | Nenhum token/autorização do aplicativo verificado nesta rodada | Responsável: autora/admin Google Cloud; configurar consentimento, credenciais seguras no Render e autorizar aplicativo; retomar teste real somente após confirmação |
| C CPF sintético/LGPD | Pendente | Nenhuma validação nova nesta rodada | Revisar modelo/ramificações atuais antes de editar |
| D UX reserva | Pendente | Sem evidência nova | Revisar fluxos existentes, sem pagamentos |
| E painéis | Pendente | Sem evidência nova | Verificar papéis/consultas |
| F VF/CAT-VF/PostgreSQL | Pendente | Nenhum teste executado nesta rodada | Executar suíte e registrar logs verificáveis |
| G monografia/ABNT | Bloqueado para edição | Fontes acadêmicas restantes não lidas | Ler documentos exatos, depois auditar integralmente |
| EVO-USO-01 tutorial | Em execução (especificação; código pendente) | docs/PLANO_ESPIRAL_TUTORIAL_20261118.md e docs/RETORNO_ORIENTADOR_TUTORIAL_20261118.md nesta branch-base | Inspecionar HEAD/templates e concorrência; implementar em branch própria, testes TUT01–06, revisão humana antes do deploy |
| DOC-01 modelo/UC | Pendente | UC01–14 fonte original lida | Conferir figura relacional e consolidar apêndice sem reescrever baseline |

## Matriz de dependências inicial

| Requisito | Artefato alvo | Verificação necessária | Evidência atual | Monografia |
|---|---|---|---|---|
| RN01–05 / UC agente | Views e autorização por agência | isolamento cruzado | não executada nesta rodada | arquitetura/segurança |
| RN06–30 / UC reservas | models, views, testes de concorrência | VF01–16 + PostgreSQL | não executada nesta rodada | implementação/resultados |
| CAT / EVO fotos | migration 0007, upload e storage | CAT-VF01–06, persistência pós-deploy | não executada nesta rodada | incrementos/limitações |
| EVO-USO-01 | templates e JS tutorial | TUT01–06, acessibilidade, sem POST automático | especificação histórica; execução pendente | espiral/avaliação |
| DOC-01 | modelo relacional e UC01–14 | legibilidade PDF, correspondência com baseline | fonte UC lida, PDF não validado | apêndices |

## Próxima unidade independente

1. Verificar branches/PRs/CI e o template atual para evitar colisão com Claude/Work.
2. Implementar tutorial EVO-USO-01 em branch própria, sem depender de OAuth, com teste sintético e evidências reais.
3. Atualizar este checklist na branch integrada apropriada, somente após reconciliação; este arquivo ainda não está na branch principal.

**Segurança:** não armazenar credenciais, CPFs reais, dados empresariais nem afirmar deploy ou aceite não verificados.
