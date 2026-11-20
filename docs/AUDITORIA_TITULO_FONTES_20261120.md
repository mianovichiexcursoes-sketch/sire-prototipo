# SIRE — divergência verificável de título e identificação acadêmica (20/11/2026)

**Escopo:** auditoria documental pontual independente, sem alteração de código, baseline, monografia original ou demo. **Estado:** achado confirmado por leitura direta dos documentos; correção editorial **bloqueada por confirmação humana do título oficial**. Não é auditoria global nem aceite de banca.

## Fontes primárias lidas diretamente por ID

1. [Monografia principal](https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit), título exibido: **PROJETO DE ARQUITETURA DE SOFTWARE APLICADO AO TURISMO RODOVIÁRIO**; subtítulo na abertura: **ENGENHARIA DE REQUISITOS PARA PLATAFORMAS DE LOGÍSTICA DE LAZER**; orientador identificado como **Professor Rodrigo Pantoni**.
2. [Modelo de relatório PFC IFSP, versão dezembro/2025](https://docs.google.com/document/d/1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo/edit), capa e folha de rosto apresentam **Projeto de Arquitetura de Software Aplicado ao Turismo Rodoviário: Engenharia de Requisitos para Plataformas Escaláveis de Logística de Lazer**; orientador identificado como **Prof. Dr. Rodrigo Pantoni**.
3. [Parecer de pré-banca de 23/10/2026](https://docs.google.com/document/d/1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA/edit), achado C2 já alerta que “escaláveis” não foi demonstrado e pede confirmação do título oficial com o orientador; parecer é orientativo, não aceite.
4. [Baseline de desenvolvimento](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit), histórico ER-SIRE 2.1 e revisões posteriores preservados; [UC01–UC14](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit), seis entidades históricas não alteradas.

## Achado AUD-TIT-01

**Status: bloqueado para correção definitiva.** A presença/ausência de “Escaláveis” entre as duas fontes acadêmicas e a variação de tratamento do orientador impedem padronização automática. **Impacto:** capa, folha de rosto, título em resumo/abstract, ficha catalográfica, sumário/referências cruzadas e arquivos de entrega podem divergir. **Responsável pelo pré-requisito:** autora e orientador/secretaria acadêmica, que devem confirmar a forma registrada do título e o tratamento acadêmico correto. **Condição de retomada:** confirmação documentada do título oficial; então aplicar alteração controlada em documento vigente com histórico, preservar versões históricas e reler após salvar. Não substituir “escaláveis” por hipótese e não alegar escalabilidade testada.

**Rastreabilidade:** parecer C2 → monografia (capa/folha de rosto e resumo) ↔ modelo IFSP (capa/folha de rosto) → decisão humana pendente → revisão editorial e conferência posterior. Nenhum teste de carga ou avaliação do orientador foi realizado nesta unidade.

## Relação com a execução técnica e próximo passo

- EVO-USO-01 está sendo trabalhado em PRs #15, #20, #21, #33, #35; reconciliar esses HEADs antes de alterar templates. PR #14 é documental. Não duplicar a implementação.
- Checklist canônico ainda está em [PR #30](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/30), **não mesclada** na leitura de 20/11. Registrar AUD-TIT-01 na reconciliação do checklist, sem criar um segundo arquivo de progresso concorrente.
- Fotos reais e persistência após deploy não ficam comprovadas por PR #2 mesclada; autorização OAuth própria do aplicativo e ensaios sintéticos são gate separado.
- Próxima unidade independente: confrontar especificações textuais UC01–UC14 e modelo relacional com a seção do documento de projeto, sem renumerar baseline; preparar tabela de lacunas com evidências e não modificar a monografia antes de revisão integral.

**Evidência desta unidade:** leitura textual das três fontes e registro versionado deste achado. **Não executado:** testes Django/Playwright, CI, deploy, edição do Drive, aprovação humana e auditoria global.
