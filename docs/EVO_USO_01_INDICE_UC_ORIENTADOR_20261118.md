# EVO-USO-01 — Índice verificável dos casos de uso para o documento do projeto

Data de conferência: 18/11/2026. **Estado: índice preparado; apêndice integral e validação acadêmica pendentes.**

## Proveniência e precedência
Fonte primária lida diretamente pelo ID: [Especificação de Casos de Uso – SIRE](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit), modificada em 22/10/2026 (metadado do Drive). Baseline: [Documentação de Desenvolvimento – ER-SIRE 2.1](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit). A solicitação de 17/11 do orientador pede casos de uso no documento do projeto. A autora aprovou tutorial interativo em vez de vídeo. Não substituir, renumerar ou reescrever a baseline.

## Sumário para apêndice acadêmico
| ID original | Título exato da fonte | Público principal / função | Evidência necessária para apêndice |
|---|---|---|---|
| UC01 | Cadastrar passageiro | Visitante | Copiar fluxo principal, alternativas e exceções da fonte |
| UC02 | Autenticar usuário | Passageiro/Agente | Conferir restrições por perfil |
| UC03 | Consultar catálogo de excursões | Visitante/Passageiro | Conferir somente excursões publicadas |
| UC04 | Pesquisar excursões | Visitante/Passageiro | Registrar estado de resultado vazio |
| UC05 | Consultar detalhes da excursão | Visitante/Passageiro | Conferir disponibilidade e embarques |
| UC06 | Cadastrar excursão | Agente | Estado inicial RASCUNHO e vínculo à agência |
| UC07 | Editar excursão | Agente | Propriedade da agência e limite de capacidade |
| UC08 | Cadastrar ponto de embarque | Agente | Associação à excursão correta |
| UC09 | Publicar excursão | Agente | Pré-requisitos e pelo menos um embarque |
| UC10 | Realizar reserva | Passageiro | Disponibilidade e confirmação explícita |
| UC11 | Selecionar ponto de embarque | Passageiro | Ponto pertencente à excursão |
| UC12 | Consultar minhas reservas | Passageiro | Restringir às próprias reservas |
| UC13 | Consultar reservas da excursão | Agente | Restringir à agência |
| UC14 | Consultar passageiros da excursão | Agente | Restringir à agência |

Os títulos foram conferidos no documento original; o conteúdo detalhado deve ser transcrito/organizado com fidelidade e revisão humana, sem transformar este índice em suposta execução de testes.

## Rastreabilidade inicial EVO-USO-01
- **Visitante:** UC01, UC03–UC05 → roteiro de catálogo, detalhes e acesso → TUT-01/TUT-02 (testes propostos na PR #21; resultado não confirmado).
- **Passageiro:** UC02, UC03–UC05, UC10–UC12 → roteiro de detalhes, embarque, confirmação e minhas reservas → TUT-02/TUT-04/TUT-06; confirmação de reserva NÃO é pagamento.
- **Agente:** UC02, UC06–UC09, UC13–UC14 → roteiro de excursões, nova excursão, embarque, publicação, reservas e passageiros → TUT-03/TUT-04/TUT-06.
- **Modelo relacional:** seis entidades históricas e seus campos/chaves devem ser conferidos no diagrama original e no código efetivo ANTES de inserir tabela relacional na monografia. Não inferir nomes de campos a partir deste índice.
- **Testes:** a PR #21 contém harness sintético Playwright, mas isso não demonstra verificação em Django, em celular ou pelo orientador. Registrar SHA e logs quando disponíveis.

## Plano de integração sem interferência
1. Comparar a versão vigente do documento principal e os anexos antes de editar; preservar histórico.
2. Acrescentar apêndice com UC01–UC14, mantendo identificadores, atores, pré/pós-condições, fluxo principal, alternativas e exceções da fonte original.
3. Conferir contra baseline e código, e distinguir incrementos CAT/CPF/TUT em seção separada.
4. Acrescentar modelo relacional legível apenas após confronto entre diagrama, models.py e migrations.
5. Validar sumário, numeração, paginação e leitura após salvar; solicitar avaliação do orientador pela autora.

## Bloqueios explícitos
- **Apêndice completo no Google Doc:** não realizado nesta unidade; exige conciliação editorial com edição paralela recente da monografia (metadado Drive: 18/11/2026, 14:50 UTC) e cópia fiel das especificações integrais. Responsável: revisão técnica/autora. Retomar após conferir versão e local de inserção.
- **Aceite do tutorial:** depende de testes reais e avaliação humana; responsável: revisão técnica/orientador via autora.
- **OAuth real:** autorização do aplicativo e Render isolado não confirmados; independente deste índice.
