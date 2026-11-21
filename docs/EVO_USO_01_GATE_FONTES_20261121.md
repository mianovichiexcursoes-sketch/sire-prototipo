# EVO-USO-01 — Gate de fontes e critérios de integração (21/11/2026)

Documento **incremental**, sem alteração da baseline ER-SIRE 2.1, das seis entidades históricas ou de UC01–UC14. Não constitui teste nem aceite.

## Leitura direta das fontes oficiais (IDs exatos, 21/11/2026)

| Fonte | ID | Versão identificada | Aplicação ao tutorial |
|---|---|---|---|
| Regras RN-01–41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | sem versão no cabeçalho | RN-03/04/05: respeitar agência e papel; RN-06–11: não orientar publicação inválida |
| Desenvolvimento | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | baseline 2.1; histórico até 2.6 (12/11) | preservar modelagem e distinguir a nova volta da terceira iteração técnica |
| Guia | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | referência Django 6.1.2, SQLite/PostgreSQL | tutorial só navega; não altera regras de persistência |
| Casos de uso | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | UC01–UC14 | descrever fluxo existente por papel sem renumerar UC |
| Requisitos | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | v3.0 PFC2 | separar protótipo de visão futura (pagamento/assentos) |
| CAT | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | revisão 0.2 | detalhes e fotos opcionais, sem tornar fotos pré-requisito do tutorial |
| Registro técnico | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | registro desde 20/10 | evidência histórica não substitui teste da árvore integrada |

## Matriz de critérios EVO-USO-01 (planejada, não verificada)

| Critério | Base | Arquivo alvo provável | Cenário a verificar | Evidência exigida | Monografia |
|---|---|---|---|---|---|
| TUT-01, descoberta por perfil | RN-05, UC01–14 | `sire/templates/sire/base.html`, JS do tutorial | Visitante, Passageiro e Agente veem passos próprios | teste navegador por perfil e screenshot | metodologia / extensão de usabilidade |
| TUT-02, navegação segura | RN-03–05 | JS do tutorial | Anterior, Próximo, Pular, Fechar, Escape, foco | teste de teclado sem POST | resultados da nova volta |
| TUT-03, estados ausentes | UC03–05, UC10–14 | JS e templates existentes | alvo inexistente, catálogo vazio, lotação | teste com dados sintéticos | limitações e resultados |
| TUT-04, persistência mínima | RN-04 | JS do tutorial | storage indisponível e reinício por versão; sem CPF | teste com storage bloqueado | riscos e privacidade |
| TUT-05, responsividade | requisitos não funcionais | CSS/JS | 320px e 375×812; sem sobreposição | screenshot e inspeção manual | evidências de interface |
| TUT-06, não alteração de negócio | RN-06–30, UC10–14 | templates, views existentes | nenhum formulário enviado automaticamente; reservas só por ação explícita | regressão Django/Chromium | rastreabilidade |

## Dependências, bloqueios e reconciliação

- PR #2 está **merged** (GitHub, conferido em 21/11), mas OAuth próprio `drive.file`, upload real, exclusão e persistência após deploy **não foram comprovados nesta rodada**. Responsável: autora/operador Google Cloud e Render; retomar testes reais só após autorização e configuração segura, sem publicar segredos.
- PR #14 é **draft documental**, não implementação. Sua descrição registra PRs concorrentes #15, #20, #21, #33, #35 e #39 alterando em cadeia o mesmo JS e checklist. **Não integrar por cherry-pick indiscriminado**; comparar HEADs, ancestralidade e árvore final.
- Este arquivo é exclusivamente uma matriz de rastreabilidade nova; não modifica templates, JS, modelos, migrations, PRs concorrentes ou demo.
- Próxima unidade: integrar em branch isolada a cadeia de tutorial após reconciliação de patches; executar testes Django e Chromium, registrar SHAs, saídas, screenshots e falhas. Só depois solicitar avaliação da autora/orientador; não afirmar aceite.

## Situação desta entrega

**Concluído:** leitura direta de sete fontes e registro desta matriz em GitHub. **Pendente:** testes, integração, avaliação, auditoria global da monografia e deploy. **Bloqueado parcialmente:** ensaio real de Drive por OAuth do aplicativo não verificado.
