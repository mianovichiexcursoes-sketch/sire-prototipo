# SIRE — progresso executivo e rastreabilidade do TCC

> Atualização: 17/11/2026 (America/Sao_Paulo). **Registro de evidências, não declaração de conclusão do TCC.**
> Branch documental isolada `docs/progresso-tcc-final-20261117`, derivada do commit `08b3dcc` da correção de segurança. **Não alterar nem fazer merge/deploy na demo `etapa/postgresql-windows` sem aceite.** Esta tabela deve ser atualizada por rodada, com SHA, evidência e próxima ação.

## Situação do repositório e prevenção de conflitos

- Demo aprovada: branch `etapa/postgresql-windows`; Render `sire-demo`. Não foi feito deploy nesta rodada.
- PR [#2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2): ficha e fotos, aberta; outro fluxo de trabalho pode modificá-la. Não escrever nessa branch.
- PR [#4](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/4): testes isolados, aberta, baseada na #2.
- PR [#5](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/5): segurança das fotos, aberta e em rascunho, baseada na #4. Commit verificado `08b3dcc9b1b5cae45928a019519b9ff0bea56c0e`. **Não integrar a cadeia sem reconciliar os PRs.**
- Testes do commit `08b3dcc`: [CI fotos SQLite e PostgreSQL](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44078120711) = sucesso; [CI geral](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44078120330) = sucesso. Na suíte de fotos, 15 testes passaram no PostgreSQL; no SQLite, 14 passaram e 1 cenário de concorrência PostgreSQL foi pulado. Evidência limitada a bancos descartáveis, com Drive simulado.
- A extensão de fotos mantém referências em `sire/models.py` (`FotoExcursao`) e migration aditiva `0007`. O código do PR #5 usa `select_for_update` no upload e respostas `Cache-Control: private, no-store`. Não se deve confundir com OAuth Drive validado.
- Fonte da verificação histórica da demo: [registro de implementação](https://docs.google.com/document/d/1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM/edit). Não reatribuir resultados históricos a novas versões.

## Checklist persistente por dependência

| ID | Etapa | Status | Último commit / evidência | Próxima ação / condição |
|---|---|---|---|---|
| A1 | Ficha: tipo, descrição, roteiro, inclusos, migração aditiva 0007 | **em execução** | PR #2; baseline histórica preservada | Conferir diffs e aceitação CAT-RF-01–04; reconciliar alterações de outros agentes antes de integrar |
| A2 | Fotos: isolamento de agências, cache, máximo seis e concorrência | **concluído em código/testes isolados** | `08b3dcc`, PR #5, [CI fotos](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/actions/runs/44078120711) | Revisar PRs empilhados e integrar somente após gate; não significa validação do Drive real |
| A3 | Aceite final do incremento ficha/fotos | **bloqueado** | PRs #2/#4/#5 abertos; sem deploy de fotos comprovado | Depende de reconciliação, OAuth e validação end-to-end real |
| B1 | Configurar OAuth Drive API com escopo `drive.file` | **bloqueado** | Sem evidência de credenciais do aplicativo no Render nem autorização própria do Django | **Responsável:** titular do projeto/conta Google e Render. Criar projeto OAuth, consentimento e token fora do GitHub/chat; configurar secrets no Render e testar; a conexão do ChatGPT não autoriza o app |
| B2 | Upload/exclusão real, persistência após redeploy e controle de acesso Drive | **bloqueado** | CI atual simula Drive; não prova serviço remoto | Pré-requisito B1, ambiente de teste e arquivos exclusivamente sintéticos |
| C1 | CPF: finalidade LGPD, minimização e decisão de retenção | **pendente** | RN-04; requisitos 3.0, baseline sem CPF | Registrar justificativa, acesso, retenção, máscara e análise de risco antes de criar migration; usar só CPFs sintéticos |
| C2 | CPF: validação dígitos verificadores, formulário, proteção, testes e migration aditiva | **pendente** | Nenhum commit nesta rodada | Depende de C1; não coletar CPF real nem publicar dados |
| D | UX da reserva: resumo, preço, embarque, confirmação sem pagamento | **pendente** | UC10 e fluxo histórico | Implementar em branch isolada após comparar templates atuais; não adicionar cobrança |
| E | Painéis de agente e passageiro com consultas existentes | **pendente** | UC12–UC14, RN-03/04/05 | Rever queries, papéis e templates em branch isolada |
| F1 | Regressão CAT-VF01–06 e VF01–16 afetados, SQLite/PostgreSQL | **em execução** | CI parcial fotos #5; registros históricos não equivalem a reexecução | Matriz de cobertura; testes completos de rotas e migrações; separar automático de manual |
| F2 | Navegador responsivo, Drive real, persistência pós-deploy | **bloqueado** | Sem prova nova nesta rodada | Depende de B1/B2 e ambiente revisado; não alterar demo até aceite |
| G1 | Documentação acadêmica e transparência de IA | **pendente** | Parecer pré-banca de 23/10/2026 | Resolver contradições em relatório de divergências, sem apagar histórico; confirmar título com orientador |
| G2 | Auditoria global pasta “TCC JULIA — SIRE”, monografia, IFSP/ABNT, anexos | **pendente** | Monografia e modelo IFSP lidos nesta rodada, sem revisão integral | Inventariar toda pasta, ler cada documento, revisar conteúdo/formatação e registrar evidências sem inventar testes |
| FUT | Cloudinary/R2, assentos, pagamentos e cancelamentos | **pendente (backlog futuro)** | Requisitos 3.0, RN-31–41 | Documentar como visão de produto; **não implementar no protótipo** |

**Bloqueio B1/B2/A3/F2:** impacto = não comprova foto real, exclusão, retenção nem persistência após deploy; pré-requisito = OAuth exclusivo do aplicativo, configuração segura e ambiente de teste; responsável = titular da conta Google/Render; condição de retomada = configuração confirmada sem compartilhar segredos. Continuar C, D, E, F1 e G1 independentemente.

## Matriz de rastreabilidade — baseline versus extensão

| Regra/artefato | Implementação/alteração | Testes e evidência | Monografia/documento a conferir |
|---|---|---|---|
| ER-SIRE 2.1, UC01–UC14; seis entidades históricas | `sire/models.py`, migrations `0001–0004`, `sire/views.py` | VF01–VF16: execução histórica no registro, **não reexecução desta rodada** | Seções de escopo, ERD, casos de uso e resultados; preservar baseline |
| RN-01–05, RN-11 | `sire/views.py`: controle de agência, imagem não publicada, cache | PR #5: FOTO-02/03/04/05/09/15; CI SQLite/PostgreSQL | Segurança, privacidade e delimitação de dados |
| CAT-RF-01/02/04; UC04–07 (extensão) | `sire/forms.py`, `sire/views.py`, templates; `0006`/`0007` | CAT-VF01/02/04 pendentes de aceite completo | Incremento separado; não reescrever UC original |
| CAT-RF-03, CAT-VF03 | `sire/drive_fotos.py`, `sire/models.py:FotoExcursao`, `sire/views.py`, migration `0007` | PR #5: FOTO-13/14/16; CI PostgreSQL com concorrência; **Drive real pendente** | Arquitetura de armazenamento, limites e riscos |
| RN-17–30, UC10 | `sire/views.py` fluxo de reserva; `sire/models.py:Reserva` | Registros históricos de concorrência e reserva; não inferir pagamento | Resultados VF10–13 e escopo |
| EVO-CPF (proposta, ainda não aprovada) | **nenhum arquivo alterado** | testes futuros com CPFs sintéticos | Adendo LGPD, justificativa, migration e limitação |
| RN-31–41 | **fora do protótipo atual** | nenhum teste declarado | Trabalhos futuros: assentos, pagamento e cancelamento |

## Fontes oficiais efetivamente consultadas em 17/11/2026

Leitura direta via Google Drive dos documentos nativos, IDs abaixo. `revisionId` é um identificador técnico, não uma data de aprovação; sem histórico de revisão confirmado não presumir versão editorial.

| Fonte | ID exato | Identificação observada |
|---|---|---|
| RN-01–RN-41 | `1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0` | Regras de negócio SIRE |
| Baseline | `19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8` | Documentação de desenvolvimento, ER-SIRE 2.1 |
| Guia | `1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U` | Guia de implementação |
| UC | `1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY` | UC01–UC14 |
| Requisitos | `1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM` | Especificação de requisitos 3.0 |
| CAT | `1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is` | Complementar catálogo/ficha |
| Registro | `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM` | Implementação e rastreabilidade |
| Monografia | `1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg` | Projeto de Arquitetura de Software Aplicado ao Turismo Rodoviário |
| Modelo IFSP | `1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo` | Modelo PFC dez/2025 |
| Parecer | `1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA` | Pré-banca 23/10/2026 |
| Histórico | `1mpNI5u26q3NzVgXFeeMCHZgfWdxCgsG-WTangQWVRrE` | PROMPS TCC; não prevalece sobre baseline |

**Fonte ainda sem leitura concluída:** regulamento PFC PDF `1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL` e inventário integral da pasta central. Não afirmar conformidade ABNT/IFSP final antes dessas verificações.

## Divergências acadêmicas já identificadas (sem edição silenciosa)

1. **IA/autoria:** parecer pré-banca aponta que requisito 9.4 diz “não será utilizado Codex” enquanto registro/README documentam auxílio de IA. Preservar evidências e redigir adendo transparente, sujeito à validação da autora/orientador.
2. **Título/escalabilidade:** títulos variam entre documentos; “escaláveis” pode sugerir teste não realizado. **Não alterar título sem confirmação do orientador.**
3. **Resultados:** não confundir testes históricos Windows/Render com testes CI de fotos em PostgreSQL descartável; não declarar OAuth, browser responsivo ou pós-deploy concluídos.
4. **Modelo:** seis entidades originais da baseline não devem ser retroativamente alteradas para incluir `FotoExcursao` e novos campos; tratá-los como evolução aditiva.

## Próxima rodada (ordem e dependências)

1. Reavaliar PRs #2/#4/#5 e CI, comparar commits para não conflitar com outro agente; verificar se OAuth B1 foi realmente configurado.
2. Se B1 seguir bloqueado, iniciar **C1**: especificação de CPF com finalidade, minimização e matriz LGPD em documento separado, sem migração ainda; depois C2 apenas com requisitos de proteção aprovados.
3. Repetir testes, salvar links verificáveis, atualizar cada status/commit; não declarar TCC finalizado.
