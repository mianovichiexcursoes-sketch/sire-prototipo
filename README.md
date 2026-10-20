# SIRE — Sistema de Reserva de Excursões

Protótipo acadêmico do PFC/TCC de Engenharia Elétrica do IFSP Câmpus Sertãozinho.
Baseline de requisitos: **ER-SIRE 2.1**. Implementação assistida por IA/Codex,
autorizada pela autora nesta sessão, com histórico incremental e mapa do código.
O uso de IA não deve ser apresentado como desenvolvimento sem assistência.

## Entrega

Os Blocos 1 a 9 estão implementados. Os 16 cenários VF foram exercitados por
requisições HTTP reais, com CSRF e sessões, no ambiente Work. O relato completo
está em [docs/VERIFICACAO.md](docs/VERIFICACAO.md). Não foi criada suíte de testes.
A conferência visual em navegador e a execução no Windows permanecem pendentes.

## Versões efetivamente utilizadas

| Componente | Referência dos documentos | Executado no Work |
| --- | --- | --- |
| Python | 3.14.8 | 3.12.14 |
| Django | 6.1.2 | 6.1.2 |
| SQLite | disponível no Python | 3.53.1 |
| asgiref | dependência do Django | 3.12.1 |
| sqlparse | dependência do Django | 0.6.0 |

A versão Python de referência não foi instalada nem verificada nesta entrega.
Nenhum comando foi executado no computador Windows da autora. VS Code é a IDE
prevista para abrir e estudar estes arquivos localmente.

## Executar no Windows

Extraia o ZIP e abra a pasta `sire-prototipo`, que contém `manage.py`, no VS Code.
No terminal PowerShell:

```powershell
py --version
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m django --version
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Se a ativação não estiver disponível, execute os comandos com
`.\.venv\Scripts\python.exe` no lugar de `python`, sem mudar a política do sistema.
No Linux/macOS, crie a venv com `python3 -m venv .venv` e ative com
`source .venv/bin/activate` antes dos mesmos comandos.

Acesse <http://127.0.0.1:8000/> e o pré-cadastro interno em
<http://127.0.0.1:8000/admin/>. Encerre o servidor com Ctrl+C.
O banco é reconstruído pelas quatro migrations do domínio e pelas migrations
internas do Django. Nenhum banco ou conta de desenvolvimento acompanha o ZIP.

## Preparar a demonstração

1. Entre no Admin com o superusuário criado localmente e cadastre uma Agência.
2. Em Usuários, crie a conta do agente, com uma senha escolhida localmente.
   O agente não precisa de privilégios de equipe ou superusuário.
3. Em Perfis de usuário, associe esse usuário ao tipo AGENTE e à agência criada.
4. Saia do Admin e entre pela página `/login/` usando a conta do agente.
5. Abra “Excursões da agência”, crie uma excursão e observe o estado RASCUNHO.
6. Cadastre um ponto de embarque e publique a excursão.
7. Saia, cadastre uma conta de passageiro, entre e consulte o catálogo.
8. Abra os detalhes, selecione um embarque e confirme a reserva de uma vaga.
9. Consulte “Minhas reservas”. Depois entre como agente e consulte Reservas e
   Passageiros. Para demonstrar isolamento, pré-cadastre uma segunda agência.

O superusuário do Admin não recebe perfil de agente automaticamente. Passageiros
são cadastrados na interface pública e ficam sem agência. Agentes e agências
possuem somente pré-cadastro interno. As senhas ficam sob o mecanismo de hash do
Django; a entrega não contém senhas de demonstração.

## Código e rastreabilidade

- `sire/models.py`: cinco models do domínio; `User` padrão é a sexta entidade.
- `sire/forms.py`: cadastro e validação de entradas.
- `sire/views.py`: funções do fluxo; login/logout usam as views do Django.
- `sire/urls.py`: rotas correspondentes aos 14 UC.
- `sire/templates/sire/`: telas com herança de `base.html`.
- `sire/static/sire/css/style.css`: apresentação sem framework front-end.
- [docs/RASTREABILIDADE.md](docs/RASTREABILIDADE.md): UC → função → tela → VF.
- [docs/ANDAMENTO.md](docs/ANDAMENTO.md): decisões, etapas e limites das evidências.

## Recuperar o histórico Git incluído no ZIP

O ZIP contém `historico-sire.bundle`, que preserva os commits desta execução.
Na pasta extraída, se ela ainda não tiver um repositório Git:

```bash
git init -b main
git fetch historico-sire.bundle main
git reset --mixed FETCH_HEAD
git log --oneline
git show <hash-do-commit>
git diff <hash-anterior> <hash-seguinte>
```

Os commits estão identificados como desenvolvimento assistido; não foram
atribuídos à autora como se fossem trabalho sem assistência. O primeiro preserva
o ZIP recebido. Não foram fabricados commits retroativos de desenvolvimento.
O arquivo `historico-commits.txt` permite consultar a sequência sem importar Git.

Não houve envio ao GitHub. A busca não identificou `sire-prototipo` da autora com
permissão de escrita. O repositório local usa `main`; um remoto poderá ser
associado quando sua URL estiver disponível. Torná-lo público exige autorização.

## Funcionalidades e limites

Implementados UC01–UC14: cadastro de passageiro, autenticação, catálogo,
pesquisa por destino, detalhes, cadastro/edição de excursões da agência,
embarques, publicação, reserva com seleção de embarque, Minhas reservas,
consulta de reservas e passageiros pelo agente.

Cada Reserva ocupa uma vaga. Não existe status de reserva, quantidade de
passageiros por reserva, campo de disponibilidade ou cancelamento. Não foi
acrescentada regra de unicidade passageiro/excursão ausente da baseline; cada
confirmação válida cria uma reserva enquanto houver capacidade.

A disponibilidade é `capacidade - reservas.count()`. A gravação de reserva e a
edição da capacidade usam `transaction.atomic()` com SQLite em modo IMMEDIATE:
o bloqueio de escrita é adquirido antes de consultar novamente a capacidade.
`select_for_update()` não foi usado como garantia, pois não bloqueia linhas no
SQLite. Há timeout de 10 segundos; em conflito na reserva, a interface orienta a
tentar novamente. Não houve ensaio de carga ou de concorrência nesta execução.
Esse mecanismo é destinado à demonstração local, com limitações de concorrência
do SQLite; não constitui arquitetura para operação comercial em larga escala.

Não implementados, conforme escopo: pagamento, cancelamento, assentos, veículos,
vouchers, hospedagem, rooming list, espera e notificações. Não há API separada,
React, Vue, microserviços ou JavaScript adicional.

O projeto usa DEBUG e chave pública de desenvolvimento local. Para uma futura
implantação, é necessário configurar ambiente, chave privada própria, hosts,
HTTPS e recursos estáticos; essa implantação não foi realizada.
