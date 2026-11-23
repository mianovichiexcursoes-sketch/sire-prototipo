# SIRE — Sistema de Reserva de Excursões

[![Testes](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/workflows/testes.yml/badge.svg)](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/workflows/testes.yml)

Protótipo acadêmico do PFC/TCC de Engenharia Elétrica do IFSP Câmpus Sertãozinho,
de Julia Mianovichi. Aplicação web para consulta e reserva de excursões
rodoviárias. Baseline de requisitos: **ER-SIRE 2.1** (14 casos de uso, três
atores, seis entidades).

O desenvolvimento foi **assistido por IA** (Codex e Claude Code), sob orientação
da autora. Os commits identificam essa assistência; o código não deve ser
apresentado como escrito sem ela.

## Situação

| Item | Estado |
| --- | --- |
| UC01–UC14 da baseline | Implementados |
| Banco de dados | SQLite (padrão) ou PostgreSQL, por variável de ambiente |
| Testes automatizados | Suíte geral, fotos SQLite/PostgreSQL e tutorial no navegador com CI aprovado na PR #18 |
| Reservas simultâneas | Verificadas no PostgreSQL, sem exceder a capacidade |
| Demonstração publicada | <https://sire-demo.onrender.com> (dados fictícios) |
| Extensões fora da baseline | Login sem distinção de maiúsculas; recuperação e troca de senha; data de nascimento; aviso de privacidade |

## Tecnologias

| Componente | Versão |
| --- | --- |
| Python | 3.14 |
| Django | 6.1.2 |
| PostgreSQL | 18 (driver psycopg 3.3.9) |
| SQLite | o que acompanha o Python |
| Hospedagem da demonstração | Render, plano gratuito (gunicorn + WhiteNoise) |

Sem framework de front-end nem API separada: as telas são templates do Django.
O JavaScript do protótipo inclui o botão Mostrar/Ocultar senha e a ajuda contextual `tutorial-uso.js`. O tutorial não concede permissões nem executa formulários.

### Modelo de dados

As seis entidades históricas da baseline ER-SIRE 2.1 são mantidas. Extensões posteriores, identificadas separadamente: data de nascimento (`0005`), classificação do pacote (`0006`) e ficha/fotos com entidade técnica FotoExcursao (`0007`).


### Estado da demonstração e evidências (18/11/2026)

A [PR #18](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/18) integrou a **ficha ampliada com descrição, roteiro e inclusos**, imagens armazenadas no Google Drive, aviso de privacidade e orientação contextual **“Como usar”**. A migração `0007` introduziu a entidade técnica `FotoExcursao`, extensão posterior à baseline ER-SIRE 2.1. A demonstração está no [Render](https://sire-demo.onrender.com), na branch `etapa/postgresql-windows`; consulte o deploy mais recente para identificar o commit exato em execução.

A [PR #24](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/24) documentou **32 capturas reais** (11 no Render como Visitante e 21 em ambiente local isolado como Agente e Passageiro). A [PR #28](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/28), já integrada, corrigiu as referências e acrescentou as matrizes UC01–UC14 × VF01–VF16, CAT-VF e TUT-01–06 ao [relatório de aceite](docs/ACEITE_FUNCIONAL_FINAL_20261118.md). Foram relatados **13 itens aprovados, três com ressalvas, um bloqueado e zero falhas** nessa rodada; VF01, VF02 e VF12 não foram repetidos. Os screenshots estão em [evidencias/2026-11-18_aceite_final/](evidencias/2026-11-18_aceite_final/) e em [pasta privada no Drive](https://drive.google.com/drive/folders/1ijoatraiI5seo-tVyveDX2uIuJCRcstF).

O OAuth Google Drive `drive.file` e 13 verificações de fotos foram exercitados em **PostgreSQL local**, conforme [relatório de Drive real](docs/OAUTH_EXECUCAO_REAL_2026-11-18.md). A galeria de uma excursão foi visualizada no Render, mas **nenhum novo upload nem persistência pós-redeploy no Render foram demonstrados nessa última rodada**. A concorrência foi ensaiada anteriormente em PostgreSQL e não repetida no último teste SQLite. O professor ainda não avaliou o tutorial; a apresentação móvel possui ressalva de sobreposição do painel.

A [monografia em PDF](https://drive.google.com/file/d/1jeciw6ftt-ESq3d6NhZYIzcawjeirhH0/view) (54 páginas, revisão editorial de 23/11/2026), a [documentação de desenvolvimento em PDF](https://drive.google.com/file/d/18VHWoS8TOXs_76lOk-3hS0cfjTRkftVh/view) (99 páginas, com UC01–UC14 no Apêndice A) e o [índice do pacote de revisão](https://drive.google.com/file/d/1RA5TaencNLAJ6-B382KPJCpqTwoiZdeJ/view) estão organizados para conferência. **Não houve envio ao orientador**. Não tratar CPF, pagamentos, assentos ou escalabilidade como funcionalidades comprovadas.

## Executar no Windows

Na pasta que contém `manage.py`, no PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Acesse <http://127.0.0.1:8000/>. Sem nenhuma configuração, o banco é SQLite.

### Usar PostgreSQL

Copie `.env.example` para `.env` e preencha a senha do banco. O `.env` fica
fora do Git. As migrations preservam as quatro primeiras etapas do domínio e adicionam extensões posteriores, sem migrar automaticamente dados existentes do SQLite.

### Dados de demonstração

```powershell
$env:SIRE_DEMO_SENHA = "uma-senha-so-para-a-demo"
.\.venv\Scripts\python.exe manage.py criar_demo
```

Cria uma agência, as contas `demo_agente` e `demo_passageiro` (sem acesso ao
Admin) e três excursões fictícias. Agências e agentes reais são pré-cadastrados
pelo Admin; passageiros se cadastram pela interface pública.

## Testes

```powershell
.\.venv\Scripts\python.exe manage.py test
```

| Arquivo em `sire/tests/` | Cobre |
| --- | --- |
| `test_cenarios_vf.py` | VF01–VF16 da baseline, UC07-E3 e autorizações |
| `test_login.py` | Login sem distinção de maiúsculas no usuário |
| `test_recuperacao.py` | Código de recuperação, cadastro com e-mail, recuperação por e-mail |
| `test_conta.py` | Data de nascimento, aceite de privacidade, Minha conta, troca de senha |
| `test_concorrencia.py` | Reservas simultâneas; executa somente em PostgreSQL |

A integração contínua (`.github/workflows/testes.yml`) roda a suíte em SQLite e
em PostgreSQL 18 a cada envio. Em SQLite, os dois testes de concorrência são
pulados, porque o mecanismo em teste é o bloqueio de linha do PostgreSQL.

`scripts/teste_concorrencia.py` repete o ensaio de concorrência com um servidor
real e requisições HTTP, e grava a saída em `evidencias/`.

## Como a capacidade é protegida

A disponibilidade é sempre calculada: `capacidade − reservas`. Não há contador
nem campo de vagas. Na reserva (`sire/views.py`, `realizar_reserva`):

1. abre-se uma transação (`transaction.atomic`);
2. a excursão é lida com `select_for_update()`, que no PostgreSQL bloqueia a
   linha até o fim da transação;
3. as vagas são recontadas depois do bloqueio (`Reserva.full_clean`);
4. a reserva é gravada na mesma transação.

Uma segunda reserva da mesma excursão espera no passo 2 e, ao prosseguir, já
enxerga a primeira. No SQLite, `select_for_update()` é ignorado e quem
serializa as gravações é o modo `IMMEDIATE` configurado em `settings.py`.

## Recuperação de senha (extensão)

Ao criar a conta, o SIRE mostra um **código de recuperação**. Quem esquece a
senha informa usuário e código e define uma senha nova. O código não é gravado:
é calculado a partir da chave secreta do servidor, do identificador da conta e
do hash da senha (`sire/recuperacao.py`), sem campo, tabela ou migration novos.
Ao trocar a senha, o código muda. O envio de link por e-mail existe como opção
secundária e depende de um provedor configurado.

## Limites conhecidos

- A capacidade é garantida pela aplicação, não por restrição no banco: uma
  gravação feita por fora da view de reserva não é impedida.
- A baseline não limita a uma reserva por passageiro por excursão.
- Os ensaios de concorrência usam poucas requisições, em uma máquina; não medem
  carga, desempenho ou escalabilidade.
- Não há cancelamento, pagamento, assentos, lista de espera nem notificações.
- O usuário troca a própria senha em “Minha conta”, mas não altera e-mail,
  nome ou data de nascimento, nem exclui a conta pela interface.
- O aviso de privacidade é informativo; não foi revisado por profissional da
  área jurídica.
- O limite de tentativas da recuperação fica na memória do processo.
- A demonstração usa plano gratuito: o serviço hiberna sem uso e o banco tem
  prazo de validade. Não é ambiente de produção.
- Não houve avaliação de usabilidade com usuários externos.

## Documentação

| Arquivo | Conteúdo |
| --- | --- |
| `docs/RASTREABILIDADE.md` | Caso de uso → função → tela → cenário VF |
| `docs/VERIFICACAO.md` | Verificação funcional original, em SQLite (20/10/2026) |
| `docs/POSTGRESQL_E_CONCORRENCIA.md` | Migração para PostgreSQL e ensaios de concorrência |
| `docs/CICLO_LOGIN_E_RECUPERACAO.md` | Ciclos do login e da recuperação de senha |
| `docs/ANDAMENTO.md`, `docs/REVISAO_20-10-2026.md` | Registro da primeira entrega |
| `evidencias/` | Saída bruta dos ensaios e capturas de tela |

Os documentos de outubro descrevem o estado daquela data e foram mantidos como
registro histórico.

## Histórico

A `main` reúne as três iterações. As etapas ficaram registradas nas branches
`etapa/postgresql-windows` e `etapa/login-sem-distincao`. Os commits de
20/10/2026 foram recuperados do arquivo `historico-sire.bundle`, sem alteração.
