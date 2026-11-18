# Fotos no site publicado — teste real (18/11/2026, ~11:20)

Site: https://sire-demo.onrender.com · versão em produção contendo `72a488b`
(integração das fotos), publicada pelo Render com o grupo
`sire-drive-oauth-36a0572f` vinculado ao serviço `sire-demo`. Depois desta
integração, outra sessão publicou por cima a versão `74f50c8` (tutorial e
documentação), que contém as fotos.

Conta usada: `demo_agente` (login feito pela autora). Imagens sintéticas
geradas no navegador (faixas coloridas e texto, sem pessoas). Execução
assistida por IA (Claude Code).

| # | Verificação | Resultado |
| --- | --- | --- |
| 1 | Formulário de fotos disponível (Drive configurado no site) | Conforme |
| 2 | Upload na excursão em rascunho (#3) | Conforme — "Foto enviada ao Google Drive e vinculada à excursão." |
| 3 | Upload na excursão publicada (#1) | Conforme — idem |
| 4 | Visitante vê a foto da publicada | Conforme — HTTP 200, JPEG, `Cache-Control: private, no-store, …` |
| 5 | Visitante NÃO vê a foto do rascunho | Conforme — HTTP 404; página do rascunho também 404 |
| 6 | Catálogo e página da excursão mostram a foto | Conforme |
| 7 | Página sem link direto ao Google Drive | Conforme |
| 8 | Agente dono vê as duas fotos | Conforme — 200 JPEG |
| 9 | Remoção pelo agente apaga do site e do Drive | Conforme — "Foto removida da excursão e do Google Drive."; ambas passam a 404 |

Resultado: **9 de 9 conformes** no ambiente publicado. As duas fotos de teste
foram removidas ao final; o site ficou sem fotos para a autora cadastrar as
definitivas.

Não testado no site publicado: isolamento entre duas agências (a demo tem uma
única agência) — coberto pelos ensaios locais com o Drive real e pela suíte.
