# EVO-USO-01 — inspeção independente de tutorial (20/11/2026)

## Fontes consultadas diretamente
- RN-01–RN-41 (ID 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0): RN-03–05, RN-06–09, RN-17–24; regras de acesso e reserva.
- Desenvolvimento SIRE (ID 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8): baseline ER-SIRE 2.1, documento técnico 2.6.
- Guia (ID 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U): fluxos e modelos.
- UC01–UC14 (ID 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY).
- Requisitos (ID 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM): visão do produto versus protótipo, versão 3.0.
- Complemento CAT (ID 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is): revisão 0.2.
- Registro (ID 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM).
- Plano do orientador em docs/PLANO_ESPIRAL_TUTORIAL_20261118.md na branch docs/retorno-orientador-tutorial-20261118.

## Achado verificável
A branch `etapa/postgresql-windows` já contém referência a `sire/js/tutorial-uso.js` em `sire/templates/sire/base.html` e implementação JS do tutorial. Portanto NÃO implementar outro tutorial sem conciliação. O script existente apresenta ajuda contextual por perfil, botão Como usar, Anterior/Próximo/Pular, Escape e armazenamento apenas de status. O texto não demonstra ensaio de navegador, CI nem avaliação do orientador. Não confundir código presente com aceite.

## Lacunas e riscos específicos (inspeção estática; não resultados de teste)
1. Não existe botão **Fechar** visível no painel: apenas Pular. Critério TUT-04 pendente.
2. A escolha de alvos usa texto exato de botões e links; mudanças de copy e links ocultos podem suprimir etapas silenciosamente. Critério TUT-05: verificar em cada página e estados vazios.
3. A implementação é contextual por página, não uma sequência guiada entre páginas; o progresso não identifica uma etapa global. Critério TUT-06: validar expectativa com autora e orientador.
4. Não foi localizada suíte em `sire/tests/test_tutorial.py` nesta branch (404); isto não comprova ausência de testes em outros caminhos/branches. Critério TUT-07: localizar suíte existente antes de acrescentar testes.
5. Oferta e painel não demonstram por si só comportamento correto com teclado/foco, leitor de tela, celular ou storage indisponível; executar testes reais.
6. Não há evidência nesta inspeção de confirmação de reserva, publicação, envio de formulário ou upload acionados pelo tutorial. Não afirmar segurança conclusiva sem teste.

## Dependências e próxima unidade
- **EVO-USO-01: EM EXECUÇÃO.** Reconciliar HEADs de branches do Claude/Work antes de modificar templates ou JS. Implementar botão Fechar e testes em branch isolada; não mesclar/publicar sem regressão.
- **B OAuth: BLOQUEADO para teste real**, exige autorização própria do aplicativo e credenciais seguras no Render, responsabilidade da autora/operador; não bloqueia tutorial.
- **F validação: PENDENTE** de suíte, browser e eventual revisão humana. Demo intacta.
- **G monografia: PENDENTE** de auditoria completa e confirmação acadêmica. Preservar UC01–UC14, ER-SIRE 2.1 e seis entidades originais.

## Matriz de rastreabilidade da unidade
| Evolução | Arquivo | Verificação exigida | Evidência nesta rodada | Monografia |
|---|---|---|---|---|
| EVO-USO-01 / UC01–UC05 | base.html, tutorial-uso.js | oferta, catálogo, login, ficha, teclado | inspeção estática; browser pendente | nova volta espiral, não baseline |
| EVO-USO-01 / UC06–UC14 | tutorial-uso.js | perfil agente, publicação sem POST, embarque, reservas | inspeção estática; testes pendentes | evolução e limitações |
| RN-03–05 | data-sire-role em base.html | isolamento e autorização no servidor | não testado nesta rodada | segurança |

**Nenhum teste, merge, deploy, alteração de dados ou aceite humano foi realizado nesta unidade documental.**
