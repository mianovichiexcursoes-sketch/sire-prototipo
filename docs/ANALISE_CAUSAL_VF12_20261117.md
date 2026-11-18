# VF12 — análise causal documental (17/11/2026)

## Fontes primárias consultadas
- Registro de implementação, rastreabilidade e verificação SIRE, Google Doc ID `1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM`, seção 10.2 (VF12) e **10.3 Consolidação e preservação do histórico**. Fonte acessada diretamente nesta rodada.
- Pacote histórico de evidências `SIRE_evidencias_HTTP_2026-10-22.zip`, ID `1wLIkHrDzFXD9ZUTIR1JcsQwaA4ESb2RI`: a integridade e os nomes dos arquivos foram verificados em rodada anterior, **não** houve nova extração nesta rodada.
- Baseline ER-SIRE 2.1, guia de implementação, UC01–UC14, RN-01–41 e demais fontes oficiais consultadas diretamente nesta rodada. Nenhum documento original foi alterado.

## Achado causal explícito no documento primário
A seção 10.3 afirma que a primeira conferência VF12 foi classificada **não conforme** porque o verificador procurava a mensagem textual **“Escolha uma opção válida”**, mas o Django retornou **“Faça uma escolha válida. Sua escolha não é uma das disponíveis.”**. A quantidade de reservas não se alterou. A repetição dirigida com vagas disponíveis confirmou a rejeição do ponto de embarque alheio e preservou os IDs das reservas `[3, 2, 1]`.

**Classificação documental:** divergência na expectativa textual do verificador, **não defeito funcional comprovado do protótipo**. A própria seção 10.3 declara que não houve correção de código, modelo, migration ou README nem commit de implementação decorrente do VF12. Portanto, **não procurar ou inventar um commit de correção inexistente**. A primeira evidência não conforme deve permanecer preservada.

## Limites e rastreabilidade
- UC10/UC11, RF016–RF017: o requisito funcional verificado foi a rejeição de ponto de outra excursão, sem persistência indevida.
- VF12 inicial: não conforme quanto ao texto esperado pelo verificador; VF12 final: conforme quanto ao comportamento HTTP/ORM em SQLite, 22/10/2026.
- A análise causal aqui deriva da declaração explícita no documento primário. A comparação campo a campo dos dois JSON individuais permanece **pendente**; não foi reexecutado o cenário.
- Este resultado **não** atesta a versão atual, PostgreSQL, navegador, Drive real ou deploy.

## Próxima ação
Abrir os dois JSON individuais dentro do ZIP e comparar seus campos, timestamps e critérios; registrar diferenças sem dados pessoais. Depois executar regressão VF12 e CAT-VF em ambiente isolado, após reconciliar os HEADs das branches em edição concorrente. Não mesclar ou publicar a demo por causa desta análise.
