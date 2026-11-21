# EVO-USO-01 — índice verificável para apêndice de casos de uso (21/11/2026)

**Natureza:** preparação editorial rastreável, não apêndice final nem teste executado. Leitura direta da fonte oficial por ID em 21/11/2026: [Especificação de Casos de Uso – SIRE](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit). Conferidas também regras RN-01–41, documentação de desenvolvimento ER-SIRE 2.1, guia, requisitos v3.0, especificação CAT e registro técnico. Não substituir as especificações completas por esta lista.

## Índice para apêndice textual da monografia

| ID original | Título oficial | Rastreabilidade inicial | Situação do apêndice |
|---|---|---|---|
| UC01 | Cadastrar passageiro | Visitante; cadastro | transcrição integral pendente |
| UC02 | Autenticar usuário | Visitante/usuário; autenticação | transcrição integral pendente |
| UC03 | Consultar catálogo de excursões | Visitante; catálogo | transcrição integral pendente |
| UC04 | Pesquisar excursões | Visitante; pesquisa | transcrição integral pendente |
| UC05 | Consultar detalhes da excursão | Visitante; detalhes | transcrição integral pendente |
| UC06 | Cadastrar excursão | Agente; excursão | transcrição integral pendente |
| UC07 | Editar excursão | Agente; edição | transcrição integral pendente |
| UC08 | Cadastrar ponto de embarque | Agente; embarque | transcrição integral pendente |
| UC09 | Publicar excursão | Agente; publicação | transcrição integral pendente |
| UC10 | Realizar reserva | Passageiro; reserva | transcrição integral pendente |
| UC11 | Selecionar ponto de embarque | Passageiro; embarque | transcrição integral pendente |
| UC12 | Consultar minhas reservas | Passageiro; reservas | transcrição integral pendente |
| UC13 | Consultar reservas da excursão | Agente; reservas | transcrição integral pendente |
| UC14 | Consultar passageiros da excursão | Agente; passageiros | transcrição integral pendente |

## Critério editorial para inserir no documento do projeto

Para **cada** UC, transportar fielmente descrição, atores, pré-condições, pós-condições, fluxo principal, alternativos e exceções da fonte oficial. Conferir títulos e referências cruzadas, gerar sumário e paginação no editor do documento, sem inventar fluxos nem alegar que a monografia foi atualizada. Não renumerar UC01–UC14. Manter baseline ER-SIRE 2.1 e seis entidades históricas; CPF, fotos, catálogo ampliado e tutorial são extensões separadas.

## Dependências e bloqueios concretos

- **Pendente — integração editorial:** ler a monografia completa e confrontar seção de casos de uso, anexos e sumário antes de inserir o apêndice. Responsável: revisão acadêmica/autora. Condição de retomada: matriz UC→seção consolidada e permissão de edição verificada.
- **Pendente — modelo relacional:** confrontar nomes de tabelas, campos e relações do documento ER-SIRE 2.1 com migrations da versão efetivamente escolhida; não apresentar extensões como seis entidades originais.
- **Bloqueado — aceite do tutorial:** reconciliar PRs de código concorrentes e executar TUT-01–09 em navegador antes de declarar EVO-USO-01 verificado; avaliação humana é posterior.
- **Bloqueado — fotos reais:** OAuth `drive.file` do aplicativo Django e configuração segura no Render não comprovados. Responsável: titular da conta. Não impede apêndice UC ou tutorial local.

**Evidência desta unidade:** arquivo versionado nesta branch e link da fonte oficial acima. **Não executados:** testes, merge, deploy, edição da monografia ou avaliação do orientador. Próxima ação: comparar modelo relacional com migrations, então preparar apêndice completo em documento acadêmico autorizado, preservando histórico.
