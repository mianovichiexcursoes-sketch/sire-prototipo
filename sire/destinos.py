"""Vocabulário inicial de destinos para a evolução do catálogo.

O modelo permanece textual: destinos legados e personalizados são preservados.
"""
import re
import unicodedata

DESTINOS = (
    "Angra dos Reis - RJ", "Aparecida - SP", "Arraial do Cabo - RJ",
    "Balneário Camboriú - SC", "Bertioga - SP", "Beto Carrero World - SC",
    "Bonito - MS", "Brotas - SP", "Cabo Frio - RJ", "Caldas Novas - GO",
    "Campos do Jordão - SP", "Capitólio - MG", "Carrancas - MG",
    "Curitiba - PR", "Florianópolis - SC", "Foz do Iguaçu - PR",
    "Guarujá - SP", "Holambra - SP", "Hopi Hari - SP",
    "Ilha Grande - RJ", "Ilhabela - SP", "Monte Verde - MG",
    "Olímpia - SP", "Ouro Preto - MG", "Paraty - RJ", "Penedo - RJ",
    "Petrópolis - RJ", "Porto Seguro - BA", "Rio de Janeiro - RJ",
    "Santos - SP", "São Paulo - SP", "São Roque - SP",
    "São Thomé das Letras - MG", "Serra Negra - SP", "Socorro - SP",
    "Thermas dos Laranjais - SP", "Trindade - RJ", "Ubatuba - SP",
)

def chave(texto):
    texto = unicodedata.normalize("NFKD", texto.casefold())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", texto).strip()

_MAPA = {}
for destino in DESTINOS:
    _MAPA[chave(destino)] = destino
    _MAPA[chave(destino.rsplit(" - ", 1)[0])] = destino
_MAPA.update({
    "capitolio minas gerais": "Capitólio - MG",
    "aparecida do norte": "Aparecida - SP",
    "sao paulo capital": "São Paulo - SP",
})

def padronizar_destino(texto):
    texto = " ".join(texto.split())
    return _MAPA.get(chave(texto), texto)

def grupos_destinos(valores):
    """Agrupa grafias reconhecidas sem regravar registros antigos."""
    grupos = {d: [] for d in DESTINOS}
    for valor in valores:
        grupos.setdefault(padronizar_destino(valor), []).append(valor)
    return dict(sorted(grupos.items(), key=lambda item: chave(item[0])))
