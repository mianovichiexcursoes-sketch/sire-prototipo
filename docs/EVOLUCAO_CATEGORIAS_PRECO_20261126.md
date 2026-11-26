# Evolução proposta — categorias, preço e catálogo compacto

26/11/2026. Inspiração de interação: https://voudetrip.com.br/viagens-para/monte-verde (categorias e seção institucional); https://www.airbnb.com.br/help/article/479 (faixa de preço). Não se reproduzem identidade visual, avaliações ou garantias comerciais de terceiros.

- CAT-RF-01: seleção de categoria e limites de preço por pessoa, independentes e inclusivos; validação de valores não negativos e mínimo <= máximo. Combinação com filtros existentes, somente excursões publicadas. Três grupos principais: destino, período de saída (data inicial e final) e tipo de pacote. Categoria e demais critérios em painel nativo recolhível com controles numéricos e deslizador auxiliar de teto.
- CAT-RF-06: categoria principal opcional definida pelo agente em UC06/UC07, exibida no UC03/UC05. Migration 0008 acrescenta um campo, sem nova tabela ou alteração da referência histórica ER-SIRE 2.1. Não se inventam categorias para registros anteriores.
- Seção institucional Por que o SIRE? apresenta funcionalidades existentes e natureza acadêmica, sem alterar UC01–UC14.
- Testes adicionais em test_filtros_destinos.py e script de navegador. Resultado depende da CI. Não modifica o PDF já preparado para entrega nem vídeos, que pertencem à versão anterior.
