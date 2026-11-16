# SIRE — iteração em espiral: acesso e recuperação

## Objetivo

O teste da demonstração em 12/11/2026 identificou que uma variação
de maiúsculas no nome da conta de demonstração impedia o login.
Esta iteração refina o UC02 e propõe recuperação por e-mail como extensão
de autenticação. Não altera as seis entidades ou a regra de reserva.

## Riscos e decisões

- Uma grafia alternativa só é resolvida automaticamente se corresponder
  a uma única conta. Em colisões, exige-se a grafia exata. A senha
  continua distinguindo maiúsculas e minúsculas.
- Contas individuais usam o token do Django e um domínio HTTPS definido
  no servidor. A resposta não indica se o e-mail existe. As contas
  compartilhadas da banca ficam fora do fluxo e são geridas pelo Render.
- A entrega pela internet depende de remetente verificado e chave do
  Resend. As variáveis devem ficar no ambiente do serviço:
  SIRE_RESEND_API_KEY, SIRE_EMAIL_FROM e SIRE_RESET_DOMAIN
  (somente o hostname, sem esquema ou caminho).
- Antes de habilitar o envio público, validar as cotas do provedor e
  aplicar limitação de solicitações para proteger o envio contra abuso.

## Validação e próximo ciclo

Validação local com SQLite e caixa de e-mail em memória: login com três
grafias, senha incorreta, usuário inexistente, colisão de nomes,
exclusão da conta demo, redefinição e rejeição de link reutilizado.
A entrega real de e-mail e a homologação no PostgreSQL do Render
ficam pendentes. VF03 é a referência para login; o fluxo de recuperação
deve ser registrado como verificação separada da baseline.

## Ciclo seguinte (16/11/2026): recuperação por código

### Problema observado

A recuperação por e-mail foi ativada na demonstração em 13/11/2026, mas o
provedor de envio só entrega a qualquer destinatário depois da verificação
de um domínio próprio. Sem ela, apenas o e-mail da titular da conta do
provedor recebia o link. A exigência da autora — toda pessoa cadastrada deve
conseguir recuperar a senha — não era atendida.

### Risco

Manter um recurso que funciona para uma única pessoa e falha em silêncio
para as demais; e condicionar uma função do protótipo a um serviço externo e
ao acesso ao DNS do domínio da agência.

### Decisão

Adotar o código de recuperação como mecanismo principal. O código é mostrado
na criação da conta; quem esquece a senha informa usuário e código e define
uma senha nova. A recuperação por e-mail permanece no código como opção
secundária, sem ser pré-requisito.

### Como funciona (`sire/recuperacao.py`)

- O código não é gravado: é calculado por HMAC-SHA256 com a chave secreta do
  servidor, o identificador da conta e o hash da senha atual. Não há campo,
  tabela ou migration novos; a baseline ER-SIRE 2.1 e as seis entidades
  permanecem inalteradas.
- Formato: 20 caracteres em quatro grupos (100 bits), aceito com ou sem
  hífens e em minúsculas. A comparação é feita em tempo constante.
- Ao trocar a senha, o código anterior deixa de valer, um novo é mostrado e
  as sessões abertas são encerradas.
- A conta autenticada consulta o código atual em “Código de recuperação”.
- Uma única mensagem de erro para usuário ou código inválidos.
- Limite de 5 tentativas recusadas por hora, por IP e por usuário.
- As contas compartilhadas da banca ficam fora do mecanismo.

### Limites

- Quem perde a senha e o código depende da redefinição pela agência.
- Se a chave secreta do servidor mudar, ou se uma atualização do Django
  regravar o hash da senha, os códigos emitidos deixam de valer.
- O contador de tentativas fica na memória do processo (instância única).
- Posse do usuário e do código equivale à posse da conta.

### Verificação

`scripts/teste_recuperacao_codigo.py`, em SQLite descartável: 25 verificações
conformes (emissão no cadastro, ausência do código no banco e na sessão,
consulta autenticada, código errado, usuário inexistente, senha fraca,
recuperação válida, troca do código, sessões encerradas, contas
compartilhadas, nomes em grafias diferentes e limite de tentativas). Saída em
`evidencias/2026-11-16_recuperacao_por_codigo_local/`. As verificações
anteriores de login e de recuperação por e-mail foram reexecutadas e
permaneceram conformes.
