"""Código de recuperação de senha (extensão, fora da baseline ER-SIRE 2.1).

Cada conta tem um código que permite criar uma senha nova sem depender de
e-mail. O código NÃO é guardado no banco: é calculado a partir da chave secreta
do servidor, do identificador da conta e do hash da senha atual. Por isso:

- não há campo, tabela ou migration novos;
- quem lê o banco não encontra o código;
- ao trocar a senha, o código antigo deixa de valer e um novo é gerado.

Limite conhecido: se a chave secreta do servidor mudar, ou se uma atualização
do Django regravar o hash da senha, os códigos emitidos deixam de valer; a
pessoa obtém o código atual depois de entrar na conta.
"""

import base64
import hmac
import re

from django.utils.crypto import salted_hmac

# Contas compartilhadas da banca: a senha é definida pela autora na hospedagem
# e não pode ser trocada por quem as utiliza.
CONTAS_COMPARTILHADAS = {"demo_passageiro", "demo_agente"}

_SAL = "sire.recuperacao.codigo.v1"


def conta_compartilhada(usuario):
    return usuario.username.lower() in CONTAS_COMPARTILHADAS


def codigo_de(usuario):
    """Código atual da conta, no formato XXXXX-XXXXX-XXXXX-XXXXX (100 bits)."""
    resumo = salted_hmac(
        _SAL, f"{usuario.pk}:{usuario.password}", algorithm="sha256"
    ).digest()
    letras = base64.b32encode(resumo).decode("ascii")[:20]
    return "-".join(letras[i : i + 5] for i in range(0, 20, 5))


def normalizar(texto):
    """Aceita o código com ou sem hífens, espaços e em minúsculas."""
    return re.sub(r"[^A-Z2-7]", "", (texto or "").upper())


def confere(usuario, texto):
    """Compara em tempo constante o código informado com o código da conta."""
    return hmac.compare_digest(normalizar(codigo_de(usuario)), normalizar(texto))
