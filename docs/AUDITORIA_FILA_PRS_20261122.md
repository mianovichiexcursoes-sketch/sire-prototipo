# Auditoria de fila de PRs — 22/11/2026

**Natureza:** inventário de integração, sem alteração de protótipo, banco, demo ou monografia. **Estado:** revisão humana pendente. Fonte: consulta direta à API GitHub em 22/11/2026 e leitura direta dos documentos oficiais RN, baseline, guia, UC, requisitos, CAT e registro por seus IDs.

## Constatações verificadas

- PR #2 está **merged** em 18/11/2026, commit de merge `72a488beb518b4dcca275970afb81892b97f3d4b`; isso **não comprova** OAuth do Django nem persistência real de fotos.
- PR #14 está **open/draft**, documentação do retorno do orientador; a decisão vigente é tutorial interativo, não vídeo.
- Consulta de PRs abertas retornou múltiplas implementações e correções concorrentes do tutorial: #15, #20, #33, #35, #64; testes isolados #21, #39, #42, #53, #54; documentação e checklists paralelos #30, #66, #68. Nenhum desses resultados comprova integração ou aceite.
- Há várias PRs documentais com escopo sobreposto (#31, #34, #36, #47, #56, #58, #62, #63, #65). **Não mesclar em lote** nem declarar que uma substitui outra sem comparar diffs.

## Dependências e próxima unidade executável

| Item | Estado | Evidência | Próxima ação |
| --- | --- | --- | --- |
| EVO-USO-01 código | Em execução, integração não comprovada | PRs #15/#20/#33/#35/#64 | Obter diffs e HEADs atuais, consolidar em branch de integração isolada; preservar autoria e não sobrescrever templates concorrentes |
| EVO-USO-01 testes | Pendente | PRs #21/#39/#42/#53/#54 | Rodar suíte Django e Playwright no HEAD **integrado**, registrar logs e SHA; teclado/Escape, 320px, perfis, não submissão |
| Checklist canônico | Pendente de reconciliação | PRs #30/#66 | Comparar conteúdo e selecionar atualização incremental de `docs/PROGRESSO_TCC_FINAL.md` sem substituir histórico |
| Fotos/Drive | Bloqueado para aceite real | PR #2 merged; OAuth de aplicativo não comprovado | Autora provisiona OAuth `drive.file` e segredos no Render, sem expô-los; depois testar upload, exclusão e persistência |
| Avaliação acadêmica | Pendente | feedback de 17/11 registrado em #14 | Após integração e testes, autora solicita nova tentativa ao orientador; não inventar avaliação |

## Gate de fonte e fronteira histórica

Documentos consultados diretamente nesta rodada: RN-01–41 (`1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`); desenvolvimento baseline (`19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`, histórico 2.6 de 12/11); guia (`1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`); UC01–UC14 (`1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`); requisitos 3.0 (`1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`); CAT (`1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`); registro (`1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`).

Preservar baseline ER-SIRE 2.1, seis entidades e UC01–UC14. O tutorial é EVO-USO-01, não renumeração da terceira iteração técnica. RN-31–41 não autoriza implementar pagamentos/assentos no protótipo.

## Limitações desta rodada

Sem clone local: `git ls-remote` falhou por DNS (`Could not resolve host: github.com`) no ambiente de execução. Consulta da API GitHub pelo conector funcionou. **Não foram executados testes, merge, deploy, revisão visual nem validação do OAuth.** Este documento não substitui checklist canônico nem demonstra conclusão funcional.
