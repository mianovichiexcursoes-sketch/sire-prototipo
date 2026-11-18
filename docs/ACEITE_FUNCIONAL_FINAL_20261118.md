# Aceite funcional final — SIRE — 18/11/2026

Registro dos testes manuais que foram **executados de verdade no navegador** em 18/11/2026, com 32 prints reais.
Nada aqui foi simulado. Este documento **não** representa aprovação do orientador.
Revisão 2 (consolidação para revisão da autora): mesmos resultados da revisão 1 (PR #24), com a matriz de rastreabilidade acrescentada e duas correções de referência (ver seção 8).

## 1. Onde está cada coisa

| Material | Local |
|---|---|
| Pasta no Drive (privada; só a autora acessa o conteúdo) | https://drive.google.com/drive/folders/1ijoatraiI5seo-tVyveDX2uIuJCRcstF |
| Prints do Render (R01–R11) | subpasta "R01–R11 — Render (produção, visitante)": https://drive.google.com/drive/folders/1ufLz1h9jdCue40qsJJRgPxDXoavrx3iR |
| Prints locais (L01–L21) | subpasta "L01–L21 — Local (ambiente isolado, dados fictícios)": https://drive.google.com/drive/folders/1VCuoXazkm_nPablH-sZFmQv6qgHc0lPk |
| Os mesmos prints no GitHub | `evidencias/2026-11-18_aceite_final/` |
| PR dos testes (integrada) | https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/24 (commit `6879744`, integrada em `07eec77`) |
| Definições VF01–VF16 e UC01–UC14 | `docs/VERIFICACAO.md`, `docs/RASTREABILIDADE.md` e o Registro de Implementação (Google Docs) |
| Definições CAT-VF-01 a 06 | Especificação complementar, seção 5 (Google Docs `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`) |

## 2. Ambientes (não misturar)

| Sigla | Tipo de evidência | Versão | Dados | Perfil |
|---|---|---|---|---|
| **R** | Teste manual **em produção**, no Render (https://sire-demo.onrender.com) | commit `e220974`, conferido no painel do Render antes dos testes | demonstração fictícia já existente; nada criado nem apagado | Visitante (sem login) |
| **L** | Teste manual **local** em http://127.0.0.1:8017, com SQLite próprio do teste | mesmo commit `e220974` | Agência Aceite A e B, agente_a, agente_b, passageiro_1 e passageiro_2, todos fictícios (`@example.test`) | Agente A, Agente B, Passageiro 1 e 2 |
| **A** | Testes **automatizados** (`manage.py test sire`, SQLite) | `e220974` | banco de teste temporário | — |
| **H** | Evidências **anteriores**, **não repetidas** nesta rodada | ver seção 6 | — | — |

- Ferramenta: navegador embutido do Claude Desktop (Chromium), com tela de 1100×760 (computador) e 375×812 (celular emulado).
- Horário (Brasília): Render das 14:45 às 14:48; local das 14:49 às 14:53.
- Senhas: a senha de teste local existe só no banco temporário e não aparece em prints, commits nem documentos. No Render, o assistente não digitou nenhuma senha.
- Testes automatizados: **107 OK, 3 ignorados**. Os 3 ignorados são os de concorrência, que só rodam com PostgreSQL.

## 3. Resumo

| Situação | Quantidade | Cenários |
|---|---|---|
| ✅ Aprovado | 13 | 1, 2, 3, 4, 5, 6, 6b, 7, 8, 9, 10, 12, 13 |
| ⚠️ Aprovado com ressalva | 3 | 9b, 11, 14 |
| ⛔ Bloqueado | 1 | 2b (login no Render) |
| ❌ Falhou | 0 | — |

**Não é "100% aprovado".** VF01, VF02 e VF12 **não foram repetidos** nesta rodada; continuam valendo as evidências HTTP de outubro (seção 5).

## 4. Resultado por cenário

| # | Cenário | Amb. | Procedimento | Esperado | Observado | Status | Prints | Requisito / UC / VF |
|---|---|---|---|---|---|---|---|---|
| 1 | Catálogo e busca | R | Abrir o catálogo; buscar destino "Litoral"; buscar "Inexistente-XYZ" | Lista só as publicadas; o filtro funciona; a busca vazia avisa | 3 publicadas; "Litoral" → 1 (Praia fictícia); "Inexistente-XYZ" → 0, com "Nenhuma excursão publicada encontrada." (conferido no texto da página, sem print) | ✅ | R01, R05 | RF012, RF013 · UC03, UC04 · VF09 · CAT-VF-01 (parcial) |
| 2 | Login de passageiro e agente | L | Entrar como `AGENTE_A` (em maiúsculas), passageiro_1, passageiro_2 e agente_b | Cada perfil vê o próprio menu | Agente: "Excursões da agência"; passageiro: "Minhas reservas". O login com maiúsculas funcionou | ✅ | L01, L10, L19 | RF002–RF003 · UC02 · VF03 |
| 2b | Login no Render | R | — | — | **Não executado**: a sessão de demonstração expirou, e o assistente não digita senha em site público | ⛔ | — | UC02 · VF03 |
| 3 | Agente cria excursão | L | Nova excursão "ACEITE A — Cachoeira fictícia", com descrição, roteiro, inclusos e capacidade 2 | Salva em RASCUNHO | "Excursão cadastrada em RASCUNHO." | ✅ | L03, L04 | RF004–RF005, RF010 · UC06 · VF04 · CAT-VF-02 (parcial) |
| 4 | Publicar sem embarque | L | Clicar em Publicar sem ponto de embarque | Recusa; continua em rascunho | "Publicação exige RASCUNHO, dados válidos e ao menos um ponto de embarque." | ✅ | L05 | RF010–RF011 · UC09 · VF07 |
| 5 | Embarque e publicação | L | Adicionar "Praça Aceite A (fictícia) — 06:00" e publicar | Embarque salvo; status Publicada | "Ponto de embarque cadastrado." e "Excursão publicada no catálogo." | ✅ | L06 | RF007, RF010–RF011 · UC08, UC09 · VF06, VF08 |
| 6 | Publicada aparece no catálogo | L | Buscar "Cachoeira" | Aparece, com a agência A | Aparece "ACEITE A — Cachoeira fictícia", da Agência Aceite A | ✅ | L08 | RF012–RF013 · UC03, UC04 · VF09 |
| 6b | Rascunho escondido do visitante | R | Abrir `/excursao/3/` | Não abre | HTTP 404 | ✅ | R08 | UC05 · VF09 · CAT-VF-04 (parcial) |
| 7 | Reserva e Minhas reservas | L | passageiro_1 escolhe o embarque e confirma | Reserva criada e listada | "Reserva realizada com sucesso."; Reserva nº 1 aparece em Minhas reservas | ✅ | L12, L13 | RF016–RF017, RF019 · UC10, UC11, UC12 · VF11, VF14 |
| 8 | Agente consulta a reserva | L | agente_a abre Reservas e Passageiros | Mostra as reservas e os embarques | "Disponibilidade: 0 de 2 vagas"; reservas 1 e 2 com nome, nascimento e embarque | ✅ | L17, L18 | RF020, RF021 · UC13, UC14 · VF15, VF16 · CAT-VF-06 · TUT-06 |
| 9 | Disponibilidade e lotação | L | Capacidade 2: passageiro_1 e passageiro_2 reservam; passageiro_2 tenta de novo pela tela e por envio direto | Vagas 2 → 0; terceira reserva recusada | 0 vagas; "Não há vagas disponíveis."; o formulário some; o envio direto também é recusado; total fica em 2 | ✅ | L16 | RF015, RF023 · UC05, UC10 · VF10, VF13 |
| 9b | Concorrência | A + H | Os testes automatizados de concorrência ficaram ignorados (não há PostgreSQL); não houve teste manual simultâneo | Nenhuma reserva acima da capacidade | Não repetido nesta rodada. Há evidência anterior com PostgreSQL (seção 6) | ⚠️ | — | RF023 · UC10 |
| 10 | Isolamento entre perfis e agências | L | Passageiro abre a área do agente; agente_a abre a excursão da B; agente_b abre editar, reservas e passageiros da A; passageiro_2 abre Minhas reservas | Bloquear tudo | Passageiro: 403. A → B: 404. B → A: 404 nas três páginas. passageiro_2 não vê a reserva do passageiro_1 | ✅ | L09, L14, L15, L19, L20 | RF003, RF006, RF019–RF021 · UC07, UC12–UC14 · VF03, VF05, VF14–VF16 · CAT-VF-02 (parcial) |
| 11 | Ficha, roteiro, inclusos e galeria | L + R | Ver a ficha da excursão nova (L); ver a Praia fictícia com foto (R) | Seções exibidas; foto carregada | L: "Sobre o pacote", "Roteiro da viagem" e "O que está incluso" corretos. R: 1 foto carregada pelo próprio SIRE, sem link do Drive na página. Sem Drive, a edição local mostra um aviso e os outros campos continuam editáveis. **Nenhuma foto nova foi enviada** | ⚠️ | L07, L12, R06, R07 | CAT-RF-02/03/04 · UC05–UC07 · CAT-VF-04 (parcial); CAT-VF-03 não repetido |
| 12 | Tutorial por perfil | R + L | Abrir o tutorial como visitante, agente e passageiro | Textos e destaques certos para cada perfil | Ver seção 7 | ✅ | R01, R02, L01, L02, L10, L11 | EVO-USO-01 · TUT-01, TUT-02 |
| 13 | Próximo, Voltar, Pular, reabrir e Esc | R + L | Usar todos os botões e a tecla Esc | Navega, fecha, reabre e devolve o foco | Ver seção 7 | ✅ | R02, R03, R04, L11 | EVO-USO-01 · TUT-01, TUT-03, TUT-04 |
| 14 | Computador e celular | R + L | Tela de 1100 px e de 375 px | Sem rolagem lateral; menu e tutorial usáveis | Em 375 px não há rolagem lateral; o painel do tutorial cobre a parte de baixo da tela enquanto está aberto | ⚠️ | R10, R11, L21 | CAT-RNF-01 · CAT-VF-05 (parcial) · TUT-03 |

## 5. Matriz de rastreabilidade — baseline ER-SIRE 2.1 (UC01–UC14, VF01–VF16)

A correspondência entre UC, requisito e VF foi copiada de `docs/RASTREABILIDADE.md`, sem alterações. A coluna "Outubro" resume o resultado histórico (HTTP em 20/10 e 22/10, registrado em `docs/VERIFICACAO.md` e no Registro de Implementação, seção 10). A coluna "18/11" mostra o que foi refeito nesta rodada.

| UC | Requisitos | VF | Outubro (histórico) | 18/11 (esta rodada) | Prints |
|---|---|---|---|---|---|
| UC01 Cadastrar passageiro | RF001, RF003 | VF01, VF02 | Conforme (HTTP) | **Não repetido** | — |
| UC02 Autenticar usuário | RF002–RF003 | VF03 | Conforme (HTTP) | ✅ local (login e bloqueio 403); ⛔ Render | L01, L10, L14, L19 |
| UC03 Consultar catálogo | RF012 | VF09 | Conforme (HTTP) | ✅ Render e local | R01, L08 |
| UC04 Pesquisar excursões | RF013 | VF09 | Conforme (HTTP) | ✅ Render (com resultado e sem resultado) e local | R05, L08 |
| UC05 Consultar detalhes | RF015, RF023 | VF10 | Conforme (HTTP) | ✅ Render (40 vagas) e local (2 → 0); rascunho dá 404 | R07, R08, L12, L16 |
| UC06 Cadastrar excursão | RF004–RF005, RF010 | VF04 | Conforme (HTTP, inclusive com agência e status forjados) | ✅ local, criada em rascunho. O teste com dados forjados **não foi repetido** | L03, L04 |
| UC07 Editar excursão | RF006 | VF05 | Conforme (HTTP) | ✅ local: edição de outra agência dá 404. Salvar a edição da própria excursão **não foi feito** | L09, L20 (L07 mostra a tela de edição) |
| UC08 Cadastrar ponto de embarque | RF007 | VF06 | Conforme (HTTP) | ✅ local | L06 |
| UC09 Publicar excursão | RF010–RF011 | VF07, VF08 | Conforme (HTTP) | ✅ local: recusa sem embarque; publica com embarque | L05, L06 |
| UC10 Realizar reserva | RF016, RF023 | VF11, VF12, VF13 | Conforme (HTTP) | ✅ VF11 e VF13 local. VF12 (embarque de outra excursão) **não foi repetido** | L12, L13, L16 |
| UC11 Selecionar ponto de embarque | RF017 | VF11, VF12 | Conforme (HTTP) | ✅ VF11 local. VF12 **não foi repetido** | L12 |
| UC12 Consultar minhas reservas | RF019 | VF14 | Conforme (HTTP) | ✅ local, inclusive passageiro_2 sem ver a reserva do passageiro_1 | L13, L15 |
| UC13 Consultar reservas da excursão | RF020 | VF15 | Conforme (HTTP) | ✅ local; outra agência dá 404 | L17, L09 |
| UC14 Consultar passageiros da excursão | RF021 | VF16 | Conforme (HTTP) | ✅ local; outra agência dá 404 | L18, L20 |

Resumo por VF nesta rodada: **refeitos e conformes** VF03 a VF11 e VF13 a VF16 (13 de 16); **não repetidos** VF01, VF02 e VF12. VF03 ficou bloqueado só no Render.

### Extensão do catálogo (CAT-VF, especificação complementar, seção 5)

| CAT-VF | Definição (resumo) | 18/11 | Prints |
|---|---|---|---|
| CAT-VF-01 | Combinar filtros, testar limites de data, nenhum resultado e limpar | **Parcial**: filtro por destino com resultado e sem resultado. Datas, tipo e limpeza não foram refeitos (foram conformes em 16/11, conforme a seção 7 da especificação) | R05, L08 |
| CAT-VF-02 | Salvar informação complementar e recusar edição entre agências | **Parcial**: descrição, roteiro e inclusos foram salvos e exibidos, e a edição entre agências deu 404. Editar e salvar de novo não foi feito | L03, L12, L09, L20 |
| CAT-VF-03 | Foto válida aceita, inválida recusada, persistência após deploy | **Não repetido**. Evidência anterior na seção 6. A persistência após redeploy do Render continua sem prova | — |
| CAT-VF-04 | Ficha nova, ficha antiga e rascunho | **Parcial**: ficha nova completa (L), ficha publicada só com foto (R) e rascunho com 404 (R) | L12, R06, R07, R08 |
| CAT-VF-05 | Paleta, contraste e ações em vários tamanhos de tela | **Parcial**: 1100 px e 375 px sem rolagem lateral. Contraste não foi medido nesta rodada | R10, R11, L21 |
| CAT-VF-06 | Fluxo completo de reserva, antes e depois | ✅ local: agente publica → passageiro reserva → agente vê a mesma reserva; vagas de 2 para 0 depois de duas reservas (a etapa intermediária com 1 vaga não foi registrada em print) | L06, L12, L13, L17 |

## 6. Evidências anteriores (não repetidas em 18/11)

| Tema | Data | Ambiente | Resultado registrado | Arquivo |
|---|---|---|---|---|
| Concorrência de reservas | 12/11/2026 09:54 | Windows, PostgreSQL 18.6 local, HTTP real com passageiros simultâneos | Cenário A (última vaga): 20/20 rodadas conformes. Cenário B (10 passageiros, 3 vagas): 5/5 conformes. **Nenhuma lotação excedida** | `docs/POSTGRESQL_E_CONCORRENCIA.md`, `evidencias/2026-11-12_0954_postgresql_windows/`, `docs/resultados-concorrencia-postgresql.json` |
| Fotos no Google Drive real | 18/11/2026 10:09 e 10:32 | Windows, PostgreSQL local, OAuth `drive.file` | 13 de 13 verificações conformes em cada ensaio: envio, JPEG, arquivo não público, acesso por perfil, remoção. Persistência só após reiniciar o processo local, **não após redeploy do Render** | `evidencias/2026-11-18_1008_drive_real/resultados.json`, `evidencias/2026-11-18_1032_drive_real/resultados.json`, `docs/OAUTH_EXECUCAO_REAL_2026-11-18.md` |
| Verificação HTTP VF01–VF16 | 20/10 e 22/10/2026 | Linux/Work, SQLite | 16 de 16 conformes por HTTP, sem navegador | `docs/VERIFICACAO.md`, `docs/resultados-http.json` |

Em 18/11 esses testes **não** foram executados de novo. Eles aparecem aqui só como referência.

## 7. Testes complementares do tutorial "Como usar" (EVO-USO-01)

O tutorial é uma evolução da experiência de uso (EVO-USO-01), **não** é um caso de uso da baseline. Os critérios TUT-01 a TUT-06 são os definidos no pedido de testes da autora de 18/11/2026.

| Critério | O que foi feito | Observado | Status | Prints |
|---|---|---|---|---|
| TUT-01 — No primeiro acesso, oferece ajuda que pode ser recusada e reaberta | Visitante no Render; agente e passageiro no local | Aparece "Quer conhecer o SIRE?" com Começar e Agora não. "Como usar" reabre na etapa 1 | ✅ | R01, L01, L10 |
| TUT-02 — Orientação de acordo com o perfil e a página | Abrir nos três perfis | Visitante: 4 etapas no catálogo. Agente: "Excursões da agência" (2 etapas sem excursão, 6 com excursão). Passageiro: 3 etapas na ficha ("Confira a viagem", "Selecionar embarque e reservar", "Minhas reservas") | ✅ | R02, L02, L11 |
| TUT-03 — Celular e computador, teclado e Esc, sem cobrir o essencial | 1100 px e 375 px; Próximo, Voltar, Pular, Concluir, Esc | Tudo funciona. O Esc devolve o foco para "Como usar". No celular, o painel cobre a parte de baixo da tela enquanto está aberto | ⚠️ ressalva visual (conta no cenário 14) | R03, R04, R11, L21 |
| TUT-04 — Não envia formulário nem altera dados | Percorrer o tutorial do passageiro até Concluir e recarregar a página | Vagas continuaram 2 antes e depois | ✅ | L11 |
| TUT-05 — Lista vazia, falta de vagas e armazenamento indisponível não bloqueiam | Área do agente sem excursões; tela de edição sem Drive; excursão lotada | O tutorial abre com a lista vazia. A edição continua com o aviso de Drive indisponível. A tela de lotação aparece normalmente | ✅ | L02, L07, L16 |
| TUT-06 — A mesma reserva aparece para o passageiro e para o agente autorizado | Reserva nº 1 nas duas visões | Reserva nº 1 aparece para passageiro_1 e para agente_a; agente_b recebe 404 | ✅ | L13, L17, L20 |

## 8. Correções em relação à revisão 1 (PR #24)

1. Na revisão 1, o cenário 2 (login) estava ligado a "VF01, VF02". O certo, segundo `docs/VERIFICACAO.md`, é **VF03**: VF01 e VF02 tratam de cadastro, e não foram repetidos.
2. Na revisão 1, era citada a pasta `evidencias/2026-11-18_demo_fotos_publicada/`, que não existe. As evidências de fotos estão em `evidencias/2026-11-18_1008_drive_real/` e `evidencias/2026-11-18_1032_drive_real/`.

Nenhum resultado mudou: a contagem continua 13 / 3 / 1 / 0.

## 9. Ressalvas e pendências

1. **Login no Render (2b):** os fluxos com login foram reproduzidos só no ambiente local, com o mesmo commit. Para ter a prova no Render, a autora precisa entrar com as contas de demonstração.
2. **Fotos:** nenhum envio novo nesta rodada. A persistência após redeploy do Render continua sem prova (CAT-VF-03).
3. **Concorrência:** prova só pela evidência de 12/11 (seção 6).
4. **VF01, VF02 e VF12** não foram repetidos no navegador.
5. **Melhorias visuais (não impedem o uso):** a página 404 do Render aparece em inglês e sem o visual do SIRE; o tutorial cobre parte da tela no celular.
6. As páginas 404 locais (L09, L20) mostram a tela técnica do Django porque o ambiente local roda com DEBUG ligado. No Render, o DEBUG fica desligado.
7. **Orientador:** nenhuma avaliação, mensagem ou compartilhamento foi feito.

## 10. Lista de prints (32)

| Arquivo | Conteúdo |
|---|---|
| R01_render_catalogo_oferta_tutorial.jpg | Catálogo do visitante com a oferta "Quer conhecer o SIRE?" |
| R02_render_tutorial_visitante_etapa1.jpg | Etapa 1 de 4, com Voltar desativado |
| R03_render_tutorial_visitante_etapa2_proximo.jpg | Etapa 2 depois de Próximo |
| R04_render_tutorial_voltar_esc.jpg | Depois de Voltar e Esc: tutorial fechado e foco em "Como usar" |
| R05_render_busca_litoral.jpg | Busca "Litoral" com 1 resultado |
| R06_render_detalhe_praia_foto.jpg | Detalhe da Praia fictícia com foto |
| R07_render_detalhe_praia_vagas_embarques.jpg | Vagas (40), embarques e "Entre para reservar" |
| R08_render_excursao3_nao_publica_404.jpg | Excursão não publicada dá 404 |
| R09_render_privacidade.jpg | Aviso de privacidade |
| R10_render_mobile_catalogo.jpg | Catálogo no celular (375 px) |
| R11_render_mobile_tutorial.jpg | Tutorial no celular |
| L01_local_agente_oferta_tutorial.jpg | Agente logado, com a oferta do tutorial |
| L02_local_tutorial_agente_area.jpg | Tutorial do agente em "Excursões da agência" |
| L03_local_nova_excursao_ficha.jpg | Formulário de nova excursão preenchido |
| L04_local_excursao_rascunho.jpg | Excursão salva em rascunho |
| L05_local_publicar_sem_embarque_recusado.jpg | Publicação recusada sem embarque |
| L06_local_publicada_com_embarque.jpg | Publicada depois do embarque |
| L07_local_fotos_drive_indisponivel.jpg | Aviso de fotos sem Drive; edição continua |
| L08_local_catalogo_mostra_publicada.jpg | Catálogo com a excursão nova |
| L09_local_agenteA_404_excursao_agenciaB.jpg | Agente A barrado na excursão da B |
| L10_local_passageiro_detalhe_oferta.jpg | Passageiro no detalhe, com a oferta do tutorial |
| L11_local_tutorial_passageiro_etapa3.jpg | Tutorial do passageiro, etapa 3, com Concluir |
| L12_local_ficha_roteiro_inclusos_reserva.jpg | Roteiro, inclusos e confirmação da reserva |
| L13_local_minhas_reservas_p1.jpg | Reserva nº 1 em Minhas reservas |
| L14_local_passageiro_403_area_agente.jpg | Passageiro barrado na área do agente (403) |
| L15_local_p2_sem_reservas_isolamento.jpg | Passageiro 2 não vê a reserva do passageiro 1 |
| L16_local_lotacao_sem_vagas.jpg | "Não há vagas disponíveis", com 0 vagas |
| L17_local_agente_reservas.jpg | Agente vê as reservas, 0 de 2 vagas |
| L18_local_agente_passageiros.jpg | Lista de passageiros fictícios |
| L19_local_agenteB_lista_propria.jpg | Agente B vê só a própria excursão |
| L20_local_agenteB_404_passageiros_A.jpg | Agente B barrado nos passageiros da A |
| L21_local_mobile_tutorial_agente.jpg | Tutorial do agente no celular |

## 11. Como repetir a verificação local (para o orientador)

1. Baixe o repositório na branch `etapa/postgresql-windows` (commit `e220974` ou mais recente).
2. Crie a venv e instale as dependências: `python -m pip install -r requirements.txt`.
3. Use um banco SQLite separado: defina as variáveis `SIRE_DB_ENGINE=sqlite` e `SIRE_SQLITE_PATH=<arquivo novo>` e rode `python manage.py migrate`.
4. Crie, pelo `python manage.py shell` ou pelo admin, duas agências fictícias, um agente para cada uma e dois passageiros com senhas de teste escolhidas por você.
5. Rode `python manage.py runserver 127.0.0.1:8017` e siga os procedimentos da seção 4, na ordem.
6. Testes automatizados: `python manage.py test sire` (esperado: 107 OK e 3 ignorados com SQLite).

Os dados do teste local de 18/11 ficaram só no banco temporário da máquina. Nada foi criado nem apagado no Render.
