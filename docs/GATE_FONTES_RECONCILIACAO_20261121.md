# Verificação de fontes e decisão de integração — 21/11/2026

## Evidência direta nesta rodada
Google Drive, consulta por ID exato em 21/11/2026: RN 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 (71 parágrafos); baseline 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 (1248); guia 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U (395); UC 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY (279); requisitos 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM (498); CAT 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is (60); registro 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM (262). Metadados de revisão retornados pelo Google Docs, mas não equivalem a data de modificação. Trechos de identificação e escopo consultados; leitura integral das regras específicas e inspeção da implementação ainda pendentes.

## Achado verificável
O checklist docs/PROGRESSO_TCC_FINAL.md não existe na branch padrão consultada (404), mas existe nas branches feat/evo-uso-01-tutorial-20261118 e audit/tcc-tutorial-gate-20261120-1104. Portanto, **não criar outro checklist concorrente na branch padrão nem declarar que o checklist está consolidado**. A branch feat/evo-uso-01-tutorial-20261118 já registra implementação do tutorial em tutorial-uso.js e base.html, ainda sem aceite. Existem branches de correção de viewport, acessibilidade e storage, que precisam ser reconciliadas antes de qualquer novo código compartilhado.

## Bloqueios e próxima unidade
- EVO-USO-01: **em execução**, não concluído. Dependência: reconciliar branches e confirmar testes funcionais em navegador e avaliação do orientador. Responsável técnico: implementação; avaliação: autora/orientador. Sem merge/deploy nesta rodada.
- OAuth: **bloqueado para ensaio real** até autorização do aplicativo Django e configuração segura de credenciais; responsável: autora/operador Google Cloud e Render. Não bloqueia documentação independente.
- Checklist principal: **pendente de consolidação**, devido a múltiplas versões em branches isoladas; preservar versões históricas e escolher uma única PR de integração.
- Próxima unidade independente: auditar diferenças dos checklists e branches do tutorial, consolidar rastreabilidade e planejar ensaio de teclado/mobile sem alterar templates compartilhados.
- Nenhum teste, CI, deploy ou avaliação humana executado nesta rodada. Não inferir aceite de commits ou documentos.
