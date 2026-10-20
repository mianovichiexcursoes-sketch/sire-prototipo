"""View inicial provisória; o catálogo real será feito no Bloco 5."""
from django.shortcuts import render


def pagina_inicial(request):
    return render(request, "sire/catalogo.html")

from django.contrib import messages
from django.shortcuts import redirect
from .forms import CadastroPassageiroForm


def cadastro_passageiro(request):
    form = CadastroPassageiroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cadastro concluído. Entre com sua conta.')
        return redirect('sire:login')
    return render(request, 'sire/cadastro_passageiro.html', {'form': form})
