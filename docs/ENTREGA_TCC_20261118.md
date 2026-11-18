# SIRE — Termo de reconciliação e entrega técnica (18/11/2026)

**Status: candidato de entrega validado em CI; publicação/aceite finais ainda não comprovados.** Autora: Julia Mianovichi. TCC de Engenharia Elétrica, IFSP Câmpus Sertãozinho. Implementação assistida por ChatGPT, Codex e Claude Code. O documento distingue explicitamente evidências executadas de condições ainda pendentes.

## 1. Versões, branches e fatos verificados

- **Demo pública**: https://sire-demo.onrender.com — Render relatou `live` no commit **7c531342** de `etapa/postgresql-windows` (18/11/2026, consulta da API Render). É a versão rosa, com pesquisa de excursões e reserva. **Não é** a versão consolidada de fotos/tutorial.
- **Candidato de release**: PR #18, https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/18, branch `entrega/consolidacao-final-20261118`, construída sobre o commit `82b1b97` da PR #17 e incrementada com as correções de OAuth/privacidade da PR #16. O commit `cd93a81d` é a base consolidada testada, seguida de atualizações documentais.
- **CI da base consolidada**: [Django geral](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319295069), [fotos em SQLite/PostgreSQL](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319295483), [tutorial em navegador](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44319294940). Esses workflows indicaram sucesso no commit `cd93a81d`. A CI dos commits documentais posteriores deve ser conferida separadamente.
- **Drive real, fora da demo**: [relatório completo](docs/OAUTH_EXECUCAO_REAL_2026-11-18.md) e [JSON do ensaio](../evidencias/2026-11-18_1032_drive_real/resultados.json) registram 13 de 13 verificações conformes em Windows/PostgreSQL local após OAuth `drive.file` renovado com o aplicativo Google em produção. Foi testada persistência após reiniciar **processo local**, não após deploy Render; os arquivos sintéticos de ensaio foram removidos.
- **Segredos**: grupo Render `sire-drive-oauth-36a0572f` (ID `evg-dbuq4kom7kps73d5trfg`) contém três variáveis, mas o relatório de execução afirma que ele **não estava vinculado a serviço**; não registrar valores, tokens nem chaves em Git, Drive ou impressões. As chaves temporárias de API criadas na configuração foram relatadas como revogadas.
- **Monografia atual**: https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit — seção 3.2.3 relata retorno do orientador e EVO-USO-01; subseção 3.2.3.5 adicionada em 18/11 registra a CI consolidada e as limitações da integração.
- **Documentação de desenvolvimento**: https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit — Apêndice A contém as especificações completas UC01–UC14. Regra de negócio de referência RN-01–RN-41: https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit

## 2. Rastreabilidade resumida e escopo

| Artefato | Requisitos e regras | Implementação | Evidência / limite |
| --- | --- | --- | --- |
| Baseline histórica | ER-SIRE 2.1, UC01–UC14, RN-01–RN-30 pertinentes | User, Agencia, PerfilUsuario, Excursao, PontoEmbarque, Reserva; Django ORM | VF01–VF16 registrados em artefatos de outubro e regressão posterior; preservar escopo histórico |
| Catálogo rosa e filtros | CAT-RF-01, CAT-RNF-01 | formulários, views e templates da branch de demonstração | PR #1 merged, commit 7c531342 live no Render |
| Ficha completa | CAT-RF-02/04, UC05–UC07, RN-03/11/14 | migração 0007, formulário, detalhes, galeria | CI e testes locais; versão pública com ficha ampliada pendente |
| Fotos | CAT-RF-03, RN-03/04/05/11 | FotoExcursao (entidade técnica nova, fora da baseline), Google Drive, proxy protegido | CI SQLite/PG e 13 verificações reais locais; sem ensaio de persistência pós-redeploy Render |
| Tutorial contextual | EVO-USO-01, retorno do orientador de 17/11 | JavaScript progressivo por perfil, botão Como usar, fechamento por Escape | Workflow de navegador aprovado; ainda falta avaliação da interface publicada pelo orientador |
| CPF | EVO-CPF-01, RN-04/05 | **Não implementado**; somente especificação LGPD proposta na PR #8 | não colocar nos resultados de software |
| Pagamentos, assentos, cancelamentos, favoritos, avaliações | visão evolutiva RN-31–41, backlog | **Não implementados** | proposta de trabalhos futuros, não conformidade testada |

## 3. Condições necessárias antes de declarar entrega final

1. **Segurança:** confirmar que nenhum token, segredo ou dado real foi commitado ou exposto em evidências; manter escopo `drive.file` e revogação das chaves temporárias.
2. **Integração:** verificar checks para o HEAD final da PR #18, revisão de diffs, e integrá-la **sem sobrescrever** mudanças paralelas. Fazer migração 0007 de modo seguro e verificar o build no Render.
3. **Drive no Render:** o responsável deve vincular o grupo existente de segredos ao serviço de demonstração pelo painel do Render **antes** de testar upload real na demo. Não criar recurso pago nem usar dados de passageiros reais.
4. **E2E:** repetir com identidades e imagens sintéticas: agente cadastra excursão/embarque/publica, envia foto; visitante abre, passageiro reserva, agente consulta a reserva; verificar disponibilidade e imagem depois do deploy, permissões de rascunho e remoção.
5. **Modelagem:** conferir a figura do modelo relacional presente no projeto versus entidades e relações efetivas. A lista de pendências do Visual Paradigm sobre cardinalidade Agência/PerfilUsuario ainda não foi encerrada no editor; não atribuir aceite ao diagrama sem prova.
6. **Acadêmico:** concluir auditoria de ABNT e referências, comparar figuras, resultados e métodos da monografia com o código efetivo. O orientador precisa confirmar o título oficial e validar uso do tutorial. O relato de "entrevista" deve ter registro demonstrável ou ser tratado como relato da experiência profissional da autora, sem inventar participantes e datas.
7. **Aceite:** só então exportar PDF final da monografia e cópia dos documentos na pasta central do Drive, em revisão pela autora e orientador.

## 4. Limitações e condições de apresentação à banca

- O sistema do TCC é um **protótipo** multiagência, não uma operação comercial de viagens: não processa pagamentos, não escolhe poltronas e não comprova escalabilidade por testes de carga.
- O Google Drive pessoal foi uma escolha acadêmica de baixo custo; Cloudinary/R2 são melhorias futuras possíveis, não funcionalidades entregues.
- Autores de código/registro devem ser informados conforme ocorrido: IA assistiu construção, Git e verificações; autora definiu problema, requisitos, limites e avaliações. Não declarar programação manual que não ocorreu.
- Revisões realizadas em 18/11/2026: inclusão de seção de CI/Drive real na monografia e da presente reconciliação. A revisão global de todas as páginas ABNT, posição das imagens e fontes **ainda depende de inspeção visual PDF**.

## 5. Decisão registrada

**A PR #18 é o candidato único de integração** para evitar sequência de merges de PRs antigas que têm bases divergentes. PRs #2, #7, #9, #15, #16 e #17 podem ser mantidas como histórico até confirmar que todos os diffs necessários estão nela. Não fazer deploy na demo por mera existência de CI verde se o grupo OAuth ainda não estiver vinculado e o plano de testes final não estiver concluído.
