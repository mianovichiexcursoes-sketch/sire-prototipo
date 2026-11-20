# SIRE — índice fiel dos casos de uso históricos UC01–UC14

Data da conferência: 20/11/2026. **Documento auxiliar para apêndice acadêmico; não substitui a especificação textual original.**

Fonte primária consultada diretamente por ID: [Especificação de Casos de Uso – SIRE](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit). Conferidas também as fontes originais RN-01–RN-41, ER-SIRE 2.1, Guia de Implementação, Requisitos v3, especificação CAT e registro de implementação. A data de modificação e revisão formal de cada fonte **não foram verificadas** nesta unidade.

| ID histórico | Título literal na fonte | Ator/fluxo a conferir na transcrição integral | Situação |
|---|---|---|---|
| UC01 | Cadastrar passageiro | Visitante | Índice conferido; texto integral não transcrito |
| UC02 | Autenticar usuário | Usuário autenticável | Índice conferido; texto integral não transcrito |
| UC03 | Consultar catálogo de excursões | Visitante | Índice conferido; texto integral não transcrito |
| UC04 | Pesquisar excursões | Visitante | Índice conferido; texto integral não transcrito |
| UC05 | Consultar detalhes da excursão | Visitante | Índice conferido; texto integral não transcrito |
| UC06 | Cadastrar excursão | Agente | Índice conferido; texto integral não transcrito |
| UC07 | Editar excursão | Agente | Índice conferido; texto integral não transcrito |
| UC08 | Cadastrar ponto de embarque | Agente | Índice conferido; texto integral não transcrito |
| UC09 | Publicar excursão | Agente | Índice conferido; texto integral não transcrito |
| UC10 | Realizar reserva | Passageiro | Índice conferido; texto integral não transcrito |
| UC11 | Selecionar ponto de embarque | Passageiro, dentro de UC10 | Índice conferido; texto integral não transcrito |
| UC12 | Consultar minhas reservas | Passageiro | Índice conferido; texto integral não transcrito |
| UC13 | Consultar reservas da excursão | Agente | Índice conferido; texto integral não transcrito |
| UC14 | Consultar passageiros da excursão | Agente | Índice conferido; texto integral não transcrito |

## Dependências e rastreabilidade ainda pendentes

1. Comparar **integralmente** descrição, pré/pós-condições, fluxo principal, alternativos e exceções de cada UC contra a fonte, antes de inserir apêndice no documento de projeto; esta tabela é apenas um índice e os atores são indicação preliminar.
2. Associar UC01–UC14 a RF/RN da baseline, views/URLs/templates/models/migrations **na árvore integrada efetiva**, testes VF01–VF16, evidência e seção da monografia. Não presumir correspondência nem testes aprovados.
3. Modelo relacional legível e seis entidades históricas: transcrever somente após cotejo do modelo ER-SIRE 2.1 com o código e registrar extensões separadamente.
4. EVO-USO-01 é incremento de orientação, **não renumera** UC01–UC14; tutorial deve indicar apenas telas disponíveis para cada perfil, sem enviar formulários.
5. PRs concorrentes #15/#20/#21 e #33/#35/#39 ainda precisam de reconciliação de JS/templates; PR #14 documental. OAuth próprio drive.file é dependência de integração real de fotos, não do índice ou tutorial.

## Evidência e limite da unidade

Leitura direta do documento original em 20/11/2026 e extração dos 14 títulos, sem execução de Django, Chromium, PostgreSQL, merge, deploy ou avaliação humana. Nenhuma alteração de baseline, código, banco ou demo. **Próxima ação:** cotejar fluxos completos UC com a versão real do código e integrar no apêndice acadêmico após revisão.
