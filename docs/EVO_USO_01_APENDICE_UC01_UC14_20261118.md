# EVO-USO-01 — Apêndice documental dos casos de uso UC01–UC14

**Preparado em 18/11/2026. Estado: transcrição documental para revisão, NÃO inserida na monografia e NÃO homologada pelo orientador.**

## Fonte e preservação histórica
Fonte primária: [Especificação de Casos de Uso — SIRE](https://docs.google.com/document/d/1h5T8l9PPBGralJYaTqjG0K-czRBrGok6tzWRCHenWOY/edit), consultada diretamente nesta rodada. O texto abaixo conserva os identificadores e os fluxos da fonte histórica. A baseline ER-SIRE 2.1, suas seis entidades e os UC01–UC14 não são renumerados. Incrementos CAT/CPF/EVO-USO-01 são documentados separadamente. Este arquivo é um anexo de trabalho para posterior integração acadêmica, sem alegar que os cenários foram testados.

## Sumário
UC01 Cadastrar passageiro · UC02 Autenticar usuário · UC03 Consultar catálogo de excursões · UC04 Pesquisar excursões · UC05 Consultar detalhes da excursão · UC06 Cadastrar excursão · UC07 Editar excursão · UC08 Cadastrar ponto de embarque · UC09 Publicar excursão · UC10 Realizar reserva · UC11 Selecionar ponto de embarque · UC12 Consultar minhas reservas · UC13 Consultar reservas da excursão · UC14 Consultar passageiros da excursão.

## Texto-fonte preservado para revisão e inserção

> **Nota editorial:** transcrição do documento próprio da autora, não uma nova especificação. A numeração interna e os cabeçalhos são preservados; corrigir apenas em revisão controlada da monografia.

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DE SÃO PAULO – CÂMPUS SERTÃOZINHO
BACHARELADO EM ENGENHARIA ELÉTRICA


JULIA MIANOVICHI


ESPECIFICAÇÃO DE CASOS DE USO – SIRE
SISTEMA DE RESERVA DE EXCURSÕES


SERTÃOZINHO - SP
2026


1 OBJETIVO E ORGANIZAÇÃO DO DOCUMENTO
Este documento técnico complementar reúne as especificações textuais dos casos de uso pertencentes ao escopo do protótipo do Sistema de Reserva de Excursões (SIRE). O conteúdo é derivado da baseline ER-SIRE 2.1 e mantém rastreabilidade com os requisitos funcionais, requisitos não funcionais e regras de negócio consolidados na Documentação de Desenvolvimento de Software – SIRE.


A estrutura adotada para cada caso de uso compreende: descrição, atores, pré-condições, pós-condições, fluxo principal, fluxos alternativos e fluxos de exceção, conforme o modelo trabalhado na disciplina de Engenharia de Software.


2 ATORES CONSIDERADOS
Visitante – pessoa não autenticada que pode consultar excursões públicas e cadastrar-se como passageiro.
Passageiro – usuário cadastrado que especializa Visitante e pode autenticar-se, realizar reservas e consultar suas próprias reservas.
Agente – usuário previamente cadastrado e vinculado a uma agência, responsável por cadastrar, editar e publicar excursões e consultar reservas e passageiros de sua agência.


3 ESPECIFICAÇÕES DOS CASOS DE USO
UC01 – Cadastrar passageiro
Descrição: permitir que um Visitante registre uma conta de passageiro para utilizar as funcionalidades privadas do SIRE.
Atores: Visitante.
Pré-condições: o Visitante acessa a funcionalidade de cadastro de passageiro.
Pós-condições: uma conta de usuário é registrada com perfil PASSAGEIRO e fica disponível para autenticação posterior.
5.1 Fluxo Principal
1. O Visitante acessa a opção de cadastro de passageiro.
2. O sistema apresenta os campos obrigatórios para criação da conta.
3. O Visitante informa os dados solicitados.
4. O Visitante solicita a conclusão do cadastro.
5. O sistema valida as informações obrigatórias.
6. O sistema registra a conta de usuário e associa o perfil PASSAGEIRO.
7. O sistema informa que o cadastro foi concluído com sucesso.
5.2 Fluxos Alternativos
A1. O Visitante desiste do cadastro antes da confirmação; o sistema não cria a conta.
5.3 Fluxos de Exceção
E1. Uma ou mais informações obrigatórias estão ausentes ou inválidas; o sistema informa a inconsistência e não conclui o cadastro.
E2. O identificador de acesso informado já está em uso; o sistema informa a impossibilidade de concluir o cadastro com aquele identificador.
Rastreabilidade: RF001; RF003; RNF003; RNF006.


UC02 – Autenticar usuário
Descrição: permitir a autenticação de Passageiro ou Agente por meio de credenciais válidas, identificando o perfil associado ao acesso.
Atores: Passageiro; Agente.
Pré-condições: o usuário possui conta previamente cadastrada.
Pós-condições: uma sessão autenticada é iniciada e as funcionalidades autorizadas para o perfil do usuário podem ser acessadas.
5.1 Fluxo Principal
1. O usuário acessa a opção de autenticação.
2. O sistema solicita as credenciais de acesso.
3. O usuário informa suas credenciais.
4. O sistema verifica a validade das credenciais.
5. O sistema identifica o perfil associado ao usuário.
6. O sistema inicia a sessão autenticada.
7. O sistema disponibiliza as funcionalidades compatíveis com o perfil identificado.
5.2 Fluxos Alternativos
A1. Não há fluxo alternativo obrigatório específico para a autenticação.
5.3 Fluxos de Exceção
E1. As credenciais informadas são inválidas; o sistema rejeita a autenticação e apresenta mensagem compreensível.
E2. O usuário tenta acessar uma funcionalidade incompatível com seu perfil; o sistema impede o acesso.
Rastreabilidade: RF002; RF003; RNF001; RNF006.


UC03 – Consultar catálogo de excursões
Descrição: disponibilizar ao Visitante as excursões publicadas por diferentes agências em um catálogo comum.
Atores: Visitante, incluindo Passageiro por especialização.
Pré-condições: nenhuma autenticação é obrigatória.
Pós-condições: as excursões com estado PUBLICADA são apresentadas ao ator.
5.1 Fluxo Principal
1. O ator acessa o catálogo de excursões.
2. O sistema recupera as excursões com estado PUBLICADA.
3. O sistema apresenta as excursões disponíveis no catálogo.
4. O ator pode selecionar uma excursão para consultar seus detalhes.
5.2 Fluxos Alternativos
A1. Não existem excursões publicadas; o sistema informa que não há excursões disponíveis.
5.3 Fluxos de Exceção
E1. O sistema não consegue recuperar os dados do catálogo; apresenta mensagem de indisponibilidade sem exibir informações inconsistentes.
Rastreabilidade: RF011; RF012; RN005.


UC04 – Pesquisar excursões
Descrição: permitir a pesquisa das excursões publicadas utilizando, no mínimo, o destino como critério de consulta.
Atores: Visitante, incluindo Passageiro por especialização.
Pré-condições: o catálogo público está acessível.
Pós-condições: o sistema apresenta as excursões publicadas compatíveis com o critério informado.
5.1 Fluxo Principal
1. O ator acessa a funcionalidade de pesquisa.
2. O ator informa o destino desejado.
3. O sistema pesquisa entre as excursões publicadas.
4. O sistema apresenta os resultados compatíveis.
5. O ator pode selecionar um resultado para consultar seus detalhes.
5.2 Fluxos Alternativos
A1. Nenhuma excursão publicada corresponde ao destino informado; o sistema apresenta resultado vazio e mensagem apropriada.
A2. O ator não informa um destino; o sistema mantém ou reapresenta o catálogo de excursões publicadas.
5.3 Fluxos de Exceção
E1. O sistema não consegue executar a consulta aos dados; apresenta mensagem de indisponibilidade.
Rastreabilidade: RF013.


UC05 – Consultar detalhes da excursão
Descrição: permitir a consulta das principais informações de uma excursão publicada antes da realização de uma reserva.
Atores: Visitante, incluindo Passageiro por especialização.
Pré-condições: a excursão selecionada está disponível para consulta pública.
Pós-condições: o sistema apresenta destino, datas, valor, agência responsável, pontos de embarque e disponibilidade calculada da excursão.
5.1 Fluxo Principal
1. O ator seleciona uma excursão apresentada no catálogo ou nos resultados da pesquisa.
2. O sistema identifica a excursão selecionada.
3. O sistema recupera suas informações e os pontos de embarque associados.
4. O sistema calcula a disponibilidade com base na capacidade e nas reservas que ocupam vaga.
5. O sistema apresenta os detalhes da excursão.
5.2 Fluxos Alternativos
A1. A disponibilidade calculada é igual a zero; o sistema apresenta os detalhes e informa que não há vagas disponíveis, impedindo o início de uma nova reserva.
5.3 Fluxos de Exceção
E1. A excursão não está mais publicada ou não pode ser localizada; o sistema informa que o conteúdo não está disponível.
Rastreabilidade: RF015; RF023; RN005; RN009; RN011; RN012.


UC06 – Cadastrar excursão
Descrição: permitir que um Agente cadastre uma nova excursão vinculada à agência à qual está associado.
Atores: Agente.
Pré-condições: o Agente está autenticado, possui perfil AGENTE e está vinculado a uma agência.
Pós-condições: a excursão é persistida, vinculada à agência do Agente e registrada inicialmente com estado RASCUNHO.
5.1 Fluxo Principal
1. O Agente acessa a opção de cadastro de excursão.
2. O sistema apresenta os campos necessários ao cadastro.
3. O Agente informa os dados obrigatórios da excursão.
4. O Agente solicita a gravação.
5. O sistema valida as informações fornecidas.
6. O sistema vincula a excursão à agência do Agente.
7. O sistema registra a excursão com estado RASCUNHO.
8. O sistema informa que o cadastro foi concluído.
5.2 Fluxos Alternativos
A1. O Agente interrompe o cadastro antes da gravação; o sistema não cria a excursão.
5.3 Fluxos de Exceção
E1. Faltam informações obrigatórias ou algum valor informado é inválido; o sistema não grava a excursão e informa a inconsistência.
E2. O usuário não possui perfil AGENTE ou não está vinculado a uma agência; o sistema impede o cadastro.
Rastreabilidade: RF004; RF005; RF010; RN001; RN002; RN004; RN009.


UC07 – Editar excursão
Descrição: permitir que um Agente altere as informações de uma excursão pertencente à sua agência.
Atores: Agente.
Pré-condições: o Agente está autenticado e a excursão selecionada pertence à agência à qual está vinculado.
Pós-condições: as alterações válidas são persistidas na excursão selecionada.
5.1 Fluxo Principal
1. O Agente acessa as excursões de sua agência.
2. O Agente seleciona uma excursão.
3. O sistema apresenta as informações atuais da excursão.
4. O Agente altera as informações desejadas.
5. O Agente solicita a gravação.
6. O sistema valida as informações alteradas.
7. O sistema persiste as alterações.
8. O sistema informa que a edição foi concluída.
5.2 Fluxos Alternativos
A1. O Agente decide não salvar as alterações; o sistema mantém os dados anteriores.
5.3 Fluxos de Exceção
E1. A excursão não pertence à agência do Agente; o sistema impede a operação.
E2. As alterações deixam informações obrigatórias ausentes ou inválidas; o sistema não grava os novos dados.
E3. A capacidade informada é menor que a quantidade de reservas que já ocupam vagas; o sistema impede a alteração para preservar o limite de capacidade.
Rastreabilidade: RF006; RF003; RN003; RN011; RNF004.


UC08 – Cadastrar ponto de embarque
Descrição: permitir que um Agente cadastre um ou mais pontos de embarque associados a uma excursão de sua agência.
Atores: Agente.
Pré-condições: o Agente está autenticado e a excursão selecionada pertence à sua agência.
Pós-condições: um novo ponto de embarque, contendo local e horário, fica associado à excursão.
5.1 Fluxo Principal
1. O Agente acessa uma excursão de sua agência.
2. O Agente seleciona a opção de cadastrar ponto de embarque.
3. O sistema solicita local e horário.
4. O Agente informa os dados.
5. O Agente solicita a gravação.
6. O sistema valida as informações.
7. O sistema associa o ponto de embarque à excursão.
8. O sistema informa que o ponto foi cadastrado.
5.2 Fluxos Alternativos
A1. Após cadastrar um ponto, o Agente repete o fluxo para adicionar outro ponto de embarque à mesma excursão.
5.3 Fluxos de Exceção
E1. Local ou horário obrigatório não é informado; o sistema não registra o ponto.
E2. A excursão não pertence à agência do Agente; o sistema impede a operação.
Rastreabilidade: RF007; RN003; RN008.


UC09 – Publicar excursão
Descrição: permitir que o Agente disponibilize no catálogo uma excursão em estado RASCUNHO que possua as informações mínimas necessárias ao fluxo do protótipo.
Atores: Agente.
Pré-condições: o Agente está autenticado; a excursão pertence à sua agência; a excursão está em estado RASCUNHO.
Pós-condições: a excursão assume o estado PUBLICADA e passa a ser disponibilizada no catálogo público.
5.1 Fluxo Principal
1. O Agente acessa uma excursão em estado RASCUNHO.
2. O Agente solicita a publicação.
3. O sistema verifica se as informações obrigatórias da excursão estão preenchidas.
4. O sistema verifica se a capacidade está definida.
5. O sistema verifica se existe pelo menos um ponto de embarque associado.
6. O sistema altera o estado da excursão para PUBLICADA.
7. O sistema confirma a publicação.
8. A excursão passa a ser exibida no catálogo público.
5.2 Fluxos Alternativos
A1. Não há fluxo alternativo de sucesso: a publicação somente ocorre quando todas as condições obrigatórias são atendidas.
5.3 Fluxos de Exceção
E1. Faltam informações obrigatórias; o sistema mantém o estado RASCUNHO e informa a pendência.
E2. Não existe ponto de embarque cadastrado; o sistema impede a publicação e informa a necessidade de cadastrar ao menos um ponto.
E3. A excursão não pertence à agência do Agente; o sistema impede a publicação.
Rastreabilidade: RF007; RF010; RF011; RN003; RN005; RN006; RN009.


UC10 – Realizar reserva
Descrição: permitir que um Passageiro autenticado registre uma reserva em uma excursão publicada com disponibilidade, associando-a a um ponto de embarque válido.
Atores: Passageiro.
Pré-condições: o Passageiro está autenticado; a excursão está PUBLICADA; existe pelo menos um ponto de embarque associado; há disponibilidade maior que zero.
Pós-condições: uma Reserva é persistida e associada ao Passageiro, à Excursão e ao Ponto de Embarque selecionado; a reserva passa a ocupar uma vaga.
5.1 Fluxo Principal
1. O Passageiro acessa os detalhes de uma excursão publicada.
2. O Passageiro solicita a realização da reserva.
3. O sistema calcula e verifica a disponibilidade da excursão.
4. O sistema executa o UC11 – Selecionar ponto de embarque.
5. O Passageiro confirma a intenção de reservar.
6. O sistema recalcula a disponibilidade antes de concluir a operação.
7. O sistema valida se o ponto de embarque selecionado pertence à excursão.
8. O sistema cria a reserva associando Passageiro, Excursão e Ponto de Embarque.
9. O sistema considera a nova reserva no cálculo da disponibilidade.
10. O sistema informa que a reserva foi realizada com sucesso.
5.2 Fluxos Alternativos
A1. O Passageiro desiste antes da confirmação; nenhuma reserva é criada.
5.3 Fluxos de Exceção
E1. A disponibilidade é igual a zero no momento da confirmação; o sistema não cria a reserva e informa a indisponibilidade.
E2. A excursão não está mais em estado PUBLICADA; o sistema não conclui a reserva.
E3. O ponto de embarque selecionado não pertence à excursão; o sistema rejeita a operação.
Rastreabilidade: RF016; RF017; RF023; RN007; RN008; RN010; RN011; RN012; RNF003; RNF004; RNF006.


UC11 – Selecionar ponto de embarque
Descrição: permitir que o Passageiro escolha, durante a realização da reserva, um ponto de embarque pertencente à excursão selecionada.
Atores: Passageiro.
Pré-condições: o UC10 – Realizar reserva está em execução e a excursão possui pelo menos um ponto de embarque cadastrado.
Pós-condições: um ponto de embarque válido fica selecionado para utilização no fluxo da reserva.
5.1 Fluxo Principal
1. O sistema apresenta os pontos de embarque vinculados à excursão.
2. O Passageiro seleciona um dos pontos apresentados.
3. O sistema valida que o ponto selecionado pertence à excursão.
4. O sistema mantém a seleção para continuidade do UC10 – Realizar reserva.
5.2 Fluxos Alternativos
A1. A excursão possui apenas um ponto de embarque; o sistema apresenta esse ponto como única opção disponível.
5.3 Fluxos de Exceção
E1. Nenhum ponto de embarque está disponível para a excursão; o sistema impede o prosseguimento da reserva.
E2. O ponto selecionado não pertence à excursão; o sistema rejeita a seleção.
Rastreabilidade: RF017; RN008.


UC12 – Consultar minhas reservas
Descrição: permitir que o Passageiro autenticado consulte somente as reservas às quais esteja associado.
Atores: Passageiro.
Pré-condições: o Passageiro está autenticado.
Pós-condições: o sistema apresenta as reservas associadas ao Passageiro autenticado, sem expor reservas de outros usuários.
5.1 Fluxo Principal
1. O Passageiro acessa a área de suas reservas.
2. O sistema identifica o usuário autenticado.
3. O sistema recupera somente as reservas associadas a esse Passageiro.
4. O sistema apresenta as reservas encontradas e suas informações disponíveis.
5.2 Fluxos Alternativos
A1. O Passageiro não possui reservas; o sistema informa que não existem reservas associadas ao usuário.
5.3 Fluxos de Exceção
E1. O usuário não está autenticado; o sistema impede o acesso à área privada.
Rastreabilidade: RF019; RN013; RNF001; RNF002.


UC13 – Consultar reservas da excursão
Descrição: permitir que o Agente consulte as reservas relacionadas a uma excursão pertencente à sua agência.
Atores: Agente.
Pré-condições: o Agente está autenticado, possui perfil AGENTE e a excursão selecionada pertence à sua agência.
Pós-condições: o sistema apresenta as reservas associadas à excursão selecionada dentro das permissões do Agente.
5.1 Fluxo Principal
1. O Agente acessa as excursões de sua agência.
2. O Agente seleciona uma excursão.
3. O Agente solicita a consulta das reservas.
4. O sistema verifica se a excursão pertence à agência do Agente.
5. O sistema recupera as reservas da excursão.
6. O sistema apresenta as reservas encontradas.
5.2 Fluxos Alternativos
A1. A excursão ainda não possui reservas; o sistema apresenta a consulta sem registros.
5.3 Fluxos de Exceção
E1. A excursão não pertence à agência do Agente; o sistema impede a consulta.
E2. O usuário não possui perfil AGENTE ou não está autenticado; o sistema impede o acesso.
Rastreabilidade: RF020; RN003; RN014; RNF001; RNF002.


UC14 – Consultar passageiros da excursão
Descrição: permitir que o Agente consulte os passageiros associados às reservas de uma excursão pertencente à sua agência.
Atores: Agente.
Pré-condições: o Agente está autenticado, possui perfil AGENTE e a excursão selecionada pertence à sua agência.
Pós-condições: o sistema apresenta somente os passageiros vinculados às reservas da excursão selecionada, respeitando as restrições de acesso aos dados pessoais.
5.1 Fluxo Principal
1. O Agente acessa uma excursão de sua agência.
2. O Agente solicita a consulta dos passageiros.
3. O sistema verifica se a excursão pertence à agência do Agente.
4. O sistema recupera as reservas da excursão.
5. O sistema identifica os passageiros associados às reservas recuperadas.
6. O sistema apresenta a relação de passageiros autorizada para a operação.
5.2 Fluxos Alternativos
A1. A excursão não possui reservas; o sistema apresenta a consulta sem passageiros associados.
5.3 Fluxos de Exceção
E1. A excursão não pertence à agência do Agente; o sistema impede a consulta.
E2. O usuário não possui perfil AGENTE ou não está autenticado; o sistema impede o acesso.
Rastreabilidade: RF021; RN003; RN014; RNF001; RNF002.


4 RASTREABILIDADE
A rastreabilidade detalhada entre os casos de uso, requisitos, regras de negócio, classes, tabelas e cenários de verificação está registrada na Documentação de Desenvolvimento de Software – SIRE e no Registro de Implementação, Rastreabilidade e Verificação – SIRE.


A indicação de rastreabilidade ao final de cada caso de uso relaciona o comportamento especificado aos requisitos funcionais, requisitos não funcionais e regras de negócio que o fundamentam. A matriz do documento principal foi complementada pela rastreabilidade entre casos de uso, classes, tabelas, funcionalidades implementadas e cenários de verificação no registro técnico da implementação.


5 REFERÊNCIAS
MIANOVICHI, Julia. Documentação de Desenvolvimento de Software – SIRE: Sistema de Reserva de Excursões. Sertãozinho, 2026.
SOMMERVILLE, Ian. Engenharia de software. 9. ed. São Paulo: Pearson Prentice Hall, 2011.

## Pendências para aceitação acadêmica
- Comparar esta transcrição à versão vigente da especificação original antes da inserção.
- Integrar como apêndice na monografia após conciliar edições paralelas; atualizar sumário, paginação, legendas e rastreabilidade.
- Distinguir claramente os incrementos CAT, CPF e tutorial da baseline; validar com orientador.
- Não interpretar descrição de fluxo como teste executado ou funcionalidade implantada.
