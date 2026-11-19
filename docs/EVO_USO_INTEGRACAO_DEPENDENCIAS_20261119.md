# EVO-USO-01 — reconciliação executável e gates (19/11/2026)

## Proveniência e escopo
Leitura direta em 19/11 das fontes originais: RN-01–41 (1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0), baseline ER-SIRE 2.1 (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8), guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U), UC01–14 (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY), requisitos v3 (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM), CAT revisão 0.2 (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is) e registro técnico (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM). Baseline histórica, seis entidades e UC01–UC14 não são alteradas aqui.

## Dependências verificadas por HEAD de PR
| Unidade | HEAD observado | Base | Estado | Próxima ação |
|---|---|---|---|---|
| Tutorial #15 | 3f4549bfba35411b6e02918a8cfd6a1f6f4111d6 | etapa/postgresql-windows | Implementação proposta | Usar como ancestral, não reaplicar manualmente |
| Acessibilidade #20 | 63f341ab9769436c252c5cf71151a976ea9498ec | feat/evo-uso-01-tutorial-20261118 | Proposta | Verificar alterações por perfil e foco |
| Browser #21 | f977ab8e33173fc21ee8b29d5eb03ab8d74c8ed4 | fix/evo-uso-01-acessibilidade-20261118 | Testes escritos; execução não comprovada nesta rodada | Executar suíte no HEAD integrado |
| Fechar #33 | 8bd96705e19afc0b5d0a89671270ae8232bbf175 | etapa/postgresql-windows | Implementação paralela | Comparar JS com #20, evitar substituição |
| Móvel #35 | bf917708f09d01befb8c7576dfc43d9d2a1e8158 | fix/tutorial-fechar-acessibilidade-20261119 | CSS proposto, sem reteste visual | Revalidar rodapé em 320px/375×812 |
| Contrato #39 | 387317168f250ef3beb66a84385322a620b9b8a5 | fix/tutorial-mobile-viewport-20261119 | Teste estático escrito, não executado | Rodar unittest e verificar falhas |

**Dois ramos paralelos**: #15 → #20 → #21 e #33 → #35 → #39. A segunda cadeia NÃO inclui automaticamente #20/#21. Não mesclar #21 e #39 como se fossem versões independentes completas. Resolver diferenças de `sire/static/sire/js/tutorial-uso.js` e `sire/templates/sire/base.html` por comparação de patches e testes, preservando controles Fechar e melhorias de acessibilidade.

## Gates de execução e evidência
1. **Pendente** — integrar em branch nova e isolada, sem modificar demo; registrar SHA exato do HEAD combinado e conflitos resolvidos.
2. **Pendente** — `python -m unittest discover -s tests -p 'test_tutorial_contract.py' -v` (contrato estático; não valida navegador).
3. **Pendente** — `python -m unittest discover -s tests -p 'test_tutorial_browser.py' -v` com dependências Chromium, registrar saída, duração e ambiente; conferir TUT-01–09 e não submissão.
4. **Pendente** — testes Django/SQLite e PostgreSQL autorizado, migrações e regressões UC/CAT; verificar separação de papéis.
5. **Pendente** — captura real 320px, 375×812, desktop, teclado, Escape, foco, alvo ausente e armazenamento bloqueado. Correção CSS não é aceite.
6. **Bloqueado (responsável: autora/operadora)** — OAuth `drive.file` do aplicativo Django e segredos seguros no Render; pré-requisito para testar persistência real das fotos, não para tutorial. Retomar após autorização verificável.
7. **Bloqueado (responsável: autora/orientador)** — avaliação de usabilidade e autorização de publicação; requer versão testada. Não atribuir aceite antecipado.

## Rastreabilidade mínima
| ID | Fonte | Artefato | Verificação pendente | Monografia |
|---|---|---|---|---|
| EVO-USO-01 / TUT-01–09 | Feedback 17/11 e decisão 18/11, UC01–14 | JS tutorial, base.html, PRs #15/#20/#21/#33/#35/#39 | Navegador, teclado, perfis, viewport, ausência de escrita | Metodologia espiral, resultados e limitações (ainda não atualizados aqui) |
| RN-01–05 | Regras oficiais | Controle de papéis existente; tutorial só apresenta ações do perfil | Regressão autorização entre agências | Rastreabilidade/segurança |
| RN-17–30 | Regras oficiais | Reserva existente; tutorial não envia formulário | Confirmar nenhuma reserva involuntária | Casos de uso/resultados |
| CAT-VF01–06 | CAT rev. 0.2 | Incremento ficha/fotos PR #2 | Upload/exclusão e persistência pós-deploy somente com OAuth válido | Evoluções e limitações |

## Limitações desta entrega
Esta unidade é reconciliação documental baseada em leitura das fontes e dos metadados/diffs das PRs. A tentativa de acesso Git remoto no ambiente de execução falhou por DNS (`Could not resolve host: github.com`); não foram executados testes locais, CI, merge, deploy ou ensaios visuais. A leitura por conector GitHub não representa acesso ao diretório local de outro agente. Checklist canônico `docs/PROGRESSO_TCC_FINAL.md` não foi sobrescrito porque está ausente na branch padrão consultada e existe em múltiplas PRs concorrentes (#15/#30/#31/#37); consolidar após integração, preservando históricos.
