# EVO-USO-01 — Correção de orientação por perfil (21/11/2026)

**Estado: implementado em branch isolada; testes e integração pendentes.**

## Achado reproduzível por inspeção de código
Na branch `feat/evo-uso-01-tutorial-20261118`, o array de etapas era selecionado apenas por `role === "agente"`; todo outro perfil recebia `Criar conta` e `Entrar`, inclusive `passageiro` autenticado. O teste existente `tests/test_tutorial_browser.py::TutorialBrowserTests::test_tut02_passenger_no_signup_instruction` espera que `Criar conta` não seja apresentado ao passageiro e que `Minhas reservas` apareça em cinco passos. O teste e a implementação eram contraditórios. Não foi executado navegador nesta rodada.

## Correção e rastreabilidade
- EVO-USO-01 / TUT-02 → `sire/static/sire/js/tutorial-uso.js` → separação explícita de `agente`, `passageiro` e `visitante`.
- Passageiro: Catálogo, Detalhes, Selecionar embarque, Confirmar reserva, Minhas reservas. Sem convite para novo cadastro.
- Visitante: preserva roteiro original de cadastro e acesso; agente: preserva roteiro administrativo.
- Sem alterações de models, migrations, reservas, dados, perfis ou deploy. Baseline ER-SIRE 2.1 e UC01–UC14 inalterados.

## Checklist e dependências
| Item | Status | Último commit | Evidência | Próxima ação |
|---|---|---|---|---|
| TUT-02: não recomendar cadastro a passageiro autenticado | Implementado, **não verificado** | `97e341de420dac363c28648a2f0e18ca755040b0` | diff do JS e teste TUT-02 já existente | Integrar com correções concorrentes do JS e executar Chromium |
| TUT-01–09 e regressões | Pendente | — | testes em PRs independentes | Executar navegador 320px/375px, Escape, foco, storage e não envio de formulário |
| OAuth drive.file / fotos reais | Bloqueado | — | autorização do aplicativo não comprovada | Autora autorizar app e configurar segredos exclusivamente no Render; testar em ambiente isolado |
| Aceite do orientador e deploy | Bloqueado | — | sem avaliação humana | Revisar integração testada antes de qualquer publicação |

## Gate de fontes
Consultados diretamente por ID em 21/11/2026: RN-01–41, ER-SIRE 2.1, guia de implementação, UC01–UC14, requisitos v3, especificação CAT e registro de implementação. A decisão de 18/11/2026 define tutorial interativo e não vídeo. Versões/data de modificação de cada fonte não foram verificadas nesta rodada.

**Conflito de integração:** PRs #15, #20, #33 e #35 também alteram `tutorial-uso.js`. Esta branch não deve ser mesclada isoladamente sem comparar os HEADs e reconciliar o conteúdo. Não foi executado teste, CI ou deploy nesta rodada; nenhum resultado é presumido.
