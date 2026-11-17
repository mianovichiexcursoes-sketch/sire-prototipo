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
| Testes automatizados | 67 testes; rodam a cada envio em SQLite e PostgreSQL 18 |
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
O único JavaScript é `sire/static/sire/js/mostrar-senha.js`, que acrescenta o
botão “Mostrar” aos campos de senha; sem ele os formulários continuam
funcionando.

### Modelo de dados

As seis entidades da baseline ER-SIRE 2.1 são mantidas. Uma única alteração
posterior foi feita no esquema: o campo opcional `data_nascimento` em
`PerfilUsuario` (migration `0005`), registrado como extensão.


### Ficha ampliada e fotos — segundo incremento em desenvolvimento

A branch `etapa/ficha-fotos-sire` acrescenta descrição, roteiro, inclusos e fotos em uma extensão opcional da ER-SIRE 2.1. Imagens ficam no Google Drive pessoal por OAuth `drive.file`, e o PostgreSQL guarda somente IDs de arquivos. Ainda não foi integrada à demo: exige autorização da conta Google, migração 0007 e validação funcional antes de publicar. O SIRE atual permanece publicado na branch `etapa/postgresql-windows`.

Consulte [projeto técnico e plano de verificação](docs/INCREMENTO_FICHA_FOTOS_DRIVE.md) e execute localmente `scripts/autorizacao_drive.py` após criar credenciais OAuth na Google Cloud. O armazenamento no Google Drive aproveita a cota gratuita da conta, mas não é solução de CDN escalável. Cloudinary, Cloudflare R2 e equivalentes constam como evolução futura, não como dependência atual.

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
fora do Git. As mesmas quatro migrations do domínio criam o esquema; nenhum
dado do SQLite é transferido.

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
