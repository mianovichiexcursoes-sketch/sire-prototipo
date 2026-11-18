# SIRE — Termo de reconciliação e entrega técnica (18/11/2026)

**Status: publicação técnica confirmada no Render e CI aprovado; aceites funcionais de fotos no Render e conferência acadêmica final pendentes.** Autora: Julia Mianovichi. TCC de Engenharia Elétrica, IFSP Câmpus Sertãozinho. Implementação assistida por ChatGPT, Codex e Claude Code. O documento distingue explicitamente evidências executadas de condições ainda pendentes.

## 1. Versões, branches e fatos verificados

- **Demo pública**: https://sire-demo.onrender.com — Render confirmou o novo deploy **dep-dburju68bjmc739njca0** no commit **74f50c844b44d3a3d95f5afc06fdde31977cd91d** da branch `etapa/postgresql-windows` como **live** em 18/11/2026 às 11h46 (Brasília). Logs do build: `133 static files copied`, `No migrations to apply`, gunicorn iniciado e serviço live. O código de fotos, ficha e tutorial foi publicado; o comportamento de fotos na demo ainda depende do vínculo OAuth e de validação funcional.
- **Integração realizada**: PR #18 merged em 18/11/2026, merge commit **74f50c84**; a PR #18, https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/18, branch `entrega/consolidacao-final-20261118`, construída sobre o commit `82b1b97` da PR #17 e incrementada com as correções de OAuth/privacidade da PR #16. O commit `cd93a81d` é a base consolidada testada, seguida de atualizações documentais.
- **CI da base consolidada**: [Django geral](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319295069), [fotos em SQLite/PostgreSQL](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319295483), [tutorial em navegador](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319294940). Esses workflows indicaram sucesso no commit `cd93a81d`. A CI dos commits documentais posteriores deve ser conferida separadamente.
- **Drive real, fora da demo**: [relatório completo](OAUTH_EXECUCAO_REAL_2026-11-18.md) e [JSON do ensaio](../evidencias/2026-11-18_1032_drive_real/resultados.json) registram 13 de 13 verificações conformes em Windows/PostgreSQL local após OAuth `drive.file` renovado com o aplicativo Google em produção. Foi testada persistência após reiniciar **processo local**, não após deploy Render; os arquivos sintéticos de ensaio foram removidos.
- **Segredos**: grupo Render `sire-drive-oauth-36a0572f` (ID `evg-dbuq4kom7kps73d5trfg`) contém três variáveis, mas o relatório de execução afirma que ele **não estava vinculado a serviço**; não registrar valores, tokens nem chaves em Git, Drive ou impressões. As chaves temporárias de API criadas na configuração foram relatadas como revogadas.
- **Monografia atual**: https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit — seção 3.2.3 relata retorno do orientador e EVO-USO-01; subseção 3.2.3.5 registra CI e Drive real. O sumário (páginas impressas 10–58) foi reconciliado após edição; exportação A4 revista em 60 páginas, sem folha vazia. [PDF de revisão na pasta central](https://drive.google.com/file/d/1jeciw6ftt-ESq3d6NhZYIzcawjeirhH0/view).
- **Documentação de desenvolvimento**: https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit — Apêndice A contém as especificações completas UC01–UC14. Regras de negócio da baseline: RN001–RN014, seção 3.4 desse documento. O documento separado "Regras de Negócio do SIRE" (https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit) é o catálogo ampliado RN-01–RN-41 da visão do produto completo, com numeração própria; ver docs/RASTREABILIDADE.md

## 2. Rastreabilidade resumida e escopo

| Artefato | Requisitos e regras | Implementação | Evidência / limite |
| --- | --- | --- | --- |
| Baseline histórica | ER-SIRE 2.1, UC01–UC14, RN001–RN014 | User, Agencia, PerfilUsuario, Excursao, PontoEmbarque, Reserva; Django ORM | VF01–VF16 registrados em artefatos de outubro e regressão posterior; preservar escopo histórico |
| Catálogo rosa e filtros | CAT-RF-01, CAT-RNF-01 | formulários, views e templates da branch de demonstração | PR #1 merged, commit 7c531342 live no Render |
| Ficha completa | CAT-RF-02/04 (estendem RF008/RF009), UC05–UC07, RN003, RN005 | migração 0007, formulário, detalhes, galeria | CI e testes locais; versão pública com ficha ampliada pendente |
| Fotos | CAT-RF-03, RN003, RN005, RNF001–RNF002 | FotoExcursao (entidade técnica nova, fora da baseline), Google Drive, proxy protegido | CI SQLite/PG e 13 verificações reais locais; sem ensaio de persistência pós-redeploy Render |
| Tutorial contextual | EVO-USO-01, retorno do orientador de 17/11 | JavaScript progressivo por perfil, botão Como usar, fechamento por Escape | Workflow de navegador aprovado; ainda falta avaliação da interface publicada pelo orientador |
| CPF | EVO-CPF-01, RNF002 (catálogo ampliado: RN-04/05) | **Não implementado**; somente especificação LGPD proposta na PR #8 | não colocar nos resultados de software |
| Pagamentos, assentos, cancelamentos, favoritos, avaliações | RF022 e catálogo ampliado RN-31–RN-41 (produto completo), backlog | **Não implementados** | proposta de trabalhos futuros, não conformidade testada |

## 3. Condições necessárias antes de declarar entrega final

1. **Segurança:** confirmar que nenhum token, segredo ou dado real foi commitado ou exposto em evidências; manter escopo `drive.file` e revogação das chaves temporárias.
2. **Integração:** a PR #18 foi integrada após CI aprovado ao commit 74f50c84; o Render confirmou o build e serviço live, sem migrations pendentes. Ainda falta validar as operações em produção (não confundir status live com aceite funcional).
3. **Drive no Render:** o responsável deve confirmar/vincular o grupo existente de segredos ao serviço de demonstração pelo painel do Render **antes** de testar upload real na demo. Não fornecer segredos no chat. Não criar recurso pago nem usar dados de passageiros reais.
4. **E2E:** repetir com identidades e imagens sintéticas: agente cadastra excursão/embarque/publica, envia foto; visitante abre, passageiro reserva, agente consulta a reserva; verificar disponibilidade e imagem depois do deploy, permissões de rascunho e remoção.
5. **Modelagem:** conferir a figura do modelo relacional presente no projeto versus entidades e relações efetivas. A lista de pendências do Visual Paradigm sobre cardinalidade Agência/PerfilUsuario ainda não foi encerrada no editor; não atribuir aceite ao diagrama sem prova.
6. **Acadêmico:** o sumário da monografia foi conciliado com os títulos e páginas após a inclusão da subseção 3.2.3.5; a exportação A4 voltou a 60 páginas, sem página em branco. Ainda é necessária revisão substantiva das fontes, figuras e conformidade ABNT. O orientador precisa confirmar o título oficial e validar o tutorial; relatos de entrevistas devem ter evidência demonstrável, sem inventar participantes nem datas.
7. **Aceite:** só então exportar PDF final da monografia e cópia dos documentos na pasta central do Drive, em revisão pela autora e orientador.

## 4. Limitações e condições de apresentação à banca

- O sistema do TCC é um **protótipo** multiagência, não uma operação comercial de viagens: não processa pagamentos, não escolhe poltronas e não comprova escalabilidade por testes de carga.
- O Google Drive pessoal foi uma escolha acadêmica de baixo custo; Cloudinary/R2 são melhorias futuras possíveis, não funcionalidades entregues.
- Autores de código/registro devem ser informados conforme ocorrido: IA assistiu construção, Git e verificações; autora definiu problema, requisitos, limites e avaliações. Não declarar programação manual que não ocorreu.
- Revisões realizadas em 18/11/2026: inclusão de seção de CI/Drive real na monografia e da presente reconciliação. Foi inspecionada a exportação PDF de 60 páginas A4, com 10 imagens e conferência de páginas exemplares, inclusive a Figura 4 do modelo relacional. A revisão global de cada página e de todas as referências ABNT **continua pendente de validação acadêmica integral**.

## 5. Decisão registrada

**A PR #18 foi integrada e a versão técnica foi publicada** para evitar sequência de merges de PRs antigas que têm bases divergentes. PRs #2, #7, #9, #15, #16 e #17 podem ser mantidas como histórico até confirmar que todos os diffs necessários estão nela. Não fazer deploy na demo por mera existência de CI verde se o grupo OAuth ainda não estiver vinculado e o plano de testes final não estiver concluído.

## 6. Confirmação de publicação — 18/11/2026

Render deployment `dep-dburju68bjmc739njca0`, commit `74f50c844b44d3a3d95f5afc06fdde31977cd91d`, status `live`, finalizado `2026-11-18T14:46:14Z`. Os logs do build confirmam instalação de dependências, coleta de 133 estáticos e comando de migrations executado sem atualizações pendentes. Isso não comprova testes reais de reserva, fotos ou tutorial em navegador da URL publicada. A vinculação do grupo OAuth ao serviço ainda precisa de verificação no painel. A revisão do PDF e o aceite do orientador permanecem pendentes.

## Atualização de 18/11/2026 (noite)

- Versão live no Render conferida antes do aceite: commit `e220974`. O print R06 do aceite mostra uma foto servida pela demonstração, então o vínculo do Drive com o Render funciona para exibição. Um envio novo de foto e a persistência após redeploy continuam sem evidência registrada.
- A numeração de regras deste documento foi alinhada à baseline (RN001–RN014). A equivalência com o catálogo ampliado está em `docs/RASTREABILIDADE.md`.
- Desde 18/11, a pasta central do Drive está com acesso **restrito**. Os links do Drive citados aqui e na monografia só abrem para a autora até ela compartilhar com o orientador ou a banca.
