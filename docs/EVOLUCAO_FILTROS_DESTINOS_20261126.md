# Evolução dos filtros e destinos — proposta 26/11/2026

Referência de experiência: https://voudetrip.com.br/ e /destinos (estrutura de seleção, não identidade visual ou catálogo copiado). Incremento de UC03, UC04, UC06 e UC07, sem substituir ER-SIRE 2.1. Sem tabela ou migration nova.

- Seleção de destino em catálogo com vocabulário inicial próprio e destinos publicados legados; grafias reconhecidas são agrupadas sem reescrever o banco.
- Cadastro/edição: sugestões via datalist, padronização de grafias reconhecidas no servidor, destinos personalizados permitidos. Não exige exclusão dos dados fictícios anteriores.
- Busca livre por destino preserva contrato GET destino; nova palavra-chave consulta título, destino, descrição e roteiro. Filtros combináveis por período de saída inclusivo, tipo (bate e volta ou com hospedagem), embarque e ordenação por preço ou data.
- Embarques vêm somente de excursões publicadas. Por decisão da autora em 26/11/2026, não há filtro por duração.
- Não há campos estruturados de cidade/UF de origem ou categoria detalhada de hospedagem; não são inventados. Sem alterações em reserva, privacidade, fotos ou vídeos.
- Testes propostos: sire/tests/test_filtros_destinos.py. Verificar CI em SQLite e PostgreSQL e navegação móvel antes da publicação. Não representa teste executado nem alteração no site publicado.

Rastreabilidade adicional: CAT-RF-05 (destinos sugeridos e padronização) → UC06/UC07 → CAT-VF-07; CAT-RF-01 ampliado → UC03/UC04 → CAT-VF-01. Tutorial: destaque individual do seletor de destino para evitar sobreposição em telas estreitas. O primeiro CI geral e de fotos passou; o teste de navegador acusou sobreposição a 390 px, motivando esta correção. Novo resultado depende da reexecução.
