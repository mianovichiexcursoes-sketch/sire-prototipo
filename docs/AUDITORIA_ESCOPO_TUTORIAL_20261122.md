# EVO-USO-01 — auditoria de escopo do tutorial perante as fontes oficiais

Data da leitura: 22/11/2026. Estado: **análise documental concluída; validação de código e experiência pendente**. Documento incremental, não substitui a baseline ER-SIRE 2.1 nem a matriz TUT da PR #65.

## Fontes consultadas diretamente por ID

- [Regras RN-01–RN-41](https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit)
- [Baseline ER-SIRE 2.1](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit)
- [Guia do protótipo](https://docs.google.com/document/d/1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U/edit)
- [UC01–UC14](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit)
- [Requisitos v3](https://docs.google.com/document/d/1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM/edit)
- [Extensão CAT](https://docs.google.com/document/d/1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is/edit)
- [Registro técnico](https://docs.google.com/document/d/1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM/edit)

As datas das versões documentais não foram equiparadas à data desta leitura. Para texto vigente, confrontar revisões antes da integração.

## Matriz de fronteiras: orientação não é execução

| Origem | Orientação admissível | Comportamento proibido do tutorial | Evidência necessária |
| --- | --- | --- | --- |
| UC03–UC05; RN-10–13 | Visitante: catálogo, pesquisa, detalhe, vagas e estado da excursão | Exibir excursão não publicada como reservável ou induzir reserva quando lotada | Navegador: publicada, rascunho e sem vagas |
| UC01–UC02; RN-04–05 | Passageiro: cadastro/autenticação conforme sessão atual | Exibir instruções de novo cadastro a passageiro já autenticado; revelar dados pessoais | Sessões sintéticas autenticada/anônima |
| UC10–UC11; RN-17, RN-20–24 | Passageiro: ponto de embarque e confirmação explícita | Disparar POST, selecionar embarque ou confirmar reserva automaticamente | Inspeção JS, requests e contagem de reservas antes/depois |
| UC12–UC14; RN-03–05 | Consultas de reservas/passageiros compatíveis com papel | Orientar agente a visualizar dados de outra agência | Contas sintéticas de duas agências e respostas de autorização |
| UC06–UC09; RN-06–11, RN-14 | Agente: criar, editar, embarques e publicar | Salvar formulário ou publicar automaticamente | Inspeção requests e estado do objeto antes/depois |
| EVO-USO-01 | Próximo, Anterior, Pular, Fechar, Como usar e foco | Prender foco, ocultar botão de saída, persistir CPF ou identificador pessoal | Teclado, Escape, mobile e storage desabilitado |

A matriz relaciona **regras e casos de uso**, não comprova que a implementação atende aos itens. Verificar nomes e alcance exatos de UC12–UC14 contra a especificação antes de inserir texto acadêmico definitivo.

## Dependências e separação de trabalhos

- PR #2 está **merged** (consulta GitHub de 22/11), mas isso não valida OAuth, upload persistente ou exclusão em produção.
- PR #15 contém a proposta de tutorial; PR #20 propõe acessibilidade; PR #64 trata da orientação ao passageiro autenticado; PR #65 mantém matriz de verificação; PR #66 propõe reconciliação do checklist canônico. São propostas **não integradas** na leitura de 22/11. Não modificar os HEADs dessas PRs em paralelo.
- OAuth próprio do aplicativo com escopo `drive.file` é pré-requisito para ensaio real de integração de fotos, **não** para orientação das páginas existentes.
- Tutorial depende de alvos DOM reais, perfis e fluxos existentes. Integrar primeiro em branch de conciliação após comparar diffs, e então testar; não publicar só porque os textos foram escritos.

## Riscos a reavaliar em navegador

1. Alvo inexistente: texto alternativo útil e saída acessível, sem travar o fluxo.
2. Papel divergente: visitante não recebe ações de agente, passageiro autenticado não recebe sugestão de novo cadastro.
3. Estado vazio/lotado: instrução não oferece ação que o sistema impede.
4. Navegação por Tab/Shift+Tab/Escape e retorno de foco ao gatilho; uso sem mouse.
5. Larguras 320px e 375px: balão, destaque e botões visíveis sem corte.
6. `localStorage` indisponível: tutorial permanece utilizável sem armazenar dados pessoais.
7. Ausência de requisições mutáveis disparadas pelo tutorial; conferir estado de reserva/publicação antes e depois.

## Evidência e situação

Esta unidade consiste **somente em leitura das fontes oficiais, confronto de escopo e versionamento documental**. Não foram executados testes Django, PostgreSQL, CI, navegador, deploy ou avaliação humana. Nenhuma migration, template, dado ou demo foi alterado.

**Próxima ação:** reconciliar PRs #15/#20/#64/#65 com a branch de referência em integração isolada, inspecionar JS/DOM e executar cenários acima. Registrar SHA de integração, comando, saída e prints reais. Atualizar `docs/PROGRESSO_TCC_FINAL.md` somente após conciliar a PR #66, evitando sobrescrever o trabalho concorrente. Preservar seis entidades e UC01–UC14 da baseline; incrementos permanecem separados.
