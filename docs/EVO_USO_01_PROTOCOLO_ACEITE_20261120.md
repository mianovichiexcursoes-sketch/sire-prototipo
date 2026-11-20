# EVO-USO-01 — protocolo de aceite observável (20/11/2026)

**Natureza:** roteiro de verificação **não executado**; não constitui evidência de aprovação. Incremento separado da baseline ER-SIRE 2.1 (seis entidades, UC01–UC14). Não requer OAuth Drive para os fluxos já existentes. Nenhum dado pessoal real.

## Fontes consultadas diretamente nesta rodada
- RN-01–RN-41: Google Doc `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` (isolamento e perfis RN-01–05; publicação RN-06–16; reservas RN-17–30).
- Baseline e histórico: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8` (ER-SIRE 2.1; revisão 2.6 datada 12/11/2026).
- Guia `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`; casos de uso `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`; requisitos `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`.
- CAT `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`; registro `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`.
- Plano da autora: `docs/PLANO_ESPIRAL_TUTORIAL_20261118.md` na branch `docs/retorno-orientador-tutorial-20261118`.
**Limite:** versões/modificações atuais de todos os documentos não foram aferidas; não afirmar revisão global.

## Pré-requisitos antes de executar
1. Reconciliar em branch de integração **isolada** as cadeias de tutorial #15/#20/#21 e #33/#35/#39; verificar HEAD, diff e conflitos de templates/JS. Não sobrepor mudanças de outro agente.
2. Preparar banco descartável com agência A e B, agentes distintos, passageiro sintético, excursão publicada com embarque e outra sem vagas; sem usar dados reais.
3. Registrar commit SHA exato, versões Django/Playwright/Chromium, banco, viewport, data/hora e comandos efetivos. Salvar logs com saída/exit code e capturas anonimizadas.
4. Não mesclar nem publicar a demo aprovada com base apenas neste roteiro.

## Matriz de cenários — estado inicial: PENDENTE (não executado)

| ID | Perfil/contexto | Ação verificável | Resultado esperado | Rastreabilidade |
|---|---|---|---|---|
| TUT-01 | Visitante, navegador limpo | Abrir catálogo, aceitar convite; Anterior/Próximo/Pular/Fechar | Destaque acompanha alvo existente; fechar devolve foco; nenhuma reserva | EVO-USO-01, UC03–05 |
| TUT-02 | Visitante | Abrir Como usar após pular; navegar catálogo/detalhes | Tutorial reinicia sob demanda sem criar conta | UC03–05 |
| TUT-03 | Passageiro autenticado sintético | Percorrer acesso, embarque, confirmação e minhas reservas | Instruções do perfil correto, sem POST automático | UC02, UC10–12; RN-17–21 |
| TUT-04 | Agente A | Percorrer excursões, cadastro, embarque, publicação, reservas e passageiros | Apenas instruções de agente; nenhuma publicação por avanço | UC06–09, UC13–14; RN-01–05 |
| TUT-05 | Agente A | Tentar abrir URL administrativa de agência B | 403/404 conforme contrato existente; nenhuma informação B no tutorial | RN-03–05, UC07, UC13–14 |
| TUT-06 | Todos | Tecla Escape, Tab, Shift+Tab, Enter nos controles | Escape fecha; foco visível e retorno coerente; sem submissão | EVO-USO-01 acessibilidade |
| TUT-07 | Todos | Desativar armazenamento local ou simular erro de storage | Tutorial utilizável sem dados pessoais nem exceção JS | EVO-USO-01 privacidade |
| TUT-08 | Visitante, 320px e 375×812 | Percorrer todos os passos | Painel permanece visível e operável, sem overflow horizontal | EVO-USO-01 responsividade |
| TUT-09 | Catálogo vazio, alvo ausente e excursão lotada | Abrir Como usar e avançar | Etapas sem alvo são tratadas sem travar; não oferece reserva inválida | UC03–05, RN-20–21 |
| TUT-10 | Passageiro, formulário de reserva preenchido com dados sintéticos | Avançar/pular/fechar tutorial | Nenhuma reserva criada por interação com tutorial; reserva só via ação explícita | UC10–11, RN-17–21 |

## Registro de evidência a preencher após execução
Para cada TUT: **status** (pendente/aprovado/falhou/bloqueado), **SHA**, **comando ou passos**, **resultado observado**, **arquivo de log/captura**, **ambiente**, **data**, **defeito/PR**. Não preencher resultados antecipadamente.

## Bloqueios e próximos passos
- **Integração concorrente — EM EXECUÇÃO em PRs separadas:** responsável: equipe de desenvolvimento. Impacto: impede ensaio conclusivo da árvore integrada. Condição: branch reconciliada com SHA fixado e testes repetíveis.
- **OAuth Drive `drive.file` — autorização não verificada:** responsável: autora/administradora do aplicativo. Impacto: testes reais de persistência/exclusão de fotos após deploy, não os cenários TUT. Condição: consentimento OAuth do próprio Django, credenciais somente em ambiente seguro.
- **Avaliação humana — PENDENTE:** responsável: autora e orientador. Impacto: EVO-USO-01 não pode ser marcado como avaliado. Condição: tentativa real documentada após versão verificada.
- **Próxima unidade:** aplicar protocolo na árvore integrada, registrar resultados e atualizar `docs/PROGRESSO_TCC_FINAL.md` canônico após conciliar PRs #30/#43; completar apêndice UC01–UC14 e modelo relacional sem alterar baseline.

**Não realizados nesta unidade:** testes automatizados, ensaio manual, merge, deploy, alterações de modelos/migrations, edição de monografia ou aprovação.
