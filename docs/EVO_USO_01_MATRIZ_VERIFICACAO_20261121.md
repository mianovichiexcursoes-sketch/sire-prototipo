# EVO-USO-01 — matriz de verificação independente (21/11/2026)

**Natureza:** roteiro verificável de aceitação; não constitui execução de teste nem aprovação. Branch isolada, sem alterações em templates, modelos, migrações ou demo. Preserva ER-SIRE 2.1, seis entidades históricas e UC01–UC14.

## Fontes reabertas nesta rodada

Documentos originais consultados via Google Docs por IDs exatos: RN (1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0), baseline (19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8), guia (1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U), UC (1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY), requisitos (1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM), CAT (1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is), registro (1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM). Revisões obtidas na API, sem data de modificação comprovada; leitura orientada à identificação do documento e ao gate, não equivale à auditoria integral. Plano de tutorial lido na branch docs/retorno-orientador-tutorial-20261118.

## Roteiro TUT (pendente de execução)

| ID | Papel / cenário | Resultado exigido | Evidência a anexar | Estado |
|---|---|---|---|---|
| TUT-01 | Visitante no catálogo, primeiro acesso | Oferta opcional, botão Como usar persistente; Pular e Fechar não navegam nem submetem | gravação ou capturas sintéticas + URL/commit | Pendente |
| TUT-02 | Passageiro em detalhes/embarque/confirmação/minhas reservas | Instruções coerentes com a página; reserva só ocorre por ação explícita | fluxo sintético e resultado observado | Pendente |
| TUT-03 | Agente em excursões/nova excursão/publicação/reservas/passageiros | Orientação não atravessa permissões nem publica excursão | duas contas sintéticas de agências distintas | Pendente |
| TUT-04 | Teclado e leitor de foco | Anterior/Próximo/Pular/Fechar acessíveis, Escape fecha, foco recuperado | navegador, versão e passos | Pendente |
| TUT-05 | Celular, alvo ausente, lista vazia e sem vagas | Sem bloqueio de tela; instrução ignora ou explica alvo indisponível | viewport e captura | Pendente |
| TUT-06 | Armazenamento local indisponível | Tutorial utilizável sem falha fatal; não persiste CPF, nomes ou dados de reserva | teste com storage bloqueado | Pendente |
| TUT-07 | Reabertura e versão | Não oferece repetidamente após conclusão; Como usar reabre; apenas versão/progresso por perfil | inspeção de storage sintético | Pendente |

## Dependências e limites

- Código identificado no checklist da branch feat/evo-uso-01-tutorial-20261118: sire/static/sire/js/tutorial-uso.js e sire/templates/sire/base.html, commits históricos 91fcede / 6f1045a. Conferir HEAD antes de usar como versão sob teste.
- OAuth drive.file do **aplicativo Django** não foi validado; responsável: autora/operador Google Cloud e Render. Bloqueia fotos reais e aceite de persistência, **não** os cenários TUT de páginas já existentes. Retomar após autorização do app e configuração segura, nunca compartilhar segredos.
- PRs de código e trabalho local de outros agentes podem estar em andamento; comparar HEAD/diff antes de integração. Não modificar template compartilhado sem conciliação.
- Testes TUT e avaliação do orientador não foram executados nesta unidade. Não alegar CI, deploy ou aprovação.

## Rastreabilidade para documentação acadêmica

EVO-USO-01 / TUT-01–07 → tutorial-uso.js, base.html (a conferir no HEAD) → cenários acima (pendentes) → metodologia Modelo Espiral / resultados / limitações (atualização futura, após evidência). UC01–UC14 e baseline continuam históricos, sem renumeração. A solicitação de vídeo do orientador é histórica; a decisão da autora é tutorial interativo, ainda sujeito a validação. Modelo relacional legível e apêndice textual UC01–UC14 continuam pendentes de cotejo com fontes e código.

**Próxima ação:** executar TUT-01–07 com navegadores e perfis sintéticos em branch de ensaio; anexar resultado por caso, SHA e screenshots; só então propor correções, atualizar checklist principal e solicitar avaliação humana. Nenhum merge/deploy nesta unidade.
