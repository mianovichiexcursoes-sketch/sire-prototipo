# EVO-USO-01 — Reconciliação de linhagens (22/11/2026, 17h56 BRT)

Fontes oficiais reabertas por IDs originais: RN-01–41, ER-SIRE 2.1, guia, UC01–UC14, requisitos 3.0, CAT revisão 0.2 e registro de implementação. Baseline e seis entidades históricas preservadas.

Comparação autenticada de HEADs com a demo etapa/postgresql-windows (SHA 76f6984ae4f48a5fefe1a94d2a7fe16dc8aba4d4):

| PR | SHA | Ahead/behind | Arquivos relevantes |
|---|---|---|---|
| #15 | 3f4549bfba35411b6e02918a8cfd6a1f6f4111d6 | +3/-67, diverged | base.html, tutorial-uso.js, checklist |
| #20 | 63f341ab9769436c252c5cf71151a976ea9498ec | +4/-67, diverged | base.html, tutorial-uso.js, checklist |
| #33 | 8bd96705e19afc0b5d0a89671270ae8232bbf175 | +2/-0, ahead | tutorial-uso.js |
| #35 | bf917708f09d01befb8c7576dfc43d9d2a1e8158 | +5/-0, ahead | tutorial-uso.js |
| #64 | 1f8741a1343054dce8b7678186483987680908be | +5/-67, diverged | base.html, tutorial-uso.js, checklist |

**Achado:** duas linhagens distintas: #15 → #20/#64, defasada em 67 commits; #33 → #35, descendente da demo consultada. Não há evidência de que o merge de ambas preserve os fluxos. A ancestralidade não comprova funcionamento nem ausência de conflitos semânticos.

**EVO-USO-01: EM EXECUÇÃO.** Bloqueio: integração e testes TUT-01–10 não demonstrados. Responsável: integração técnica. Condição para retomar: comparar conteúdo real JS/template e montar branch isolada a partir do HEAD atual da demo, portar apenas correções faltantes e executar testes com perfis sintéticos, teclado, Escape, foco, mobile e estados vazios. Não realizar merge/deploy antes de revisão.

**B OAuth: BLOQUEADO** por falta de autorização própria do aplicativo e confirmação de secrets no Render; responsável autora/administrador Google Cloud e Render; retomar com configuração segura e teste real sem segredos. Independente de EVO-USO-01.

**F testes integrados: PENDENTE**; nenhum teste Django/Chromium/PostgreSQL executado nesta rodada. **G auditoria global: PENDENTE.** Checklist canônico permanece em PR #70, sem sobrescrever o trabalho concorrente. Esta nota complementa, não substitui, seu histórico. Nenhum dado real, migração, merge ou deploy alterado.
