# EVO-USO-01 — gate de integração do tutorial (19/11/2026)

**Tipo:** auditoria de dependências; não é teste nem aceite. Base de comparação: demo `etapa/postgresql-windows`. Nenhuma alteração de modelos, migrações, templates, dados ou deploy nesta unidade.

## Fontes oficiais lidas diretamente por ID em 19/11

- RN-01–41: `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` (RN-03/04/05, RN-06–14, RN-17–30 e visão futura RN-31–41).
- Baseline ER-SIRE 2.1 e histórico até 2.6: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`.
- Guia: `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`.
- UC01–UC14: `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`.
- Requisitos, escopo protótipo: `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`.
- CAT revisão 0.2: `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`.
- Registro técnico: `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`.

## Estado observado via GitHub nesta rodada

| Unidade | Estado GitHub | Evidência | Dependência / próxima ação |
|---|---|---|---|
| A — ficha/fotos | PR #2 mesclada | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2 | Merge não comprova fotos persistentes; exigir OAuth da aplicação e teste de upload/exclusão/pós-deploy |
| Tutorial inicial | PR #15 aberta, sem merge | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/15 | Não editar branch compartilhada; conferir diff com correções seguintes |
| Testes Chromium isolados | PR #21 aberta | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/21 | Executar e conferir resultados CI; suíte isolada não substitui navegador integrado |
| Correção Fechar | PR #33 aberta | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/33 | Confirmar Anterior/Próximo/Pular/Fechar e foco após reconciliação |
| Roteiro TUT-01–09 | PR #34 aberta | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/34 | Usar matriz para executar casos reais, não marcar aprovado só pela existência do roteiro |
| Ajuste celular | PR #35 aberta | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/35 | Retestar 320px e 375×812, foco, teclado e sobreposição antes do merge |
| Checklist central | PR #30 aberta | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/30 | Reconciliar com checklist existente antes de integrar; evitar dois registros canônicos |
| Aceite documental | PR #28 mesclada | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/28 | Evidências devem ser relacionadas à versão exata, sem inferir aceite do tutorial |

## Ordem segura de integração (proposta, ainda não executada)

1. Identificar HEAD SHA e arquivos alterados em #15, #21, #33 e #35; comparar os templates e CSS compartilhados. Não presumir que PRs independentes sejam cumulativas ou aplicáveis sem conflitos.
2. Preparar branch de integração a partir da base correta, incorporando somente correções reconciliadas. Preservar a demo aprovada.
3. Executar `manage.py check`, migrations check e testes Django em SQLite/PostgreSQL disponíveis, com saídas e SHA registrados. Depois executar TUT-01–09 em navegador real, por perfil, incluindo Escape, foco, ausência de alvo, armazenamento indisponível, celular e nenhum POST involuntário.
4. Registrar evidências verificáveis (comandos, ambiente, resultados, prints, SHA, limitações), atualizar checklist único e PR de integração. Só propor merge/deploy após aprovação humana e testes suficientes.
5. Para Quadrante IV, solicitar avaliação do orientador por intermédio da autora; nenhuma aprovação foi observada nesta rodada.

## Dependências e bloqueios

- **OAuth Google Drive:** bloqueado para ensaio real enquanto não houver autorização própria do Django e credenciais seguras no Render; responsável: autora/operador da conta Google Cloud e Render. Não bloqueia tutorial independente. Retomar após prova de autenticação do aplicativo, sem expor segredos.
- **Tutorial:** implementação e correções existem em PRs abertas distintas, mas a integração e os testes integrados não foram confirmados nesta rodada. Responsável técnico: agente integrador após conciliação; revisão humana da autora antes da demo.
- **Evidências:** esta unidade realizou leitura das fontes e consulta de estado das PRs, não executou suíte, navegador, deploy ou avaliação do orientador.

## Rastreabilidade incremental

| ID | Fonte | Artefato | Cenário necessário | Evidência atual | Seção acadêmica |
|---|---|---|---|---|---|
| EVO-USO-01 / TUT-01–09 | decisão autora 18/11, UC01–14, RN-03–05 | PRs #15/#21/#33/#34/#35 | perfil, navegação, foco, celular, storage e ausência de POST | PRs e roteiro; teste integrado pendente | iteração espiral adicional, resultados e limitações |
| CAT-RF-03 | CAT revisão 0.2 | PR #2 | upload/exclusão/persistência após deploy | merge observado; aceite real não inferido | evolução CAT e riscos |
| RN-17–30 / UC10–14 | regras e casos oficiais | fluxo histórico de reserva | vagas, embarque, isolamento | regressão nesta rodada não executada | verificação funcional |

**Preservação:** ER-SIRE 2.1, UC01–UC14 e seis entidades históricas não foram alteradas. Não foram usados CPFs/fotos reais nem alterados pagamentos ou assentos.
