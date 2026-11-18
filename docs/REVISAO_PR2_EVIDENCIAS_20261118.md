# SIRE — Conferência independente do incremento de ficha/fotos (18/11/2026)

**Natureza:** revisão estática do HEAD da PR #2 `faa5ba3d60b7f292be09676b13f39e9276eacafb`. Não é aprovação de testes, de OAuth real nem de publicação. Documento complementar à matriz de verificação; preserva ER-SIRE 2.1, UC01–UC14 e seis entidades originais.

## Fontes conferidas nesta rodada

Documentos originais lidos por ID: RN-01–RN-41 (`1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`), baseline (`19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`), guia (`1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`), UC (`1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`), requisitos (`1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`), CAT revisão 0.2 (`1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`), registro (`1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`). Os demais documentos acadêmicos não foram relidos nesta rodada; auditoria global permanece pendente.

## Conferência objetiva

| Item | Evidência inspecionada | Estado e próxima ação |
| --- | --- | --- |
| CAT-RF-02 / ficha textual | PR #2 inclui `sire/forms.py`, `views.py`, `detalhe_excursao.html` e `excursao_form.html` | **Implementação presente em diff, aceite pendente**: executar CAT-VF-02 e CAT-VF-05 em branch isolada |
| Migração aditiva 0007 | `sire/migrations/0007_ficha_e_fotos_drive.py` depende de `0006_excursao_tipo_pacote`; adiciona três `TextField(blank=True, default="")` e cria `FotoExcursao` com `drive_id` único | **Inspeção estática concluída**: sem remoção de campo na 0007; executar `makemigrations --check --dry-run` e migração em banco descartável antes de aprovação |
| CAT-RF-03 / fotos | `sire/drive_fotos.py` declara limite de seis, entrada de 5 MiB, 20 milhões de pixels, saída JPEG e OAuth `drive.file` | **Inspeção estática parcial**: testar upload/exclusão, permissão entre agências, erro de API e persistência real com autorização própria |
| CAT-VF-03/04/06 | `sire/test_fotos_regressao.py` usa mocks e usuários sintéticos | **Testes presentes, não executados nesta rodada**; conferir execução CI do SHA exato e PostgreSQL, além do fluxo real separado |
| Evidência documental CI | `docs/AUDITORIA_FOTOS_SEGURANCA_20261117.md` cita runs 44080498422 e 44080498754 | **Alegação histórica do documento, não reverificada nesta rodada**; checar jobs/conclusões e associação ao commit antes de declarar aprovado |
| Consistência de documentação | Cabeçalho de `sire/test_fotos_regressao.py` ainda diz que os testes 'detectam o problema atual de cache público' | **Divergência textual potencial** com a auditoria que declara correção de cache. Conferir comportamento real no HEAD e ajustar comentário em branch coordenada; não inferir regressão funcional |

## Dependências e bloqueios

**A — em revisão:** PR #2 permanece aberta e draft; responsável pela integração deve reconciliar alterações de segurança das PRs correlatas sem sobrescrever trabalho Work. Condição de retomada: revisão de diff/branches e resultados reproduzíveis por SHA.

**B — bloqueado para aceite real:** autorização OAuth do aplicativo com escopo `drive.file` e ambiente Render isolado não comprovados; responsável: autora/operador autorizado. Impacto: sem confirmação de upload, exclusão e persistência pós-deploy. Retomar após consentimento e infraestrutura de ensaio, sem segredos em GitHub/chat.

**F — pendente:** CI e regressão atual SQLite/PostgreSQL, CAT-VF01–06, VF afetados e teste visual. **Próxima unidade independente:** conferir logs GitHub Actions do SHA da PR #2 e confrontar a divergência textual do cabeçalho dos testes, sem modificar código em desenvolvimento.

**Sem alterações** em models, migrations, templates, branches de implementação, demo, dados reais ou monografia. Nenhum teste, merge ou deploy executado nesta revisão.
