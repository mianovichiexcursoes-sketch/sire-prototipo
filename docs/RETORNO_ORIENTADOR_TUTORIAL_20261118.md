# Retorno do orientador: uso guiado e nova avaliação da espiral
Registro em 18/11/2026. Estado: avaliação recebida; resposta planejada e especificada, implementação e aceite pendentes.

## Evidência de origem
Mensagens de Rodrigo Pantoni de 17/11/2026, transcritas pela autora nesta conversa:
- 09h41: solicita o modelo do banco.
- 09h43: solicita vídeo de utilização e relata não conseguir realizar operações.
- 09h55: solicita casos de uso no documento do projeto.
A autora solicitou um mini tutorial interativo indicando onde clicar. O tutorial é a resposta proposta pela autora; não atribuir esse pedido literal ao orientador. As mensagens são retorno qualitativo, não teste controlado de usabilidade.

## Fontes consultadas em 18/11
- Documento do projeto: https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit
  Seções 4.1 (diagrama UC), 4.2 (especificações em documento complementar), 4.4 (modelo relacional/Figura 4), 2.3.4 (avaliação).
- Casos de uso completos: https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit
  UC01–UC14 com atores, condições, fluxo principal, alternativas e exceções.
- Monografia: https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit
  Seções 3.2 e 4; figuras 2–4; seção 3.2.2.4 ainda intitulada encerramento.
- Código de referência: 7c53134264953908e8884bb588dd123d1d4cb972, branch etapa/postgresql-windows; templates base, agente_excursoes e detalhe_excursao lidos. Não foi verificada a execução no navegador nesta rodada.

## Resposta documental necessária
O modelo e os casos de uso estão referenciados nos documentos existentes. Isso não comprova que o professor conseguiu visualizá-los ou recebeu a versão correta.
1. Entregar modelo relacional legível junto ao documento, com legenda e referência à versão. Conferir visualmente Figura 4 e exportação PDF; leitura textual não valida legibilidade.
2. Incorporar as especificações UC01–UC14 ao pacote do projeto como apêndice, com sumário e referência explícita na seção 4.2. Apenas um link separado pode não atender ao pedido do professor.
3. Preservar seis entidades históricas, generalização Passageiro/Visitante e UC10 incluindo UC11. Separar extensões posteriores (ex.: FotoExcursao) do modelo da baseline.
4. Conferir agencia_id opcional para Passageiro e obrigatório pela regra de domínio para Agente.
Estado: fontes e localização confirmadas; apêndice consolidado e PDF ainda pendentes.

## Nova iteração inspirada no Modelo Espiral
Identificador: EVO-USO-01. Não renumerar retroativamente ciclos já documentados.
O feedback é entrada da avaliação do incremento anterior e motivação para uma nova volta. A documentação já menciona uma terceira iteração técnica; reconciliar a numeração antes de alterar a figura da espiral.

| Quadrante | Conteúdo desta volta | Estado |
|---|---|---|
| I — Objetivos, alternativas e restrições | Permitir uso inicial por Passageiro e Agente; tornar modelos e UC encontráveis. Alternativas: vídeo, guia escrito e tutorial contextual. Preservar permissões e escopo. | Especificado |
| II — Riscos e mitigação | Usuário não encontra ações; confunde perfil; tenta publicar sem embarque; confunde reserva com pagamento; tutorial cobre botões ou fica desatualizado. Usar passos por perfil, botão Pular, ajuda reabrível e ensaio em celular/desktop. | Riscos identificados; mitigação não validada |
| III — Desenvolvimento e verificação | Implementar tutorial, produzir vídeo real e consolidar pacote documental. Testar navegação, acessibilidade e regressão das operações. | Pendente |
| IV — Avaliação e próximo ciclo | Solicitar nova tentativa do orientador, registrar tarefas concluídas, dificuldades, ajuda necessária e decisões. | Pendente; não declarar aceite |

### Texto preparado para a monografia
Em 17 de novembro de 2026, o orientador relatou dificuldade para realizar operações no site e solicitou um vídeo demonstrativo, o modelo do banco de dados e a inclusão dos casos de uso no documento do projeto. Esse retorno qualitativo evidenciou limitações na apresentação dos artefatos e na orientação inicial de uso, sem constituir uma avaliação formal de usabilidade. A autora propôs um tutorial contextual, acompanhado de vídeo e organização dos documentos. O retorno foi incorporado à avaliação do incremento e ao planejamento de uma nova iteração inspirada no Modelo Espiral. Nesta iteração, foram definidos objetivos de orientação por perfil, riscos de navegação e critérios de verificação. A implementação, a gravação e a reavaliação pelo orientador permanecem pendentes; portanto, não se afirma melhoria de usabilidade comprovada nem encerramento dessa iteração.

Inserção proposta: metodologia após avaliação do incremento; resultados com status real; limitações e trabalhos futuros coerentes. Rever a expressão “encerramento do projeto” à luz da nova avaliação, sem apagar o fechamento histórico da baseline. Texto preparado, ainda não inserido na monografia.

## Tutorial interativo — contrato de implementação
- Oferta no primeiro acesso: “Quer conhecer o SIRE?” com “Começar” e “Agora não”.
- Ajuda permanente “Como usar”, permitindo repetir o tutorial.
- Controles: Anterior, Próximo, Pular/Fechar e indicador de etapa.
- Orientar o elemento real visível; não executar submissões, publicação, reserva ou exclusão automaticamente.
- Diferenciar visitante, passageiro e agente pela sessão existente; nunca permitir escolher um papel para ganhar acesso.
- Não repetir automaticamente em cada página. Guardar somente versão/progresso sem credenciais ou dados pessoais; continuar funcional se armazenamento do navegador estiver indisponível.
- Suportar teclado, Escape, foco visível, leitores de tela e celular; devolver foco ao acionador.
- Se alvo não existir (catálogo vazio, sem excursão, permissões diferentes), explicar o estado ou pular passo sem travar.
- Não prometer recursos ainda não publicados, como fotos reais ou pagamento.

### Fluxo Passageiro (UC01–05, UC10–12)
1. Catálogo: localizar excursão e consultar detalhes.
2. Criar conta ou Entrar: esclarecer que cadastro público cria Passageiro.
3. Detalhes: conferir destino, datas, valor e vagas.
4. “Selecionar embarque e reservar”: escolher ponto de embarque.
5. “Confirmar reserva de uma vaga”: explicar que gera reserva; não realiza pagamento.
6. “Minhas reservas”: conferir resultado.
Sem excursões/vagas, mostrar orientação adequada; não criar dados automaticamente.

### Fluxo Agente (UC02, UC06–09, UC13–14)
Pré-condição: conta de Agente previamente provisionada e vinculada a agência. Cadastro público não concede esse papel.
1. “Excursões da agência”.
2. “Nova excursão”: preencher campos e salvar rascunho.
3. “Adicionar embarque”: informar local e horário.
4. “Publicar”: disponível com requisitos atendidos; exige ação explícita do agente.
5. Conferir excursão no catálogo.
6. “Reservas” e “Passageiros”: consultar somente excursões da própria agência.
Os rótulos acima foram conferidos nos templates da versão de referência; revisar contra a versão final antes de gravar.

## Vídeo demonstrativo — roteiro de 3 a 5 minutos
1. Abertura: URL, objetivo acadêmico e distinção entre Passageiro e Agente.
2. Agente: mostrar login sem filmar senha; criar excursão fictícia, adicionar embarque e publicar no ambiente de demonstração isolado.
3. Passageiro: abrir catálogo em sessão separada, entrar com conta fictícia, consultar detalhes, escolher embarque e confirmar uma vaga.
4. Mostrar “Minhas reservas”; voltar ao Agente e conferir a mesma reserva.
5. Encerrar indicando “Como usar” (somente após implementado) e localização do documento/modelo/UC.
Gravar tela real com cursor e legendas; não usar dados de clientes, tokens ou capturas simuladas. Registrar versão, ambiente e data. Vídeo ainda não gravado.

## Critérios de aceite e registro da próxima avaliação
- TUT-01: primeiro acesso oferece ajuda, dispensável e reabrível.
- TUT-02: orientações e alvos correspondem ao perfil e à página.
- TUT-03: funciona em celular e desktop, teclado/Escape, sem encobrir controles essenciais.
- TUT-04: tutorial não envia formulários nem altera dados.
- TUT-05: estados vazios, sem vagas e armazenamento indisponível não bloqueiam uso.
- TUT-06: mesma reserva pode ser localizada pelo Passageiro e pelo Agente autorizado; isolamento preservado.
- DOC-01: PDF legível contém modelo relacional, diagrama e especificações UC01–UC14 acessíveis pelo sumário.
- VID-01: vídeo reproduz o fluxo publicado para avaliação e não expõe credenciais.
- AVAL-01: orientador recebe pacote e tenta tarefas; registrar conclusão, dúvidas, intervenção e tempo apenas se medido. Não fabricar aprovação ou mensagem enviada.

## Concorrência e continuidade
Há novas branches OAuth, incluindo fix/oauth-execucao-real-20261118, mas nomes/commits não identificam com certeza a atividade local do Claude. Não é possível garantir ausência de alterações ainda não enviadas ao GitHub.
Este registro ocupa arquivo novo em branch exclusiva. Nenhum template, código OAuth, migração, configuração Render, documento original ou demo foi modificado.
Próxima execução: implementar tutorial em branch isolada com arquivos próprios, comparar alterações remotas antes de editar base.html, testar, reconciliar com Claude e revisar antes de publicar. OAuth não é pré-requisito para orientação dos fluxos já existentes.
Não considerar esta entrega documental como tutorial implementado, vídeo entregue, monografia atualizada ou aceite concluído.
