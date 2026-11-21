# Auditoria de gates de integração — 21/11/2026, 02h BRT

## Fontes consultadas nesta unidade
Leitura direta dos documentos Google por IDs: RN-01–RN-41 (especialmente RN-01–05, 06–16), documentação de desenvolvimento (baseline ER-SIRE 2.1, histórico até 2.6), guia de implementação, UC01–UC14, requisitos v3.0, especificação CAT rev. 0.2 e registro de implementação. Esta auditoria não substitui a leitura integral da monografia nem constitui teste.

## Constatação verificável
- [PR #2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2): **merged** em 18/11/2026 às 14:05:15 UTC, merge SHA `72a488beb518b4dcca275970afb81892b97f3d4b`. Sua descrição ainda diz 'implementação em branch isolada' e que falta OAuth do aplicativo. A mesclagem é um fato; não demonstra que fotos funcionem na demo nem que o Render tenha recebido deploy.
- [PR #15](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/15): **open/draft**, HEAD `3f4549bfba35411b6e02918a8cfd6a1f6f4111d6`; implementação inicial do tutorial já existe. Sua descrição exige conciliação com #20/#21/#33 antes de integrar.
- [PR #56](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/56): **open/draft**, HEAD `817e8f27d5620cd7b583c8fb7787fabf8f632fa6`, matriz TUT documental. Esta branch parte desse HEAD, sem editar templates ou migrations.

## Gates e condições de retomada
| Item | Estado | Impacto | Pré-requisito e responsável | Evidência necessária / próxima ação |
|---|---|---|---|---|
| CAT fotos, RN-03–05 | **pendente de aceite** | Risco de exposição interagências e perda de mídia | Desenvolvimento: revisão de autorização e regressão em banco isolado | Testes com duas agências sintéticas, até seis fotos, exclusão e migração aditiva 0007; logs + SHA |
| OAuth Django `drive.file` | **bloqueado para aceite real** | Sem comprovação de upload/exclusão e persistência após deploy | Titular do aplicativo e Render: autorização OAuth própria, variáveis seguras e ambiente de ensaio | Confirmar configuração sem publicar segredos; ensaio real com imagens sintéticas e persistência após redeploy |
| EVO-USO-01 | **em execução** | Não há aceite do orientador nem regressão confirmada nesta unidade | Desenvolvimento: conciliar #15/#20/#21/#33/#35/#39/#53/#54 | Executar TUT-01–09 com navegador e regressões Django; pedir avaliação do orientador por intermédio da autora |
| Auditoria acadêmica | **pendente** | TCC não pode ser declarado finalizado | Autora/desenvolvimento: monografia integral, modelo IFSP, anexos e título oficial | Inventário e relatório de divergências com correções verificadas; título validado com orientador |

## Rastreabilidade mínima
RN-03–05 / CAT-RF fotos → modelos, views, migration 0007 (revisão pendente) → CAT-VF e isolamento interagências (não reexecutados) → especificação CAT e seção de resultados da monografia (não auditada). EVO-USO-01 → PR #15 e PRs dependentes → TUT-01–09 (não reexecutados) → avaliação da volta da espiral (pendente). UC01–UC14 e seis entidades permanecem baseline histórica.

**Não executado nesta unidade:** suíte Django, SQLite/PostgreSQL, Playwright, testes reais de fotos, deploy, merge, edição de monografia ou avaliação humana. Não afirmar êxito desses itens. A próxima unidade elegível é conciliação técnica dos PRs de tutorial e execução de testes em ambiente isolado; OAuth não bloqueia esse trabalho.
