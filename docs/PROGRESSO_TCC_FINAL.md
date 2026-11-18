# PROGRESSO TCC FINAL — registro de unidade documental (18/11/2026 14h)

**Escopo desta branch:** índice dos 14 casos de uso para retorno do orientador. Não substitui os checklists de outras branches/PRs. Preservar baseline ER-SIRE 2.1, UC01–UC14 e seis entidades.

| Item | Estado | Último commit | Evidência | Próxima ação |
|---|---|---|---|---|
| EVO-USO-01 índice UC | **Concluído (somente índice)** | `7b32020b` | `docs/EVO_USO_01_INDICE_UC_ORIENTADOR_20261118.md` e fonte original UC | Conferir e inserir apêndice integral no documento do projeto |
| EVO-USO-01 tutorial | Em execução | PR #21 / #20 | Código e suíte proposta, sem resultado de navegador confirmado | Verificar CI e testar Django, teclado, celular e perfis |
| EVO-USO-01 modelo relacional | Pendente | — | Baseline ER-SIRE 2.1 consultada | Comparar diagrama, models.py e migrations, gerar modelo legível |
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
