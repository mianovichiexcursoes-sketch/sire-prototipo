"""Views do SIRE. Correspondência com os UC em docs/RASTREABILIDADE.md."""

import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.core.cache import cache
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import OperationalError, transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import CadastroPassageiroForm, ExcursaoForm, PontoEmbarqueForm, ReservaForm
from .models import Excursao, Reserva, StatusExcursao, TipoPerfil


def cadastro_passageiro(request):
    form = CadastroPassageiroForm((request.POST if request.method == "POST" else None))
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Cadastro concluído. Entre com sua conta.")
        return redirect("sire:login")
    return render(request, "sire/cadastro_passageiro.html", {"form": form})


logger = logging.getLogger("sire.recuperacao")


class RecuperarSenhaView(PasswordResetView):
    """Recuperação de senha (extensão, fora da baseline) com limite de pedidos.

    No máximo LIMITE pedidos por hora para o mesmo endereço IP e para o mesmo
    e-mail. Acima disso nada é enviado, mas a resposta é a mesma, para não
    revelar se o e-mail existe nem se o limite foi atingido. O contador fica
    na memória do processo: basta para a demonstração de instância única.
    """

    LIMITE = 3
    JANELA = 60 * 60

    def form_valid(self, form):
        ip = (
            self.request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip()
            or self.request.META.get("REMOTE_ADDR", "")
        )
        chaves = [
            f"recuperar:ip:{ip}",
            f"recuperar:email:{form.cleaned_data['email'].lower()}",
        ]
        if any(cache.get(chave, 0) >= self.LIMITE for chave in chaves):
            logger.warning("Recuperação de senha: limite de pedidos atingido.")
            return HttpResponseRedirect(self.get_success_url())
        for chave in chaves:
            cache.add(chave, 0, self.JANELA)
            cache.incr(chave)
        # O registro não guarda o e-mail: só quantas contas podem receber o link.
        contas = sum(1 for _ in form.get_users(form.cleaned_data["email"]))
        logger.info("Recuperação de senha: pedido recebido; contas elegíveis: %s.", contas)
        try:
            return super().form_valid(form)
        except Exception:
            # Falha do provedor de e-mail: o motivo fica no registro do servidor
            # e o usuário recebe a mesma resposta neutra, sem página de erro.
            logger.error("Recuperação de senha: o envio falhou; resposta neutra devolvida.")
            return HttpResponseRedirect(self.get_success_url())


def exigir_perfil(request, tipo):
    perfil = getattr(request.user, "perfil", None)
    if (
        not perfil
        or perfil.tipo != tipo
        or (tipo == TipoPerfil.AGENTE and not perfil.agencia_id)
    ):
        raise PermissionDenied("Seu perfil não permite esta operação.")
    return perfil


@login_required
def agente_excursoes(request):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    return render(
        request,
        "sire/agente_excursoes.html",
        {
            "excursoes": Excursao.objects.filter(agencia=perfil.agencia),
            "agencia": perfil.agencia,
        },
    )


@login_required
def cadastrar_excursao(request):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    form = ExcursaoForm((request.POST if request.method == "POST" else None))
    if request.method == "POST" and form.is_valid():
        excursao = form.save(commit=False)
        excursao.agencia = perfil.agencia
        excursao.save()
        messages.success(request, "Excursão cadastrada em RASCUNHO.")
        return redirect("sire:agente_excursoes")
    return render(request, "sire/excursao_form.html", {"form": form})


@login_required
def editar_excursao(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    # A mesma transação serializa a redução de capacidade e as reservas:
    # no PostgreSQL pelo bloqueio da linha (FOR UPDATE); no SQLite, BEGIN IMMEDIATE.
    with transaction.atomic():
        excursao = get_object_or_404(
            Excursao.objects.select_for_update(), pk=id, agencia=perfil.agencia
        )
        form = ExcursaoForm(
            (request.POST if request.method == "POST" else None), instance=excursao
        )
        if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "Excursão atualizada.")
            return redirect("sire:agente_excursoes")
    return render(
        request, "sire/excursao_form.html", {"form": form, "excursao": excursao}
    )


@login_required
def cadastrar_ponto_embarque(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
    form = PontoEmbarqueForm((request.POST if request.method == "POST" else None))
    if request.method == "POST" and form.is_valid():
        ponto = form.save(commit=False)
        ponto.excursao = excursao
        ponto.save()
        messages.success(request, "Ponto de embarque cadastrado.")
        return redirect("sire:agente_excursoes")
    return render(
        request, "sire/ponto_embarque_form.html", {"form": form, "excursao": excursao}
    )


@login_required
@require_POST
def publicar_excursao(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    with transaction.atomic():
        excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
        if excursao.pode_publicar():
            excursao.status = StatusExcursao.PUBLICADA
            excursao.save(update_fields=["status"])
            messages.success(request, "Excursão publicada no catálogo.")
        else:
            messages.error(
                request,
                "Publicação exige RASCUNHO, dados válidos e ao menos um ponto de embarque.",
            )
    return redirect("sire:agente_excursoes")


def catalogo(request):
    excursoes = Excursao.objects.filter(status=StatusExcursao.PUBLICADA).select_related(
        "agencia"
    )
    return render(request, "sire/catalogo.html", {"excursoes": excursoes})


def buscar_excursoes(request):
    destino = request.GET.get("destino", "").strip()
    excursoes = Excursao.objects.filter(status=StatusExcursao.PUBLICADA).select_related(
        "agencia"
    )
    if destino:
        excursoes = excursoes.filter(destino__icontains=destino)
    return render(
        request, "sire/catalogo.html", {"excursoes": excursoes, "destino": destino}
    )


def detalhe_excursao(request, id):
    excursao = get_object_or_404(Excursao, pk=id, status=StatusExcursao.PUBLICADA)
    return render(request, "sire/detalhe_excursao.html", {"excursao": excursao})


@login_required
def realizar_reserva(request, id):
    exigir_perfil(request, TipoPerfil.PASSAGEIRO)
    excursao = get_object_or_404(Excursao, pk=id, status=StatusExcursao.PUBLICADA)
    if request.method == "GET" and not excursao.possui_vaga():
        messages.error(request, "Não há vagas disponíveis.")
        return render(request, "sire/detalhe_excursao.html", {"excursao": excursao})
    form = ReservaForm(
        (request.POST if request.method == "POST" else None), excursao=excursao
    )
    if request.method == "POST" and form.is_valid():
        try:
            # O bloqueio é obtido ANTES de reler as vagas. No PostgreSQL,
            # select_for_update() trava a linha da excursão (SELECT ... FOR UPDATE):
            # a segunda reserva espera a primeira confirmar e só então conta as
            # vagas. No SQLite esse recurso é ignorado e quem serializa as
            # gravações é o BEGIN IMMEDIATE configurado em settings.py.
            with transaction.atomic():
                excursao = get_object_or_404(
                    Excursao.objects.select_for_update(),
                    pk=id,
                    status=StatusExcursao.PUBLICADA,
                )
                reserva = Reserva(
                    passageiro=request.user,
                    excursao=excursao,
                    ponto_embarque=form.cleaned_data["ponto_embarque"],
                )
                reserva.full_clean()
                reserva.save()
            messages.success(request, "Reserva realizada com sucesso.")
            return redirect("sire:minhas_reservas")
        except ValidationError as erro:
            form.add_error(None, "; ".join(erro.messages))
        except OperationalError as erro:
            if "locked" not in str(erro).lower() and "busy" not in str(erro).lower():
                raise
            form.add_error(
                None,
                "O banco está ocupado. Tente novamente; a reserva não foi confirmada.",
            )
    return render(
        request, "sire/detalhe_excursao.html", {"excursao": excursao, "form": form}
    )


@login_required
def minhas_reservas(request):
    exigir_perfil(request, TipoPerfil.PASSAGEIRO)
    reservas = Reserva.objects.filter(passageiro=request.user).select_related(
        "excursao", "excursao__agencia", "ponto_embarque"
    )
    return render(request, "sire/minhas_reservas.html", {"reservas": reservas})


@login_required
def reservas_excursao(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
    reservas = excursao.reservas.select_related("passageiro", "ponto_embarque")
    return render(
        request,
        "sire/reservas_excursao.html",
        {"excursao": excursao, "reservas": reservas},
    )


@login_required
def passageiros_excursao(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
    reservas = excursao.reservas.select_related("passageiro", "ponto_embarque")
    return render(
        request,
        "sire/passageiros_excursao.html",
        {"excursao": excursao, "reservas": reservas},
    )
