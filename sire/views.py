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

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction, OperationalError
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Excursao, TipoPerfil, StatusExcursao
from .forms import ExcursaoForm


def exigir_perfil(request, tipo):
    perfil = getattr(request.user, 'perfil', None)
    if not perfil or perfil.tipo != tipo or (tipo == TipoPerfil.AGENTE and not perfil.agencia_id):
        raise PermissionDenied('Seu perfil não permite esta operação.')
    return perfil


@login_required
def agente_excursoes(request):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    return render(request, 'sire/agente_excursoes.html', {
        'excursoes': Excursao.objects.filter(agencia=perfil.agencia), 'agencia': perfil.agencia})


@login_required
def cadastrar_excursao(request):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    form = ExcursaoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        excursao = form.save(commit=False)
        excursao.agencia = perfil.agencia
        excursao.save()
        messages.success(request, 'Excursão cadastrada em RASCUNHO.')
        return redirect('sire:agente_excursoes')
    return render(request, 'sire/excursao_form.html', {'form': form})


@login_required
def editar_excursao(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    # A mesma transação serializa a redução de capacidade e as reservas no SQLite.
    with transaction.atomic():
        excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
        form = ExcursaoForm(request.POST or None, instance=excursao)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, 'Excursão atualizada.')
            return redirect('sire:agente_excursoes')
    return render(request, 'sire/excursao_form.html', {'form': form, 'excursao': excursao})

from .forms import PontoEmbarqueForm


@login_required
def cadastrar_ponto_embarque(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
    form = PontoEmbarqueForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ponto = form.save(commit=False)
        ponto.excursao = excursao
        ponto.save()
        messages.success(request, 'Ponto de embarque cadastrado.')
        return redirect('sire:agente_excursoes')
    return render(request, 'sire/ponto_embarque_form.html', {'form': form, 'excursao': excursao})


@login_required
@require_POST
def publicar_excursao(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    with transaction.atomic():
        excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
        if excursao.pode_publicar():
            excursao.status = StatusExcursao.PUBLICADA
            excursao.save(update_fields=['status'])
            messages.success(request, 'Excursão publicada no catálogo.')
        else:
            messages.error(request, 'Publicação exige RASCUNHO, dados válidos e ao menos um ponto de embarque.')
    return redirect('sire:agente_excursoes')


def catalogo(request):
    excursoes = Excursao.objects.filter(status=StatusExcursao.PUBLICADA).select_related('agencia')
    return render(request, 'sire/catalogo.html', {'excursoes': excursoes})


def buscar_excursoes(request):
    destino = request.GET.get('destino', '').strip()
    excursoes = Excursao.objects.filter(status=StatusExcursao.PUBLICADA).select_related('agencia')
    if destino:
        excursoes = excursoes.filter(destino__icontains=destino)
    return render(request, 'sire/catalogo.html', {'excursoes': excursoes, 'destino': destino})


def detalhe_excursao(request, id):
    excursao = get_object_or_404(Excursao, pk=id, status=StatusExcursao.PUBLICADA)
    return render(request, 'sire/detalhe_excursao.html', {'excursao': excursao})
