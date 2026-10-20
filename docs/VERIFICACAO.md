# Verificação funcional — 20/10/2026

## Método e ambiente

Execução pontual por HTTP real em servidor Django local, usando urllib, cookies de
sessão e tokens CSRF. O ORM foi usado para preparar agentes/agências e observar
a persistência. O código auxiliar ficou em scratch, fora do projeto; não foi
criada uma suíte automatizada, nem executado teste de regressão. Esta evidência
é programática pelo terminal e não substitui demonstração manual em navegador.

Python 3.12.14; Django 6.1.2; SQLite 3.53.1. Banco exclusivo de desenvolvimento
gerado pelas migrations, com dados fictícios. Senhas temporárias não registradas.

## Resultados observados

| Cenário | Procedimento | Resultado observado | Situação |
| --- | --- | --- | --- |
| VF01 | Cadastro público | http: 200; usuario: True; perfil: [['PASSAGEIRO', None]] | Conforme em HTTP |
| VF02 | Repetir identificador | http: 200; contas: 1; erro_duplicado: True | Conforme em HTTP |
| VF03 | Login de Passageiro e Agente e acesso privado | login_http: [200, 200]; passageiro_minhas: 200; agente_area: 200; passageiro_area_agente: 403 | Conforme em HTTP |
| VF04 | Criar excursão com tentativa de forjar agência/status | http: 200; status: RASCUNHO; agencia_correta: True | Conforme em HTTP |
| VF05 | Tentar editar excursão de outra agência | http: 404; titulo_preservado: True | Conforme em HTTP |
| VF06 | Cadastrar embarque | http: 200; local: Terminal A; excursao_correta: True | Conforme em HTTP |
| VF07 | Publicar sem embarque | http: 200; status: RASCUNHO | Conforme em HTTP |
| VF08 | Publicar excursão válida | http: 200; status: PUBLICADA | Conforme em HTTP |
| VF09 | Catálogo e pesquisa | http: 200; publicada_visivel: True; rascunho_oculto: True; pesquisa_encontra: True; pesquisa_vazia: True; detalhe_rascunho: 404 | Conforme em HTTP |
| VF10 | Detalhes após reserva | http: 200; disponibilidade: 1; exibe_vagas: True; exibe_embarque: True | Conforme em HTTP |
| VF11 | Reserva com embarque válido | http: 200; reservas: 1; disponibilidade: 1 | Conforme em HTTP |
| VF12 | Tentar reservar embarque de outra excursão | http: 200; reservas_permanecem: 1; erro_selecao: True | Conforme em HTTP |
| VF13 | Tentar reservar excursão lotada | http: 200; reservas: 2; capacidade: 2; erro_sem_vagas: True | Conforme em HTTP |
| VF14 | Consultar reservas do primeiro passageiro | http: 200; propria_visivel: True; outra_oculta: True | Conforme em HTTP |
| VF15 | Reservas da agência e tentativa externa | http_propria: 200; reserva_visivel: True; http_outra: 404 | Conforme em HTTP |
| VF16 | Passageiros da excursão | http: 200; passageiros_visiveis: True; http_outra: 404 | Conforme em HTTP |

O HTTP 200 de POST normalmente é a página final após um redirecionamento ou a
reexibição de um formulário com erro. O status 200 isoladamente não determina
sucesso: foram conferidos também mensagem e/ou registros persistidos. O HTTP
404 para recursos de outra agência é bloqueio intencional sem expor seus dados.

## Verificações adicionais

- Passageiro na área do agente: HTTP 403.
- Agente na reserva: HTTP 403.
- Passageiro na publicação: HTTP 403.
- Tentativa de reduzir capacidade de 2 para 1 com duas reservas: capacidade permaneceu 2.
- Cadastro forjando agência/status: a excursão ficou na agência autenticada e em RASCUNHO.
- Embarque enviado com excursão forjada: foi associado à excursão autorizada da URL.
- Logout por POST encerrou a sessão.
- CSS retornou HTTP 200.
- Página inicial retornou HTTP 200.

Dados brutos: [resultados-http.json](resultados-http.json).

## Comandos executados

```bash
python -m pip install -r requirements.txt
python manage.py check
python manage.py makemigrations sire
python manage.py migrate
python manage.py makemigrations --check --dry-run
python manage.py runserver 127.0.0.1:8012 --noreload
```

Os comandos foram executados com o Python da venv no Work. `check` retornou
“System check identified no issues”; migrations foram aplicadas; o comando final
de detecção retornou “No changes detected”. Os servidores locais foram encerrados.

## Não verificado nesta execução

- Navegação manual e inspeção visual de desktop/mobile: pendentes por falta de navegador executável.
- Execução no Windows e Python 3.14.8: pendentes.
- Concorrência simultânea/carga: não executada; a proteção consta do código, não de evidência de carga.
- Publicação em GitHub ou hospedagem: não realizada.

Os resultados não foram transcritos nos documentos acadêmicos originais.

## Conferência pontual após os ajustes finais

- POST de cadastro vazio: HTTP 200 com erros de campos obrigatórios, sem criação de conta.
- GET direto da reserva lotada: HTTP 200 com indisponibilidade e sem botão de confirmação.
- Renderização após formatação dos templates: catálogo, login, pesquisa e detalhes retornaram HTTP 200.
- `python -m pip check`: nenhuma dependência quebrada.

Essas conferências foram motivadas pela correção de POST vazio e pelo ajuste do
GET de reserva lotada; não constituem repetição de uma suíte de regressão.

A reconstrução em diretório separado, sem banco prévio, também aplicou todas as
migrations internas e as quatro migrations do domínio com sucesso. Nenhum banco
dessa conferência é incluído na distribuição.
