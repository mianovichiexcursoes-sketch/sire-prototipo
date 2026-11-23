# EVO-USO-01 — Matriz de verificação independente (22/11/2026)

**Estado: PLANEJADO, NÃO EXECUTADO.** Base de comparação: `etapa/postgresql-windows`. Este documento não atesta execução, aceite, CI ou deploy. Não altera ER-SIRE 2.1, UC01–UC14 ou seis entidades originais. Não depende do OAuth Drive para os fluxos existentes.

## Fontes originais lidas diretamente em 22/11/2026
- RN-01–RN-41: `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` (versão não indicada no cabeçalho). RN-03 isolamento; RN-04 dados pessoais; RN-05 perfis; RN-06 publicação; RN-08–09 embarque.
- Desenvolvimento: `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`, histórico 2.6 e baseline 2.1.
- Guia: `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`, SQLite original e PostgreSQL adicional.
- Casos de uso: `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`, UC01–UC14.
- Requisitos: `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`, v3.0 PFC2, visão ampliada separada do protótipo.
- Catálogo/ficha: `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`, revisão 0.2.
- Registro: `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`, histórico desde 20/10/2026.

## Cenários de aceite propostos (todos PENDENTES)
| ID | Perfil e condição | Ação | Resultado esperado | Dependência |
|---|---|---|---|---|
| TUT-01 | Visitante, primeira visita | Abrir catálogo | Oferta de tutorial sem redirecionar nem enviar formulário | Browser e build candidato |
| TUT-02 | Visitante, catálogo vazio | Avançar tutorial | Alvo ausente não causa exceção; opção pular/fechar acessível | Browser |
| TUT-03 | Passageiro autenticado | Percorrer detalhes, embarque, confirmação, minhas reservas | Só alvos permitidos e existentes; nenhuma reserva criada pelo tutorial | Conta sintética |
| TUT-04 | Agente autenticado | Percorrer excursões, criação, embarque, publicação, reservas, passageiros | Sem submissão/publicação; apenas dados da própria agência | Duas agências sintéticas |
| TUT-05 | Visitante/Passageiro/Agente | Pressionar Escape e navegar por Tab/Shift+Tab | Fechamento e foco previsíveis, sem armadilha de teclado | Browser |
| TUT-06 | Qualquer perfil | Anterior, Próximo, Pular e Fechar | Controles operantes, estado coerente e retorno do foco | Browser |
| TUT-07 | Qualquer perfil | Reabrir por Como usar | Tutorial reinicia sob demanda, sem repetição forçada | Browser |
| TUT-08 | Qualquer perfil | Bloquear localStorage/sessionStorage | Tutorial continua utilizável, sem exceção fatal | Browser |
| TUT-09 | Qualquer perfil | Inspecionar storage | Só versão/progresso; nenhum CPF, email, nome ou token | Browser |
| TUT-10 | Qualquer perfil | Viewport 320px e 375px | Botões visíveis, sem overflow impeditivo | Browser mobile |
| TUT-11 | Passageiro, excursão lotada | Abrir detalhes e tutorial | Não orienta reserva como disponível nem cria reserva | Fixture sintética |
| TUT-12 | Agente de agência A | Tentar rota administrativa da agência B | Controle de acesso continua aplicado no servidor | Django teste isolado |

## Procedimento de execução e registro
1. Antes de editar, obter HEAD atual da demo e das PRs #15, #20, #33, #35, #64; comparar os diffs de `base.html` e do JS efetivo. Outro agente pode ter trabalho local invisível: não sobrescrever.
2. Construir candidato em branch isolada. Não mesclar patch mobile sem reconciliar correções de perfil e acessibilidade.
3. Executar suíte Django em SQLite e, se houver PostgreSQL de ensaio isolado, repetir; salvar comando, versão, saída, duração, SHA e falhas. Não apontar banco de produção.
4. Executar TUT-01–12 no navegador com dados sintéticos; registrar navegador, viewport, evidência visual sem dados pessoais e resultado individual PASSOU/FALHOU/BLOQUEADO.
5. Regressão: UC01–UC14 afetados, VF01–VF16 aplicáveis, CAT-VF01–06. Verificar autorização entre agências e não submissão automática.
6. Somente após evidência e revisão humana considerar merge; não publicar na demo automaticamente. Solicitar nova avaliação do orientador por meio da autora.

## Rastreabilidade
| Origem | Artefato a conferir | Verificação | Monografia |
|---|---|---|---|
| EVO-USO-01 + UC03–05 | catálogo, detalhe, tutorial JS, base | TUT-01,02,05–10 | metodologia/volta da espiral, resultados |
| EVO-USO-01 + UC10–12 | reserva, embarque, minhas reservas | TUT-03,11 | limites do protótipo |
| EVO-USO-01 + UC06–09,13–14 + RN-03–05 | agente, excursões, passageiros | TUT-04,12 | autorização e avaliação de risco |
| LGPD + RN-04–05 | storage de progresso | TUT-08,09 | minimização de dados |

**Bloqueios separados:** OAuth `drive.file` do Django depende de autorização própria e configuração segura no Render (responsável: autora/operador); impede aceite real de fotos, não os TUT. Avaliação pelo orientador depende de teste/revisão e mediação da autora. Evidências de teste: ainda não produzidas.