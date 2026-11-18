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

### Numeração válida (nota de 18/11/2026)

Os identificadores RF001–RF023, RNF001–RNF007 e RN001–RN014 usados aqui são os
da **Documentação de Desenvolvimento** (seções 3.2, 3.3 e 3.4), que contém a
baseline ER-SIRE 2.1. Na pasta central também existem dois documentos mais
antigos com **outra numeração**, que não deve ser misturada com esta:

- "Especificação de Requisitos de Software — SIRE" (versão 3.0, PFC2), com
  RF-01–RF-23, RD-01–RD-09 e uma lista própria de RN-01–RN-14. Exemplo: nela,
  o RF-05 é "Editar excursão" e o RF-18 aparece como Protótipo. Na baseline, o
  RF005 é "Cadastro de excursão" e o RF018 é Produto completo.
- "Regras de Negócio do SIRE", com o catálogo ampliado RN-01–RN-41 (visão do
  produto completo). Exemplo: lá, o RN-06 é "Informações mínimas para
  publicação"; na baseline, o RN006 tem esse sentido e o RN008 é "Ponto de
  embarque válido".

Em caso de divergência, vale a Documentação de Desenvolvimento.

Decisões da baseline que explicam o que **não** foi implementado (seção 3.1.8):
(a) e (b) agentes e agências são cadastrados previamente, pela administração
do Django, sem autocadastro; (c) a excursão só tem os estados RASCUNHO e
PUBLICADA; (d) a reserva concluída ocupa vaga, e o ciclo de estados da reserva
(RF018) fica para o produto completo; (e) o cancelamento (RF022) fica para o
produto completo; (f) a publicação exige pelo menos um ponto de embarque.

Todas as funções abaixo estão em `sire/views.py`, salvo indicação. As rotas
estão em `sire/urls.py`, os forms em `sire/forms.py` e os templates na pasta
`sire/templates/sire/`.

| UC | Requisitos | Função / componente | Template | VF |
| --- | --- | --- | --- | --- |
| UC01 Cadastrar passageiro | RF001, RF003 | cadastro_passageiro; CadastroPassageiroForm | cadastro_passageiro.html | VF01, VF02 |
| UC02 Autenticar usuário | RF002–RF003 | LoginView com LoginSireForm e LogoutView do Django; exigir_perfil | login.html; base.html | VF03 |
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

### Requisitos fora da matriz do protótipo (situação em 18/11/2026)

| Requisito | Escopo na baseline | Situação no código | Onde |
| --- | --- | --- | --- |
| RF008 Registro de roteiro | Produto completo (implementação simplificada possível) | Implementado depois da baseline, como extensão (campo `roteiro`, migration 0007; CAT-RF-02) | `ExcursaoForm`; `detalhe_excursao.html` |
| RF009 Informações complementares | Produto completo | Parcial, como extensão: `descricao` e `inclusos` (migration 0007; CAT-RF-02). "Não incluídos" e condições comerciais **não** existem | idem |
| RF014 Filtros de pesquisa | Produto completo | Parcial, como extensão (CAT-RF-01): período de saída e tipo de pacote. O filtro por **local de embarque**, citado no RF014, **não** foi implementado; o tipo de pacote não estava no RF014 | `buscar_excursoes`; `FiltroCatalogoForm` |
| RF018 Situação da reserva | Produto completo (decisão 3.1.8 d) | Não implementado: `Reserva` não tem campo de situação | — |
| RF022 Cancelamento de reserva | Produto completo (decisão 3.1.8 e) | Não implementado | — |

Extensões posteriores à baseline que **não** têm RF correspondente:
- `data_nascimento` em `PerfilUsuario` (migration 0005), informada no cadastro,
  visível ao próprio passageiro e ao agente da excursão (UC14). A finalidade
  está declarada no aviso de privacidade ("identificar o passageiro na lista
  da excursão"), mas nenhum RF da baseline pede esse dado. Ele é uma extensão,
  e não um requisito original (ver RNF002, proteção de dados pessoais).
- Recuperação de acesso por código, aviso de privacidade, troca de senha e
  tutorial "Como usar" (EVO-USO-01).
- Fotos (`FotoExcursao`, migration 0007; CAT-RF-03).

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
As migrations 0001–0004 criam as seis entidades da baseline com os campos
previstos no guia. Restrições de valor, capacidade e status reforçam regras
sobre esses campos. Tabelas internas do framework não constituem entidades do
domínio.

Extensões posteriores à baseline (não alteram 0001–0004):

| Migration | O que acrescenta |
| --- | --- |
| 0005_perfil_data_nascimento | `PerfilUsuario.data_nascimento` (opcional no banco) |
| 0006_excursao_tipo_pacote | `Excursao.tipo_pacote` (opcional) |
| 0007_ficha_e_fotos_drive | `Excursao.descricao`, `roteiro`, `inclusos` e a entidade técnica `FotoExcursao` (sétima tabela de domínio, fora da baseline) |

Observação sobre os modelos: a ERS antiga lista "agente" e "passageiro" como
entidades. Na baseline, ambos são `User` + `PerfilUsuario` (campo `tipo`), sem
um segundo modelo de usuário (Documentação de Desenvolvimento, seção 4.5.3).

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
4. No POST válido, `transaction.atomic()` abre a transação. No SQLite, ela é
   do tipo IMMEDIATE (`settings.py`). No PostgreSQL, a excursão é relida com
   `select_for_update()` (`SELECT … FOR UPDATE`), que bloqueia a linha até o
   fim da transação.
5. Com a linha bloqueada, `Reserva.full_clean()` confirma perfil, publicação,
   pertencimento do ponto e disponibilidade atual.
6. `Reserva.save()` grava uma reserva; a transação confirma a gravação.
7. A próxima contagem já inclui essa reserva. O passageiro é redirecionado para
   Minhas reservas com mensagem de sucesso.

Não há camada de services/repositories ou alteração dos diagramas aprovados.
