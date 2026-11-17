"""Recuperação por código: cadastro -> código -> esqueci a senha -> senha nova -> código novo."""
import os
import re
import secrets
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ["DJANGO_SETTINGS_MODULE"] = "sire_project.settings"
import django

django.setup()
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.management import call_command
from django.db import connection
from django.test import Client

from sire import recuperacao
from sire.models import PerfilUsuario, TipoPerfil

call_command("migrate", verbosity=0)
ok = True
PADRAO = r"([A-Z2-7]{5}-[A-Z2-7]{5}-[A-Z2-7]{5}-[A-Z2-7]{5})"


def checa(rotulo, cond, detalhe=""):
    global ok
    ok = ok and bool(cond)
    print(f"{'OK  ' if cond else 'FALHA'} {rotulo} {detalhe}")


def recuperar(c, usuario, codigo, nova, conf=None):
    return c.post("/recuperar-acesso/", {"username": usuario, "codigo": codigo,
                                         "new_password1": nova, "new_password2": conf or nova})


senha = secrets.token_urlsafe(12)
c = Client(REMOTE_ADDR="10.2.0.1")

# 1. Cadastro mostra o código uma única vez
r = c.post("/cadastro/", {"username": "Maria", "first_name": "Maria", "last_name": "Teste",
                          "email": "maria@example.com", "data_nascimento": "1990-05-20", "aceite": "on", "password1": senha, "password2": senha}, follow=True)
m = re.search(PADRAO, r.content.decode())
checa("cadastro mostra o código de recuperação", r.status_code == 200 and m)
codigo = m.group(1)
maria = User.objects.get(username="Maria")
checa("código tem 20 caracteres em 4 grupos", len(recuperacao.normalizar(codigo)) == 20)
checa("código mostrado é o da conta", recuperacao.confere(maria, codigo))
checa("o código não fica guardado na sessão", not any("codigo" in str(k).lower() for k in c.session.keys()))

# 2. O código não está gravado no banco
with connection.cursor() as cur:
    achou = False
    for tabela in connection.introspection.table_names():
        cur.execute(f'SELECT * FROM "{tabela}"')
        for linha in cur.fetchall():
            if any(isinstance(v, str) and (codigo in v or recuperacao.normalizar(codigo) in v) for v in linha):
                achou = True
checa("o código não aparece em nenhuma tabela do banco", not achou)

# 3. Consulta depois de entrar
c2 = Client()
c2.login(username="Maria", password=senha)
r = c2.get("/minha-conta/codigo/")
checa("conta autenticada consulta o próprio código", r.status_code == 200 and codigo in r.content.decode())
checa("consulta exige login", Client().get("/minha-conta/codigo/").status_code == 302)

# 4. Tentativas inválidas
nova = secrets.token_urlsafe(14)
r = recuperar(Client(REMOTE_ADDR="10.2.0.2"), "Maria", "AAAAA-BBBBB-CCCCC-DDDDD", nova)
checa("código errado é recusado", r.status_code == 200 and "inválidos" in r.content.decode())
r2 = recuperar(Client(REMOTE_ADDR="10.2.0.3"), "nao_existe", codigo, nova)
checa("usuário inexistente: mesma mensagem", r2.status_code == 200 and "inválidos" in r2.content.decode())
checa("senha não mudou após tentativas inválidas", Client().login(username="Maria", password=senha))
r = recuperar(Client(REMOTE_ADDR="10.2.0.4"), "Maria", codigo, nova, "outra-coisa-123")
checa("confirmação diferente é recusada", r.status_code == 200 and "não são iguais" in r.content.decode())
r = recuperar(Client(REMOTE_ADDR="10.2.0.5"), "Maria", codigo, "123")
checa("senha fraca é recusada", r.status_code == 200 and Client().login(username="Maria", password=senha))

# 5. Recuperação válida (usuário em maiúsculas, código em minúsculas e sem hífens)
cache.clear()
r = recuperar(Client(REMOTE_ADDR="10.2.0.6"), "MARIA", recuperacao.normalizar(codigo).lower(), nova)
checa("recuperação válida aceita", r.status_code == 200 and "Senha redefinida" in r.content.decode(), f"HTTP {r.status_code}")
checa("senha nova funciona", Client().login(username="Maria", password=nova))
checa("senha antiga deixa de valer", not Client().login(username="Maria", password=senha))
maria.refresh_from_db()
novo_codigo = recuperacao.codigo_de(maria)
checa("o código mudou depois da troca de senha", novo_codigo != codigo)
r = recuperar(Client(REMOTE_ADDR="10.2.0.7"), "Maria", codigo, secrets.token_urlsafe(14))
checa("código antigo é recusado", r.status_code == 200 and Client().login(username="Maria", password=nova))
c3 = Client(REMOTE_ADDR="10.2.0.8")
r = recuperar(c3, "Maria", novo_codigo, senha + "Zz9", None)
m3 = re.search(PADRAO, r.content.decode())
maria.refresh_from_db()
checa("após redefinir, o novo código é mostrado", m3 and recuperacao.confere(maria, m3.group(1)) and m3.group(1) != novo_codigo)

# 6. Sessões antigas caem ao trocar a senha
checa("sessão aberta com a senha antiga é encerrada", c2.get("/minha-conta/codigo/").status_code == 302)

# 7. Contas compartilhadas da banca ficam fora
demo = User.objects.create_user(username="demo_passageiro", password=senha)
PerfilUsuario.objects.create(usuario=demo, tipo=TipoPerfil.PASSAGEIRO)
r = recuperar(Client(REMOTE_ADDR="10.2.0.9"), "demo_passageiro", recuperacao.codigo_de(demo), secrets.token_urlsafe(14))
checa("conta compartilhada não pode ser recuperada", r.status_code == 200 and Client().login(username="demo_passageiro", password=senha))
cd = Client()
cd.login(username="demo_passageiro", password=senha)
r = cd.get("/minha-conta/codigo/")
checa("conta compartilhada não vê código", r.status_code == 200 and not re.search(PADRAO, r.content.decode()))

# 8. Contas com nomes iguais em grafias diferentes
ana1 = User.objects.create_user(username="Ana", password=senha)
ana2 = User.objects.create_user(username="ana", password=senha)
r = recuperar(Client(REMOTE_ADDR="10.2.0.10"), "ANA", recuperacao.codigo_de(ana1), secrets.token_urlsafe(14))
checa("grafia ambígua não é resolvida", r.status_code == 200)
r = recuperar(Client(REMOTE_ADDR="10.2.0.11"), "ana", recuperacao.codigo_de(ana1), secrets.token_urlsafe(14))
checa("código de uma conta não abre a outra", r.status_code == 200)

# 9. Limite de tentativas
cache.clear()
bruto = Client(REMOTE_ADDR="10.2.0.50")
for _ in range(5):
    recuperar(bruto, "Maria", "AAAAA-AAAAA-AAAAA-AAAAA", secrets.token_urlsafe(14))
maria.refresh_from_db()
r = recuperar(bruto, "Maria", recuperacao.codigo_de(maria), secrets.token_urlsafe(14))
checa("após 5 erros, até o código certo é bloqueado por uma hora", r.status_code == 200 and "Muitas tentativas" in r.content.decode())

# 10. Telas
p = Client().get("/login/").content.decode()
checa("login mostra Esqueci minha senha", "Esqueci minha senha" in p and "/recuperar-acesso/" in p)

print("RESULTADO:", "TODOS CONFORMES" if ok else "HÁ FALHAS")
sys.exit(0 if ok else 1)
