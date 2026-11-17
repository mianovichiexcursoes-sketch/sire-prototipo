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
