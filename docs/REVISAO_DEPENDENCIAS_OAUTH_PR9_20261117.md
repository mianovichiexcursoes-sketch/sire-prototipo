# SIRE — revisão de dependências OAuth e testes isolados

Data: 17/11/2026 (rodada noturna). Análise documental; **não é execução de OAuth, CI ou deploy**.

## Fontes e preservação

Foram consultados diretamente pelos IDs originais os 12 arquivos exigidos (RN-01–41, desenvolvimento ER-SIRE 2.1, guia, UC01–14, requisitos 3.0, CAT, registro técnico, monografia, modelo IFSP, regulamento PFC PDF, parecer e histórico PROMPS). A baseline de seis entidades e UC01–14 permanece histórica; nenhuma alteração no código ou na monografia nesta unidade.

## Estado remoto confirmado

- PR #2: aberta e draft, base `etapa/postgresql-windows`, HEAD `faa5ba3d60b7f292be09676b13f39e9276eacafb` (consulta GitHub).
- PR #7: aberta e draft, base `fix/fotos-cache-lock-20261117`, HEAD `0a7f77cee3785bf755ccfe4927c6014a0d1063e7`.
- **PR #9 encontrada nesta rodada:** aberta e draft, base `fix/oauth-seguro-20261117`, HEAD `2a354a75f01401f49db639fa6e52752fe7a2d60c`; adiciona opção `--grupo-render` para criar Environment Group sem vinculação a serviço, conforme [guia próprio](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/fix/oauth-grupo-render-20261117/docs/OAUTH_GRUPO_RENDER.md). O texto da PR relata nove testes simulados aprovados, **não reproduzidos nesta rodada**.
- A branch independente `test/oauth-falha-parcial-20261117` contém `sire/tests/test_oauth_failure_paths.py`, lido nesta rodada. Ela parte da PR #7 e **não inclui necessariamente** o fluxo de Environment Group da PR #9. Não mesclar ou afirmar cobertura de PR #9 com esses dois testes.

## Revisão estática do teste isolado

- Cenário 1 simula GET de serviço e falha HTTP 503 no segundo PUT; exige ausência do terceiro PUT e saída stdout vazia. **Não comprova atomicidade**, reversão do primeiro PUT, segurança de stderr ou funcionamento real do Render.
- Cenário 2 simula nome de serviço não permitido; exige recusa antes de PUT. **Não comprova** bloqueio da demo em todos os estados reais.
- O teste foi somente **lido**, não executado; resultado atual: NÃO VERIFICADO. É aplicável ao caminho antigo `enviar_render`, enquanto o fluxo novo de grupo da PR #9 deve ser testado separadamente.

## Bloqueios e condições

| Item | Status | Dependência/impacto | Responsável e retomada |
|---|---|---|---|
| OAuth real drive.file | BLOQUEADO | Cliente OAuth e consentimento do próprio Django ainda não comprovados; impede fotos reais | Autora/operador Google Cloud; retomar com autorização própria e registro sem segredos |
| Grupo Render real | BLOQUEADO | Execução real e confirmação de grupo não comprovadas; não autoriza deploy | Autora/operador Render; verificar grupo não vinculado sem expor valores |
| Regressão testes isolados | PENDENTE | Ambiente de execução com código disponível; nenhum CI atual verificado | Desenvolvimento; executar comando, guardar saída, SHA e versão Python |
| Reconciliação PR #2/#7/#9 | PENDENTE | Cadeia de bases e trabalho Work concorrente; risco de sobrescrita | Revisão técnica; comparar patches e CI, criar plano de integração sem merge automático |
| Fotos reais e persistência | BLOQUEADO | Depende OAuth, grupo, serviço/banco isolados e aceite | Desenvolvimento/autora; testar sintéticos após pré-requisitos |

## Próxima ação independente

Verificar CI/execução dos testes da branch isolada e preparar regressão VF/CAT sem tocar na demo. Conferir primeiro se o Work avançou PR #2/#9. Nenhuma migração, merge, deploy, alteração de dados ou credenciais nesta entrega.
