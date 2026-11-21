# Reconciliação técnica de diffs EVO-USO-01 — 21/11/2026

## Escopo e evidência
Comparação direta dos patches GitHub [PR #15](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/15) (head `3f4549bfba35411b6e02918a8cfd6a1f6f4111d6`) e [PR #20](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/20) (head `63f341ab9769436c252c5cf71151a976ea9498ec`). Ambas abertas/draft na consulta. Fontes oficiais RN, baseline, guia, UC01–UC14, requisitos, CAT e registro técnico lidas diretamente por ID do Drive nesta rodada. Não se inspecionaram alterações locais invisíveis de outros agentes.

## Arquivos compartilhados e dependência
- `sire/static/sire/js/tutorial-uso.js`: PR #15 cria o arquivo; PR #20 altera **o mesmo arquivo** e depende da base #15. Não aplicar #20 diretamente sobre a demo.
- `sire/templates/sire/base.html`: PR #15 introduz `data-sire-role` e carrega script com `defer`. PR #20 não altera este template; alterações concorrentes de outros PRs precisam ser reconciliadas separadamente.
- `docs/PROGRESSO_TCC_FINAL.md`: ambas alteram o mesmo checklist; estado de PR #2 no patch de #20 está desatualizado (consulta atual: merged). Preservar a correção posterior e histórico.
- `docs/EVO_USO_01_CORRECOES_20261118.md`: adicionado somente por #20, não substitui evidências de testes.

## Mudanças concretas do patch #20
1. Versão do guia v1→v2; roteiro próprio do Passageiro autenticado.
2. Correspondência de alvo por texto exato dentro de `main`/navegação, em vez de busca ampla por substring.
3. Remoção de `position:relative;z-index:2` do destaque.
4. Índice persistido por perfil e versão, com captura de falhas de `localStorage`.
5. Ciclo de Tab e retorno de foco; requer validação real com teclado/leitor de tela.

## Riscos e critérios para integração
| Critério | Estado observado | Próxima prova necessária |
|---|---|---|
| Script presente em página de cada perfil | Código proposto, não executado aqui | Django + navegador, Visitante/Passageiro/Agente sintéticos |
| Alvo exato corresponde a texto real | Não verificado | Testar catálogo, detalhes, reserva e painéis; registrar alvos ausentes |
| Sem clique ou POST involuntário | Não verificado dinamicamente | Inspecionar eventos e comparar contagens de registros antes/depois |
| Tab, Shift+Tab, Escape, foco | Código proposto | Ensaiar desktop e viewport 375×812, com evidências |
| Storage indisponível | Tratamento proposto | Executar ensaio com SecurityError e registrar resultado |
| Autorização multiagência e reservas | Fora do diff tutorial | Regressões RN-03/04, UC10–14, SQLite e PostgreSQL |
| Avaliação de orientador | Pendente | Autora solicitar nova tentativa após testes |

## Decisão
**Não mesclar nem publicar** PR #15 isolada nem #20 sem conciliação das demais branches e verificações. OAuth `drive.file` do aplicativo bloqueia persistência REAL de fotos, mas não bloqueia o ensaio do tutorial. Nenhum teste, CI, deploy, aprovação humana ou alteração de monografia foi realizado nesta unidade. A baseline ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem intactos.
