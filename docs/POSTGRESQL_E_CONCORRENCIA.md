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

## Execução completa de 12/11/2026, 09:54 — Testes A, B, C e VF afetados

SIRE completo (Django + `runserver`) sobre o PostgreSQL 18.6 do Windows, banco
`sire`, usuário `sire_app`, isolamento READ COMMITTED. Cinco rodadas por teste.
Saída bruta em `evidencias/2026-11-12_0954_postgresql_windows/`
(`ambiente.txt`, `relatorio.txt`, `resultados.json`).

| Teste | Situação inicial | Rodadas | Vagas ini→fim | Confirmações | Recusas | Persistidas | Erros | Excesso | Duração (ms) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 2 passageiros distintos, 1 vaga | 5 | 1→0 em todas | 1 em todas | 1 em todas | 1 em todas | 0 | 0 | 613–685 |
| B | 10 passageiros distintos, 3 vagas | 5 | 3→0 em todas | 3 em todas | 7 em todas | 3 em todas | 0 | 0 | 1843–1919 |
| C | Mesmo passageiro, 2 sessões, 5 vagas | 5 | 5→3 em todas | 2 em todas | 0 | 2 em todas | 0 | 0 | 700–823 |

No Teste C, o mesmo passageiro ficou com duas reservas em todas as rodadas. É o
comportamento previsto: a baseline ER-SIRE 2.1 não limita a uma reserva por
passageiro por excursão, e nenhuma regra de unicidade foi criada.

| Verificação | Esperado | Obtido | Situação |
| --- | --- | --- | --- |
| VF10 | Disponibilidade exibida 2 − 1 = 1 | HTTP 200; vagas exibidas: 1 | Conforme |
| VF11 | Reserva confirmada com vínculos corretos | HTTP 200; 1 reserva; passageiro, excursão e embarque corretos | Conforme |
| VF12 | Embarque de outra excursão rejeitado; total inalterado | HTTP 200; rejeitado; reservas 1 → 1 | Conforme |
| VF13 | Excursão lotada: mensagem, sem nova reserva, sem HTTP 500 | HTTP 200; mensagem de lotação; reservas 2 → 2 | Conforme |
| UC07-E3 | Capacidade 2 → 1 com 2 reservas: recusada | HTTP 200; capacidade permaneceu 2; mensagem de erro exibida | Conforme |
| Autorização da reserva | Agente: HTTP 403; RASCUNHO: HTTP 404 | Agente: HTTP 403; rascunho: HTTP 404; nenhuma reserva criada | Conforme |

As durações incluem a espera pelo bloqueio e servem só para mostrar que as
requisições se sobrepuseram; não são medida de desempenho. VF01–VF09 e
VF14–VF16 não foram reexecutados no PostgreSQL.

## Três evidências distintas

1. **SQLite (20 e 22/10/2026):** VF01–VF16 por HTTP, em `VERIFICACAO.md`.
2. **Mecanismo de bloqueio no PostgreSQL 16.15 em nuvem (11/11/2026):** ensaio
   com `pgbench`, sem Django, registrado no Drive. Comprova o comportamento do
   banco, não o SIRE em execução.
3. **SIRE completo no PostgreSQL 18.6 do Windows (12/11/2026):** esta seção.

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
