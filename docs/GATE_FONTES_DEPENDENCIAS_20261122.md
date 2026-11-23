# Gate de fontes e dependências — 22/11/2026 (rodada independente)

> Documento de auditoria incremental, **não** substitui o checklist canônico docs/PROGRESSO_TCC_FINAL.md. Não altera baseline ER-SIRE 2.1, UC01–UC14 nem entidades históricas. Sem merge/deploy.

## Leitura direta de fontes oficiais nesta rodada

Consulta pela API Google Docs, por ID exato, com leitura dos trechos iniciais e identificação de revisões. A leitura integral de cada documento **não** foi concluída nesta rodada; logo nenhuma implementação, teste conclusivo ou revisão da monografia é autorizada com base apenas neste registro.

| Fonte | ID | Revisão observada (prefixo) | Situação |
|---|---|---|---|
| RN-01–RN-41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | AHj4eMQguVGb | acessível; leitura parcial |
| Desenvolvimento ER-SIRE | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | AHj4eMTd3MUu | acessível; leitura parcial |
| Guia protótipo | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | AHj4eMQaNMjG | acessível; leitura parcial |
| UC01–UC14 | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | AHj4eMR9ieGd | acessível; leitura parcial |
| Requisitos | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | AHj4eMTi8Nvi | acessível; leitura parcial |
| Catálogo e ficha | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | AHj4eMTSU0RT | acessível; leitura parcial |
| Registro implementação | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | AHj4eMR_QOz9 | acessível; leitura parcial |

## Concorrência verificada

GitHub retornou branches de tutorial existentes: feat/evo-uso-01-tutorial-20261118, fix/tutorial-fechar-acessibilidade-20261119, fix/tutorial-mobile-viewport-20261119 e test/tutorial-storage-indisponivel-20261120. Portanto **não duplicar** implementação do tutorial sem conferir seus diffs, PRs e testes. docs/PLANO_ESPIRAL_TUTORIAL_20261118.md foi lido na branch docs/retorno-orientador-tutorial-20261118; registra a decisão de tutorial interativo em lugar de vídeo. A tentativa de ler docs/PROGRESSO_TCC_FINAL.md no ref padrão retornou 404; verificar em outras branches antes de criar/substituir checklist canônico.

## Status e dependências

| Item | Status | Evidência | Próxima ação |
|---|---|---|---|
| EVO-USO-01 | em execução em branches existentes; **não verificado** | branches listadas acima e plano no GitHub | conferir PR, HEAD, testes e fluxos antes de tocar templates |
| A ficha/fotos | pendente de reconciliação | PR #2 informada pela autora; não inspecionada integralmente nesta rodada | inspecionar diff, migração 0007, testes e CI |
| B OAuth Drive | bloqueado para validação real | nenhuma autorização OAuth Django verificada nesta rodada | titular autorizar aplicativo e configurar segredos fora do repositório; só então testar |
| C–F | pendente | sem testes executados nesta rodada | leitura das seções pertinentes e inspeção dos branches antes de implementar |
| G auditoria global | pendente | fontes principais acessíveis parcialmente; monografia não lida | inventário completo, leitura integral, rastreabilidade e revisão documentada |

**Regra de desbloqueio:** a ausência de OAuth não impede UX/tutorial/documentação local, mas não autoriza afirmar persistência de fotos no Drive. A leitura parcial de fonte oficial impede alterações dependentes até leitura pertinente. Nenhum teste, deploy ou aceite foi executado nesta rodada.

## Próxima unidade independente

Verificar branches/PRs do tutorial, comparar contra a branch de demonstração e ler integralmente seções pertinentes de RN/UC/guia. Se o tutorial já estiver implementado, priorizar evidência independente de acessibilidade/teclado/armazenamento indisponível em branch isolada; se não, implementar somente lacuna demonstrada. Atualizar checklist canônico existente após localizar seu ref correto. Preservar demo.
