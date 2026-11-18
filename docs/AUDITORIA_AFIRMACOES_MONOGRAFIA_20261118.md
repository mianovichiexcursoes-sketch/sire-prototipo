# Auditoria pontual de afirmações da monografia — 18/11/2026

**Escopo:** leitura direta da monografia Google Docs `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg` (modificada em 18/11/2026 às 22:30:57 UTC) e do parecer de pré-banca `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA` (23/10/2026). Não é revisão integral de ABNT, nem aceite de código. Documento de constatações; nenhuma edição na monografia.

| ID | Constatação diretamente observada | Estado | Evidência | Próxima ação |
|---|---|---|---|---|
| AUD-MON-01 | Título principal atual é **Projeto de Arquitetura de Software Aplicado ao Turismo Rodoviário**, com subtítulo **Engenharia de Requisitos para Plataformas de Logística de Lazer**. O termo “escaláveis” não aparece no texto extraído. | Parcialmente corrigido; confirmação humana pendente | Capa/folha de rosto da monografia; pré-banca C2 | Confirmar título/subtítulo com orientador; não mudar unilateralmente |
| AUD-MON-02 | Texto da monografia agora reconhece explicitamente assistência de ChatGPT, Codex e Claude Code. | Texto presente, validação acadêmica pendente | Seção de autoria/IA da monografia; pré-banca C1/C5 | Conferir redação e citações com orientador; reconciliar a especificação histórica sem apagá-la |
| AUD-MON-03 | A monografia informa entrevista com 14 perguntas e respostas em `Entrevista.pdf`, mas observa ausência de identificação nominal e data. | Ressalva documentada | Seção de elicitação da monografia; pré-banca C3 | Inspecionar o PDF original e caracterizar método, participantes e limites sem inventar dados |
| AUD-MON-04 | A monografia registra decisão da autora por tutorial interativo em 18/11, sem alegar aprovação formal do orientador. | Registro presente; avaliação pendente | Seção de retorno do orientador | Conferir tutorial em navegador, inclusive sobreposição no celular, e solicitar avaliação pela autora |
| AUD-MON-05 | A monografia relata 107 testes aprovados e 3 ignorados no commit `e220974`; também diz que login de agente/passageiro no Render não foi executado. | Declaração documental, não reexecução desta auditoria | Seção de resultados; PR #24 | Conferir logs originais, diferenciar ambientes e repetir cenários faltantes |
| AUD-MON-06 | A monografia refere **Apêndice A do documento de desenvolvimento**, mas não contém apêndice integral UC01–UC14 no próprio texto extraído. | Requisito de entrega a confirmar | Trecho final da monografia e documento de desenvolvimento | Confirmar com orientador se apêndice deve integrar a monografia ou somente o documento do projeto; revisar sumário e anexos |

## Gate e rastreabilidade
- Fontes de regra lidas diretamente nesta rodada: RN-01–41, baseline ER-SIRE 2.1, guia, UC01–UC14, requisitos versão 3.0, CAT revisão 0.2, registro de implementação, monografia e parecer.
- Baseline histórica preservada: seis entidades e UC01–UC14. Não reinterpretar recursos novos como parte da baseline.
- EVO-USO-01 → tutorial JS/templates → TUT em navegador (pendente de verificação nesta unidade) → metodologia/resultados/limitações na monografia.
- PR #2 está **merged** em 18/11/2026; isso não prova autorização OAuth nem persistência de fotos. PR #14 continua aberta; outras branches de tutorial existem. Não tocar em arquivos concorrentes.
- Esta unidade não executou testes, CI, deploy, OAuth ou edição acadêmica. Não declarar conclusão funcional.

## Bloqueios e responsáveis
- **Avaliação do orientador:** falta revisão humana; responsável: autora/orientador; retomar após apresentação do tutorial e do modelo/UC.
- **OAuth de fotos:** autorização própria do Django e confirmação segura do ambiente; responsável: autora/operador Google Cloud e Render; impede comprovação de upload/persistência real, não impede documentação.
- **Conciliação Git:** branches e PRs paralelas em andamento; antes de qualquer merge verificar HEADs, CI e diffs.

**Próxima unidade independente:** conferir o arquivo Entrevista.pdf na pasta TCC JULIA — SIRE e registrar a classificação metodológica fiel; depois auditar sumário/apêndice e referências da monografia. Não reescrever históricos silenciosamente.
