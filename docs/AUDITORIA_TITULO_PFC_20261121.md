# Auditoria pontual de identidade acadêmica — 21/11/2026

Estado: **divergência confirmada em documentos originais; correção do título bloqueada por validação do orientador**. Esta nota não altera a monografia, não atesta conformidade ABNT e não modifica a demo.

## Evidência direta e rastreabilidade
- Monografia principal (ID `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg`): capa apresenta **PROJETO DE ARQUITETURA DE SOFTWARE APLICADO AO TURISMO RODOVIÁRIO** e subtítulo **ENGENHARIA DE REQUISITOS PARA PLATAFORMAS DE LOGÍSTICA DE LAZER**; folha de rosto repete a formulação.
- Modelo de relatório PFC (ID `1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo`, identificado como versão 12/2025): capa e folha de rosto usam **Projeto de Arquitetura de Software Aplicado ao Turismo Rodoviário: Engenharia de Requisitos para Plataformas Escaláveis de Logística de Lazer**. O adjetivo *Escaláveis* é diferença material.
- Parecer de pré-banca (ID `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA`, 23/10/2026), achado C2: alerta para promessa de escalabilidade não comprovada e exige confirmação do título oficial com orientador.
- Regulamento PFC Engenharia Elétrica (ID `1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL`, março/2026): consultado diretamente; sua existência não resolve qual título foi aprovado.
- Baseline (ID `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`): versão 2.1 histórica e seis entidades/UC01–UC14 devem ser preservadas; não inferir escalabilidade demonstrada a partir de suporte PostgreSQL.

## Bloqueio com responsável e condição de retomada
**Bloqueado: uniformização do título acadêmico.** Pré-requisito: confirmação escrita da autora/orientador do título registrado e subtítulo aprovado. Responsável: autora e orientador. Impacto: capa, folha de rosto, resumo, abstract, referências cruzadas e artefatos de entrega não podem ser harmonizados definitivamente. Retomar após confirmação; preservar versões anteriores e registrar alteração datada.

## Unidade independente executada
Confronto textual de quatro documentos originais com IDs exatos, registrando divergência verificável e ação humana necessária. **Não executados nesta unidade:** testes Django, navegador, PostgreSQL, CI, merge, deploy, OAuth ou revisão integral ABNT. Não é aceite do tutorial.

## Próxima ação técnica independente
Conciliar a cadeia de PRs do tutorial #15/#20/#21/#33/#35/#39 e respectivas bases, sem reescrever branches de outros agentes; testar TUT-01–09 em árvore integrada isolada com evidência de SHA e capturas. Em paralelo, auditar seções de metodologia/resultado da monografia sem editar título antes da aprovação.
