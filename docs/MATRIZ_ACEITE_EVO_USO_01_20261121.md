# EVO-USO-01 — matriz independente de aceite (21/11/2026)

**Estado: especificação de verificação, NÃO execução de testes nem aprovação.** Criada em branch documental isolada para não alterar templates, migrations ou trabalho concorrente. Baseline ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem históricos. Fontes originais consultadas nesta rodada diretamente por ID: RN-01–41 (1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0), baseline (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8), guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U), UC (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY), requisitos (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM), CAT (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is), registro (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM). Datas de modificação não verificadas.

| Critério | Perfil e cenário sintético | Resultado esperado | Evidência necessária | Estado |
|---|---|---|---|---|
| TUT-01 | Visitante, navegador limpo | Convite inicial e botão permanente Como usar; catálogo/detalhes indicados | captura + URL + commit | Pendente |
| TUT-02 | Passageiro fictício autenticado | Embarque, confirmação e minhas reservas; nenhum envio automático | captura + registro de requests | Pendente |
| TUT-03 | Agente fictício autorizado | Excursões, cadastro, embarques, publicação, reservas e passageiros, sem acesso de outra agência | captura + teste de autorização RN-03–05 | Pendente |
| TUT-04 | Teclado e leitor de tela | Anterior/Próximo/Pular/Fechar, foco visível, Escape e rótulos; sem bloqueio permanente | roteiro e resultado manual | Pendente |
| TUT-05 | Alvo ausente, lista vazia, sem vagas, localStorage negado | Degradação segura, sem erro fatal e sem dados pessoais em armazenamento | console + testes e captura | Pendente |
| TUT-06 | Mobile estreito e desktop | Destaque no elemento correto, sem sobreposição impeditiva | screenshots por viewport | Pendente |
| REG-01 | Passageiro e agente sintéticos | Reservas e permissões inalteradas; UC01–UC14 sem regressão | saída real SQLite/PostgreSQL + SHA | Pendente |

## Dependências e critérios de retomada
- **Tutorial:** já há implementação concorrente em `feat/evo-uso-01-tutorial-20261118` e branches de correção; reconciliar HEAD/diffs antes de tocar em `base.html` ou JS. Responsável: integrador técnico. Sem verificação de navegador e revisão, não integrar/publicar.
- **OAuth drive.file:** autorização própria do Django, credenciais seguras e ambiente isolado não confirmados nesta rodada. Responsável: autora/operador Cloud e Render. Bloqueia upload/exclusão/persistência real de fotos e aceite dessa integração, **não** tutorial nem verificação independente. Retomar após autorização verificada sem publicar segredos.
- **Avaliação:** o orientador não confirmou novo aceite; autora deverá solicitar teste depois de uma versão verificada. Não inferir métricas ou aprovação.
- **Auditoria acadêmica:** apêndice UC01–UC14, modelo relacional, revisão integral da monografia e comparação com modelo IFSP seguem pendentes; não modificar documentos históricos sem reconciliação.

## Rastreabilidade
EVO-USO-01 → `sire/static/sire/js/tutorial-uso.js` e `sire/templates/sire/base.html` (branch de implementação, ainda sem aceite) → TUT-01–06 → evidência manual pendente → metodologia/resultados da monografia pendentes. RN-03–05/UC baseline → REG-01 → suíte e autorização entre agências pendentes. Não há nova migration nesta unidade.

## Próxima ação
Comparar implementação e correções recentes do tutorial, executar TUT-01–06 em ambiente isolado e registrar resultados reais, sem merge/deploy da demo. Depois consolidar no checklist principal com SHA e evidências. Esta matriz é planejamento verificável, não prova de teste.
