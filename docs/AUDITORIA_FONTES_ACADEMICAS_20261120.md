# SIRE — confronto preliminar das fontes acadêmicas complementares (20/11/2026)

**Natureza:** leitura direta das fontes originais por ID no Google Drive, sem alterar originais; inventário parcial, não auditoria global concluída. Não constitui aceite acadêmico nem comprovação de testes.

| Fonte | ID | Modificação informada pelo Drive (UTC) | Achado verificável | Próxima ação |
|---|---|---|---|---|
| Monografia principal | `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg` | 18/11/2026 22:30 | Capa e folha de rosto trazem título principal **PROJETO DE ARQUITETURA DE SOFTWARE APLICADO AO TURISMO RODOVIÁRIO**, subtítulo **ENGENHARIA DE REQUISITOS PARA PLATAFORMAS DE LOGÍSTICA DE LAZER**; orientador grafado **Professor Rodrigo Pantoni** | Confirmar com orientador título/subtítulo e titulação antes de padronizar |
| Modelo de relatório PFC | `1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo` | 30/06/2026 20:05 | Capa e folha de rosto usam subtítulo diferente: **Engenharia de Requisitos para Plataformas Escaláveis de Logística de Lazer**; orientador **Prof. Dr. Rodrigo Pantoni** | Registrar divergência, não copiar automaticamente título nem titulação |
| Regulamento PFC Engenharia Elétrica | `1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL` | 28/09/2026 13:00 | Documento em PDF do IFSP Sertãozinho; Art. 1º estabelece disciplina de realização do PFC e Art. 2º o caracteriza como atividade obrigatória | Conferir integralmente exigências de apresentação, avaliação e entrega; não inferir conformidade ABNT da leitura inicial |
| Parecer de pré-banca | `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA` | 23/10/2026 10:40 | Parecer **orientativo e independente**, alerta para divergências entre históricos/vigentes, UML e código, alegações de escalabilidade e transparência de autoria | Transformar alertas em matriz de achados com localização e evidência, sem atribuir aprovação à banca |
| PROMPS TCC | `1mpNI5u26q3NzVgXFeeMCHZgfWdxCgsG-WTangQWVRrE` | 28/09/2026 16:54 | Histórico de orientações e ideias, inclusive formulação anterior do título; **não** substitui requisitos oficiais | Usar apenas como histórico datado; prevalecem baseline e decisões posteriores aprovadas |

## Dependências e rastreabilidade

- **G — título/ABNT:** status **pendente de validação humana**; pré-requisito: decisão explícita da autora com orientador sobre título e qualificação. Responsável: autora/orientador. Condição para retomar: confirmação registrável. Não alterar capa, folha de rosto nem título no Drive antes disso.
- **G — auditoria global:** status **em execução parcial**; estas cinco fontes foram acessadas, mas ainda falta inventário completo da pasta “TCC JULIA — SIRE”, revisão integral de monografia e anexos, confrontação com RF/RN/UC/CAT/EVO, referências e figuras. Não declarar conclusão.
- **EVO-USO-01:** o pedido de tutorial interativo permanece incremento independente; este confronto acadêmico não prova TUT-01–09, não resolve conflitos de JS das PRs #15/#20/#33/#35 e não autoriza merge/deploy.
- **B — OAuth:** bloqueio separado para integração real de fotos; titular do aplicativo/Render deve autorizar `drive.file` e configurar credenciais em ambiente seguro. Este bloqueio não impede auditoria documental nem testes locais de tutorial.

**Evidência:** documentos originais pelos IDs exatos acima, consultados diretamente em 20/11/2026. Esta unidade não executou testes Django, PostgreSQL, Chromium, migrações, CI, deploy ou avaliação de orientador. Preservadas baseline ER-SIRE 2.1, UC01–UC14 e seis entidades históricas.
