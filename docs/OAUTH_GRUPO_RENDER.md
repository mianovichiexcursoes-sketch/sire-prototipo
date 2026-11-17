# Autorização local com grupo de segredos separado

17/11/2026 — assistência de IA. Complemento da PR #7; não é deploy do aplicativo.

O modo `--grupo-render WORKSPACE_ID` permite obter a autorização antes de provisionar um banco de ensaio. O navegador e o script devem rodar no mesmo computador. Requer somente Python 3 (biblioteca padrão), cliente OAuth desktop criado no projeto SIRE TCC, API Drive habilitada, conta de teste adicionada e chave de API Render. Entradas pelo getpass; nunca digitar segredos em comandos, arquivos ou chat.

O script valida por GET o ID e nome SIRE. do workspace antes do consentimento. Após PKCE/state e validação estrita de drive.file, cria um grupo novo `sire-drive-oauth-<sufixo>` com apenas CLIENT_ID, CLIENT_SECRET e REFRESH_TOKEN. A chave Render não integra o grupo. `serviceIds` e `secretFiles` vazios: não vincula à demo, não muda banco, não solicita deploy, não armazena segredos no disco. O nome não secreto do grupo é exibido como comprovante. Falha de rede após POST pode deixar um grupo criado; conferir o painel antes de repetir. Não remover grupos anteriores automaticamente.

No Windows PowerShell, após baixar o script desta revisão:

```
py .\autorizacao_drive.py --grupo-render tea-dbqsq4on74is73d4onpg
```

Ordem das entradas ocultas: RENDER_API_KEY; SIRE_DRIVE_CLIENT_ID; SIRE_DRIVE_CLIENT_SECRET. Em seguida, aprovar a conta no Google no navegador aberto pelo script. O resultado esperado é CONCLUIDO e o nome do grupo. Somente o resultado efetivamente observado comprova autorização/salvamento. Revogar a chave Render temporária criada para este procedimento após confirmar o grupo; não revogar chaves de integrações existentes.

Chave Render: Account Settings > API Keys. Se houver escopos, workspace SIRE., leitura do workspace e leitura/escrita de Environment Groups. Não são necessários acessos a bancos, deploys ou edição de serviços. Sem escopos disponíveis, a chave clássica tem alcance maior; criar uma temporária apenas para esta execução e revogá-la depois.

Evidências: `python -m unittest sire.tests.test_oauth_drive -v`: nove testes aprovados, incluindo três novos para criação de grupo sem vínculo, rejeição de workspace divergente e rejeição de segredos extras. Compilação Python e diff check sem erros. Chamadas simuladas; OAuth real e criação real do grupo ainda dependem da execução pela autora. Nenhum teste remoto de upload, remoção, permissões ou persistência é declarado neste incremento.

Fontes oficiais consultadas: https://api-docs.render.com/reference/create-env-group ; https://api-docs.render.com/reference/retrieve-owner ; https://render.com/docs/configure-environment-variables ; https://render.com/docs/api-keys .

Continuidade: verificar grupo no Render sem revelar seus valores, preparar ensaio isolado persistente, testar fotos sintéticas e reconciliar cadeia de PRs. Manter a demo preservada. O grupo resolve a guarda das credenciais; não resolve sozinho a infraestrutura de ensaio nem o aceite funcional.
