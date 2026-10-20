# SIRE — Sistema de Reserva de Excursões

Protótipo acadêmico do PFC/TCC de Engenharia Elétrica do IFSP Câmpus Sertãozinho.
Engenharia de Requisitos: baseline **ER-SIRE 2.1**.

## Estado do código

**Bloco 1 — estrutura inicial do Django.** Este pacote **não** contém ainda o fluxo
funcional de cadastro, autenticação, gestão de excursões ou reservas. Esses
recursos serão desenvolvidos nos Blocos 2 a 9, conforme o guia de implementação.

## Tecnologias previstas

- Python: referência **3.14.8** (conferir versão real instalada antes de registrar no TCC);
- Django: **6.1.2**, registrado em `requirements.txt`;
- SQLite: versão incluída no ambiente Python do computador;
- Django Templates, HTML e CSS;
- Django ORM e migrations para a criação do banco;
- Git e GitHub para controle de versão.

**Atenção:** O código foi preparado a partir do planejamento consolidado. Na máquina
que gerou os arquivos, o Django não estava instalado. É preciso validar a execução
localmente antes de declarar o Bloco 1 concluído de forma funcional.

## 1. Preparar e executar no Windows

Abra a pasta **sire-prototipo** no Visual Studio Code. No menu **Terminal → Novo Terminal**,
certifique-se de estar na pasta que contém `manage.py`.

Confira o Python instalado:

```powershell
py --version
```

Crie um ambiente virtual:

```powershell
py -m venv .venv
```

Se estiver usando **PowerShell**, ative com:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se estiver usando **Prompt de Comando (cmd)**, use em vez disso:

```bat
.venv\Scripts\activate.bat
```

Instale a dependência definida no projeto:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m django --version
```

## 2. Preparar o banco SQLite

Execute na mesma pasta, com o ambiente virtual ativado:

```powershell
python manage.py check
python manage.py makemigrations
python manage.py migrate
```

No Bloco 1, `makemigrations` deve indicar que **não há mudanças** para a app `sire`.
O `migrate` aplica somente as migrations internas do Django (autenticação, sessões,
admin etc.), necessárias para preparar o banco SQLite.

Crie um superusuário de demonstração para o Django Admin interno:

```powershell
python manage.py createsuperuser
```

Inicie o servidor local:

```powershell
python manage.py runserver
```

Abra no navegador:

- http://127.0.0.1:8000/ — página inicial provisória;
- http://127.0.0.1:8000/admin/ — área administrativa interna.

Para encerrar o servidor, pressione **Ctrl+C** no terminal.

## 3. Registrar o Bloco 1 com Git

Se ainda não existe repositório local, execute:

```powershell
git init
git add .
git commit -m "Estrutura inicial do projeto Django"
git branch -M main
```

**Não há repositório GitHub criado por este pacote.** A conexão ao GitHub será
realizada somente depois de decidir nome e visibilidade do repositório.

## Estrutura principal

```text
sire-prototipo/
  manage.py
  requirements.txt
  .gitignore
  README.md
  sire_project/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
  sire/
    __init__.py
    admin.py
    apps.py
    forms.py
    models.py
    urls.py
    views.py
    migrations/
      __init__.py
    templates/sire/
      base.html
      catalogo.html
    static/sire/css/
      style.css
```

## O que será implementado nos próximos blocos

- Agência e PerfilUsuario, com relação ao `django.contrib.auth.models.User`;
- cadastro e autenticação de Passageiro; pré-cadastro de Agente via Admin;
- Excursão, PontoEmbarque, Reserva e regras de acesso;
- catálogo, pesquisa, detalhes, reservas e consultas.

Não fazem parte do protótipo: pagamentos, cancelamentos, veículos, assentos,
vouchers, hospedagem, notificações, lista de espera ou funcionalidades comerciais adicionais.

> Atenção: `settings.py` usa uma `SECRET_KEY` de desenvolvimento e `DEBUG=True`.
> Não publicar esta configuração em um servidor de produção.
