# Auditoria pontual — identificação acadêmica e título (21/11/2026)

**Natureza:** confronto textual de documentos originais do Drive; não é revisão ABNT integral nem aprovação do orientador. Nenhuma edição foi feita nos originais.

## Fontes lidas diretamente por ID
- Monografia principal, ID `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg`, conteúdo textual retornado com 101657 caracteres nesta consulta; data de modificação não aferida.
- Modelo de relatório PFC 12/2025, ID `1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo`, conteúdo textual retornado com 84437 caracteres; vigência do modelo não confirmada.
- Parecer pré-banca 23/10/2026, ID `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA`, conteúdo textual retornado com 16962 caracteres.
- Gate técnico desta rodada: RN `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`, baseline `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`, guia `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`, UC `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`, requisitos `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`, CAT `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`, registro `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`.

## Divergências verificadas
| ID | Documento e evidência literal breve | Achado | Estado / ação |
|---|---|---|---|
| TIT-01 | Monografia, folha inicial: `PROJETO DE ARQUITETURA DE SOFTWARE APLICADO AO TURISMO RODOVIÁRIO`; subtítulo `ENGENHARIA DE REQUISITOS PARA PLATAFORMAS DE LOGÍSTICA DE LAZER` | Modelo PFC traz subtítulo diferente: `Engenharia de Requisitos para Plataformas Escaláveis de Logística de Lazer`. A palavra **Escaláveis** implica afirmação potencialmente mais forte que a evidência de protótipo | **Bloqueado para alteração**: confirmar título/subtítulo oficial com orientador; responsável autora/orientador. Não substituir silenciosamente |
| TIT-02 | Monografia: `Orientador: Professor Rodrigo Pantoni`; modelo PFC: `Orientador: Prof. Dr.Rodrigo Pantoni` | Divergência na forma de qualificação e espaço após `Dr.` | **Pendente**: validar titulação e forma institucional; corrigir apenas após confirmação |
| TIT-03 | Parecer pré-banca: risco de promessas não testadas pelo título e divergências entre documentos | Reforça necessidade de separar arquitetura projetada de funcionalidades e desempenho efetivamente verificados | **Pendente**: revisão narrativa integral e confronto com código, logs e avaliação |

## Limites da evidência
A presença textual de RESUMO, ABSTRACT, REFERÊNCIAS ou APÊNDICE não comprova sua qualidade, paginação, completude ou formatação. A leitura de texto não verifica margens, sumário automático, imagens e estilos. Nenhum teste Django, PostgreSQL, navegador, deploy, OAuth ou aceite humano foi executado nesta unidade. Baseline ER-SIRE 2.1, UC01–UC14 e seis entidades originais não foram alterados.

## Próxima unidade independente
Auditar uma seção substantiva da monografia contra fontes e código (metodologia espiral, alegações de testes e autoria assistida por IA), registrando citações e correções propostas sem fabricar resultados. Em paralelo, conciliar tutorial PRs e executar TUT em árvore isolada. Não fazer merge/deploy antes dos gates.