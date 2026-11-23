# SIRE — Termo de reconciliação e entrega técnica (18/11/2026)

**Status: protótipo publicado, aceite de navegador documentado com ressalvas e pacote acadêmico pronto para revisão; aprovação do orientador e persistência de fotos após redeploy no Render não comprovadas.** Autora: Julia Mianovichi. TCC de Engenharia Elétrica, IFSP Câmpus Sertãozinho. Implementação assistida por ChatGPT, Codex e Claude Code. O documento distingue explicitamente evidências executadas de condições ainda pendentes.

## 1. Versões, branches e fatos verificados

- **Demo pública**: https://sire-demo.onrender.com — Render confirmou o novo deploy **dep-dburju68bjmc739njca0** no commit **74f50c844b44d3a3d95f5afc06fdde31977cd91d** da branch `etapa/postgresql-windows` como **live** em 18/11/2026 às 11h46 (Brasília). Logs do build: `133 static files copied`, `No migrations to apply`, gunicorn iniciado e serviço live. O código de fotos, ficha e tutorial foi publicado; o comportamento de fotos na demo ainda depende do vínculo OAuth e de validação funcional.
- **Integração realizada**: PR #18 merged em 18/11/2026, merge commit **74f50c84**; a PR #18, https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/18, branch `entrega/consolidacao-final-20261118`, construída sobre o commit `82b1b97` da PR #17 e incrementada com as correções de OAuth/privacidade da PR #16. O commit `cd93a81d` é a base consolidada testada, seguida de atualizações documentais.
- **CI da base consolidada**: [Django geral](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319295069), [fotos em SQLite/PostgreSQL](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319295483), [tutorial em navegador](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319294940). Esses workflows indicaram sucesso no commit `cd93a81d`. A CI dos commits documentais posteriores deve ser conferida separadamente.
- **Drive real, fora da demo**: [relatório completo](OAUTH_EXECUCAO_REAL_2026-11-18.md) e [JSON do ensaio](../evidencias/2026-11-18_1032_drive_real/resultados.json) registram 13 de 13 verificações conformes em Windows/PostgreSQL local após OAuth `drive.file` renovado com o aplicativo Google em produção. Foi testada persistência após reiniciar **processo local**, não após deploy Render; os arquivos sintéticos de ensaio foram removidos.
- **Segredos**: grupo Render `sire-drive-oauth-36a0572f` (ID `evg-dbuq4kom7kps73d5trfg`) contém três variáveis, mas o relatório de execução afirma que ele **não estava vinculado a serviço**; não registrar valores, tokens nem chaves em Git, Drive ou impressões. As chaves temporárias de API criadas na configuração foram relatadas como revogadas.
- **Monografia atual**: https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit — seção 3.2.3 relata retorno do orientador e EVO-USO-01; subseção 3.2.3.5 registra CI e Drive real. O sumário e a lista de ilustrações foram conciliados após os testes; em 23/11/2026 houve revisão editorial e uma nova exportação de 54 páginas A4, sem folha vazia. [PDF de revisão na pasta central](https://drive.google.com/file/d/1jeciw6ftt-ESq3d6NhZYIzcawjeirhH0/view).
- **Documentação de desenvolvimento**: https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit — Apêndice A contém as especificações completas UC01–UC14. Regra de negócio de referência RN-01–RN-41: https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit

## 2. Rastreabilidade resumida e escopo

| Artefato | Requisitos e regras | Implementação | Evidência / limite |
| --- | --- | --- | --- |
| Baseline histórica | ER-SIRE 2.1, UC01–UC14, RN-01–RN-30 pertinentes | User, Agencia, PerfilUsuario, Excursao, PontoEmbarque, Reserva; Django ORM | VF01–VF16 registrados em artefatos de outubro e regressão posterior; preservar escopo histórico |
| Catálogo rosa e filtros | CAT-RF-01, CAT-RNF-01 | formulários, views e templates da branch de demonstração | PR #1 integrada; catálogo e busca observados no Render em R01 e R05 da PR #24 |
| Ficha completa | CAT-RF-02/04, UC05–UC07, RN-03/11/14 | migração 0007, formulário, detalhes, galeria | Publicada; ficha completa verificada localmente e foto existente visualizada no Render; sem upload novo na rodada final |
| Fotos | CAT-RF-03, RN-03/04/05/11 | FotoExcursao (entidade técnica nova, fora da baseline), Google Drive, proxy protegido | CI SQLite/PG e 13 verificações reais locais; sem ensaio de persistência pós-redeploy Render |
| Tutorial contextual | EVO-USO-01, retorno do orientador de 17/11 | JavaScript progressivo por perfil, botão Como usar, fechamento por Escape | Visitante em Render, Agente/Passageiro local; ressalva visual no celular; avaliação do orientador pendente |
| CPF | EVO-CPF-01, RN-04/05 | **Não implementado**; somente especificação LGPD proposta na PR #8 | não colocar nos resultados de software |
| Pagamentos, assentos, cancelamentos, favoritos, avaliações | visão evolutiva RN-31–41, backlog | **Não implementados** | proposta de trabalhos futuros, não conformidade testada |

## 3. Condições necessárias antes de declarar entrega final

1. **Segurança:** confirmar que nenhum token, segredo ou dado real foi commitado ou exposto em evidências; manter escopo `drive.file` e revogação das chaves temporárias.
2. **Integração:** a PR #18 foi integrada após CI aprovado ao commit 74f50c84; o Render confirmou o build e serviço live, sem migrations pendentes. Ainda falta validar as operações em produção (não confundir status live com aceite funcional).
3. **Drive no Render:** o responsável deve confirmar/vincular o grupo existente de segredos ao serviço de demonstração pelo painel do Render **antes** de testar upload real na demo. Não fornecer segredos no chat. Não criar recurso pago nem usar dados de passageiros reais.
4. **E2E:** repetir com identidades e imagens sintéticas: agente cadastra excursão/embarque/publica, envia foto; visitante abre, passageiro reserva, agente consulta a reserva; verificar disponibilidade e imagem depois do deploy, permissões de rascunho e remoção.
5. **Modelagem:** conferir a figura do modelo relacional presente no projeto versus entidades e relações efetivas. A lista de pendências do Visual Paradigm sobre cardinalidade Agência/PerfilUsuario ainda não foi encerrada no editor; não atribuir aceite ao diagrama sem prova.
6. **Acadêmico:** o sumário da monografia foi conciliado com os títulos e páginas após a inclusão da subseção 3.2.3.5; a exportação de 18/11/2026 ficou com 61 páginas, sem página em branco; a revisão editorial de 23/11/2026 reduziu o arquivo para 54 páginas sem retirar o conteúdo técnico essencial. Ainda é necessária revisão substantiva das fontes, figuras e conformidade ABNT. O orientador precisa confirmar o título oficial e validar o tutorial; relatos de entrevistas devem ter evidência demonstrável, sem inventar participantes nem datas.
7. **Aceite:** monografia e documentação de desenvolvimento já foram exportadas para revisão no Drive, com sumários conferidos. Ainda dependem da leitura da autora e da avaliação acadêmica; não foram enviadas ao orientador.

## 4. Limitações e condições de apresentação à banca

- O sistema do TCC é um **protótipo** multiagência, não uma operação comercial de viagens: não processa pagamentos, não escolhe poltronas e não comprova escalabilidade por testes de carga.
- O Google Drive pessoal foi uma escolha acadêmica de baixo custo; Cloudinary/R2 são melhorias futuras possíveis, não funcionalidades entregues.
- Autores de código/registro devem ser informados conforme ocorrido: IA assistiu construção, Git e verificações; autora definiu problema, requisitos, limites e avaliações. Não declarar programação manual que não ocorreu.
- Revisões realizadas em 18/11/2026: inclusão de seção de CI/Drive real na monografia e da presente reconciliação. Foi inspecionada a exportação PDF de 61 páginas A4, com 10 imagens e conferência de páginas exemplares, inclusive a Figura 4 do modelo relacional. A revisão global de cada página e de todas as referências ABNT **continua pendente de validação acadêmica integral**.

## 5. Decisão registrada

**A PR #18 foi integrada e a versão técnica foi publicada** para evitar sequência de merges de PRs antigas que têm bases divergentes. PRs #2, #7, #9, #15, #16 e #17 podem ser mantidas como histórico até confirmar que todos os diffs necessários estão nela. Não fazer deploy na demo por mera existência de CI verde se o grupo OAuth ainda não estiver vinculado e o plano de testes final não estiver concluído.

## 6. Confirmação de publicação — 18/11/2026

Render deployment `dep-dburju68bjmc739njca0`, commit `74f50c844b44d3a3d95f5afc06fdde31977cd91d`, status `live`, finalizado `2026-11-18T14:46:14Z`. Os logs do build confirmam instalação de dependências, coleta de 133 estáticos e comando de migrations executado sem atualizações pendentes. Isso não comprova testes reais de reserva, fotos ou tutorial em navegador da URL publicada. A vinculação do grupo OAuth ao serviço ainda precisa de verificação no painel. A revisão do PDF e o aceite do orientador permanecem pendentes.

## 7. Consolidação documental — 18/11/2026

A [PR #24](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/24) reuniu 32 capturas, e a [PR #28](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/28) incorporou a revisão 2 do [relatório de aceite](ACEITE_FUNCIONAL_FINAL_20261118.md), com matriz UC01–UC14 × VF01–VF16, CAT-VF e TUT-01–06. Resultado da rodada Chromium: **13 itens aprovados, três com ressalva, um bloqueado e nenhuma falha registrada**. VF01, VF02 e VF12 não foram repetidos. R01–R11 são imagens do Render público como Visitante, e L01–L21 são imagens de ambiente local isolado como Agente e Passageiro. Não confundir resultados de ambientes diferentes; a concorrência com PostgreSQL e o envio real ao Drive possuem evidências anteriores e não foram repetidos nessa rodada.

Arquivos para revisão da autora, sem envio externo:
- [Monografia PDF — 54 páginas A4](https://drive.google.com/file/d/1jeciw6ftt-ESq3d6NhZYIzcawjeirhH0/view)
- [Documentação de desenvolvimento PDF — 99 páginas A4, com Apêndice A UC01–UC14](https://drive.google.com/file/d/18VHWoS8TOXs_76lOk-3hS0cfjTRkftVh/view)
- [Relatório e 32 prints em pasta privada](https://drive.google.com/drive/folders/1ijoatraiI5seo-tVyveDX2uIuJCRcstF)
- [Índice do pacote atualizado](https://drive.google.com/file/d/1RA5TaencNLAJ6-B382KPJCpqTwoiZdeJ/view)

O vínculo entre credenciais OAuth e o serviço Render, assim como a persistência das fotos após redeploy na demo, ainda requer comprovação independente; há uma imagem previamente publicada visível. O tutorial tem ressalva visual em celular e ainda não recebeu avaliação formal do orientador. A edição nativa do modelo no Visual Paradigm e o título/folha de aprovação não tiveram confirmação institucional. **Nenhum e-mail ao professor foi enviado.**

## 8. Revisão editorial da monografia — 23/11/2026

A edição nativa da monografia foi revista sem alterações no código do SIRE e exportada novamente em **54 páginas A4**. Foram condensados trechos repetitivos, reconciliados sumário e lista de ilustrações, mantidas as Figuras 2–4 (diagramas) e uma captura da lotação, e preservadas as demais capturas de reservas e consultas na documentação de desenvolvimento e no pacote de evidências. O Quadro 1 foi movido integralmente para uma única página. A redação diferencia verificações por HTTP, suíte automatizada e ensaio concorrente PostgreSQL. A avaliação institucional e os metadados de aprovação continuam pendentes. A versão anterior de 61 páginas foi guardada como histórico no Drive: https://drive.google.com/file/d/1nnuLT6sn9s78X0f08Ox5Jxw59BaO8Vof/view . Cópia editável pré-revisão: https://docs.google.com/document/d/1FzxXKlwfAQlnSLr1JMbHgc1Ao5RwrrywzRdkf4n79WY/edit . PDF vigente: https://drive.google.com/file/d/1jeciw6ftt-ESq3d6NhZYIzcawjeirhH0/view .
