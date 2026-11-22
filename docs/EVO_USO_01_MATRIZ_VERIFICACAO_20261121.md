# EVO-USO-01 — matriz de verificação independente (21/11/2026)

**Estado: plano de ensaio; nenhum teste de navegador executado neste documento.** Base de inspeção: `feat/evo-uso-01-tutorial-20261118`, arquivos `sire/static/sire/js/tutorial-uso.js` (blob `41039cd9f6d464cd746e70ee33656d97f26f4946`) e `sire/templates/sire/base.html` (blob `7dfff230ebb346a007cdf2e65533c9bc4e84c483`). Não altera código, demo, migrações ou dados. Fontes originais RN, baseline, guia, UC01–14, requisitos, CAT e registro consultadas por ID no Google Drive em 21/11/2026; versão/data de cada documento não revalidada.

| ID | Perfil e cenário | Resultado esperado | Evidência requerida | Estado |
|---|---|---|---|---|
| TUT-01 | Visitante sem armazenamento prévio abre catálogo | Convite aparece; Começar abre guia; Agora não fecha | captura + navegador/viewport | Pendente |
| TUT-02 | Visitante percorre Anterior/Próximo/Pular | Contador coerente, nenhum POST, navegação e reserva não disparadas | vídeo ou registro de eventos de rede | Pendente |
| TUT-03 | Passageiro autenticado abre Como usar | Etapas de catálogo, embarque, confirmação e minhas reservas; nenhum passo de agente | captura + usuário sintético | Pendente |
| TUT-04 | Agente autenticado abre Como usar | Etapas de agência, publicação e passageiros; nenhuma operação de escrita automática | captura + usuário sintético | Pendente |
| TUT-05 | Escape e teclado, foco | Escape fecha; foco volta ao acionador; controles acessíveis por teclado | roteiro de teclado + captura | Pendente |
| TUT-06 | Página sem alvo de destaque | Mensagem de indisponibilidade, sem erro JS nem bloqueio | console e captura | Pendente |
| TUT-07 | localStorage bloqueado | Guia continua funcional, sem dados pessoais persistidos | console + navegador isolado | Pendente |
| TUT-08 | Mobile 320/375/768 px | Guia utilizável sem sobrepor ações críticas permanentemente | capturas por viewport | Pendente |
| TUT-09 | Sem vagas e estado vazio | Tutorial não induz reserva impossível nem cria registro | base sintética + evidência de consulta | Pendente |
| TUT-10 | Perfil/agência distintos | Orientação não expõe dados de outra agência | ensaio de autorização + logs redigidos | Pendente |

## Achados de inspeção estática (não equivalem a falha reproduzida)

1. `findTarget(label)` procura correspondência textual aproximada em `a,button,h1,h2,nav a`; títulos genéricos ou alvos ausentes podem destacar elemento inesperado. Exigir ensaio em cada página e considerar seletores estáveis `data-tutorial` numa alteração isolada, após conciliar templates com o outro agente.
2. O convite é inserido sem teste de sobreposição com componentes da página; conferir em viewport pequeno e com zoom 200%.
3. `remember()` captura exceção de armazenamento e o guia continua disponível; ensaio real com storage indisponível ainda necessário.
4. Não há disparo explícito de `submit()` nem `fetch()` no script inspecionado. Isto **não prova** ausência de efeitos colaterais no navegador; testar rede e formulários.

## Dependências e bloqueios

- OAuth `drive.file`: responsável autora/operador do aplicativo; bloqueia aceitação de fotos reais, **não** os cenários TUT-01–08.
- Avaliação do orientador: depende de versão revisada, demonstração e retorno humano; não houve aceite.
- Integração: comparar HEADs das branches `feat/evo-uso-01-tutorial-20261118`, `fix/tutorial-fechar-acessibilidade-20261119`, `fix/tutorial-mobile-viewport-20261119` e `test/tutorial-storage-indisponivel-20261120` antes de tocar `base.html` ou JS.

## Rastreabilidade

EVO-USO-01 → `tutorial-uso.js` + `base.html` → TUT-01–10 → capturas/logs **pendentes** → seção de metodologia/avaliação da monografia **pendente**. RN-03–05 e UC01–UC14 permanecem históricos; tutorial é extensão, não novo caso original. A matriz acima não substitui CAT-VF01–06 nem VF01–16.

**Próxima ação:** reconciliar os fixes existentes, executar TUT-01–08 em navegador isolado com contas sintéticas, anexar evidência por ID, atualizar checklist persistente e só então considerar integração. Nenhum merge/deploy nesta unidade.
