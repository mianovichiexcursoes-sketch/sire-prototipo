# Matriz de fontes oficiais e gate de integração — 22/11/2026, 15h55 BRT

**Natureza:** evidência documental incremental isolada; não é checklist canônico, implementação, teste ou aceite. Branch criada a partir de `main` para evitar editar os arquivos concorrentes do tutorial. Não modifica a demo.

## Leitura direta nesta rodada
Documentos Google Drive consultados pelo ID original e com texto retornado pela integração, não apenas por memória:
- RN-01–RN-41: [regras oficiais](https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit). RN-03/04/05 restringem isolamento, dados pessoais e papéis; RN-06–14 tratam publicação e integridade; RN-17–30 tratam reservas/capacidade/concorrência; RN-31–41 incluem visão ampliada, não autorizando implementação automática.
- [Documentação de desenvolvimento](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit): histórico ER-SIRE 2.1 preservado, com versão 2.6 datada de 12/11; sumário contém seção 4.4 modelo relacional e Apêndice A UC.
- [Guia de implementação](https://docs.google.com/document/d/1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U/edit): seis entidades de domínio/conceituais incluindo User padrão, sem coluna de disponibilidade; SQLite original e PostgreSQL como evolução.
- [Casos de uso UC01–UC14](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit): fonte consultada nesta rodada, preservar numeração.
- [Requisitos](https://docs.google.com/document/d/1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM/edit): distinguir produto e protótipo.
- [Extensão CAT](https://docs.google.com/document/d/1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is/edit): CAT-RF-01–04 e CAT-RNF-01–02 são incrementos; CAT-VF não equivale a ensaio realizado.
- [Registro técnico](https://docs.google.com/document/d/1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM/edit): UC01–UC14 vinculados a views/forms/templates e VF01–16 históricos; declara assistência de IA e diferencia HTTP de navegador.

Versão/data: somente as datas expressamente observadas acima; revisão atual do Drive não aferida por hash nesta rodada.

## Estado concorrente e impedimentos
- Consulta GitHub de PRs ordenadas por atualização mostrou #72, #70, #71 e #64, todas com trabalhos de reconciliação ou tutorial. A PR #14 permanece aberta/draft, com dependências de #15/#20/#21/#33/#35/#39 e #64. Não aplicar patches sobre o JS compartilhado sem reconciliação.
- `docs/PROGRESSO_TCC_FINAL.md` retornou **404 na branch padrão main** nesta rodada. O checklist existe em branches/PRs documentais concorrentes conforme #70/#71; não criar outro concorrente e não afirmar que o checklist canônico foi atualizado.
- OAuth `drive.file` próprio do aplicativo e credenciais seguras no Render: não comprovados nesta rodada; não testar integração real de fotos nem afirmar persistência pós-deploy.
- Nenhum teste Django, PostgreSQL, Chromium, CI ou deploy executado nesta unidade. Nenhum dado real ou credencial utilizado.

## Matriz mínima de rastreabilidade / próximas verificações

| Referência | Arquivo/área a conferir (não alterado aqui) | Verificação necessária | Evidência atual | Monografia |
| --- | --- | --- | --- | --- |
| RN-03–05; UC06–09,13–14 | sire/views.py; forms.py; models.py | acesso cruzado entre agências, perfis e URLs diretas | VF históricos no registro; regressão atual pendente | requisitos, modelagem, resultados |
| RN-17–30; UC10–12 | models.py; views.py; reserva e embarque | última vaga concorrente, ponto de outra excursão, isolamento | VF históricos; suíte atual pendente | verificação e limitações |
| CAT-RF-01–04 | catálogo/ficha, fotos e migrations | filtros, até 6 fotos, upload/exclusão, migração aditiva | especificação lida; testes atuais pendentes | evolução da espiral |
| EVO-USO-01 / TUT | tutorial-uso.js; base.html; CSS; testes browser | perfis, alvo visível, Escape/Fechar/Pular, 320/375px, não enviar forms | PRs concorrentes; integração e avaliação pendentes | metodologia, resultados e apêndice |
| ER-SIRE 2.1 / UC01–14 | docs de baseline e modelos atuais | comparar modelo relacional com código sem reescrever baseline | documentação lida; conferência código atual pendente | seção 4 e apêndice |

## Próxima ação
Reconciliar as PRs de tutorial e checklist por ancestralidade e HEAD, executar testes reais com dados sintéticos, então atualizar o checklist canônico em sua branch vencedora e registrar os resultados verificados. Esta entrega documental não deve ser mesclada automaticamente. Revisão humana e avaliação do orientador permanecem pendentes.
