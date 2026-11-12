# PostgreSQL e ensaio de reservas simultâneas — 12/11/2026

Execução no computador Windows da autora, com assistência de IA (Claude Code).
Complementa `VERIFICACAO.md`, que registrava concorrência como não verificada.

## Ambiente efetivamente utilizado

| Componente | Versão |
| --- | --- |
| Sistema | Windows 11 |
| Python | 3.14.8 |
| Django | 6.1.2 |
| PostgreSQL | 18.6 (serviço local, banco `sire`, usuário `sire_app`) |
| Driver | psycopg 3.3.9, usando a libpq da instalação do PostgreSQL |
| Servidor | `manage.py runserver --noreload` (multithread) |

## O que mudou no código

- `sire_project/settings.py`: banco escolhido por variáveis de ambiente ou `.env`.
  Sem configuração, permanece SQLite, como na entrega original.
- `sire/views.py`: `select_for_update()` na reserva e na edição de capacidade.
  No PostgreSQL gera `SELECT ... FOR UPDATE` e trava a linha da excursão; a
  segunda transação espera a primeira confirmar e só então reconta as vagas.
- `requirements.txt`: inclusão de `psycopg[binary]`.
- `scripts/teste_concorrencia.py`: ensaio reproduzível.
- Models e migrations não foram alterados: as mesmas quatro migrations do
  domínio criaram as tabelas no PostgreSQL. `db.sqlite3` não foi modificado.

## Método do ensaio

Passageiros fictícios autenticados por HTTP real (sessão e CSRF). Os POSTs de
reserva são liberados juntos por `threading.Barrier`. Ao final de cada rodada,
o número de reservas é lido do banco. Os dados fictícios são removidos ao final.

- **Cenário A — última vaga:** capacidade 2, uma reserva prévia; dois
  passageiros disputam a vaga restante.
- **Cenário B — disputa ampla:** capacidade 3; dez passageiros simultâneos.

## Resultados observados

| Banco | Cenário | Rodadas | Conformes | Rodadas com lotação excedida | Respostas fora do esperado |
| --- | --- | --- | --- | --- | --- |
| PostgreSQL 18.6 | A — última vaga | 20 | 20 | 0 | 0 |
| PostgreSQL 18.6 | B — disputa ampla | 5 | 5 | 0 | 0 |
| SQLite 3.50.4 | A — última vaga | 20 | 20 | 0 | 0 |
| SQLite 3.50.4 | B — disputa ampla | 5 | 5 | 0 | 0 |

Em todas as rodadas do cenário A, uma reserva foi gravada e a outra tentativa
recebeu “Não há vagas disponíveis”. No cenário B, três reservas foram gravadas
e sete tentativas foram recusadas por lotação. Em nenhuma rodada o total de
reservas no banco ultrapassou a capacidade.

Dados brutos, com o resultado e os tempos de cada tentativa:
[resultados-concorrencia-postgresql.json](resultados-concorrencia-postgresql.json) e
[resultados-concorrencia-sqlite.json](resultados-concorrencia-sqlite.json).
O ensaio em SQLite usou um banco descartável, fora do projeto.

## Como repetir

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe scripts\teste_concorrencia.py
```

## Limites desta evidência

- Ensaio em uma única máquina, com servidor de desenvolvimento; não é teste de
  carga nem mede desempenho.
- 25 rodadas por banco demonstram o comportamento esperado, não o provam para
  todo cenário possível.
- Não foi executado um contraexemplo sem o bloqueio para comparação.
- A conferência visual em navegador e a publicação da demonstração continuam
  pendentes.
