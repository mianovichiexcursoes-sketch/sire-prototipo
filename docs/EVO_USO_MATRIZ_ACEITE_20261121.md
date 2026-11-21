# EVO-USO-01 — matriz de aceite e dependências (21/11/2026)

**Natureza:** unidade documental de preparação de verificação, não evidência de aprovação de teste. Fontes originais lidas diretamente por ID em 21/11/2026: regras RN-01–RN-41, desenvolvimento SIRE (baseline ER-SIRE 2.1), guia de implementação, UC01–UC14, requisitos v3.0, catálogo/ficha rev. 0.2 e registro de implementação. A versão editorial da fonte não deve ser confundida com a data da leitura.

**Preservação histórica:** seis entidades e UC01–UC14 da baseline não são renumerados. EVO-USO-01 é extensão aprovada pela autora em 18/11, após feedback qualitativo do orientador em 17/11. Vídeo não é entrega exigida nesta evolução; o tutorial interativo substitui essa proposta.

| Critério EVO-USO-01 | Fonte / relação com baseline | Implementação a inspecionar | Ensaio objetivo (a executar) | Evidência exigida | Situação |
|---|---|---|---|---|---|
| TUT-01 descoberta | UC de consulta pública e cadastro; extensão EVO-USO-01 | PR #15 e derivadas; template/JS real | Primeiro acesso exibe oferta; botão Como usar reabre após Pular | Captura + log com SHA | Pendente de execução integrada |
| TUT-02 papéis | RN-03, RN-04, RN-05 | Seleção de passos por papel | Visitante não recebe instruções administrativas; agente não recebe instruções privadas de outro perfil | Cenários sintéticos por papel | Pendente |
| TUT-03 alvos | UC01–UC14; EVO-USO-01 | Seletores e páginas reais | Alvo inexistente/estado vazio não bloqueia fluxo | Captura e log | Pendente |
| TUT-04 navegação | EVO-USO-01 | Botões Anterior, Próximo, Pular, Fechar | Avanço, retrocesso e fechamento não enviam formulários | Teste navegador + rede/DB isolado | Pendente |
| TUT-05 teclado | RN-05; extensão de acessibilidade | PRs #20/#33 e derivadas | Foco visível, Tab/Shift+Tab, Escape, retorno de foco | Playwright + captura | Pendente |
| TUT-06 celular | EVO-USO-01 | CSS e layout responsivo | 320px e 375×812, sem corte de controles nem alvo inatingível | Capturas em viewport explícito | Pendente |
| TUT-07 persistência mínima | RN-04 e minimização | localStorage com fallback | SecurityError não quebra tutorial; armazenar apenas versão/progresso, sem PII | Teste isolado PR #54 + log | Pendente de execução |
| TUT-08 segurança de ações | RN-06–16, RN-17–30 | Fluxos publicação/reserva | Tutorial nunca publica excursão nem confirma reserva por si só | Testes DB sintético antes/depois | Pendente |
| TUT-09 avaliação | Feedback 17/11; decisão 18/11 | Versão revisada e roteiro | Autora solicita ao orientador nova tentativa; registrar resultado real | Registro datado do retorno | Bloqueado por testes e avaliação humana |

## Dependências e isolamento

- **Tutorial:** requer conciliação de PRs #15/#20/#21/#33/#35/#39/#53/#54 antes de alegar suíte integrada. Não requer OAuth Drive para fluxos já disponíveis. Responsável técnico: integração/revisão de código; retomar após HEAD único e ambiente de teste reproduzível.
- **Drive OAuth:** sem confirmação de autorização própria do Django com escopo `drive.file` e configuração segura no Render, não afirmar upload, exclusão ou persistência pós-deploy. Responsável: titular Google/Render; retomar com autorização e ensaios sintéticos verificáveis.
- **Aceite:** testes técnicos não substituem avaliação da autora/orientador; não contatar orientador sem autorização.
- **Demo:** branch `etapa/postgresql-windows` e serviço `sire-demo` não são alterados por esta documentação. Sem merge, deploy ou teste executado nesta unidade.

## Próxima ação verificável

Comparar os HEADs e arquivos sobrepostos das PRs de tutorial, produzir uma branch de integração isolada, executar testes Django/SQLite e Playwright no SHA exato, depois PostgreSQL em ambiente separado. Guardar logs e screenshots com data, SHA, navegador, viewport e resultado. Não concluir TUT-01–09 com base apenas em existência de arquivos de teste. Documentar depois os resultados reais na monografia, sem alterar a baseline.
