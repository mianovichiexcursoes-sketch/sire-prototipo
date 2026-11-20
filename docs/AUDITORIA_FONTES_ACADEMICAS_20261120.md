# Auditoria pontual de fontes acadêmicas — 20/11/2026

> Escopo: conferência documental por IDs exatos; não é auditoria integral da monografia nem aceite de banca. Nenhum código, banco, migração ou deploy foi alterado.

| Fonte | ID | Última modificação informada pelo Drive | Achado verificável | Próxima ação |
|---|---|---|---|---|
| Monografia principal | `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg` | 18/11/2026 | Capa usa título principal **Projeto de Arquitetura de Software Aplicado ao Turismo Rodoviário** e subtítulo **Engenharia de Requisitos para Plataformas de Logística de Lazer**; orientador indicado como Professor Rodrigo Pantoni | Conferir título/subtítulo oficiais com orientador antes de qualquer alteração |
| Modelo PFC IFSP (dez/2025) | `1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo` | 30/06/2026 | Modelo contém título ampliado com **Plataformas Escaláveis de Logística de Lazer**, diferente da capa da monografia; identifica Prof. Dr. Rodrigo Pantoni | Tratar como divergência editorial, não como autorização para alegar escalabilidade |
| Regulamento PFC Engenharia Elétrica (mar/2026) | `1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL` | 28/09/2026 | Documento acessível; capítulo inicial define PFC como atividade obrigatória | Conferir capítulos de apresentação, avaliação e entrega antes de declarar conformidade |
| Parecer pré-banca 23/10/2026 | `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA` | 23/10/2026 | Aponta contradições entre documentos, UML versus código, promessas do título e necessidade de transparência sobre auxílio de IA | Criar matriz de divergências por seção e registrar correções sem reescrever histórico |
| PROMPS TCC (histórico) | `1mpNI5u26q3NzVgXFeeMCHZgfWdxCgsG-WTangQWVRrE` | 28/09/2026 | Contém título ampliado e orientações históricas, não substitui especificações oficiais | Classificar como histórico e confrontar com fontes vigentes |

## Gate de rastreabilidade

Foram também acessadas diretamente nesta rodada as fontes RN-01–41, baseline de desenvolvimento ER-SIRE 2.1, guia de implementação, UC01–UC14, requisitos v3, complemento CAT rev. 0.2 e registro técnico. A leitura dos trechos iniciais e identificação das fontes **não equivale à auditoria integral de seus conteúdos**.

- **EVO-USO-01**: a PR #15 implementa tutorial em branch própria; PR #53 contém contrato estático móvel, mas declara testes não executados por falha DNS. Nenhum resultado de navegador ou CI foi inferido.
- **A**: PR #2 fechada e mesclada; fotos reais continuam dependentes de autorização OAuth própria do Django e verificação no ambiente.
- **B**: bloqueado por OAuth `drive.file` e configuração segura no Render. Responsável: autora/operador autorizado. Condição de retomada: autorização e evidência de configuração sem revelar segredos.
- **G**: auditoria global da pasta e da monografia completa permanece pendente. Esta unidade apenas registra divergências verificadas de capa/modelo e alertas do parecer.
- **Integridade**: não alterar baseline ER-SIRE 2.1, seis entidades ou UC01–UC14; não tratar escopo ampliado como implementado.

## Evidências

Fontes primárias: [monografia](https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit), [modelo IFSP](https://docs.google.com/document/d/1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo/edit), [regulamento](https://drive.google.com/file/d/1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL/view), [parecer](https://docs.google.com/document/d/1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA/edit), [histórico](https://docs.google.com/document/d/1mpNI5u26q3NzVgXFeeMCHZgfWdxCgsG-WTangQWVRrE/edit). PRs [#2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2), [#15](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/15), [#53](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/53).

**Próxima unidade independente**: inventariar todos os arquivos da pasta TCC JULIA — SIRE e criar tabela documento → versão → status → divergência → correção → evidência; depois auditoria seção a seção da monografia. Não reivindicar revisão completa, testes ou aceite humano.
