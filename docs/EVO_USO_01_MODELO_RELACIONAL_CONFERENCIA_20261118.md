# EVO-USO-01 — Modelo relacional textual conferido (18/11/2026, 15h BRT)

**Natureza:** anexo técnico de conciliação para o orientador; NÃO substitui o diagrama histórico nem altera a baseline ER-SIRE 2.1. **Não inserido na monografia.**

## Fontes efetivamente lidas
- [Documentação de Desenvolvimento do SIRE, baseline ER-SIRE 2.1](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit), seções de escopo e modelagem.
- [Regras RN-01–RN-41](https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit), em especial RN-01–05, RN-17–30.
- [Registro de Implementação](https://docs.google.com/document/d/1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM/edit), seção 3 (seis entidades e disponibilidade derivada).
- Código efetivo inspecionado: [sire/models.py na branch da demo](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/etapa/postgresql-windows/sire/models.py), [migration 0001](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/etapa/postgresql-windows/sire/migrations/0001_initial.py) e [migration 0006](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/etapa/postgresql-windows/sire/migrations/0006_excursao_tipo_pacote.py). Não houve execução de banco nesta unidade.

## Seis entidades históricas e relacionamentos observados no código
| Entidade lógica | Tabela / origem | Campos e chaves observados em models.py | Relacionamentos e proteção |
|---|---|---|---|
| Usuário | `auth_user` (Django `User`) | campos do Django não reproduzidos neste anexo | 1:1 PerfilUsuario; 1:N Reserva |
| Agência | `sire_agencia` | `id` PK, `nome` | 1:N PerfilUsuario (opcional); 1:N Excursao; PROTECT na exclusão referenciada |
| PerfilUsuario | `sire_perfil_usuario` | `id` PK, `usuario_id` único/FK, `tipo`, `agencia_id` FK opcional | AGENTE exige agência, PASSAGEIRO não a possui; constraint `perfil_agencia_compativel` |
| Excursao | `sire_excursao` | `id` PK, `titulo`, `destino`, `data_saida`, `data_retorno`, `valor`, `capacidade`, `status`, `agencia_id` | 1:N PontoEmbarque e Reserva; capacidade positiva, valor não negativo, status RASCUNHO/PUBLICADA |
| PontoEmbarque | `sire_ponto_embarque` | `id` PK, `local`, `horario`, `excursao_id` | FK excursão CASCADE; Reserva aponta para ponto com PROTECT |
| Reserva | `sire_reserva` | `id` PK, `data_reserva`, `passageiro_id`, `excursao_id`, `ponto_embarque_id` | FKs PROTECT; `clean()` verifica perfil, embarque da excursão, publicação e vaga |

**Disponibilidade não é entidade:** `Excursao.calcular_disponibilidade()` retorna `capacidade - reservas.count()`. A garantia de concorrência exige inspecionar também o fluxo transacional de `views.py` e testar PostgreSQL; não se conclui atomicidade apenas pelo método do modelo.

## Evoluções — separadas da baseline
| Incremento | Evidência do código da branch inspecionada | Situação de rastreabilidade |
|---|---|---|
| Data de nascimento | `PerfilUsuario.data_nascimento` opcional, comentário remete à migration 0005 | Verificar arquivo exato `0005_perfil_data_nascimento.py` antes de afirmar migração |
| Classificação | `Excursao.tipo_pacote` opcional; migration `0006_excursao_tipo_pacote.py` lida | Incremento CAT, não sétima entidade histórica |
| Ficha | `Excursao.descricao`, `roteiro`, `inclusos` no models.py da branch consultada | Verificar migration 0007 e branch/PR de origem antes de declarar integração |
| Fotos | `FotoExcursao` com `excursao_id`, `drive_id` único, `criada_em`; `db_table=sire_foto_excursao` | **Sétima entidade evolutiva, não baseline**. Não comprovada persistência real no Drive |
| CPF | Não consta do `PerfilUsuario`/ `Reserva` inspecionados nesta branch | Não inferir implantação; EVO-RF-05 exige finalidade LGPD, validação e testes sintéticos |
| Tutorial | Não altera o esquema relacional por requisito; estado no navegador sem dados pessoais | EVO-USO-01; testes TUT pendentes de evidência real |

**Atenção à divergência de branches:** `models.py` da branch `etapa/postgresql-windows` contém campos de ficha/fotos, mas a busca direta pelo nome presumido `0007_ficha_fotos.py` nessa branch retornou 404. Isto **não** prova ausência da migration: conferir listagem de arquivos, branch e HEAD atuais. Não executar `migrate` ou deploy sem reconciliar modelos e migrations.

## Rastreabilidade acadêmica
- RN-01–05 → PerfilUsuario/Agencia/Excursao e autorização das views → UC06–UC09, UC13–UC14 → VF03–VF08/VF15–VF16 → documentação seção 4 (modelagem) e seção 5 (verificação).
- RN-17–30 → Reserva/Excursao/PontoEmbarque + transação das views → UC10–UC12 → VF10–VF14 → seções 4 e 5. **Não confundir código inspecionado com teste executado.**
- CAT-RF-02/03/04 → campos de ficha, FotoExcursao, migration aditiva a verificar → CAT-VF-02/03/04/06 → extensão técnica separada.
- EVO-USO-01 → navegação e tutorial por perfil (sem nova entidade) → TUT-01–06 propostos → nova volta da espiral, ainda sem avaliação humana.

## Próximas ações objetivas
1. Inspecionar a árvore real de migrations e PR #2 para identificar o nome e o HEAD da 0007; confrontar `models.py` com `makemigrations --check --dry-run` em ambiente isolado.
2. Confrontar o diagrama original da seção 4.4 com este quadro e registrar diferenças sem reescrever o histórico.
3. Acrescentar o quadro como **anexo evolutivo** ao documento principal após conciliação com edição paralela; verificar leitura pós-gravação.
4. Completar o apêndice UC01–UC14 com os fluxos integrais da especificação oficial, sem inventar resultados de VF/TUT.
5. Executar testes de tutorial e autorização com usuários sintéticos; não publicar sem revisão.

**Estado:** modelo textual de código conferido; equivalência integral com o diagrama, migrações e banco real **pendente**. Nenhum merge, teste, migração ou deploy realizado nesta unidade.
