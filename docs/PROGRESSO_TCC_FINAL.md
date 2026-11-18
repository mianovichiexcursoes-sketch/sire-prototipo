# PROGRESSO TCC FINAL — registro de unidade documental (18/11/2026 14h)

**Escopo desta branch:** índice dos 14 casos de uso para retorno do orientador. Não substitui os checklists de outras branches/PRs. Preservar baseline ER-SIRE 2.1, UC01–UC14 e seis entidades.

| Item | Estado | Último commit | Evidência | Próxima ação |
|---|---|---|---|---|
| EVO-USO-01 índice UC | **Concluído (somente índice)** | `7b32020b` | `docs/EVO_USO_01_INDICE_UC_ORIENTADOR_20261118.md` e fonte original UC | Conferir e inserir apêndice integral no documento do projeto |
| EVO-USO-01 tutorial | Em execução | PR #21 / #20 | Código e suíte proposta, sem resultado de navegador confirmado | Verificar CI e testar Django, teclado, celular e perfis |
| EVO-USO-01 modelo relacional | Em execução (quadro de código concluído) | `32b2ffb` | `docs/EVO_USO_01_MODELO_RELACIONAL_CONFERENCIA_20261118.md`; models.py/0001/0006 lidos | Conferir diagrama, árvore real 0007, banco e inserir anexo no documento após conciliação |
| A — Ficha/fotos | Verificação pendente | PR #2 fechada, merge não confirmado | PR #2, CI histórico de fotos | Conciliar integração e persistência real |
| B — OAuth Drive | **Bloqueado** | PR #9 | Ausência de comprovação da autorização própria do app e ambiente isolado | Autora/operador configurar OAuth drive.file e Render seguro; retomar teste real |
| C — CPF/LGPD | Pendente de conciliação | PR dedicada | Não ensaiado nesta unidade | Revisar PR e testes sintéticos |
| D — UX reserva | Pendente de conciliação | — | — | Rever branch independente |
| E — Painéis | Pendente | — | — | Verificar consultas e permissões |
| F — VF/CAT regressão | Parcial | CI histórico | Não testado nesta unidade | Ensaios SQLite/PostgreSQL e navegador |
| G — auditoria acadêmica | Pendente | — | Documentos oficiais acessados | Inventário Drive e auditoria integral da monografia |

## Fontes oficiais consultadas diretamente (18/11/2026)
RN (ID 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0, mod. 28/09); baseline (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8, mod. 18/11); guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U, mod. 12/11); UC (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY, mod. 22/10); requisitos (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM, mod. 23/10); CAT (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is, mod. 18/11); registro (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM, mod. 18/11); monografia (1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg, mod. 18/11); modelo IFSP (1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo); regulamento (1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL); pré-banca (1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA); histórico PROMPS (1mpNI5u26q3NzVgXFeeMCHZgfWdxCgsG-WTangQWVRrE).

## Bloqueios e continuidade
- **Concorrência documental:** monografia modificada em 18/11 às 14:50 UTC; não sobrescrever sem conciliação da revisão atual. Responsável: revisão técnica/autora. Retomar após comparar versão e localizar apêndice.
- **OAuth:** falta autorização do aplicativo e ambiente Render isolado confirmados; bloqueia ensaio real de fotos, não índice UC nem tutorial.
- **Avaliação:** professor ainda não reavaliou tutorial; solicitar apenas via autora após testes.
- **Limites:** este índice não equivale a apêndice completo, modelo de dados validado, teste de navegador, aceite nem deploy.

## Unidade 18/11/2026 15h — modelo relacional
- Entrega: `32b2ffb` — quadro das seis entidades históricas, FKs e extensões em arquivo novo, sem tocar modelos/migrations nem monografia.
- **Bloqueio parcial:** nome/branch da migration 0007 ainda não confirmado; tentativa de leitura por caminho presumido retornou 404. Impacto: não atestar sincronismo entre esquema e models. Responsável: revisão técnica. Retomar após listagem efetiva da árvore e teste isolado.
- **Conflito editorial:** documento principal teve edição paralela recente; não houve alteração nele. Responsável: revisão técnica/autora. Retomar após comparação do conteúdo vigente e autorização de integração.
- **Próximo item independente:** apêndice UC01–UC14 a partir da especificação oficial e/ou testes TUT-01–06, após conferir estado das PRs e CI. Nenhum teste/deploy/merge nesta unidade.

## Unidade 18/11/2026 16h — apêndice UC01–UC14
- **Concluído (artefato de revisão):** transcrição integral do documento oficial de casos de uso em `docs/EVO_USO_01_APENDICE_UC01_UC14_20261118.md`; commit `1f0c0b65dbec5af81c274be2e21b4a6b434c7684`. Fonte lida diretamente pelo ID original nesta rodada. Não houve alteração da monografia, modelos, migrations ou demo.
- **Pendente:** conciliar monografia atual e incorporar apêndice com sumário/paginação, confirmar texto com orientador; conferir diagrama e migrations da branch efetiva; testar TUT-01–06 e registrar logs.
- **Bloqueio de integração:** monografia em edição paralela; responsável revisão acadêmica/autora; condição para retomar: comparação da versão atual e local de inserção sem sobrescrever alterações. OAuth Drive permanece bloqueado para ensaio real de fotos, mas não impede documentação.
- **Próxima unidade independente:** inspecionar o CI da PR #21 e a árvore de migrations em branch real; preparar matriz código/migration/teste sem alegar validação não realizada.

## Unidade 18/11/2026 17h55 — reconciliação de aceite (PR #24)
- **Concluído (documentação verificável):** `docs/EVO_USO_01_RECONCILIACAO_ACEITE_20261118_17H.md`, commit `0ad3cd5e7654dca7d18263a2e4496a3ebda42651`. Fonte: `docs/ACEITE_FUNCIONAL_FINAL_20261118.md` incorporado na branch da demo pela PR #24 (merge 18:48 UTC); leitura direta das fontes RN/baseline/guia/UC/requisitos/CAT/registro nesta rodada.
- **EVO-USO-01 — em execução, teste funcional documentado por outro agente:** 13 aprovados, 3 ressalvas, 1 bloqueado, 0 falhas; 107 testes OK e 3 ignorados **conforme registro da PR #24**, não reexecutados nesta rodada. Evidências de tutorial visitante/agente/passageiro e mobile em `evidencias/2026-11-18_aceite_final/`. Próxima ação: conciliar tutorial no HEAD publicado, corrigir sobreposição no celular e revalidar.
- **B — OAuth Drive — evidência parcial, não declarar bloqueio absoluto:** PR #18 relata 13 ensaios reais e o aceite confirma foto existente no Render. **Bloqueado para nova comprovação** de upload/exclusão/persistência pós-deploy até ambiente autorizado e reexecução; responsável técnica/autora. Próxima ação: conferir integração segura e ensaio real sem segredos.
- **G — monografia/apêndice — conciliação necessária:** PR #17 relata inserção prévia dos UC01–UC14 na documentação principal; PR #23 e #26 propõem complementos. Não inserir duplicado. Responsável revisão acadêmica; retomar após comparar conteúdo atual e sumário.
- **Pendência humana:** login autenticado no Render (cenário 2b) e reavaliação do orientador. Não foram realizados merge, deploy, testes nem edições do Google Docs nesta unidade.
