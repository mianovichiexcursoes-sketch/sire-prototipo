# Inventário verificável do Drive SIRE — 20/11/2026

**Escopo:** listagem direta por Google Drive das pastas acessíveis. Isto é inventário de metadados, **não** leitura integral nem auditoria ABNT concluída. Não modifica originais, dados ou demo.

| Pasta | ID | Itens diretos encontrados | Conteúdo e tratamento |
|---|---|---:|---|
| [TCC JULIA — SIRE](https://drive.google.com/drive/folders/10bECylYN5oH7QNBFlZx5CA-1FEz3Y678) | `10bECylYN5oH7QNBFlZx5CA-1FEz3Y678` | 32 | Monografia editável e PDF, documentação editável e PDF, especificações RN/RF/UC/CAT, guia, registro técnico, modelo relacional, diagramas PNG, fontes de elicitação, ZIPs e três subpastas |
| [Evidências — Aceite Final](https://drive.google.com/drive/folders/1ijoatraiI5seo-tVyveDX2uIuJCRcstF) | `1ijoatraiI5seo-tVyveDX2uIuJCRcstF` | 4 | Dois relatórios (Google Doc e MD), pastas L e R |
| [L01–L21 — Local](https://drive.google.com/drive/folders/1VCuoXazkm_nPablH-sZFmQv6qgHc0lPk) | `1VCuoXazkm_nPablH-sZFmQv6qgHc0lPk` | 21 | Capturas locais de perfis, rascunho, publicação, reservas, isolamento e tutorial |
| [R01–R11 — Render](https://drive.google.com/drive/folders/1ufLz1h9jdCue40qsJJRgPxDXoavrx3iR) | `1ufLz1h9jdCue40qsJJRgPxDXoavrx3iR` | 11 | Capturas de visitante, catálogo, detalhes, tutorial e celular |
| [VII Colóquio 2026](https://drive.google.com/drive/folders/1X3hMVjcLAfad4-yaum9gYae2JhIpEnhb) | `1X3hMVjcLAfad4-yaum9gYae2JhIpEnhb` | 4 | Apresentação e resumo, PDF e versões editáveis |
| [Histórico de versões](https://drive.google.com/drive/folders/1aODsRDbdq32WtLM8V7KANjTX_qqvLblT) | `1aODsRDbdq32WtLM8V7KANjTX_qqvLblT` | 5 | Bundle PostgreSQL, ZIP, especificação UC histórica, documentação baseline e revisão ABNT |

**Total observado:** 77 entradas listadas, incluindo 5 pastas e 72 arquivos (contagem de entradas por diretório, não de documentos únicos; não equivale a cobertura de todos os compartilhamentos fora dessa árvore). Nenhuma subpasta adicional apareceu nas três subpastas de segundo nível nem nas duas pastas de capturas.

## Evidência nova encontrada e distinção de estados

O documento [Aceite funcional final — revisão 2](https://docs.google.com/document/d/1c0G1H1I-Y90KJrGMJuwUHXkRj_gjP41ran7ROKiR53g/edit) foi lido diretamente. **Ele relata** teste em 18/11 no commit `e220974`, 107 testes SQLite OK e 3 ignorados (concorrência PostgreSQL), 13 cenários aprovados, 3 com ressalva, 1 bloqueado (login Render) e 0 falhas; 32 capturas estão inventariadas. Esses são resultados históricos atribuídos ao relatório, **não testes repetidos nesta rodada**. O documento declara que não representa aceite do orientador.

Lacunas expressas no próprio relatório: VF01, VF02 e VF12 não repetidos em 18/11; CAT-VF-01 e CAT-VF-02 parciais; CAT-VF-03 não repetido e persistência após novo deploy não comprovada; tutorial móvel com painel cobrindo parte inferior; concorrência PostgreSQL não repetida; login autenticado no Render bloqueado. A evidência de tutorial no commit `e220974` não valida automaticamente as PRs de correção posteriores (#20/#33/#35/#54) nem o HEAD integrado.

## Próximas verificações independentes

1. Conferir versões/SHAs entre relatório, PR #24 e branch efetiva antes de atribuir resultados a qualquer código novo.
2. Revisar a monografia **inteira** e os PDFs finais; cotejar legendas e figuras com R01–R11/L01–L21; preservar distinção local/Render e histórico versus atual.
3. Comparar diagrama/modelo relacional, seis entidades baseline e extensões contra migrations; não renumerar UC01–UC14.
4. Reconciliar tutorial em branch isolada, executar TUT e regressões atuais; não publicar automaticamente.
5. Configuração OAuth própria e persistência real de fotos continuam bloqueadas até autorização/ambiente seguro; aprovação humana continua pendente.

**Nesta unidade:** apenas leitura/listagem e versionamento documental. Nenhum teste, deploy, merge, OAuth, edição de monografia ou aprovação foi executado.
