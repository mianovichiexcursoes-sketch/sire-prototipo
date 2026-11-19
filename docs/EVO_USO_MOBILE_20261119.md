# EVO-USO-01 — ajuste isolado de viewport móvel (19/11/2026)

Fontes consultadas diretamente: RN-01–41 (ID 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0); baseline 2.1/histórico 2.6 (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8); guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U); UC01–14 (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY); requisitos 3.0 (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM); CAT 0.2 (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is); registro (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM).

| Item | Status | Commit/evidência | Próxima ação |
|---|---|---|---|
| EVO-USO-01 / TUT — painel móvel | IMPLEMENTADO, NÃO VERIFICADO | 45d401bf7a92586f91ad1b11f828dfb144f8d7e2; alteração de media query em tutorial-uso.js | Testar em Chromium 375×812 e teclado, observar rodapé e alvos inferiores, verificar viewport 320px e orientação paisagem |
| Fechar explícito | IMPLEMENTADO NA BRANCH PAI, NÃO VERIFICADO | PR #33 | Rodar regressão no SHA integrado |
| OAuth Drive | BLOQUEADO para teste real | Sem prova de autorização própria Django/Render nesta rodada | Operadora configura credenciais no ambiente seguro; não registrar segredos |
| Avaliação orientador | BLOQUEADO | Sem novo parecer | Autora solicita avaliação após revisão/testes |
| Checklist canônico | PENDENTE DE CONCILIAÇÃO | PRs #30/#31 editam o mesmo arquivo | Reconciliar sem sobrescrever trabalho paralelo |

**Mudança:** limite responsivo da altura do diálogo para reduzir a cobertura de conteúdo inferior. CSS de fallback para navegadores sem unidade dvh. Nenhuma submissão, modelo, migração, dados pessoais, merge ou deploy. **Não é evidência de correção visual:** falta ensaio real em navegador. Preserva baseline ER-SIRE 2.1, seis entidades e UC01–14.

Rastreabilidade: EVO-USO-01 → tutorial-uso.js (media query) → TUT móvel / rodapé → evidência manual pendente → seção da espiral na monografia pendente. PR #24 documenta a ressalva original. Branch derivada do HEAD da PR #33 para manter o botão Fechar, sem editar a branch concorrente.
