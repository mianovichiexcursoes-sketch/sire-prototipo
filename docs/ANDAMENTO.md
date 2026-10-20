# Andamento e decisões da execução — 20/10/2026

A autora autorizou o uso de Codex com a condição de rastrear o que foi feito.
O desenvolvimento foi realizado com assistência de IA, em um único projeto
extraído de `sire-prototipo-bloco-1.zip`. Nenhum comando foi executado no Windows.

## Etapas registradas

| Commit | Etapa | Conteúdo |
| --- | --- | --- |
| e18c26d | Bloco 1 | Preservação exata da estrutura do ZIP recebido |
| 442a3d8 | Bloco 2 | Agencia, PerfilUsuario, autenticação e cadastro; migration 0001 |
| 07e8f64 | Bloco 3 | Excursao, cadastro/edição vinculados à agência; migration 0002 |
| 2adcb65 | Bloco 4 | Embarques e publicação; migration 0003 |
| d4dde1a | Bloco 5 | Catálogo, pesquisa por destino e detalhes |
| 1e8e738 | Bloco 6 | Reserva e validação transacional; migration 0004 |
| c1b656c | Bloco 7 | Consulta das reservas do passageiro |
| 657e114 | Bloco 8 | Consultas de reservas e passageiros da agência |
| 96f3fc6 | Bloco 9 | Navegação, mensagens e CSS |

Commits posteriores registram legibilidade, correção de submissões vazias e
esta documentação. `historico-commits.txt` contém a sequência final completa.
Use `git show HASH` para ver os arquivos alterados e as diferenças de cada etapa.

## Verificações e limites do processo

Foram executados `manage.py check` após os blocos, migrations nos blocos que
alteraram models e conferência final de migrations. A verificação funcional HTTP
foi consolidada depois do Bloco 9; não foi realizada verificação manual em
navegador a cada bloco. Portanto, os commits intermediários registram incrementos
de código, e não versões individualmente aprovadas por demonstração manual.
Métodos introduzidos em Excursao referenciam relacionamentos que só foram
materializados nos blocos seguintes; a entrega completa tem essas dependências.
Não reescrevemos o histórico para esconder essa sequência.

Uma tentativa inicial de acessar o servidor entre chamadas de terminal falhou
por isolamento de rede do ambiente. Depois, servidor e requisições foram
executados no mesmo contexto e o HTTP 200 da página inicial foi observado.
O servidor usado nas verificações foi encerrado ao final.

A tentativa de revisão visual com Chromium não pôde prosseguir: o navegador não
estava instalado e seu download retornou um arquivo inválido. Não há evidência
visual produzida nem aprovação de layout em navegador nesta execução.

O guia cita Python 3.14.8; foi usado Python 3.12.14 disponível no Work. Django
6.1.2 foi instalado diretamente do requirements.txt. Não se afirma compatibilidade
verificada em Python 3.14.8 ou execução no computador da autora.

## Decisões simples para explicar na banca

- User do Django evita duplicação de autenticação; PerfilUsuario define papel e agência.
- Admin limita-se ao pré-cadastro de Agência e de usuários/perfis de Agente.
- Agência e status não são editáveis no formulário da excursão: vêm do servidor.
- Filtro pela agência protege também URLs digitadas diretamente.
- Só há RASCUNHO e PUBLICADA, sem fluxo de cancelamento ou retirada de publicação.
- Cada reserva ocupa uma vaga; disponibilidade é sempre calculada.
- BEGIN IMMEDIATE serializa escrita no SQLite antes do recálculo das vagas.
- Senhas, ambiente virtual e banco de verificação não acompanham a entrega.
- Nenhuma suíte automatizada, teste de regressão ou infraestrutura de testes foi criada.

## Pendências reais

1. Executar a demonstração manual em navegador e no Windows da autora.
2. Confirmar a instalação na versão Python 3.14.8, se for mantida como ambiente de referência.
3. Conferir visualmente as imagens finais dos diagramas; os campos foram seguidos pelo guia.
4. Associar um repositório GitHub da autora com acesso de escrita; não houve publicação.

Os documentos acadêmicos originais e os diagramas não foram modificados.

## Ajustes finais

Os arquivos Python, HTML e CSS foram formatados para leitura e revisão, com
imports agrupados. Um POST vazio passou a ser tratado como formulário enviado,
com apresentação dos erros obrigatórios. O GET direto de reserva lotada passou
a exibir indisponibilidade sem oferecer confirmação. Conferências pontuais
confirmaram esses dois comportamentos e a renderização dos templates alterados.
As ferramentas de formatação ficaram fora das dependências da aplicação.
