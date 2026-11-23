# EVO-CPF-01 — Análise prévia de necessidade e proteção (proposta, sem implementação)

Data: 23/11/2026. Estado: **pendente de decisão da autora**. Esta análise é uma extensão proposta, não altera a baseline ER-SIRE 2.1, suas seis entidades ou UC01–UC14. Nenhum CPF real foi coletado e nenhuma migração foi criada.

## Fontes consultadas diretamente
- Regras oficiais RN-01–RN-41, ID `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`: RN-03 (isolamento), RN-04 (proteção dos dados de passageiros), RN-05 (perfis).
- Desenvolvimento SIRE, ID `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`: baseline ER-SIRE 2.1.
- Guia, ID `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`.
- Casos de uso UC01–UC14, ID `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`.
- Requisitos v3.0, ID `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`.
- Complemento CAT revisão 0.2, ID `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`.
- Registro técnico, ID `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`.

## Decisão necessária antes de modelar
A necessidade de CPF **não está comprovada** pelo mero desejo de aproximar a interface de plataformas de viagem. A autora deve declarar uma finalidade operacional específica, demonstrar por que nome e dados já existentes não bastam, identificar base legal aplicável, momento mínimo de coleta, responsável e prazo de retenção. Sem essa decisão, a opção de menor risco é **não coletar CPF** no protótipo. Não pressupor consentimento como base legal universal.

## Controles de desenho propostos (não implementados)
1. Não incluir CPF em catálogo público, URL, logs, analytics, screenshots, fixtures versionadas, mensagens de erro ou campos HTML preenchidos por padrão.
2. Permitir acesso apenas ao próprio passageiro, agente autorizado da agência responsável quando estritamente necessário e administrador autorizado, conforme RN-03–05. Testar acesso cruzado entre agências.
3. Validar 11 dígitos e dígitos verificadores no servidor, rejeitar sequências repetidas; máscara no cliente é apenas auxílio visual. Testar com valores sintéticos exclusivamente.
4. Definir se unicidade é realmente necessária antes de criar índice; proteger consulta, exportação, retenção e exclusão. Evitar expor CPF completo na interface; considerar criptografia de campo se armazenamento for aprovado, com gestão de chaves fora do Git.
5. Implementar migration **aditiva e reversível** somente após avaliação de dados existentes, sem preencher CPFs retroativamente. Nunca usar dados reais nos ensaios.

## Rastreabilidade e gates
| ID | Fonte | Artefato previsto | Cenário previsto | Evidência atual | Monografia |
|---|---|---|---|---|---|
| EVO-CPF-01 | RN-04/05; requisitos 3.0 | este documento | finalidade e minimização aprovadas | proposta documental, sem aceite | evolução de requisitos/LGPD |
| EVO-CPF-02 | RN-03/04/05 | formulário/modelo/migration futuros | validação sintética, papéis e agência cruzada | **não executado** | arquitetura e testes |
| EVO-CPF-03 | UC01/UC10 (sem renumerar) | UX e política de retenção futuras | fluxo sem CPF quando não necessário | **não executado** | limitações e evolução |

## Dependências e continuidade
**Bloqueio específico C2:** decisão documentada sobre finalidade, base legal, necessidade e retenção, pela autora; sem ela, não criar campo/migration nem coletar CPF. **Trabalho independente liberado:** EVO-USO-01 tutorial, UX sem CPF, painéis, testes de regressão sem dados pessoais e auditoria acadêmica. OAuth `drive.file` é dependência exclusiva da integração real de fotos, não deste documento nem do tutorial.

## Conciliação concorrente
PR #2 está mesclada, mas não comprova OAuth ou persistência real de fotos. PRs #39, #64 e #75 permaneciam abertas na consulta de 23/11; não modificar seus JS/templates ou o checklist concorrente sem reconciliação. A PR deste documento não solicita merge automático, deploy nem aprovação de resultados de testes.
