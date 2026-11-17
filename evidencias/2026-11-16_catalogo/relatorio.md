# SIRE — Identidade visual e filtros do catálogo

Verificação de 16/11/2026 (horário de Brasília). Código de partida: `75fcc6d`.
Requisitos e critérios: **SIRE — Especificação complementar: catálogo e ficha da excursão**, no Drive do projeto. A ER-SIRE 2.1 segue como referência da entrega original. Este é o primeiro incremento da evolução do catálogo; a descrição, o roteiro, os inclusos e o armazenamento de fotos serão avaliados no próximo incremento.

Ambientes descartáveis com dados fictícios: Django 6.1.2 em Linux, Chromium 153 com servidor local e SQLite, e cliente HTTP do Django com PostgreSQL 18.6 (READ COMMITTED). A demo do Render não foi usada ou alterada para estes ensaios.

| Requisito e caso de uso | Verificação | Resultado observado |
| --- | --- | --- |
| CAT-RF-01 · UC04 | CAT-VF-01 | Filtros isolados e por interseção; as datas-limite foram incluídas, rascunhos ficaram ocultos, e a pesquisa geral manteve o registro antigo. Datas invertidas geraram aviso sem apagar a seleção. Busca vazia e limpeza também conferidas. |
| CAT-RF-02 · UC06/UC07 | CAT-VF-02, somente tipo | Cadastro continuou em rascunho; o tipo foi salvo e reapareceu na edição; seleção inválida e edição entre agências foram recusadas. |
| CAT-RF-04 · UC05 | CAT-VF-04, somente tipo | A ficha mostra a classificação quando existe; a ficha legada permaneceu acessível com os dados anteriores e os rascunhos retornaram 404. |
| CAT-RNF-01 | CAT-VF-05 | Marca rosa e branca, foco visível ao navegar por Tab, controles e ações disponíveis em 320, 390, 768 e 1440 px. Contraste de 7,81:1 na marca e no botão principal, 9,38:1 na etiqueta e 3,63:1 na borda do campo, nas combinações medidas. |
| CAT-RNF-02 · UC06–UC10, UC12 e consultas do agente | CAT-VF-06 | O agente cadastrou e publicou. O passageiro escolheu embarque e confirmou. A reserva nº 2 apareceu para ambos, com 4 → 3 vagas. A migração 0005 → 0006 preservou excursão, embarque, conta e reserva preexistentes. Conferidos também login em maiúsculas, recuperação visível na tela de login, controle para mostrar senha e restrições de perfil e agência. |
| CAT-RF-03 · UC06/UC07 | CAT-VF-03 | Pendente. Não houve escolha de armazenamento ou teste de foto. |

O catálogo manteve a rota de busca anterior. O agente pode classificar excursões da própria agência; a migração não atribui tipo a registros antigos. A categoria “Com hospedagem” é informativa.

A suíte existente executou 67 testes no PostgreSQL, todos aprovados, incluindo os testes de concorrência existentes. No SQLite, 65 testes passaram e 2 foram ignorados por exigirem PostgreSQL. Essa execução da suíte não substitui os ensaios de carga ou o aceite no Render.

Evidências: [saída do navegador](resultados-navegador.json), [saída em PostgreSQL](resultados-postgresql.json), [catálogo no computador](01_catalogo_com_filtros.png), [catálogo em 390 px](02_catalogo_celular.png), [reserva do passageiro](03_reserva_passageiro.png) e [a mesma reserva do agente](04_reserva_agente.png). Os campos de data usam o controle nativo do navegador; os cartões exibem as datas em dia/mês/ano.

Para a avaliação da espiral, revisar a proposta de integração e conferir o incremento na demo depois da publicação. Registrar separadamente o próximo incremento de ficha e fotos; a persistência das imagens requer decisão antes do upload.
