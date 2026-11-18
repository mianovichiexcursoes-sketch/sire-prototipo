# Correções pendentes na monografia — revisão crítica de 18/11/2026

A monografia está em revisão paralela pelo ChatGPT. Por isso, estas correções **não** foram aplicadas no Google Docs; elas ficam aqui para a autora decidir e aplicar.
Fonte de verdade para requisitos e regras: Documentação de Desenvolvimento (baseline ER-SIRE 2.1, seções 3.1.8, 3.2, 3.3, 3.4 e 4.5.3). Equivalências de numeração: `docs/RASTREABILIDADE.md`.

## A. Contradições internas (prioridade alta)

| # | Onde | O que está escrito | O que contradiz | Correção sugerida |
|---|---|---|---|---|
| A1 | 4.4, penúltima frase do 3º parágrafo | "Não foram executados testes de carga, regressão automatizada, suíte unitária…" | 2.6 (67 testes desde 16/11), 3.2.3.3 (97) e 4.3 (107 no commit e220974, com CI) | Trocar por: "Não foram executados testes de carga nem avaliação formal de usabilidade. A suíte automatizada (107 testes no commit e220974) cobre regressão funcional, mas não desempenho." |
| A2 | 2.6, 3.2.3.3 e 4.3 | 67, 97 e 107 testes sem explicação | — | Deixar explícito que a suíte cresceu: 67 (16/11, 75fcc6d) → 97 (integração local) → 107 (e220974) |
| A3 | 3.2.2.4, "Cenários funcionais" | "CPF, **idade** e mapa de poltronas não integram os dados verificados" | Migration 0005: data de nascimento no cadastro, visível ao agente (UC14) | "CPF e mapa de poltronas não integram os dados. A data de nascimento foi acrescentada depois da baseline (migration 0005), com finalidade declarada no aviso de privacidade." |
| A4 | QP3, 3.2.1.3, 4.1, 4.4 e 5 | "seis entidades" no presente | FotoExcursao (migration 0007) é a sétima tabela de domínio | Escrever "as seis entidades **da baseline**" e citar a FotoExcursao como extensão técnica (a seção 3.4.2 e a Figura 4 já fazem isso) |
| A5 | 3.2.2.1 | "fotos de excursões (…) registradas para evolução futura (…) sem acrescentar entidades" | Fotos implementadas em novembro com nova entidade | Acrescentar: "posteriormente implementadas como extensão (CAT-RF-03), ver 3.2.3.5" |

## B. Textos desatualizados

| # | Onde | Problema | Correção sugerida |
|---|---|---|---|
| B1 | 2.9, 3.2.2.3, 4.1, 5 e Quadro 4 | Falam só em SQLite | "SQLite na implementação original; PostgreSQL na demonstração (Render) e nos ensaios de concorrência" |
| B2 | 3.4.3 | Cadastro descrito só com username, nome, sobrenome e e-mail | Incluir data de nascimento e aceite do aviso de privacidade (extensões de 16/11) |
| B3 | 3.4.5 | Pesquisa descrita só com `destino__icontains` | Incluir os filtros de período e tipo de pacote (CAT-RF-01, extensão parcial do RF014). O filtro por local de embarque do RF014 não foi implementado |
| B4 | 3.2.3.5 e 5.4 | "não há confirmação de vínculo [do Drive] ao serviço"; versão live 74f50c84 | Versão live conferida em 18/11: e220974. O print R06 mostra foto servida pela demo. Continuam sem evidência: um envio novo registrado e a persistência após redeploy |
| B5 | Capítulo 4, 1º parágrafo | "documentação (…) atualizados em 22/10/2026" | Citar também os registros de novembro (concorrência, extensões e aceite de 18/11) |
| B6 | Resumo, Abstract e 5 (1º parágrafo) | Citam só os 16 cenários HTTP | Acrescentar uma frase sobre a suíte automatizada e a rodada de 18/11 (13 aprovados, 3 com ressalva, 1 bloqueado) |
| B7 | Resumo, Figura 1 e 5.2 | "duas iterações e uma técnica complementar" | Houve também os incrementos de catálogo (16/11), ficha e fotos (17–18/11) e EVO-USO-01. Ou atualizar a contagem e a figura, ou dizer que a figura representa só as duas iterações originais e listar as voltas posteriores |
| B8 | 4.3, último parágrafo | Cita a revisão 2 (PR #28) com link para `etapa/postgresql-windows`, que ainda tem a revisão 1 | Integrar a PR #28 antes da entrega, ou trocar o link para a branch da PR |
| B9 | 4.4 (concorrência) | Relata só a campanha de 5 rodadas (Testes A, B e C) | `docs/POSTGRESQL_E_CONCORRENCIA.md` tem também a campanha de 25 rodadas (20 + 5) em PostgreSQL e SQLite. Citar as duas ou dizer qual foi escolhida e por quê |

## C. Rastreabilidade e escopo (para a banca não perguntar)

| # | Situação | Sugestão |
|---|---|---|
| C1 | Na pasta central há uma "Especificação de Requisitos" v3.0 (PFC2) e um "Regras de Negócio" (RN-01–RN-41) com **numeração diferente** da baseline (ex.: RF-05 = Editar vs. RF005 = Cadastro; RF-18 aparece como Protótipo) | Colocar no topo desses dois documentos: "Documento histórico, substituído pela Documentação de Desenvolvimento (baseline ER-SIRE 2.1); numeração não equivalente". Na monografia, dizer em 3.2.1.1 que a numeração oficial é a da Documentação de Desenvolvimento |
| C2 | RF008, RF009 e RF014 (Produto completo) foram parcialmente implementados como CAT-RF-01/02 | Citar na monografia que os CAT-RF **estendem** esses RF, em vez de serem requisitos sem origem |
| C3 | Administrador | A monografia diz "três atores". A decisão 3.1.8 (a/b) da baseline já explica que agências e agentes são cadastrados previamente pela administração do Django. Citar essa decisão em 3.2.1.1 ou 4.2 |

## D. Formais (ABNT)

| # | Onde | Problema |
|---|---|---|
| D1 | Referências | ISO/IEC/IEEE 29148:2018 está listada, mas não é citada no texto. Citar em 2.1 ou remover |
| D2 | Pré-textuais | A dedicatória aparece duas vezes (antes dos Agradecimentos e no fim deles), com textos diferentes |
| D3 | 2.7, 4.1 e referência 2026a | Versão documental "2.5"; `RASTREABILIDADE.md` citava "2.4". Conferir no histórico de alterações do documento qual é a vigente e usar só ela |
| D4 | 3.2.3.5 | Hash "72a488" truncado (6 caracteres); usar 7 ou mais, conferido no GitHub |
| D5 | 2.6 | Resultados do projeto (67 testes, commit) dentro do Referencial Teórico; mover para a Metodologia |

## E. Antes de entregar ao orientador

- Desde 18/11, a pasta "TCC JULIA — SIRE" está com acesso restrito. Os links do Drive citados na monografia (registro técnico, documentação de desenvolvimento, ZIP, bundle e evidência .txt de concorrência) só abrem para a autora. Compartilhe com o orientador e a banca quando decidir entregar.
