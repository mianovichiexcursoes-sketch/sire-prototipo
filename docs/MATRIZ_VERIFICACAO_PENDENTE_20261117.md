# SIRE — Matriz de verificação pendente (VF01–VF16 e CAT-VF01–06)

Registro documental independente, 17/11/2026 15h55 (Brasília). **Não é resultado de execução.** Baseline ER-SIRE 2.1, UC01–UC14 e seis entidades originais preservados. Fonte primária: regras RN-01–RN-41 (Drive ID 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0), casos de uso (ID 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY), guia (ID 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U), registro técnico (ID 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM), complemento CAT revisão 0.2 (ID 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is).

## Matriz de rastreabilidade e execução

| Cenário | UC / regras relacionadas | Arquivo / superfície a verificar | Evidência exigida | Estado |
|---|---|---|---|---|
| VF01–VF02 | UC01, RN-04/05 | cadastro_passageiro, CadastroPassageiroForm | registro sintético, validações e restrição de acesso | PENDENTE de nova execução |
| VF03 | UC02, RN-05 | LoginView/LogoutView, login.html | autenticação e encerramento de sessão | PENDENTE |
| VF04–VF05 | UC06/07, RN-01–03/06–16 | ExcursaoForm, models, views | cadastro/edição próprios e recusa de outra agência | PENDENTE |
| VF06 | UC08, RN-08/09 | PontoEmbarqueForm, views | ponto associado à excursão correta | PENDENTE |
| VF07–VF08 | UC09, RN-06/10/11 | publicar_excursao, Excursao.pode_publicar | publicação válida/inválida e catálogo | PENDENTE |
| VF09 | UC03/04 | catalogo, buscar_excursoes | busca e filtros conforme versão | PENDENTE |
| VF10 | UC05 | detalhe_excursao, calcular_disponibilidade | dados públicos e disponibilidade | PENDENTE |
| VF11–VF13 | UC10/11, RN-17–30 | realizar_reserva, Reserva.clean | embarque, capacidade, duplicidade, concorrência | PENDENTE |
| VF14–VF16 | UC12–UC14 | views e painéis de reservas | consultas por passageiro/agência e isolamento | PENDENTE |
| CAT-VF01 | CAT catálogo | catalogo.html, filtros | filtros combinados e estados vazios | PENDENTE |
| CAT-VF02 | CAT-RF-02, UC06/07 | models/forms/views, migração 0007 | campos opcionais, dados antigos e edição autorizada | PENDENTE |
| CAT-VF03 | CAT-RF-03 | FotoExcursao, drive_fotos.py | até seis fotos, formatos, tamanho, autorização, exclusão | PARCIAL: CI com Drive simulado; Drive real BLOQUEADO |
| CAT-VF04 | CAT-RF-04, UC05 | detalhe_excursao.html | descrição, roteiro, inclusos, galeria, reserva intacta | PENDENTE |
| CAT-VF05 | CAT catálogo | responsividade CSS/templates | evidência visual desktop/celular | PENDENTE |
| CAT-VF06 | CAT-RF-03/04, RN-03–05 | views de fotos, catálogo e reserva | foto privada de rascunho, isolamento, regressão | PARCIAL: CI simulado; ensaio real BLOQUEADO |

**Limite de mapeamento:** os agrupamentos VF acima são índices de planejamento a conferir com a tabela exata do registro técnico antes de registrar aprovação por cenário. Não substituir descrições oficiais por esta síntese.

## Dependências e critérios de aceite

1. CI de fotos SQLite/PostgreSQL [execução 44097899889](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44097899889) foi previamente confirmado como sucesso para Drive **simulado**; não repetir como se fosse teste real.
2. OAuth real requer cliente próprio com escopo drive.file, autorização da autora, segredos protegidos e ambiente isolado. Sem isso, upload, exclusão e persistência após deploy permanecem **BLOQUEADOS** (responsável: autora/operador autorizado; condição: OAuth funcional em ensaio isolado).
3. CPF é extensão EVO-CPF separada, sem coleta real; implementação aguarda finalidade/base legal e reconciliação de branches. Não altera VF históricos retroativamente.
4. Executar testes isolados e registrar data, SHA, banco, comando, saída, screenshots quando cabíveis e divergências. Não mesclar nem publicar antes de revisão e aceite.
5. Monografia: futura seção de resultados e rastreabilidade; não afirmar verificações inexistentes.


## Conciliação com o registro técnico original — 17/11/2026, 17h (Brasília)

**Leitura primária:** registro de implementação Google Doc ID `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`, seções **5 RESULTADOS OBSERVADOS** e **10.2 Registros individuais**. Esta seção é uma reconciliação de **evidência histórica**, não uma nova execução. A documentação registra testes HTTP/ORM assistidos por IA em 22/10/2026, Python 3.12.14, Django 6.1.2 e SQLite 3.53.1, em banco separado, com artefatos `VFxx.json` e `execucao-2026-10-22.json`. Os arquivos JSON originais **não foram reabertos nesta rodada**: seus resultados permanecem declarações do registro, não confirmação independente dos anexos.

| VF | Resultado histórico descrito no registro de 22/10 (não reexecutado) | Evidência a recuperar/confirmar |
|---|---|---|
| VF01 | cadastro criou User e PerfilUsuario PASSAGEIRO sem agência | VF01.json |
| VF02 | identificador duplicado recusado, uma conta preservada | VF02.json |
| VF03 | login dos dois perfis; passageiro recebeu HTTP 403 na gestão | VF03.json |
| VF04 | excursão criada como RASCUNHO da agência autenticada, ignorando agência/status forjados | VF04.json |
| VF05 | edição de outra agência recebeu HTTP 404, sem alteração | VF05.json |
| VF06 | ponto de embarque vinculado à excursão autorizada na URL | VF06.json |
| VF07 | publicação sem embarque recusada; RASCUNHO preservado | VF07.json |
| VF08 | excursão válida passou a PUBLICADA | VF08.json |
| VF09 | catálogo exibiu publicada, ocultou rascunho, filtrou destino; detalhe de rascunho HTTP 404 | VF09.json |
| VF10 | detalhe exibiu embarque e 1 vaga após reserva em capacidade 2 | VF10.json |
| VF11 | reserva com embarque válido criada, ocupando uma vaga | VF11.json |
| VF12 | embarque de outra excursão recusado, sem criar reserva | VF12.json |
| VF13 | lotação impediu terceira reserva com capacidade 2 | VF13.json |
| VF14 | passageiro viu apenas reservas próprias | VF14.json |
| VF15 | agente consultou reservas próprias; agência alheia HTTP 404 | VF15.json |
| VF16 | agente consultou passageiros próprios; agência alheia HTTP 404 | VF16.json |

**Lacuna identificada:** a tabela anterior rotulava todos os VF como pendentes de nova execução sem distinguir a execução histórica de 22/10. Manter ambos os fatos: (a) há relato histórico individual de conformidade HTTP/ORM; (b) ainda faltam recuperação dos JSON, regressão sobre HEAD atual, PostgreSQL em ensaio isolado, avaliação visual e CAT-VF específicos. Não usar esses relatos para aprovar a PR #2 ou publicar a demo.

**Próxima unidade:** localizar o pacote original de evidências `VFxx.json` no Drive/GitHub e verificar integridade, timestamps, ambiente e associação ao commit original. Em paralelo, reconciliar HEADs das PRs abertas e preservar branch de desenvolvimento em edição pelo Work.


## Confronto documental das evidências históricas — 17/11/2026, 19h55 (Brasília)

**Fontes lidas diretamente nesta unidade:** documentos oficiais pelos 12 IDs do inventário; `docs/resultados-http.json` da branch `etapa/postgresql-windows` (blob `e3323f54f39a995dc479f39bcb384dfc0a599a5e`); e registro técnico de implementação. O ZIP histórico foi localizado e teve sua integridade verificada na rodada anterior, mas **os arquivos individuais internos não foram reabertos nesta unidade**. Esta conciliação confronta os resultados agregados, não executa os cenários.

| Cenários | Resultado verificável no JSON agregado histórico | Limitação para aceite atual |
|---|---|---|
| VF01–VF03 | Cadastro de PASSAGEIRO, recusa de duplicidade, login e 403 para passageiro na área de agente | Não há nova execução nem inspeção de dados de produção |
| VF04–VF06 | Criação como RASCUNHO na agência correta; edição alheia 404; embarque vinculado corretamente | Isolamento requer regressão no HEAD atual |
| VF07–VF09 | Publicação inválida preserva RASCUNHO; válida vira PUBLICADA; catálogo oculta rascunho | Filtros CAT incrementais não foram ensaiados aqui |
| VF10–VF13 | Disponibilidade 1 após reserva; embarque alheio rejeitado; lotação limita 2/2 | Concorrência PostgreSQL atual exige execução separada |
| VF14–VF16 | Passageiro vê apenas próprias reservas; consultas de outra agência retornam 404 | Repetir sobre versão atual e permissões de fotos |
| EXTRA (4 entradas) | Redução indevida de capacidade recusada; papéis; logout POST; CSS/login inválido | Não substituir testes visuais nem CAT-VF |

**VF12 — histórico de falha e correção:** o pacote original recuperado na rodada anterior contém `VF12-primeira-conferencia.json` marcado **não conforme** e `VF12.json` final marcado **conforme**; a versão agregada Git registra `erro_selecao=true` e `reservas_permanecem=1`. Preservar os três registros e sua ordem, sem interpretar o resultado final como ausência de defeito inicial. Para fechar a rastreabilidade, inspecionar os campos completos dos dois JSONs individuais e identificar commit/correção causal, sem inferi-los.

**Estado:** CONCLUÍDO apenas este confronto documental do JSON agregado. VF01–VF16 no código atual, CAT-VF01–06, navegador, OAuth real e persistência pós-deploy continuam PENDENTES/BLOQUEADOS conforme dependências. Próxima unidade: verificar detalhadamente o diff de VF12 inicial/final dentro do ZIP e o vínculo com commit histórico; depois executar regressão isolada sem tocar na demo.
