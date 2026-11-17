# SIRE — Incremento 2: ficha completa e fotos no Google Drive

**Situação:** implementação em branch de desenvolvimento; integração/deploy e aceite funcional **pendentes**. Documento da evolução do protótipo, sem alteração retroativa da baseline ER-SIRE 2.1.

## Objetivo, escopo e requisitos

A ficha de excursão continua com as informações originais (título, destino, datas, preço, agência, embarques, disponibilidade e reserva), recebendo os seguintes campos **opcionais** na entidade `Excursao`: `descricao`, `roteiro` e `inclusos`. Um agente só altera excursões da própria agência; novas excursões continuam em RASCUNHO.

Para CAT-RF-03, `FotoExcursao` vincula uma excursão ao `drive_id` retornado pelo Google Drive; a imagem não fica no banco nem no disco temporário do Render. A primeira foto funciona como capa no catálogo, e todas aparecem na ficha. `FotoExcursao` é uma nova entidade técnica *desta extensão*, não uma substituição das seis entidades e dos UC01–UC14 históricos.

## Decisão técnica da espiral

O Google Drive pessoal foi escolhido para o protótipo acadêmico por aproveitar o espaço gratuito disponível na conta da autora, sujeito à cota real da conta. O Django usa a API do Google Drive com OAuth 2.0 da conta proprietária e escopo limitado `drive.file`. A conexão do Google Drive dentro do ChatGPT **não autoriza automaticamente o Django publicado**; é necessário configurar um cliente OAuth separado uma única vez.

Fotos são verificadas como JPG/PNG/WebP, limitadas a 5 MB de entrada e 20 milhões de pixels, transpostas conforme EXIF, redimensionadas para no máximo 1600 × 1600 e convertidas para JPEG otimizado (máximo de 2 MB). Limite de seis fotos por excursão. O SIRE cria uma pasta própria chamada `SIRE - Fotos de excursões` na conta autorizada. A imagem é distribuída por uma rota Django que consulta o Drive e mantém cache temporário, sem depender de links públicos instáveis. Fotos de excursões não publicadas só são servidas a agentes da agência proprietária.

Quando o Drive não está configurado, o cadastro textual continua funcionando e a interface indica que o envio de fotos está indisponível. Ao remover foto, a aplicação tenta excluir o arquivo remoto antes de excluir a referência no banco. A exclusão da própria excursão também exigirá política explícita de limpeza de arquivos, se vier a ser disponibilizada na interface no futuro.

## Preparar conexão gratuita com o Google Drive (uma vez)

1. Na conta Google que guardará as fotos, criar um projeto no [Google Cloud Console](https://console.cloud.google.com/) e ativar a **Google Drive API**. Isso não exige contratar um armazenamento adicional, mas está sujeito a cotas e políticas do Google.
2. Configurar a tela de consentimento OAuth e permitir o escopo `https://www.googleapis.com/auth/drive.file`. Durante o modo *Testing*, adicionar a conta responsável como usuário de teste. Para uso prolongado, revisar o estado de publicação do aplicativo; tokens de testes externos podem expirar em sete dias.
3. Criar um cliente OAuth do tipo **Aplicativo para computador** para a autorização administrativa única via navegador local e callback loopback com PKCE. Não é um login Google dos passageiros.
4. Usar um serviço e banco de ensaio separados, nome do serviço iniciado por `sire-oauth-test`, sem compartilhar o banco da demonstração. Definir apenas o identificador não secreto `SIRE_DRIVE_RENDER_SERVICE_ID` antes de executar `python scripts/autorizacao_drive.py` no computador onde o navegador será aberto.
5. O script solicita Client ID, Client Secret e chave de API do Render com entrada oculta (ou recebe de ambiente seguro). Nunca colocar valores em arquivos, comandos com histórico ou chat. A chave Render fica somente no processo local e não é enviada ao Google nem ao serviço Django.
6. Após consentimento explícito da conta, o script exige somente `drive.file` no retorno e envia as três credenciais SIRE diretamente aos campos de ambiente do serviço de ensaio via HTTPS. Não imprime tokens, códigos nem URL de autorização. Não lê os demais segredos; usa atualização individual de chaves. Em falha parcial, conferir quais chaves foram salvas e repetir o fluxo seguro. Não há rollback automático nem deploy solicitado pelo script.
7. A demonstração pública é recusada por nome, URL ou branch. Depois da revisão, testar fotos sintéticas, permissões, remoção e persistência após redeploy no ensaio. A promoção para a demo é uma etapa posterior; este script não a executa.

**Estado real em 17/11/2026:** o Console ficou indisponível antes do login nesta sessão. Nenhum projeto, consentimento, cliente OAuth ou segredo real foi criado/configurado. O fluxo acima foi preparado e testado com provedores simulados; não é evidência de autorização real.

**Importante:** O Google Drive não é um CDN de imagens e não tem as garantias ou ferramentas de distribuição de um serviço especializado. O proxy Django pode aumentar latência e tráfego no Render; isso deve ser tratado como limitação acadêmica do protótipo, não solução de produção escalável.

## Implementação / rastreabilidade

| Identificador | Artefatos de implementação | Aceite previsto |
| --- | --- | --- |
| CAT-RF-02 / UC06–UC07 | `sire/models.py`, `sire/forms.py`, `sire/templates/sire/excursao_form.html`, migração 0007 | Cadastrar/editar textos, manter opcionais, recusar agência alheia |
| CAT-RF-03 / UC06–UC07 | `FotoExcursao`, `sire/drive_fotos.py`, URLs/views de fotos, galeria | Foto válida adicionada; inválida ou excessiva recusada; remoção autorizada; foto persiste após deploy |
| CAT-RF-04 / UC05 | `detalhe_excursao.html`, `catalogo.html`, CSS | Ficha antiga continua navegável; rascunhos não aparecem; nova ficha mostra textos e fotos; reserva intacta |
| CAT-RNF-02 / UC09–UC13 | Views existentes de publicação e reserva mantidas | Agente publica, passageiro escolhe embarque e reserva, agente consulta; vagas decrementadas |

## Estado das evidências

**Implementado em código:** campos opcionais, modelo relacional de foto referenciada, adaptador Google Drive OAuth `drive.file`, form para envio, validação/otimização, remoção e exibição, templates e estilos. O código está isolado em `etapa/ficha-fotos-sire`.

**Ainda não comprovado:** credenciais reais da conta no Render, acesso da API/limites da conta, envio e remoção real de foto, persistência após novo deploy, migração aplicada na demo, verificação visual em celular, regressão funcional com CAT-VF-01–06, execução do fluxo de reserva no Render e validação dos testes do commit final. Não criar resultado “conforme” antes dessas evidências.

**Plano de verificação posterior:** executar `python manage.py check`, `python manage.py makemigrations --check --dry-run` e `python manage.py test` em banco isolado; conferir as entradas CAT-VF-02, CAT-VF-03, CAT-VF-04 e CAT-VF-06 em navegador; testar arquivo malformado, tipo inválido, 5MB+, limite de seis fotos, autorização entre agências, e imagem de rascunho. Verificar que os arquivos continuam no Drive depois de um segundo deploy da branch de ensaio. Registrar horário, commit, ambiente, IDs fictícios e prints.

## Evolução futura proposta

Substituir o adaptador de armazenamento Google Drive por **Cloudinary**, **Cloudflare R2** ou serviço equivalente após decisão de custos, privacidade e desempenho. Manter a camada de upload e exibição desacoplada do modelo de excursão, migrando os arquivos e as referências com ferramenta dedicada. Melhorias potenciais: thumbnails em tamanhos responsivos, cache/CDN, exclusão assíncrona segura, observabilidade, controle de quota, limpeza de fotos órfãs e ordenação da galeria. Essas possibilidades são backlog evolutivo, **não funcionalidades entregues**.

## Fontes técnicas

- Google Drive API — escopos de autenticação: https://developers.google.com/workspace/drive/api/guides/api-specific-auth
- Google Drive API — envio de arquivos: https://developers.google.com/workspace/drive/api/guides/manage-uploads
- Especificação complementar SIRE: https://docs.google.com/document/d/1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is/edit
