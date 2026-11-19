# Gate de fontes oficiais — EVO-USO-01 (19/11/2026, 10h55 BRT)

Unidade documental isolada baseada no HEAD da PR #37 (556de163). Não representa implementação, testes, aceite, merge ou deploy. Esta evidência registra leitura direta dos documentos nativos por ID; revisões são identificadores técnicos do Google Docs, não datas de aprovação.

| Fonte | ID | Revisão consultada |
|---|---|---|
| RN-01–RN-41 | 1REAmrici0i-JKgP8N78OlN4lVsLUs4blV8A0fE09kQ0 | AHj4eMQguVGb_4XDjpIILo1Ueu3oX74YzVU-Y3pjwZRW8SqamIbGe_xdMG_PkwTcvmpm8WSHhBiXi54l4ahoI6g3UbBVdUxMjmog4LuqsHs |
| ER-SIRE 2.1 / documentação | 19U5JhTHfk8IbvWfdAAUg8Z81fwQ8wsji6m4vxTN9Ed8 | AHj4eMTd3MUuANlRTlg4m2XrvinNmjWa66sdQEiaLKJL47kzrBUbkgePcfhFjs6KpbfGSkqaZv6vvBYgZYtY1nhoDY7XVUqytJwfIG8EkGs |
| Guia do protótipo | 1QzjUnoxF9MBukMQEexTuzK1O16czpMIParG5QgSab8U | AHj4eMQaNMjGn0nQytWmd1zCgC4eXduS5sJ-NYwLZOQtS5LvcMTDuZXWcdCg2KrDm02eDTrUv9zFLRxlOpMpmeAElRCdGivJKqIAUAmbgk4 |
| UC01–UC14 | 1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY | AHj4eMR9ieGd6kQkg8v57yrInG6V_mFxksUY7zZhppBjMPMHKLKqrFh-QgDIehKmhTKnOfxY13Rtx6xRB44A_q0U1uxqUr4Ji-CbBHxnT9Y |
| Requisitos v3 | 1RTgG9fDY71_8hsncRQKWNd2cQGwRTQfo72xLAitwBaM | AHj4eMTi8NviSAJ3x85wLTlG-5Oq8qM3pHYIzotUlXt5pUOO-KC2I8vyOz1-8LJLQigBx27FlqZzhcg2w3UdynaSzHMjImYxqEFHs1IAyxM |
| CAT | 1EKm59rEfdHFgK0Ze5EfxBc5AC1g4hwfx1UVogbXL7Is | AHj4eMTSU0RTheqYeHkWD0Zq9snLQEYLwb6Ruu9Yf36JmWk-Y5D51wnT7_ujOKJXqaajTFULu9V5n2AjYtEH8jXtqVN0I_jRAhwRX2BWrEs |
| Registro de implementação | 1g3MnJfhbMFsDE-x42HemvypzXbAOh0wi3GPK7rwMqaM | AHj4eMR_QOz9L1B-9E5roWp0mibyS37cGqh303DyLnFInxYRuajnk6JJyKMLIwShaLtDwLcvFz8klfgj_2rzYxFrf36gqDMRbfzsGga-U-8 |

## Restrições verificadas para o tutorial

- RN-01–05: Agente vinculado à agência; isolamento administrativo; dados do Passageiro apenas para autorizados; controles por perfil. O tutorial não deve exibir instruções administrativas ao Visitante/Passageiro.
- RN-06–14: publicação depende de campos mínimos; excursões em rascunho não entram no catálogo; finalizadas/canceladas não recebem novas reservas. O tutorial deve explicar esses estados sem executar publicação.
- UC01: cadastro de passageiro exige ação explícita de conclusão; desistência não cria conta. Tutorial não deve enviar formulário.
- Guia: AGENTE não possui cadastro público; é pré-cadastrado pelo Django Admin. Tutorial não deve sugerir cadastro público de agente.
- Baseline histórica ER-SIRE 2.1, seis entidades e UC01–UC14 permanecem inalteradas; tutorial é EVO-USO-01.

## Matriz inicial de rastreabilidade (a completar após inspeção do código)

| Requisito | Comportamento de tutorial | Código/migração | Teste | Evidência | Monografia |
|---|---|---|---|---|---|
| RN-03, RN-05, EVO-USO-01 | orientação por perfil sem revelar administração | Pendente de reconciliação das PRs #15/#20/#21/#33/#35; sem migração prevista | TUT-perfis pendente | Nenhum teste executado nesta unidade | Nova volta espiral, pendente |
| RN-06, RN-11, UC de excursão, EVO-USO-01 | explicar rascunho/publicação sem acioná-la | Pendente de reconciliação | TUT-sem-envio pendente | Nenhum teste executado | Resultados pendentes |
| UC01, EVO-USO-01 | explicar cadastro sem criar conta | Pendente de reconciliação | TUT-cadastro pendente | Nenhum teste executado | Limitações pendentes |

## Bloqueios e retomada

- **Integração real Drive/fotos — bloqueada:** falta evidência de OAuth `drive.file` do aplicativo Django, credenciais protegidas e teste em Render; responsável: autora/administrador do projeto; retomar somente após autorização segura verificável. Não bloqueia o tutorial.
- **Aceite do tutorial — pendente:** a cadeia de PRs #33/#35 requer conciliação, testes de navegador (320px e 375×812), foco/Escape, perfis, estados vazios e revisão humana. Responsável: desenvolvimento/testes e autora para aceite. Não mesclar nem publicar antes.
- **Auditoria final acadêmica — pendente:** leitura integral da monografia, modelo IFSP, regulamento e parecer ainda não concluída nesta unidade. Não declarar conformidade ABNT.

Próxima ação: conciliar as alterações reais de templates/CSS/JS das PRs de tutorial em branch isolada, executar TUT-01–09 e regressões com dados sintéticos, anexar resultados e atualizar checklist canônico. A PR #37 mantém o checklist atual; reconciliar sem sobrescrevê-lo.
