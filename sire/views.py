"""View inicial provisória; o catálogo real será feito no Bloco 5."""
from django.shortcuts import render


def pagina_inicial(request):
    return render(request, "sire/catalogo.html")
