# EVO-USO-01 — auditoria de cobertura do ensaio Chromium (23/11/2026)

Fonte inspecionada diretamente: `scripts/teste_tutorial_navegador.py` na branch `fix/evo-uso-consolidacao-20261123`. Fontes oficiais lidas por IDs originais: RN-01–41, baseline ER-SIRE 2.1, guia, UC01–UC14, requisitos v3, CAT 0.2 e registro técnico. Esta análise é estática do script; **não é execução de testes**.

## Cobertura efetivamente programada
- Viewports: **1280×900 e 390×844**, não 320×568 nem 375×812.
- Visitante: convite Começar, botão Como usar, alvos destacados e não sobrepostos, passos presentes, persistência do convite, Escape e retorno do foco, ausência de scroll horizontal e erros JS.
- Passageiro sintético: login, acesso direto à reserva, abertura do tutorial, Pular, escolha do ponto, clique **explícito no botão de confirmação de reserva**, consulta em Minhas reservas. O teste faz POST de reserva intencional no banco temporário; não demonstra sozinho que o tutorial jamais dispara POST.
- Agente sintético: login, papel `data-sire-role=agente`, acesso às reservas. Não cobre integralmente criação, publicação, passageiros ou isolamento entre duas agências.
- Storage indisponível: bloqueio de localStorage/sessionStorage e confirmação de que Como usar continua visível.
- Artefatos previstos: `tutorial-1280.png`, `tutorial-390.png`, `resultados-navegador.json`. O conteúdo dos screenshots não foi inspecionado nesta análise.

## Lacunas objetivas para TUT-01–12
1. Executar 320×568 e 375×812, conferir posição visual de diálogo/alvo, zoom e foco em dispositivo móvel.
2. Testar Tab e Shift+Tab (armadilha de foco), botão Fechar, Anterior, Pular e Escape em todos os perfis; retorno de foco também ao fechar.
3. Verificar estados sem vagas, alvos ausentes, páginas de detalhe/cadastro/embarque/confirmação/minhas reservas e todas as páginas de agente.
4. Instrumentar rede/requests para comprovar que **somente ações explícitas de formulário** geram POST e que a navegação do tutorial não altera reservas/publicações.
5. Criar duas agências sintéticas para isolamento RN-03/RN-04/RN-05 e executar regressões SQLite/PostgreSQL em HEAD atualizado.
6. Anexar logs, screenshots inspecionados, SHA exato e matriz TUT por cenário; obter revisão humana antes de merge/deploy.

## Dependências
OAuth `drive.file` próprio do Django é bloqueio **apenas** de ensaios reais de fotos; não bloqueia este tutorial. A PR #2 já foi mesclada historicamente, mas seu merge não comprova persistência real de fotos. CPF continua condicionado à decisão de finalidade/minimização. Baseline ER-SIRE 2.1, UC01–UC14 e seis entidades não são alteradas. Nenhum segredo ou dado real utilizado.

**Status:** análise de cobertura concluída; validação TUT e aceite permanecem pendentes. Próxima ação: ampliar o script e executar em HEAD reconciliado, sem publicar a demo.
