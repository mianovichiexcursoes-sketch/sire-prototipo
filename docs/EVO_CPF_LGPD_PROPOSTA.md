# EVO-CPF-01 — proposta de extensão controlada (17/11/2026)

**Estado: especificação preliminar, não aprovada nem implementada.** Não integra a baseline ER-SIRE 2.1, os UC01–UC14 históricos nem as seis entidades originais. A coleta de CPF real está proibida nos ensaios.

## Fundamento e fronteira
Fontes oficiais consultadas diretamente em 17/11/2026: [RN-01–41](https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit), especialmente RN-04 (dados pessoais restritos) e RN-05 (papéis); [UC01](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit) (cadastro de passageiro); [guia do protótipo](https://docs.google.com/document/d/1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U/edit); [ERS 3.0](https://docs.google.com/document/d/1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM/edit). O UC01 original não exige CPF: torná-lo obrigatório seria **alteração de requisito** e depende de decisão explícita da autora e análise de necessidade.

## Decisões pendentes antes de codificar
- **Finalidade específica:** propor identificação administrativa de passageiro para evitar homônimos na gestão de reservas; verificar se o identificador interno já atende. Não invocar obrigação legal sem comprovação.
- **Necessidade e minimização:** preferência inicial por **não coletar CPF** enquanto finalidade, base legal, necessidade, transparência e retenção não forem aprovadas. Se aprovado, preferir campo opcional e coleta no momento estritamente necessário, nunca requisito automático de UC01.
- **Base legal e aviso de privacidade:** registrar hipótese fundamentada e validação responsável; informar finalidade, controlador, acesso, retenção, direitos e contato antes da coleta. Consentimento não deve ser presumido nem usado como base legal automática.
- **Acesso:** passageiro vê apenas o próprio dado; agente autorizado apenas quando necessário à excursão sob sua agência; administrador somente sob necessidade. Não incluir CPF em URLs, logs, analytics, templates públicos, exports gerais ou mensagens de erro.
- **Armazenamento:** definir criptografia em repouso para dado de alto impacto, gestão de chaves fora do repositório, backups, exclusão/retenção e tratamento de duplicidade. Máscara de exibição não é proteção de armazenamento.
- **Migração:** somente aditiva e reversível após aprovação; avaliar campo em perfil do passageiro, jamais reescrever a baseline. Nenhum migration ou modelo criado nesta unidade.

## Critérios de aceite propostos, exclusivamente sintéticos
1. Normalizar pontuação e aceitar apenas 11 dígitos; recusar sequências repetidas e dígitos verificadores incorretos; testes de DV sem registros reais.
2. Máscara de entrada e exibição parcial, sem considerar a máscara medida de segurança.
3. Verificar acesso cruzado entre dois passageiros, duas agências e visitante anônimo; sem vazamento em respostas, logs, cache e exportações.
4. Confirmar finalidade, base legal, aviso, retenção e tratamento de exclusão antes de ativar o campo em qualquer ambiente.
5. Regressão UC01–UC14 e RN-03–05; testes SQLite e PostgreSQL; sem deploy até revisão.

## Rastreabilidade de evolução
| ID | Fonte | Código/migração | Teste/evidência | Monografia |
|---|---|---|---|---|
| EVO-CPF-01 | UC01, RN-04/05, ERS 3.0 | **não implementado** | critérios acima, **não executados** | seção futura de extensões e LGPD |
| EVO-CPF-PRIV | RN-03–05 | política de acesso a definir | ensaios sintéticos, **pendentes** | riscos, minimização e limitações |

**Próxima ação:** validar finalidade e necessidade com a autora; verificar branches concorrentes antes de alterar modelos. Esta especificação não autoriza coletar CPF real.
