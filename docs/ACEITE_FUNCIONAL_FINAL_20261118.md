# Aceite funcional final — SIRE — 18/11/2026

Registro dos testes manuais que foram **executados de verdade no navegador**, com prints reais.
Nada aqui foi simulado, e o documento não representa aprovação do orientador.

## 1. Ambientes e ferramenta

| Sigla | Ambiente | Versão | Dados | Perfil usado |
|---|---|---|---|---|
| **R** | Render, publicado em https://sire-demo.onrender.com | commit `e220974` (conferido no painel do Render antes dos testes) | demonstração fictícia já existente; nada foi criado nem apagado | Visitante (sem login) |
| **L** | Local isolado em http://127.0.0.1:8017, SQLite próprio do teste | mesmo commit `e220974` | Agência Aceite A/B, agente_a, agente_b, passageiro_1, passageiro_2, todos fictícios (`@example.test`) | Agente A, Agente B, Passageiro 1, Passageiro 2 |
| **CI** | Suíte automática (`manage.py test sire`) | `e220974` | banco de teste temporário | — |
| **Drive** | Evidência real anterior de fotos no Google Drive | ver `evidencias/2026-11-18_1032_drive_real/` e `evidencias/2026-11-18_demo_fotos_publicada/` | foto de praia enviada pela autora | Agente de demonstração |

- Ferramenta: navegador embutido do Claude Desktop (Chromium), com tela de **1100×760** (computador) e **375×812** (celular, emulado).
- Data e hora: Render de 14:45 a 14:48 (17:45–17:48 UTC); local de 14:49 a 14:53 (horário de Brasília).
- Senhas: as contas locais usam uma senha de teste que só existe no banco temporário. Ela **não aparece** em prints, commits nem neste documento. No Render, o assistente não digitou nenhuma senha.
- Suíte automática no mesmo commit: **107 testes OK, 3 ignorados** (os de PostgreSQL concorrente, que só rodam com PostgreSQL).

## 2. Resultado por cenário

Legenda: ✅ aprovado · ⚠️ aprovado com ressalva · ⛔ bloqueado (precisa de ação humana) · ❌ falhou

| # | Cenário | Amb. | Procedimento | Esperado | Observado | Status | Prints | Requisito / UC |
|---|---|---|---|---|---|---|---|---|
| 1 | Catálogo e busca | R | Abrir o catálogo; buscar destino "Litoral"; buscar "Inexistente-XYZ" | Lista só publicadas; filtro funciona; busca vazia avisa | 3 excursões publicadas; "Litoral" → 1 (Praia fictícia); "Inexistente-XYZ" → 0, com "Nenhuma excursão publicada encontrada." (conferido pelo texto da página, sem print) | ✅ | R01, R05 | VF09, VF10, CAT-VF-01, UC buscar |
| 2 | Login de passageiro e agente | L | Entrar como `AGENTE_A` (em maiúsculas), sair, entrar como passageiro_1 e passageiro_2, e como agente_b | Cada perfil vê o seu menu | Agente: "Excursões da agência"; passageiro: "Minhas reservas". O login com maiúsculas funcionou | ✅ | L01, L10, L19 | VF01, VF02 |
| 2b | Login no Render | R | — | — | **Não executado**: a sessão de demonstração expirou e o assistente não digita senha em site público | ⛔ | — | VF02 |
| 3 | Agente cria excursão | L | Nova excursão "ACEITE A — Cachoeira fictícia", com descrição, roteiro, inclusos e capacidade 2 | Fica salva em RASCUNHO | "Excursão cadastrada em RASCUNHO." | ✅ | L03, L04 | VF04, CAT-VF-02, RN-06 |
| 4 | Publicar sem embarque | L | Clicar Publicar sem ponto de embarque | Recusar e continuar em rascunho | "Publicação exige RASCUNHO, dados válidos e ao menos um ponto de embarque." Continua em Rascunho | ✅ | L05 | VF07, RN-26 |
| 5 | Embarque e publicação | L | Adicionar "Praça Aceite A (fictícia) — 06:00" e publicar | Embarque salvo; status Publicada | "Ponto de embarque cadastrado." e depois "Excursão publicada no catálogo." | ✅ | L06 | VF06, VF08, RN-11 |
| 6 | Excursão publicada no catálogo | L | Buscar "Cachoeira" | Aparece com a agência A | Aparece "ACEITE A — Cachoeira fictícia", Agência Aceite A | ✅ | L08 | VF09, CAT-VF-01 |
| 6b | Rascunho não aparece para visitante | R | Abrir `/excursao/3/` | Não publicada não abre | HTTP 404 | ✅ | R08 | VF09, RN-11 |
| 7 | Reserva e Minhas reservas | L | passageiro_1 escolhe o embarque e confirma | Reserva criada e listada | "Reserva realizada com sucesso."; Reserva nº 1 em Minhas reservas | ✅ | L12, L13 | VF11, VF14, RN-27 |
| 8 | Agente consulta a reserva | L | agente_a abre Reservas e Passageiros da excursão | Mostra as duas reservas e o embarque | "Disponibilidade: 0 de 2 vagas"; reservas 1 e 2 com nome, nascimento e embarque | ✅ | L17, L18 | VF15, VF16, TUT-06, RN-28 |
| 9 | Disponibilidade e lotação | L | Capacidade 2: passageiro_1 e passageiro_2 reservam; passageiro_2 tenta de novo, pela página e por envio direto | Vagas 2 → 0; terceira reserva recusada | Vagas 0; "Não há vagas disponíveis."; o formulário some; o envio direto também foi recusado e o total ficou em 2 | ✅ | L16 | VF10, VF13, RN-20/21/22/24 |
| 9b | Concorrência real | CI | Testes automáticos de corrida | Sem reserva além da capacidade | Os testes de PostgreSQL concorrente foram **ignorados** nesta rodada local (só rodam com PostgreSQL). Não houve teste manual de concorrência | ⚠️ | — | RN-29/30 |
| 10 | Isolamento entre perfis e agências | L | Passageiro abre a área do agente; agente_a abre a excursão da agência B; agente_b abre a excursão da agência A; passageiro_2 abre Minhas reservas antes de reservar | Bloquear tudo | Passageiro: 403. Agente A → excursão B: 404. Agente B → editar, reservas e passageiros da A: 404 nos três. agente_b vê só a própria excursão. passageiro_2 não via a reserva do passageiro_1 | ✅ | L09, L14, L15, L19, L20 | VF03, VF05, CAT-VF-02, RN-03 |
| 11 | Ficha, roteiro, inclusos e galeria | L + R | Ver a ficha da excursão nova (L); ver a Praia fictícia com foto (R) | Seções exibidas; foto carregada | L: "Sobre o pacote", "Roteiro da viagem" e "O que está incluso" corretos. R: 1 foto da galeria carregada, servida pelo próprio SIRE (sem link direto do Drive). Sem Drive, a tela de edição local mostra um aviso e os outros campos continuam editáveis | ⚠️ | L07, L12, R06, R07 | CAT-VF-03, CAT-VF-04, TUT-05 |
| 12 | Tutorial "Como usar" por perfil | R + L | Abrir o tutorial como visitante, agente e passageiro | Textos e destaques certos para cada perfil | Visitante: 4 etapas no catálogo. Agente: "Excursões da agência" (2 etapas sem excursão, 6 com excursão). Passageiro: 3 etapas na excursão ("Confira a viagem", "Selecionar embarque e reservar", "Minhas reservas") | ✅ | R01, R02, L01, L02, L10, L11 | TUT-01, TUT-02 |
| 13 | Próximo, Voltar, Pular, reabrir e Esc | R + L | Usar todos os botões e a tecla Esc | Navega, fecha, reabre e devolve o foco | Próximo 1→2 e Voltar 2→1. Esc fecha e o foco volta em "Como usar". "Como usar" reabre na etapa 1. Pular fecha. Na última etapa aparece "Concluir". O tutorial não mudou as vagas (2 antes e depois) | ✅ | R02, R03, R04, L11 | TUT-01, TUT-03, TUT-04 |
| 14 | Computador e celular | R + L | Tela de 1100 px e de 375 px | Sem rolagem lateral; menu e tutorial usáveis | Em 375 px não há rolagem horizontal. O menu quebra em linhas e o painel do tutorial ocupa 359 px na parte de baixo, com Voltar, Próximo e Pular visíveis | ⚠️ | R10, R11, L21 | VF-05 (CAT), TUT-03 |

### Contagem

| Situação | Quantidade |
|---|---|
| ✅ Aprovado | 13 |
| ⚠️ Aprovado com ressalva | 3 (9b, 11, 14) |
| ⛔ Bloqueado | 1 (2b, login no Render) |
| ❌ Falhou | 0 |

Este resultado **não** é "100% aprovado": há um item bloqueado e três ressalvas.

## 3. Ressalvas e observações (sem correção feita nesta etapa)

1. **Login no Render (2b):** os fluxos de agente e passageiro foram reproduzidos só no ambiente local, com o mesmo commit. Para ter a prova no Render, a autora precisa entrar com a conta de demonstração. O assistente não digita senha em site público.
2. **Fotos (11):** hoje não houve um novo envio de foto, porque o ambiente local não tem a chave do Drive (isso é proposital). A prova de envio real está nas pastas de evidência do Drive citadas acima. No Render, a Praia fictícia tem foto, mas não tem descrição, roteiro nem inclusos preenchidos; a ficha completa foi vista no ambiente local.
3. **Concorrência (9b):** o teste manual foi em sequência. A prova de concorrência depende dos testes com PostgreSQL (CI ou máquina com PostgreSQL), que não rodaram nesta execução com SQLite.
4. **Página 404 do Render (R08):** mostra o texto padrão em inglês ("Not Found"), sem o visual do SIRE. Funciona, mas é uma melhoria visual possível.
5. **Tutorial no celular (14):** quando está aberto, o painel cobre a parte de baixo da tela, por exemplo os links "Reservas" e "Passageiros" do cartão. O item destacado continua visível, e o painel fecha com Pular, Concluir ou Esc.
6. As páginas 404 locais (L09, L20) mostram a tela técnica do Django porque o ambiente local roda com DEBUG ligado. No Render, o DEBUG fica desligado.

## 4. Lista de prints

Pasta: `evidencias/2026-11-18_aceite_final/` (os prefixos R e L indicam o ambiente)

| Arquivo | Conteúdo |
|---|---|
| R01_render_catalogo_oferta_tutorial.jpg | Catálogo do visitante com a oferta "Quer conhecer o SIRE?" |
| R02_render_tutorial_visitante_etapa1.jpg | Etapa 1 de 4, com Voltar desativado |
| R03_render_tutorial_visitante_etapa2_proximo.jpg | Etapa 2 depois de Próximo |
| R04_render_tutorial_voltar_esc.jpg | Depois de Voltar e Esc: tutorial fechado e foco em "Como usar" |
| R05_render_busca_litoral.jpg | Busca "Litoral" com 1 resultado |
| R06_render_detalhe_praia_foto.jpg | Detalhe da Praia fictícia com a foto |
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

## 5. O que ainda depende de pessoas

- **Autora:** entrar no Render como agente e como passageiro de demonstração, se quiser a prova do item 2b no site publicado.
- **Autora:** decidir se vale melhorar as ressalvas 4 e 5. Elas não impedem o uso.
- **Orientador:** avaliação. Este documento **não** registra aprovação do professor.

Os dados fictícios do teste local ficaram só no banco temporário da máquina. Nada foi criado nem apagado no Render.
