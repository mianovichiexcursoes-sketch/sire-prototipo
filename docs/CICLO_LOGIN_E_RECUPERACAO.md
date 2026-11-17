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

## Ciclo de qualidade (16/11/2026): testes automatizados e versão

Uma revisão do projeto com critérios de banca apontou a ausência de suíte
automatizada, de teste de regressão e de instalação reprodutível.

- `sire/tests/`: suíte no framework de testes do Django, com os cenários
  VF01–VF16, login, recuperação de senha e reservas simultâneas.
- `.github/workflows/testes.yml`: a suíte roda a cada envio em SQLite e em
  PostgreSQL 18. Os testes de concorrência executam só no PostgreSQL.
- Dependências com versão exata; `main` passou a conter as três iterações;
  versão `v0.3.0` marcada.

## Ciclo da conta e privacidade (16/11/2026)

### Problemas observados

A autora, ao usar a demonstração, notou que não era possível ver a senha
digitada e pediu o registro da data de nascimento do passageiro. A revisão
havia apontado que o usuário não trocava a própria senha e que o sistema
coletava dados pessoais sem aviso de privacidade.

### Risco

Erro de digitação na senha sem meio de conferir; conta sem troca de senha;
coleta de dado pessoal sem finalidade declarada. A data de nascimento exige
alterar o esquema, o que atinge a afirmação, repetida até aqui, de que nenhum
campo havia sido acrescentado.

### Decisões

- **Data de nascimento:** campo opcional `data_nascimento` em `PerfilUsuario`
  (migration `0005`). É a única alteração de esquema posterior à baseline; as
  seis entidades e as migrations 0001–0004 não mudam. O formulário de cadastro
  do passageiro a exige e recusa datas futuras ou implausíveis. Finalidade:
  identificar o passageiro na lista da excursão, visível ao agente da agência.
- **Aviso de privacidade:** página pública `/privacidade/`, com os dados
  guardados, a finalidade, quem os vê, onde ficam e por quanto tempo. O
  cadastro exige o aceite. O texto é informativo e não foi revisado por
  profissional da área jurídica.
- **Minha conta e troca de senha:** `/minha-conta/` mostra os dados da própria
  conta; `/minha-conta/senha/` troca a senha mediante a senha atual. A troca
  gera novo código de recuperação. As contas compartilhadas da banca não
  trocam senha.
- **Mostrar senha:** `sire/static/sire/js/mostrar-senha.js` acrescenta um
  botão a cada campo de senha. É o único JavaScript do projeto; sem ele os
  formulários continuam funcionando.

### Limites

- Contas criadas antes desta alteração ficam sem data de nascimento.
- O usuário ainda não altera e-mail, nome ou data de nascimento, nem exclui a
  própria conta.
- Não há registro da data e da versão do aviso aceito.

### Verificação

`sire/tests/test_conta.py`: 17 testes. A suíte completa tem 67 testes; em
SQLite, 65 aprovados e 2 pulados (concorrência). O comportamento do botão de
mostrar senha foi conferido manualmente no navegador.
