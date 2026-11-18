# EVO-USO-01 — Correções isoladas de usabilidade (18/11/2026)

Base inspecionada: PR #15, SHA 3f4549bfba35411b6e02918a8cfd6a1f6f4111d6. Fonte: RN-01–05, UC01–UC14, guia e especificação complementar consultados por ID no Google Drive. Baseline ER-SIRE 2.1 preservada.

Alterações propostas: roteiro próprio do passageiro autenticado; correspondência exata para reduzir alvos falsos; destaque sem position/z-index; foco inicial no convite; ciclo de Tab dentro do guia; retomada do índice por versão e perfil, sem dados pessoais. Nenhum clique, envio, publicação ou pagamento automático.

Limites: correspondência exata pode não encontrar alvos com texto distinto; situação de alvo ausente é apresentada ao usuário. O convite e o diálogo exigem teste de leitor de tela, navegação, viewport e revisão de contraste. Esta entrega é implementação proposta, NÃO teste funcional ou aceite.

Matriz: TUT-01 primeiro acesso e storage indisponível; TUT-02 passageiro autenticado; TUT-03 agente; TUT-04 foco/Tab/Escape; TUT-05 celular e alvo ausente; TUT-06 nenhuma escrita involuntária. Todos aguardam execução real no navegador e regressão Django. Avaliação pelo orientador pendente.

Bloqueios: OAuth real e persistência de fotos dependem de autorização do app e ambiente isolado, não do tutorial. PR #2 aparece fechada na consulta de 18/11; apurar motivo antes de marcar como integrada. Conciliação de templates e PRs antes de merge; demo intacta.
