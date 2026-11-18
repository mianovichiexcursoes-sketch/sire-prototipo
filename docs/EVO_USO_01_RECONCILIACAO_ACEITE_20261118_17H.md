# Reconciliação de evidências SIRE — 18/11/2026, 17h55 BRT

## Escopo e fontes conferidas
Leitura direta dos documentos oficiais RN (ID `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`), baseline (`19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`), guia (`1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`), UC (`1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`), requisitos (`1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`), CAT (`1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`) e registro (`1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`). Conferidos também PR #17, #18, #21, #24, #26 e o documento `docs/ACEITE_FUNCIONAL_FINAL_20261118.md` da branch `etapa/postgresql-windows`. Este documento não altera a baseline ER-SIRE 2.1, os UC01–UC14, as seis entidades nem a demo.

## Divergência temporal identificada
O checklist documental da PR #26 ainda diz que não há resultado de navegador confirmado e que OAuth não tem autorização comprovada. **Essas frases estão desatualizadas frente à evidência posterior/concorrente**:
- PR #24 foi mesclada à branch da demo em 18/11 às 18:48 UTC e acrescentou evidências de aceite funcional: 13 cenários aprovados, 3 com ressalva, 1 bloqueado, 0 falhas, 32 capturas declaradas, e suíte reportada de 107 OK / 3 ignorados no commit `e220974`. Trata-se de **resultado relatado e versionado pelo outro agente**, não de testes reexecutados nesta unidade.
- O registro de aceite informa tutorial contextual já presente na versão `e220974`, verificado no navegador em visitante, passageiro e agente, com ressalva de sobreposição no celular.
- PR #18 relata OAuth publicado, refresh token renovado e 13 verificações reais no Drive; o registro de aceite refere evidência anterior de fotos e uma foto carregada no Render. **Não equivale a confirmação de novo upload nesta rodada**, nem a autorização para expor credenciais. Não classificar OAuth como absolutamente inexistente; verificar configuração vigente e persistência de forma segura antes de encerrar a etapa B.
- PRs #22/#25/#26 contêm entregas documentais em cadeia; PR #23 já registra auditoria de UC/modelo, e PR #17 declara apêndice UC e seção da monografia atualizados. **Evitar duplicar a inserção na monografia**; comparar conteúdo atual antes de editar.

## Matriz de rastreabilidade da evidência
| Requisito | Código/artefato | Cenário | Evidência atual | Lacuna |
|---|---|---|---|---|
| EVO-USO-01 / UC catálogo | tutorial na versão `e220974`; PR #15/#17/#20 | TUT-01–04 | `ACEITE_FUNCIONAL_FINAL_20261118.md`, cenários 12–14, imagens R01–R04, L01–L02, L10–L11 | Ajustar cobertura móvel/teclado; avaliação orientador |
| RN-03/05, UC agente | views/URLs existentes; branch demo | isolamento agência/perfil | aceite cenário 10, imagens L09/L14/L15/L19/L20 | Conferir regressão no HEAD de integração |
| RN-06/11/26, UC excursão | modelos/views e migration 0007 a conferir | criar, embarque, publicar | aceite cenários 3–6 | Confirmar árvore de migrations e PostgreSQL |
| RN-20–30, UC reserva | reserva Django | lotação, concorrência | aceite cenários 7–9b | Concorrência PostgreSQL não foi reexecutada no aceite local |
| CAT / fotos | PR #17/#18 e versão demo | ficha e galeria | aceite cenário 11; foto exibida no Render | Novo envio/exclusão/persistência após deploy não reexecutados |
| UC01–UC14 / baseline | documentos oficiais + PR #23/#26 | apêndice/modelo | PRs #17/#23/#26 | Conferir apêndice realmente presente na monografia atual, sumário e paginação |

## Bloqueios e condições de retomada
1. **Avaliação do orientador**: não existe aceite dele nesta evidência. Responsável: autora/orientador. Retomar após autora solicitar nova tentativa de uso; não enviar mensagem automaticamente.
2. **Login autenticado no Render**: cenário 2b não executado. Responsável: autora, em sessão segura; testar perfis sem compartilhar senha.
3. **Persistência Drive pós-deploy e novo upload/exclusão**: ausência de reexecução na evidência de aceite; requer ambiente autorizado e procedimento sem expor segredos. Responsável: responsável técnico/autora.
4. **Integração documental concorrente**: PR #17 e #23 já descrevem mudanças no documento principal. Responsável: revisão acadêmica. Condição: comparar conteúdo atual, identificar duplicidades e preservar histórico.

## Próxima ação independente
Inspecionar no HEAD atual o tutorial móvel e propor correção da sobreposição **somente após conciliar o código publicado e as PRs abertas**, com teste de navegador e regressão em branch isolada. Alternativamente, inventariar as migrations reais e confrontar a matriz acima com os arquivos versionados. Não fazer merge/deploy sem gate.
