# SIRE — progresso executivo e auditoria de entrega

**Registro inicial:** 17/11/2026. **Status:** em andamento. Este registro é uma extensão de gestão, **não altera retroativamente** a baseline ER-SIRE 2.1 (UC01–UC14, seis entidades). Dados reais e credenciais não devem ser usados em testes nem commits.

## Fonte normativa e acesso

Fontes oficiais **lidas nesta rodada**: [RN-01–RN-41](https://docs.google.com/document/d/1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0/edit), [guia de implementação](https://docs.google.com/document/d/1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U/edit), [UC01–UC14](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit), [requisitos v3.0](https://docs.google.com/document/d/1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM/edit) e [CAT revisão 0.2](https://docs.google.com/document/d/1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is/edit). Em cada rodada, **reabrir** as seções pertinentes antes de qualquer implementação; a leitura aqui registrada não autoriza presumir futuras revisões.

Fontes a conferir antes da auditoria final: [documentação baseline](https://docs.google.com/document/d/19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8/edit), [registro de implementação](https://docs.google.com/document/d/1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM/edit), [monografia](https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit), [modelo IFSP](https://docs.google.com/document/d/1RQVZxphHgUkOFK1HXgv9GEN5sxYZxWwviQIIv_NvgTo/edit), [regulamento PFC 2026](https://drive.google.com/file/d/1AEzHiDHFro2LuLCfMzOa4GIGsPNS2_fL/view), [parecer crítico](https://docs.google.com/document/d/1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA/edit). Registrar datas/versões verificadas em cada revisão.

## Quadro de execução e dependências

| ID | Status | Dependência | Evidência atual | Próxima ação |
|---|---|---|---|---|
| A — Ficha, roteiro, inclusos e 6 fotos | **Em verificação** | CAT-RF-02/03/04; RN-03/04/06/11/14 | [branch ficha/fotos](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/tree/etapa/ficha-fotos-sire), [plano técnico](INCREMENTO_FICHA_FOTOS_DRIVE.md), [PR #2](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/2) | Conferir diff/CI, nome real da migration 0007, isolamento por agência, validação e limites, regressão sem credenciais |
| B — OAuth Drive real | **Bloqueado para aceite real** | Autorização OAuth separada do aplicativo, segredos no Render, A testado | [instruções de configuração](INCREMENTO_FICHA_FOTOS_DRIVE.md); **nenhum envio real confirmado** | Responsável pela conta configurar OAuth/Render em canal seguro; testar upload/exclusão e persistência após redeploy. Não usar autorização do conector ChatGPT como credencial Django |
| C — CPF opcional/protegido | **Pendente** | RN-04/05; UC01; definição de finalidade/minimização; branch livre | Sem código/teste confirmado | Propor extensão de requisito, implementar validação de dígitos e testes **sintéticos**, limitar exposição e armazenamento; não usar CPF real |
| D — UX de reserva | **Pendente** | UC05/10/11/12; RN-17–30/33 | Fluxo da baseline descrito no README | Melhorar resumo de pacote, preço, embarque e confirmação, sem cobrar ou selecionar assentos |
| E — Painéis | **Pendente** | RN-03/04/05/27/28; permissões | Não auditado nesta rodada | Inspecionar consultas e isolamento de agência/passageiro antes de mudar templates |
| F — Testes e validação | **Pendente** | A–E conforme cenário | README da branch declara 67 testes da baseline, **não reexecutados nesta rodada** | Rodar SQLite/PostgreSQL isolados, VF01–16, CAT-VF01–06, migrações, responsividade, fotos e persistência; anexar logs reais |
| G — Auditoria documental/monografia | **Pendente** | Inventário Drive, código/testes/evidências finais | [monografia](https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit), [parecer crítico](https://docs.google.com/document/d/1xhVM1WTwc_-0yMDn3F0gdaPrd-0g3qCS3Q9Malvk7BA/edit) | Revisar TODOS os arquivos do TCC, normas IFSP/ABNT, fontes, título aprovado, transparência IA, modelos, resultados e evidências; relatório de divergências por arquivo |

**Política de salto:** se um item estiver bloqueado, registrar bloqueio, responsável, pré-requisito e condição de desbloqueio; avançar no **primeiro item independente** com fontes consultadas. Reavaliar bloqueios na próxima rodada. Nunca fazer merge/deploy com testes pendentes.

## Matriz inicial de rastreabilidade (a expandir após inspeção do código)

| Fonte | Comportamento | Artefatos de código apontados no plano | Testes/evidências ainda necessários | Monografia |
|---|---|---|---|---|
| CAT-RF-02, UC06–07, RN-03/14 | Descrição, roteiro e inclusos opcionais; edição só pela agência | `sire/models.py`, `sire/forms.py`, `excursao_form.html`, migration 0007 | Cadastro/edição com registros antigos e agência alheia | Seção de incremento e validação a identificar |
| CAT-RF-03, RN-03/04/11 | Até 6 fotos, proteção de rascunho e exclusão | `FotoExcursao`, `sire/drive_fotos.py`, views/templates | Arquivos inválidos, 5MB+, 6 fotos, Drive real, redeploy | Incremento + limitações do armazenamento |
| CAT-RF-04, UC05/10/11, RN-20–30 | Ficha e reserva sem regressão | `detalhe_excursao.html`, `catalogo.html`, views | CAT-VF e VF afetados, reserva/vagas | Resultados com prints e ambiente |
| CPF — extensão a especificar, RN-04/05 | Identificação com minimização e proteção | **Ainda não definidos** | Testes com CPF sintético e autorização | Limites/ética/privacidade, sem alegar requisito da baseline |
| RN-33–37 | Reserva distinta de pagamento | Templates e modelos existentes a inspecionar | Não simular pagamento como processado | Escopo e trabalhos futuros |

## Log das rodadas

### 17/11/2026 — rodada 1
- **Feito:** leitura direta das fontes oficiais RN-01–RN-41, CAT 0.2, UC, requisitos e guia; inspeção do README e plano técnico na branch `etapa/ficha-fotos-sire`; criação deste checklist em branch documental separada.
- **Não verificado:** execução local de testes, checks do PR #2, migration 0007, OAuth do app, deploy e edição da monografia. Não há alegação de sucesso nesses itens.
- **Bloqueio B:** falta comprovação de cliente OAuth autorizado para o **Django**, refresh token armazenado com segurança no Render e testes reais de persistência; responsável pela conta deve configurar em ambiente seguro. A implementação independente de CPF/UX não depende de B.
- **Próxima rodada:** verificar PR #2, diff e CI; se houver trabalho concorrente ou dependência externa, iniciar uma extensão independente em branch própria e com testes; atualizar este arquivo sem sobrescrever o trabalho do outro agente.


### 17/11/2026 — rodada 2: auditoria estática da PR #2 e concorrência
- **Fonte reaberta:** regras RN-01–RN-41 (revisão Drive consultada nesta rodada), CAT revisão 0.2. Diff real da PR #2 inspecionado: `sire/drive_fotos.py`, `sire/forms.py`, `sire/views.py`, `sire/migrations/0007_ficha_e_fotos_drive.py` e `docs/INCREMENTO_FICHA_FOTOS_DRIVE.md`.
- **Constatado no código (não é teste):** migração 0007 depende de 0006 e adiciona três campos opcionais e `FotoExcursao`; `adicionar_foto` e `remover_foto` filtram excursão por agência do agente; decodificação de JPEG/PNG/WebP com limites 5 MB/20 MP, conversão JPEG 1600×1600 e até seis fotos; token do aplicativo exige variáveis próprias. Sem autorização OAuth não há teste real.
- **Risco A-01, acesso/cache (revisar antes de merge):** `imagem_excursao` retorna `Cache-Control: public, max-age=3600` quando publicada. Se a excursão for despublicada logo depois, caches do cliente/intermediário podem continuar servindo a imagem por até uma hora, mesmo que o Django passe a negar o acesso. Considerar `private, no-store` para fotos em ambos os estados ou política explícita de invalidação e testar transição publicada→rascunho. RN-03/04/11 e CAT-RF-03.
- **Risco A-02, concorrência (revisar antes de merge):** `adicionar_foto` verifica `excursao.fotos.count() >= 6` fora de trava/transação. Duas solicitações simultâneas podem ultrapassar seis fotos; testar duas adições simultâneas e introduzir serialização/controle transacional antes de aceitar CAT-RF-03.
- **Risco A-03, órfãos remotos:** falha de criação da referência após envio tenta exclusão, mas se a exclusão remota falhar, o arquivo ficará órfão sem registro de reconciliação. Documentar política de reconciliação e teste com falha simulada; não registrar credenciais.
- **Risco A-04, sem comprovação de suíte da PR:** nenhum resultado de `manage.py test`, CI ou deploy foi confirmado nesta rodada. O diff da PR #2 não inclui arquivo de testes novo. Solicitar/produzir testes isolados para os limites, autorização, draft, fotos, exclusão e migração. Não inferir aprovação a partir do README.
- **Concorrência de agentes:** o repositório registra commit recente `75fcc6d13715eeca6fdc32ecb1a9ff2b8351f35c` (conta/privacidade, 17/11/2026 01:54 UTC), indicando trabalho paralelo ativo; **não alterar** `models.py`, `forms.py`, `views.py` nem migrações compartilhadas sem reconciliar branches. Esta rodada limitou alterações à branch documental independente.
- **Próxima ação independente:** produzir testes de regressão da PR #2 em branch própria quando a base e as migrações estiverem estabilizadas; antes disso, revisar o risco de cache e limite de seis fotos com o agente responsável pela PR. OAuth real continua bloqueado até credenciais do app configuradas com segurança. A monografia segue pendente.


### 17/11/2026 — rodada 3: protocolo de regressão de fotos
- **Entrega versionada:** [PROTOCOLO_TESTES_FOTOS_PR2.md](PROTOCOLO_TESTES_FOTOS_PR2.md), commit [`6aff0f3`](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/commit/6aff0f3bd9956b61c477482bf593de901ca094f7). Inclui 16 casos com pré-condições, resultados esperados e evidências exigidas, além de sequência de execução SQLite/PostgreSQL.
- **Fontes efetivamente reabertas:** RN-01–RN-41, CAT revisão 0.2 e guia de implementação; código real `sire/views.py`, `sire/drive_fotos.py`, `sire/models.py` e `sire/forms.py` da branch PR #2. A função `imagem_excursao` ainda usa cache público de 3600 s; `adicionar_foto` ainda faz contagem sem transação; falha de compensação remota é silenciada.
- **Status A:** em verificação; testes FOTO-01–16 **não executados**, protocolo não prova conformidade. **Bloqueios para aceite:** A-01 cache público, A-02 limite sob concorrência, A-03 reconciliação de órfãos e evidências reais. Responsável: implementação da PR #2; retomar aceite após correções e testes.
- **Status B:** OAuth do aplicativo Django não comprovado; responsável pela conta configurar credenciais somente em ambiente seguro. Não usar tokens do ChatGPT.
- **Trabalho concorrente:** a PR #2 permanece aberta como rascunho; não alterados models, views, migrations ou demo.
- **Próxima ação independente:** implementar testes Django isolados do protocolo em branch que não toque no código do agente; antes de eventual merge, reconciliar PR #2 e registrar saída real. Se não houver ambiente de teste, avançar na auditoria documental e inventário do Drive, sem alegar testes concluídos.


### 17/11/2026 — rodada 4: testes Django de fotos em PR independente
- **Fontes reabertas:** documento oficial RN-01–RN-41, especificação CAT revisão 0.2 e implementação atual em `etapa/ficha-fotos-sire` (views, models, urls). PR #2 continua tendo código de fotos; esta entrega não modifica a branch da PR #2.
- **Entrega real:** commit [`0850093`](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/commit/0850093ce9bb59debc864f480465c20f80c296ee), arquivo [`sire/test_fotos_regressao.py`](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/blob/testes/fotos-regressao-isolada-20261117/sire/test_fotos_regressao.py), [PR #4 em rascunho](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/4) contra `etapa/ficha-fotos-sire`.
- **Cobertura criada (NÃO executada):** FOTO-02 visitante não acessa rascunho; FOTO-03 agente de outra agência não acessa; FOTO-04 agente responsável acessa sem cache; FOTO-05 publicação→rascunho exige `no-store` e 404; FOTO-07 sétima foto rejeitada antes do upload. Mocks de Drive, contas e IDs sintéticos; sem segredos.
- **Falha esperada em FOTO-05:** o código atual retorna `Cache-Control: public, max-age=3600`; o teste foi criado para evidenciar a falha, não para mascará-la. Ainda não houve execução da suíte, logo não há contagem de testes aprovados.
- **Bloqueios preservados:** correção de cache e concorrência de fotos na PR #2 (responsável pelo incremento), teste de concorrência real PostgreSQL FOTO-08, reconciliação de órfãos FOTO-12 e OAuth próprio do Django. Nenhum merge/deploy realizado.
- **Próximo passo:** verificar CI/logs e executar os cinco testes em ambiente isolado; corrigir problemas detectados em coordenação com o responsável pela PR #2. Se a execução estiver indisponível, avançar com documentação acadêmica independente e revisão da matriz de rastreabilidade.


### 17/11/2026 — rodada 5: ampliar testes independentes de exclusão
- **Fontes reabertas nesta rodada:** RN-01–RN-41, CAT revisão 0.2 e guia de implementação; inspecionados `sire/views.py` e `sire/models.py` na branch `etapa/ficha-fotos-sire`, além do arquivo de testes da PR #4 e commits recentes do outro agente (incluindo `75fcc6d`). Não modificados models/views/migrations, nem a demo.
- **Entrega versionada:** commit [`63863f1`](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/commit/63863f1046e932e73274c0a320ef2282f8491bff), na branch isolada da [PR #4](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/4), amplia `sire/test_fotos_regressao.py` de cinco para **sete testes criados**. Novos: FOTO-09 agente de outra agência não pode excluir foto via URL direta (404, registro preservado, sem chamada remota); FOTO-10 falha simulada do Drive ao excluir preserva referência no banco e devolve redirecionamento. Dados e erros sintéticos, exclusão remota mockada.
- **Execução/CI:** testes **não executados nesta rodada**; criação de testes não equivale a aprovação. FOTO-05 continua destinado a detectar `Cache-Control: public, max-age=3600`; sem correção de cache, é esperado falhar. FOTO-08 concorrência e FOTO-12 reconciliação de órfãos continuam pendentes.
- **Dependências e próxima ação:** executar `python manage.py test sire.test_fotos_regressao` sobre ambiente Django isolado com a PR #2, registrar saída completa e identificar falhas; solicitar ao responsável pela PR #2 correção do cache e serialização do limite de seis fotos antes de merge. OAuth Drive do aplicativo continua bloqueado até autorização segura; a documentação/CPF/UX podem progredir independentemente.


### 17/11/2026 — rodada 6: testes de falha fechada e método HTTP
- **Fontes reabertas:** RN-01–RN-41 (ênfase RN-03/04/05/11), CAT 0.2 (CAT-RF-03 e CAT-RNF-02), guia de implementação; arquivos sire/views.py e sire/urls.py da branch etapa/ficha-fotos-sire; arquivo sire/test_fotos_regressao.py da branch de testes. Verificada a separação de branches antes da escrita.
- **Entrega real:** commit [9aa070d](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/commit/9aa070dfba5c557b9807a6fb1b79253a9d4e8049) na [PR #4](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/pull/4). Agora são **nove testes Django criados** (sete anteriores mais FOTO-06 e FOTO-11): FOTO-06 exige 404 e nenhum download remoto se OAuth do aplicativo estiver ausente, mesmo com excursão publicada; FOTO-11 exige 405 para GET de exclusão, preservando registro e sem chamada ao Drive. Ambos usam mocks, sem dados reais.
- **Execução:** NÃO executados. Ambiente local desta rodada não consegue resolver github.com para clonar; conector GitHub permite ler/escrever código, mas não executar Python/Django. Nenhum CI ou deploy foi declarado aprovado. Os nove testes continuam sujeitos à validação em ambiente com dependências Django e branch da PR #2. FOTO-05 deve revelar cache público enquanto não corrigido.
- **Bloqueios:** OAuth Django real e persistência de fotos dependem da configuração segura da conta (responsável: titular da aplicação); riscos A-01 cache, A-02 concorrência e A-03 órfãos permanecem na PR #2 (responsável: implementação do incremento). Condição para aceite: correção, execução de suíte e evidências SQLite/PostgreSQL; não mesclar antes disso.
- **Próxima ação independente:** obter ambiente executável/CI para os nove testes e registrar logs. Se indisponível, ampliar documentação de privacidade/CPF ou UX em branch própria após reabrir fontes oficiais, sem alterar modelos/views/migrations em trabalho concorrente.


### 17/11/2026 — rodada 7: cobertura de publicação e remoção de referência
- **Fontes reabertas nesta rodada:** RN-01–RN-41, CAT revisão 0.2, guia de implementação. PR #2, #3 e #4 conferidas: abertas e em rascunho, sem merge; PR #2 continua com cache público em `imagem_excursao`.
- **Entrega independente:** dois testes Django adicionais em `sire/test_fotos_regressao.py`, branch `testes/fotos-regressao-isolada-20261117`, commit [`01fdf92`](https://github.com/mianovichiexcursoes-sketch/sire-prototipo/commit/01fdf92f89730c525f9cc0d931935afddfabfa40). Total **11 testes escritos**: FOTO-01 verifica acesso público à imagem de excursão publicada, MIME, nosniff e chamada ao Drive mockado; FOTO-12 verifica que referência excluída retorna 404 sem tentar download remoto.
- **Evidência e limitação:** apenas leitura do código e commit confirmados; **testes não executados** nesta rodada, sem resultado de SQLite/PostgreSQL, CI, OAuth ou deploy. O teste FOTO-05 deve revelar o cache público inadequado até correção. Não usar 11 testes escritos como sinônimo de 11 aprovados.
- **Bloqueios:** integração real Google Drive depende de OAuth do Django e segredos seguros no Render (responsável pela conta); teste da suíte requer ambiente Django acessível; correção de views e concorrência depende de conciliação com o agente da PR #2. Reavaliar em próxima rodada.
- **Próxima ação independente:** executar a suíte com evidências verificáveis; se indisponível, cobrir outros cenários com mocks sem tocar nos arquivos concorrentes. Preservar baseline, demo e dados.
