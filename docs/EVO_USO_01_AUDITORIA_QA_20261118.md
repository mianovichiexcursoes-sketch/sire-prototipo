# EVO-USO-01 — Auditoria estática e plano de verificação (18/11/2026)

**Escopo:** revisão da implementação inicial em `sire/static/sire/js/tutorial-uso.js` e `sire/templates/sire/base.html`, branch `feat/evo-uso-01-tutorial-20261118`. **Não é execução de teste de navegador nem aceite.** Revisão isolada para não editar arquivos compartilhados com outro agente.

## Fontes consultadas
Google Drive por IDs originais em 18/11/2026: RN-01–RN-41 (`1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0`), baseline (`19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8`), guia (`1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U`), UC01–14 (`1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY`), requisitos (`1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM`), catálogo (`1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is`), registro (`1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`). Plano EVO-USO-01 lido na branch `docs/retorno-orientador-tutorial-20261118`. Datas de modificação das fontes não verificadas.

## Achados por inspeção (a reproduzir)
1. **TUT-A01 — etapas do passageiro não são específicas do papel.** A condição `role === "agente" ? ... : ...` dá ao Visitante e ao Passageiro a mesma sequência; inclui `Criar conta` e `Entrar` para Passageiro autenticado. Em páginas autenticadas, alvos ausentes são esperados; adequar roteiro por papel e página, sem prometer navegação automática.
2. **TUT-A02 — seleção do alvo por texto é ambígua.** `findTarget(label)` usa correspondência parcial em `a,button,h1,h2,nav a`. Pode destacar título ou botão de ação diferente; exige seletor estável e alvo contextual, sem clicar nele.
3. **TUT-A03 — foco do convite e diálogo.** O convite inicial é inserido sem foco explícito; a janela com `aria-modal=false` foca Próximo, mas não controla Tab, não oferece foco no título e não restaura foco ao elemento do convite removido (usa ajuda como origem). Testar leitor de tela, Tab/Shift+Tab, Escape e retorno ao botão Como usar.
4. **TUT-A04 — destaque visual.** `.sire-guia-alvo` altera `position:relative` e `z-index`; pode modificar posicionamento de elementos existentes e interferir na ordem visual. Verificar cabeçalho, formulários, telas estreitas e rolagem para alvo fora da viewport.
5. **TUT-A05 — continuidade entre páginas.** `index` reinicia em 0 ao abrir; somente `seen` é salvo. Não há retomada contextual após navegação, embora o plano mencione progresso/versão. Não persistir dados pessoais.
6. **TUT-A06 — restrição de escrita.** O código examinado apenas cria DOM, lê/grava chave de tutorial no localStorage e escuta eventos dos próprios botões; não há submissão programática de formulário. Isso é inspeção estática, não teste de regressão de reservas/publicação.

## Matriz de verificação planejada — ainda NÃO executada
| ID | Cenário | Evidência exigida | Estado |
|---|---|---|---|
| TUT-01 | Visitante, primeiro acesso, começar/pular, repetir com storage desabilitado | vídeo curto ou captura + log navegador, sem dados reais | Pendente |
| TUT-02 | Passageiro sintético, catálogo/detalhes/embarque/confirmar/minhas reservas | capturas por página; verificar instruções corretas sem envio | Pendente |
| TUT-03 | Agente sintético de agência A, excursões/embarque/publicação/reservas/passageiros | capturas; verificar papel e ausência de dados da agência B | Pendente |
| TUT-04 | Tab, Shift+Tab, Enter, Escape, foco de retorno, leitor de tela | roteiro com resultados por tecla, screenshots | Pendente |
| TUT-05 | 320px, 375px, 768px e desktop, alvo fora da tela e estado vazio/sem vagas | capturas por largura e resultado de rolagem | Pendente |
| TUT-06 | Nenhuma reserva/publicação involuntária; regressão permissões | suíte Django e navegação sintética; SHA, comando, saída | Pendente |

## Dependências e sequência
- Reconciliar HEAD/diff da PR #15 e possíveis alterações invisíveis de outro agente **antes de editar** JS/template.
- Implementar correções isoladas A01–A05 em branch técnica, sem merge/deploy automático.
- Rodar testes de navegador e regressões com perfis sintéticos e registrar ambiente, SHA, evidências e falhas. Se navegador indisponível, manter status pendente e executar outra tarefa documental independente.
- Modelo relacional e apêndice UC01–UC14 devem preservar seis entidades e baseline ER-SIRE 2.1; alterações novas como extensão.
- Avaliação pelo orientador é pendência humana após versão revisada; nenhuma aprovação presumida.
