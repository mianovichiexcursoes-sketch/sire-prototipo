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
