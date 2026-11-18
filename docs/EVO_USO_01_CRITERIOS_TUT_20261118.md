# EVO-USO-01 — Critérios verificáveis do tutorial interativo

Data: 18/11/2026. **Estado: especificação independente; implementação e aceite NÃO verificados.**

## Proveniência e fronteira
Feedback de Rodrigo Pantoni de 17/11, transcrito pela autora: dificuldade de operação, pedido de modelo de dados, vídeo e casos de uso. Decisão posterior da autora: substituir vídeo por tutorial interativo; não enviar comunicação ao orientador automaticamente. Não modificar a baseline ER-SIRE 2.1, as seis entidades históricas nem UC01–UC14. A orientação é evolução de interface, não caso de uso histórico renumerado.

Fontes oficiais relidas por ID em 18/11: RN-01–41 (1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0), desenvolvimento versão 2.6 com baseline 2.1 (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8), guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U), UC01–UC14 (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY), requisitos v3.0 (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM), complemento CAT rev. 0.2 (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is) e registro técnico (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM). Não houve leitura integral da monografia nem auditoria ABNT nesta unidade.

## Critérios TUT (planejados, ainda não executados)

| ID | Critério e ensaio de aceitação | Dependência | Estado |
|---|---|---|---|
| TUT-01 | Visitante vê oferta inicial uma vez por versão e pode reabrir em Como usar | catálogo existente | PENDENTE |
| TUT-02 | Passageiro recebe passos de catálogo, detalhes, acesso, embarque, confirmação e minhas reservas; etapas ausentes são puladas sem erro | rotas reais verificadas | PENDENTE |
| TUT-03 | Agente recebe passos de excursões, nova excursão, embarque, publicação, reservas e passageiros; sem mostrar passos privados a outro perfil | RN-01–05; perfis existentes | PENDENTE |
| TUT-04 | Destaque aponta elemento real visível; não encobre permanentemente ação e não dispara clique nem submit | templates e seletores atuais | PENDENTE |
| TUT-05 | Anterior, Próximo, Pular e Fechar funcionam com mouse, toque, Tab, Enter e Escape; foco perceptível | acessibilidade frontend | PENDENTE |
| TUT-06 | Celular, zoom, ausência de elementos, listas vazias e sem vagas não travam navegação | teste navegador | PENDENTE |
| TUT-07 | Falha de localStorage não impede uso; guardar apenas versão/progresso, sem CPF, nomes ou dados de reserva | privacidade RN-04/05 | PENDENTE |
| TUT-08 | Tutorial não altera reserva, publicação, assentos, pagamentos ou dados de terceiros; testes regressivos com usuários sintéticos | suíte Django | PENDENTE |
| TUT-09 | Avaliação do orientador somente após revisão e demonstração, registrada como feedback real, não aceite presumido | autora/orientador | BLOQUEADO POR AVALIAÇÃO HUMANA |

## Riscos e controles
Perfil incorreto: mapear permissões no servidor e selecionar passos conforme contexto renderizado, nunca confiar em URL apenas. Alvo ausente: avançar para próximo passo existente. Overlay que prende foco: Escape/Fechar e retorno de foco ao botão inicial. Repetição: versão local com reinício manual. Ações involuntárias: somente realce, texto e navegação interna do tutorial, sem submissão automática. Concorrência com Claude/Work: implementar em branch isolada após comparar templates e HEADs; não editar migrations/modelos para este incremento. OAuth Drive **não é dependência** dos fluxos de tutorial existentes, mas continua bloqueando testes reais de fotos.

## Rastreabilidade e evidência
EVO-USO-01 → RN-03–05 / UC01–UC14 (referência histórica, sem alteração) → frontend a identificar após inspeção → TUT-01–09 → evidências pendentes → seção futura de metodologia espiral, resultados e limitações da monografia. Esta entrega é exclusivamente especificação de testes, sem código, teste executado, deploy, aceite ou mudança de dados.

## Próxima ação
Comparar HEADs/PRs e seletores reais, implementar primeira unidade de tutorial em branch própria; executar testes Django e navegador. Reconciliar PR #14 (menção antiga a vídeo) sem apagar a solicitação histórica. Adicionar modelo relacional legível e UC01–UC14 ao documento do projeto após confrontar fonte e código. Preservar demo até revisão.
