# EVO-USO-01 — reconciliação verificável de PRs (20/11/2026, 07h BRT)

**Natureza:** unidade de revisão técnica independente, sem alteração de aplicação ou aceitação. Base preservada: `etapa/postgresql-windows`. Este documento não substitui o checklist canônico ainda em revisão na PR #30.

## Fontes oficiais consultadas diretamente nesta execução
- Regras RN-01–41: `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` (RN-03–05, 06–16, 17–30; 31–41 fora do protótipo).
- Desenvolvimento: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`, baseline ER-SIRE 2.1, histórico documental até 2.6.
- Guia: `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`.
- UC01–UC14: `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`.
- Requisitos: `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`, versão 3.0.
- CAT: `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`, revisão 0.2.
- Registro: `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`.

## HEADs efetivamente consultados no GitHub
| PR | SHA observado | Relação e conflito a resolver | Estado |
|---|---|---|---|
| #15 | `3f4549bfba35411b6e02918a8cfd6a1f6f4111d6` | Adiciona `base.html` e `tutorial-uso.js`; ponto de partida | aberta, não mesclada |
| #20 | `63f341ab9769436c252c5cf71151a976ea9498ec` | Base #15; altera o mesmo JS, adiciona foco/roteiros | aberta, não mesclada |
| #21 | `f977ab8e33173fc21ee8b29d5eb03ab8d74c8ed4` | Base #20; adiciona `tests/test_tutorial_browser.py` e workflow Chromium | aberta, não mesclada |
| #33 | `8bd96705e19afc0b5d0a89671270ae8232bbf175` | Base demo, altera o mesmo JS para incluir Fechar; **não pressupor que contém #20** | aberta, não mesclada |
| #35 | `bf917708f09d01befb8c7576dfc43d9d2a1e8158` | Base #33; altera o mesmo JS para reduzir painel móvel; **não pressupor que contém #20/#21** | aberta, não mesclada |
| #30 | `70818b6ea174f703222705a5f2fcfa2bd44bef9e` | Checklist canônico proposto, branch própria a reconciliar | aberta, não mesclada |
| #14 | documentação, PR aberta | Decisão vigente: tutorial, não vídeo | aberta, não mesclada |
| #2 | `faa5ba3d60b7f292be09676b13f39e9276eacafb` | Ficha/fotos; **merged** não significa OAuth ou fotos testadas | mesclada |

**Achado concreto:** #20 e #33 modificam o mesmo `tutorial-uso.js` a partir de ancestrais diferentes. #21 herda #20, enquanto #35 herda #33. Aplicar #35 sobre #21 sem comparar o conteúdo integral pode descartar o roteiro por perfil, foco ou botão Fechar. A reconciliação deve preservar as quatro propriedades e executar testes no SHA final.

## Sequência executável, sem sobreposição com Claude
1. Criar branch de integração **nova** a partir da base atual, confirmar árvore e heads imediatamente antes de aplicar alterações.
2. Integrar o encadeamento #15 → #20 → #21; comparar manualmente as diferenças de `tutorial-uso.js` de #33/#35 e incorporar apenas alterações ausentes. Evitar merges cegos de branches com ancestrais distintos.
3. Confirmar no código final: botões Anterior/Próximo/Pular/**Fechar**, papel Visitante/Passageiro/Agente, retorno de foco, Escape, Tab, alvo ausente, armazenamento bloqueado, ausência de POST automático.
4. Executar suíte no SHA integrado e salvar comando/saída/ambiente; ensaiar viewport 320px e 375×812 em navegador. Testes isolados da #21 não provam integração nem responsividade da #35.
5. Atualizar `docs/PROGRESSO_TCC_FINAL.md` na branch reconciliada com status, SHA, evidências e bloqueios; atualizar documento acadêmico **somente** após nova leitura e confirmação da versão. Revisão humana antes de merge/deploy.

## Dependências explícitas
- **B / fotos Drive:** bloqueado para aceite real enquanto não houver autorização OAuth `drive.file` própria do aplicativo Django e configuração segura no Render; responsável autora/operador Google Cloud/Render; condição de retomada: credenciais configuradas fora do repositório e ensaio sintético documentado. Não impede tutorial.
- **EVO-USO-01:** em execução; bloqueio de publicação: branches não reconciliadas, testes integrados e avaliação humana pendentes. Responsável técnico pela integração e autora pela revisão; retomar após SHA integrado e logs reais.
- **G / auditoria global:** pendente de inventário completo, monografia, modelo IFSP, regulamento e verificação pós-edição. Nenhuma aprovação acadêmica inferida.

## Rastreabilidade
`EVO-USO-01 / UC01–UC14 / RN-03–05` → `base.html`, `tutorial-uso.js`, `tests/test_tutorial_browser.py` (PRs #15/#20/#21/#33/#35) → TUT-01–09 e regressões VF (a executar no integrado) → evidência: HEADs e patches consultados nesta revisão; **não há resultado de teste novo** → documentação de desenvolvimento/iteração espiral e resultados, ainda pendentes de atualização conclusiva.

**Limites desta unidade:** leitura de fontes e patches GitHub realizada; nenhum teste Django, navegador, deploy, merge ou aceite humano executado. Baseline ER-SIRE 2.1, seis entidades, UC01–UC14, dados e demo preservados.
