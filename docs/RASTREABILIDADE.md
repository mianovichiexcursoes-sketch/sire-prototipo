# Rastreabilidade — ER-SIRE 2.1

Fontes originais consultadas em 20/10/2026, sem alteração:

- [Guia de Implementação](https://docs.google.com/document/d/1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U/edit).
- [Documentação de Desenvolvimento](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit).
- [Especificação de Casos de Uso](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit).

A documentação de desenvolvimento consultada já registrava versão documental
2.4. Isso não substitui a baseline de requisitos ER-SIRE 2.1. O histórico da
conversa sobre revisão de diagramas e o arquivo de continuidade foram usados
para confirmar as decisões. As imagens corrigidas não foram localizadas como
arquivos individuais nesta execução; não se declara nova revisão visual delas.
Os campos e relacionamentos foram conferidos pelo mapeamento do guia original.

Todas as funções abaixo estão em `sire/views.py`, salvo indicação. As rotas
estão em `sire/urls.py`, os forms em `sire/forms.py` e os templates na pasta
`sire/templates/sire/`.

| UC | Requisitos | Função / componente | Template | VF |
| --- | --- | --- | --- | --- |
| UC01 Cadastrar passageiro | RF001, RF003 | cadastro_passageiro; CadastroPassageiroForm | cadastro_passageiro.html | VF01, VF02 |
| UC02 Autenticar usuário | RF002–RF003 | LoginView e LogoutView do Django; exigir_perfil | login.html; base.html | VF03 |
| UC03 Consultar catálogo | RF012 | catalogo | catalogo.html | VF09 |
| UC04 Pesquisar excursões | RF013 | buscar_excursoes | catalogo.html | VF09 |
| UC05 Consultar detalhes | RF015, RF023 | detalhe_excursao; Excursao.calcular_disponibilidade | detalhe_excursao.html | VF10 |
| UC06 Cadastrar excursão | RF004–RF005, RF010 | cadastrar_excursao; ExcursaoForm | excursao_form.html | VF04 |
| UC07 Editar excursão | RF006 | editar_excursao; Excursao.clean | excursao_form.html | VF05; capacidade |
| UC08 Cadastrar ponto de embarque | RF007 | cadastrar_ponto_embarque; PontoEmbarqueForm | ponto_embarque_form.html | VF06 |
| UC09 Publicar excursão | RF010–RF011 | publicar_excursao; Excursao.pode_publicar | agente_excursoes.html (POST) | VF07–VF08 |
| UC10 Realizar reserva | RF016, RF023 | realizar_reserva; Reserva.clean | detalhe_excursao.html | VF11–VF13 |
| UC11 Selecionar ponto de embarque | RF017 | ReservaForm; validação em Reserva.clean; incluído em UC10 | detalhe_excursao.html | VF11–VF12 |
| UC12 Consultar minhas reservas | RF019 | minhas_reservas | minhas_reservas.html | VF14 |
| UC13 Consultar reservas da excursão | RF020 | reservas_excursao | reservas_excursao.html | VF15 |
| UC14 Consultar passageiros da excursão | RF021 | passageiros_excursao | passageiros_excursao.html | VF16 |

`agente_excursoes` organiza o acesso aos UC06–UC09 e UC13–UC14; não representa
um novo caso de uso. Não existe página independente para UC11.

## Seis entidades e persistência

| Entidade | Model | Tabela | Migração |
| --- | --- | --- | --- |
| Usuario | django.contrib.auth.models.User | auth_user | internas do Django |
| Agencia | Agencia | sire_agencia | 0001_initial |
| PerfilUsuario | PerfilUsuario | sire_perfil_usuario | 0001_initial |
| Excursao | Excursao | sire_excursao | 0002_excursao |
| PontoEmbarque | PontoEmbarque | sire_ponto_embarque | 0003_pontoembarque |
| Reserva | Reserva | sire_reserva | 0004_reserva |

`usuario` no perfil é OneToOne. `agencia_id` é nullable; a validação e uma
restrição de integridade exigem agência para AGENTE e ausência para PASSAGEIRO.
Não foram adicionados campos às entidades além dos previstos no guia.
Restrições de valor, capacidade e status reforçam regras sobre os campos
existentes. Tabelas internas do framework não constituem entidades do domínio.

## Onde localizar as regras

- RN001–RN002: PerfilUsuario.clean, restrição perfil_agencia_compativel e FK de Excursao.
- RN003/RN014: exigir_perfil e get_object_or_404 com filtro de agência nas views privadas.
- RN004: default de Excursao.status e ausência de status no ExcursaoForm.
- RN005: filtro PUBLICADA em catálogo, pesquisa, detalhes e reserva.
- RN006: Excursao.pode_publicar e publicar_excursao, somente POST.
- RN007–RN008: FKs de Reserva, ReservaForm limitado à excursão e Reserva.clean.
- RN009–RN012: capacidade positiva, calcular_disponibilidade e reserva transacional.
- RN011 na edição: Excursao.clean executado pelo ModelForm dentro da transação.
- RN013: Reserva.objects.filter(passageiro=request.user) em minhas_reservas.

## Como ler o fluxo de reserva

1. `login_required` exige autenticação; `exigir_perfil` exige PASSAGEIRO.
2. A excursão é buscada com status PUBLICADA.
3. O form só aceita um ponto contido no queryset dessa excursão.
4. No POST válido, `transaction.atomic()` inicia a transação IMMEDIATE.
5. A excursão é relida; `Reserva.full_clean()` confirma perfil, publicação,
   pertencimento do ponto e disponibilidade atual.
6. `Reserva.save()` grava uma reserva; a transação confirma a gravação.
7. A próxima contagem já inclui essa reserva. O passageiro é redirecionado para
   Minhas reservas com mensagem de sucesso.

Não há camada de services/repositories ou alteração dos diagramas aprovados.
