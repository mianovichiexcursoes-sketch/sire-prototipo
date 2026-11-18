# SIRE — Auditoria bibliográfica e editorial da monografia

**Data:** 18/11/2026. **Status:** revisão técnica documentada; não equivale a aceite acadêmico do IFSP nem substitui revisão da autora e orientador.

## 1. Identificação do documento conferido

- Monografia editável: https://docs.google.com/document/d/1SPpcP6bf2Whsq3cCwjYRRDGqV45jsANOofaifG4b6jg/edit
- PDF atualizado na pasta central do Drive: https://drive.google.com/file/d/1jeciw6ftt-ESq3d6NhZYIzcawjeirhH0/view
- Arquivo com **60 páginas A4** após revisão da comparação bibliográfica, sem página quase vazia antes da metodologia.
- A monografia documenta ER-SIRE 2.1 (14 casos de uso, seis entidades), a edição posterior do PostgreSQL/Render, a ficha com fotos e a orientação EVO-USO-01. A implementação de CPF, pagamentos e assentos **não** é resultado verificado.

## 2. Conferência externa de referências

Para evitar referência bibliográfica inexistente ou dados incorretos, conferiram-se as seguintes fontes nas páginas institucionais ou editoriais indicadas. Verificar DOI e metadados é uma etapa diferente de revisar criticamente o texto integral de cada trabalho.

| Fonte | Dado confirmado | URL da fonte |
| --- | --- | --- |
| Boehm (1988) | Computer, v. 21, n. 5; DOI 10.1109/2.59 | https://ieeexplore.ieee.org/abstract/document/59/authors |
| Amelia, Nurlaili e Aditiawan (2026) | bit-Tech, v. 8, n. 3; DOI 10.32877/bt.v8i3.3382 | https://jurnal.kdi.or.id/index.php/bt/article/view/3382 |
| Mahadu et al. (2026) | IJRASET; DOI 10.22214/ijraset.2026.77695 | https://www.ijraset.com/research-paper/tour-and-travels-booking-system |
| Milojković et al. (2024) | Review of Socio-Economic Perspectives; DOI 10.19275/RSEP171 | https://reviewsep.com/index.php/rsep/article/view/171 |
| Silva et al. (2023) | Applied Tourism; DOI 10.14210/at.v8i2.19641 | https://periodicos.univali.br/index.php/ijth/article/view/19641 |
| Himanshu, Singh e Singh (2025) | Traveltrek; DOI 10.1109/IC363308.2025.10956640 | https://web.eurekamag.com/research/095/935/095935090.php |
| Django Software Foundation (2026) | Documentação oficial de 6.1 confirma terminologia Model-Template-View | https://docs.djangoproject.com/en/6.1/faq/general/ |

**Mudanças efetivas na monografia:** referência Django trocada da FAQ versão 6.0 pela 6.1, compatível com `requirements.txt` (`Django==6.1.2`); criada referência da versão publicada `MIANOVICHI (2026d)` ao GitHub e acrescentada citação no registro do incremento; fonte histórica do ZIP `MIANOVICHI (2026c)` foi preservada como etapa de outubro, sem fingir que representa todas as alterações de novembro.

## 3. Fontes de elicitação — ressalva de validade

Foi localizado o arquivo original [Entrevista.pdf](https://drive.google.com/file/d/1Q9vlm61p12B7QgHnxgTkst3M9eumRc2G/view), com 14 perguntas e respostas relacionadas à rotina de excursões, sistemas em uso e prioridades operacionais. O arquivo **não identifica nominalmente o participante nem a data**. A seção 3.2.1.1 da monografia foi esclarecida para tratar o registro como **fonte contextual do domínio**, sem atribuir amostragem ou validação externa. Essa transparência permite que a autora e o orientador validem a procedência do material.

Também existe [levantamento estruturado da experiência profissional da autora](https://docs.google.com/document/d/1XS3I8YgAFQ0Paz9XI4yVUJihqTC8-dmaYt-s5hPvv9U/edit), com ressalva expressa de que não constitui pesquisa de opinião externa. Não converter esses documentos em entrevistas independentes fictícias.

## 4. Problema editorial efetivamente corrigido

A Tabela/Quadro 1 de trabalhos correlatos ocupava o final de uma página e deixava apenas uma linha de persistência na seguinte, produzindo uma folha quase vazia antes do Capítulo 3. Foram abreviados **apenas textos de células** mantendo categorias (foco, domínio, capacidade, engenharia, persistência) e as distinções entre os estudos; agora o quadro cabe na página 24 (numeração impressa), e a Metodologia começa na página 25. O documento passou de 61 para 60 folhas PDF. O sumário e a lista de ilustrações foram corrigidos em 50 entradas após a remoção da quebra ruim.

O quadro agora identifica `SQLite / PostgreSQL` no SIRE, correspondente à baseline e à demonstração posterior. A legenda explica a comparação como descritiva; resultados de usabilidade dos outros estudos **não** são reivindicados pelo SIRE.

## 5. Itens que exigem conferência humana

1. **Título oficial**, folha de aprovação e requisitos institucionais específicos do PFC do IFSP; não substituí-los por suposição.
2. Conferir autoria/data do arquivo de entrevista, sem atribuir informações ausentes do documento.
3. Conferir a disponibilidade do material didático de Dias (2021), fonte interna que não foi autenticada por catálogo público nesta revisão.
4. Validar se cada referência é acessível ao professor e se as fontes Google Drive têm permissão de leitura.
5. Confirmar todas as legendas de figuras, qualidade de imagens e detalhes ABNT com o orientador ou biblioteca do IFSP.
6. Incluir **apenas os testes realmente executados** pelo agente em navegador e seus prints, ainda não incorporados à monografia.
7. Confirmar o status real do armazenamento de fotos no serviço Render; o teste local OAuth de 13/13 não prova persistência após redeploy público.

## 6. Regra de entrega

O PDF e os modelos são **candidatos à revisão**, não arquivos enviados. Nenhum e-mail ao professor foi enviado por esta auditoria. A autora deverá ler e aprovar o conjunto antes de qualquer compartilhamento por e-mail.
