# EVO-USO-01 — roteiro de verificação independente (19/11/2026)

**Status: PENDENTE DE EXECUÇÃO.** Este documento define testes, não declara resultados. Base de comparação: branch `etapa/postgresql-windows`. Nenhuma alteração em produção, modelos, migrações ou dados.

## Fontes efetivamente lidas em 19/11
- RN-01–41: Google Doc `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`, em particular RN-03–05 (perfis/privacidade).
- Baseline ER-SIRE 2.1: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8` (histórico até 2.6).
- Guia: `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`.
- UC01–UC14: `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`.
- Requisitos 3.0 PFC2: `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`.
- CAT revisão 0.2: `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`.
- Registro de implementação: `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`.
- Plano aprovado: `docs/PLANO_ESPIRAL_TUTORIAL_20261118.md`, branch `docs/retorno-orientador-tutorial-20261118`.

## Estado GitHub e risco de concorrência
- PR #33 introduziu ação explícita Fechar no tutorial, mas informa que **não repetiu testes**.
- PR #24 registra ressalva de sobreposição no rodapé em celular; não presumir correção.
- PRs #30/#31 alteram o checklist; reconciliar antes de sobrescrever `docs/PROGRESSO_TCC_FINAL.md`.
- O template `sire/templates/sire/base.html` da demo já carrega `tutorial-uso.js`. Portanto não duplicar o tutorial. Alterações locais de outro agente não são visíveis aqui.

## Matriz de testes proposta
| ID | Perfil e cenário | Resultado esperado | Estado / evidência | Próxima ação |
|---|---|---|---|---|
| TUT-01 | Visitante, primeiro acesso em navegador limpo | Oferta do tutorial sem criar conta ou reserva | PENDENTE / sem captura | Navegador isolado |
| TUT-02 | Passageiro autenticado sintético | Apenas alvos de catálogo, embarque, confirmação e minhas reservas | PENDENTE | Testar perfil e estados vazios |
| TUT-03 | Agente sintético de agência A | Apenas ações autorizadas; nenhuma operação da agência B | PENDENTE | Testar isolamento RN-03–05 |
| TUT-04 | Anterior, Próximo, Pular, Fechar | Transições sem POST ou submissão automática | PENDENTE | Inspecionar rede e formulários |
| TUT-05 | Escape, Tab, Shift+Tab e foco | Diálogo navegável e retorno de foco ao gatilho | PENDENTE | Teste teclado e leitor de tela |
| TUT-06 | Viewport 375×667 e 320×568 | Controles acessíveis; sem cobrir rodapé/CTA | PENDENTE; ressalva PR #24 | Corrigir CSS em branch separada após conciliação |
| TUT-07 | Elemento alvo ausente, excursão sem vagas | Pular alvo com mensagem coerente; não travar | PENDENTE | Cenários sintéticos |
| TUT-08 | localStorage bloqueado e sessão nova | Tutorial funcional sem exceção; somente progresso/versão persistidos quando possível | PENDENTE | Simular bloqueio |
| TUT-09 | Versão nova / reabrir Como usar | Oferta controlada por versão e reinício manual disponível | PENDENTE | Inspecionar storage |

## Dependências e rastreabilidade
EVO-USO-01 → `sire/static/sire/js/tutorial-uso.js`, `sire/templates/sire/base.html` → TUT-01–09 → capturas, logs de navegador e SHA **a produzir** → monografia, seção de avaliação da espiral **pendente**. RN-03–05/UC01–14 permanecem históricos, não são renumerados. OAuth Drive `drive.file` é BLOQUEADO para integração real: depende de consentimento do aplicativo e configuração segura pela autora/operadora; não impede estes testes de interface. Não usar CPFs, fotos ou pessoas reais.

## Próxima execução
1. Comparar HEAD da demo, PR #24 e PR #33 e conciliar o CSS antes de editar.
2. Executar TUT-04–06 em navegador isolado, registrar versão, SHA, screenshots e resultados observados.
3. Executar regressão Django SQLite/PostgreSQL e conferir CI; separar não executado de aprovado.
4. Atualizar checklist canônico e documentos acadêmicos após reconciliação, sem alterar baseline.
5. Solicitar avaliação humana somente após revisão e testes; **sem merge ou deploy nesta unidade**.
