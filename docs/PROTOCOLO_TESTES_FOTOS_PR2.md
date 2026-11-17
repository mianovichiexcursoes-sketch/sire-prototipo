# SIRE — protocolo executável de regressão do incremento de fotos (PR #2)

**Criado em 17/11/2026. Estado: roteiro de testes, NÃO resultado de execução.** Base inspecionada: `etapa/ficha-fotos-sire`, `sire/views.py`, `sire/drive_fotos.py`, `sire/models.py`. Aplicável a CAT-RF-02/03/04, RN-03/04/05/11/14, UC05–07 e CAT-VF. Nenhum CPF, imagem de pessoa ou token real deve entrar nos testes.

## Preparação e isolamento

1. Criar banco de teste separado, usuários sintéticos: agente A/agência A, agente B/agência B, passageiro P e visitante anônimo. Criar excursão A em rascunho com seis `FotoExcursao` fictícias; excursão B com fotos e agência B; outra publicada com uma foto.
2. Mockar `drive_fotos.configurado`, `preparar_jpeg`, `enviar`, `excluir`, `baixar` no teste HTTP. Não chamar Drive real. Para integração real, executar em ambiente de ensaio separado após OAuth e registrar apenas IDs fictícios/redigidos.
3. Antes de afirmar aceite: executar `python manage.py check`, `python manage.py makemigrations --check --dry-run`, `python manage.py test` e registrar data, branch, commit, ambiente, contagem e saída completa sanitizada. Para concorrência usar PostgreSQL de teste: SQLite não reproduz de forma confiável a semântica de `select_for_update`.

## Casos de teste de segurança (a implementar/rodar)

| ID | Cenário / preparação | Resultado esperado | Evidência |
|---|---|---|---|
| FOTO-01 | Visitante acessa imagem de excursão PUBLICADA, Drive mockado | HTTP 200, `image/jpeg`, `nosniff`; política de cache revisada | Status e cabeçalhos |
| FOTO-02 | Visitante acessa imagem de RASCUNHO | HTTP 404 e `baixar` não chamado | Status, mock |
| FOTO-03 | Agente B acessa foto de rascunho da agência A | HTTP 404 | Status |
| FOTO-04 | Agente A acessa foto de seu rascunho | HTTP 200, `private, no-store` | Status/cabeçalhos |
| FOTO-05 | Foto publicada foi lida; excursão volta a rascunho; mesma URL acessada como visitante | HTTP 404; resposta anterior NÃO deve poder ser reutilizada por cache público após despublicação | Cabeçalhos antes/depois e teste navegador/proxy |
| FOTO-06 | Agente B tenta POST de adicionar/remover foto da agência A | Negado, nenhuma chamada de upload/exclusão, nenhuma referência alterada | Status, mocks e contagem |
| FOTO-07 | Agente A tenta adicionar sétima foto | Rejeição sem `enviar` | Contagem e mock |
| FOTO-08 | Duas requisições simultâneas partem de cinco fotos | **Exatamente uma** referência nova; total seis; arquivo excedente não permanece no Drive | Teste transacional PostgreSQL e mock |
| FOTO-09 | Arquivo vazio, texto renomeado JPG, 5 MB excedidos, pixels excedidos, formato não permitido | Erro de validação, sem upload | Casos parametrizados |
| FOTO-10 | PNG/WebP/JPEG válido, com EXIF, dimensões grandes | JPEG otimizado até 1600×1600 e 2 MB, sem EXIF pessoal | Inspeção do buffer |
| FOTO-11 | Falha `enviar` | Nenhuma referência criada; mensagem segura sem token | Mock e resposta |
| FOTO-12 | Upload remoto bem-sucedido, falha ao gravar referência, exclusão remota também falha | Incidente registrado para reconciliação; não declarar ausência de órfão | Mock, mecanismo de auditoria |
| FOTO-13 | Falha `excluir` na remoção | Referência permanece no banco | Mock e contagem |
| FOTO-14 | Exclusão remota bem-sucedida | Referência removida, cache interno invalidado | Mock e cache |
| FOTO-15 | Migração 0007 aplicada a registros antigos | Campos opcionais sem perda; fotos vazias; UC05/10/11 continuam funcionando | Migração em DB de ensaio |
| FOTO-16 | Sem OAuth configurado | Texto continua editável; upload indisponível sem vazamento de segredo | Status e mensagens |

## Achados de revisão estática — não equivalem a testes

- **A-01 (alto):** `imagem_excursao` devolve `Cache-Control: public, max-age=3600` para foto publicada. Após despublicação, cliente/proxy pode servir resposta antiga; o 404 no servidor não invalida cópia externa. Antes do aceite, mudar para `private, no-store` ou demonstrar estratégia de invalidação robusta. Referência: `sire/views.py`, função `imagem_excursao`.
- **A-02 (alto):** `adicionar_foto` consulta `excursao.fotos.count()` antes de `enviar` e `FotoExcursao.objects.create`, sem serialização. Concorrência pode gerar sete fotos. Implementar limite transacional robusto com tratamento de arquivos remotos e testar PostgreSQL.
- **A-03 (médio):** se `FotoExcursao.objects.create` falhar e `drive_fotos.excluir` também, a exceção de exclusão é silenciada. Projetar reconciliação segura e sem segredos.
- **A-04:** a API OAuth da conta do ChatGPT não prova autorização do aplicativo Django; teste real de persistência após deploy continua bloqueado.

## Política de merge e evidência

Não alterar PR #2 nesta branch documental, pois outro agente pode estar trabalhando nela. Os casos acima são **pendentes** até haver testes e logs reais. Não realizar merge/deploy enquanto FOTO-05, FOTO-08 e FOTO-12 não tiverem tratamento documentado e testes relevantes concluídos. A baseline ER-SIRE 2.1 e UC01–UC14 permanecem históricas.
