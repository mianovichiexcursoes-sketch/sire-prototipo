"""Views do SIRE. Correspondência com os UC em docs/RASTREABILIDADE.md."""

import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.core.cache import cache
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import OperationalError, transaction
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from . import recuperacao, drive_fotos
from .forms import (
    CadastroPassageiroForm,
    ExcursaoForm,
    FiltroCatalogoForm,
    FotoExcursaoForm,
    PontoEmbarqueForm,
    RecuperacaoPorCodigoForm,
    ReservaForm,
)
from .models import Excursao, FotoExcursao, Reserva, StatusExcursao, TipoPerfil

logger = logging.getLogger("sire.recuperacao")

def cadastro_passageiro(request):
    form = CadastroPassageiroForm((request.POST if request.method == "POST" else None))
    if request.method == "POST" and form.is_valid():
        usuario = form.save()
        # O código é mostrado na própria resposta: não passa pela sessão nem
        # é gravado em lugar algum. Recarregar a página não o exibe de novo.
        return render(
            request,
            "sire/codigo_recuperacao.html",
            {"codigo": recuperacao.codigo_de(usuario), "motivo": "cadastro"},
        )
    return render(request, "sire/cadastro_passageiro.html", {"form": form})


@login_required
def meu_codigo(request):
    """Código atual da conta, para quem já está autenticado."""
    if recuperacao.conta_compartilhada(request.user):
        return render(request, "sire/codigo_recuperacao.html", {"motivo": "compartilhada"})
    return render(
        request,
        "sire/codigo_recuperacao.html",
        {"codigo": recuperacao.codigo_de(request.user), "motivo": "consulta"},
    )


@login_required
def minha_conta(request):
    """Dados da própria conta e atalhos para senha e código de recuperação."""
    return render(
        request,
        "sire/minha_conta.html",
        {
            "perfil": getattr(request.user, "perfil", None),
            "compartilhada": recuperacao.conta_compartilhada(request.user),
        },
    )


class TrocarSenhaView(PasswordChangeView):
    """Troca da própria senha, informando a senha atual."""

    template_name = "sire/trocar_senha.html"
    success_url = reverse_lazy("sire:meu_codigo")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and recuperacao.conta_compartilhada(request.user):
            raise PermissionDenied("A senha da conta compartilhada não pode ser trocada.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resposta = super().form_valid(form)
        messages.success(
            self.request,
            "Senha alterada. O código de recuperação mudou: anote o novo.",
        )
        return resposta


def privacidade(request):
    return render(request, "sire/privacidade.html")


def recuperar_por_codigo(request):
    """Cria uma senha nova com usuário + código de recuperação, sem e-mail."""
    LIMITE, JANELA = 5, 60 * 60
    form = RecuperacaoPorCodigoForm(request.POST if request.method == "POST" else None)
    if request.method == "POST":
        ip = (
            request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip()
            or request.META.get("REMOTE_ADDR", "")
        )
        chaves = [
            f"codigo:ip:{ip}",
            f"codigo:usuario:{request.POST.get('username', '').strip().lower()}",
        ]
        if any(cache.get(chave, 0) >= LIMITE for chave in chaves):
            logger.warning("Recuperação por código: limite de tentativas atingido.")
            form.add_error(None, "Muitas tentativas. Aguarde uma hora e tente de novo.")
        elif form.is_valid():
            usuario = form.save()
            for chave in chaves:
                cache.delete(chave)
            logger.info("Recuperação por código: senha redefinida.")
            return render(
                request,
                "sire/codigo_recuperacao.html",
                {"codigo": recuperacao.codigo_de(usuario), "motivo": "redefinicao"},
            )
        else:
            # Só as tentativas que falham contam para o limite.
            for chave in chaves:
                cache.add(chave, 0, JANELA)
                cache.incr(chave)
            logger.info("Recuperação por código: tentativa recusada.")
    return render(
        request,
        "sire/recuperar_por_codigo.html",
        {"form": form, "recuperacao_por_email": bool(settings.SIRE_RESET_DOMAIN)},
    )


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
        request, "sire/excursao_form.html",
        {
            "form": form,
            "excursao": excursao,
            "foto_form": FotoExcursaoForm(),
            "drive_pronto": drive_fotos.configurado(),
            "limite_fotos": drive_fotos.LIMITE_FOTOS,
        },
    )



@login_required
@require_POST
def adicionar_foto(request, id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    # RN-03: negar URL de outra agência antes de validar/processar qualquer arquivo.
    excursao_inicial = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
    # Rejeição barata quando já está cheio; a conferência após o lock segue
    # obrigatória para pedidos que cheguem simultaneamente.
    if excursao_inicial.fotos.count() >= drive_fotos.LIMITE_FOTOS:
        messages.error(request, "Limite de seis fotos por excursão.")
        return redirect("sire:editar_excursao", id=id)
    # Valida dados do upload antes de adquirir o bloqueio do registro.
    formulario = FotoExcursaoForm(request.POST, request.FILES)
    if not formulario.is_valid():
        messages.error(request, "Foto inválida: envie um arquivo de imagem JPG, PNG ou WebP de até 5 MB.")
        return redirect("sire:editar_excursao", id=id)
    if not drive_fotos.configurado():
        messages.error(request, "Fotos indisponíveis: falta configurar a conexão com o Google Drive.")
        return redirect("sire:editar_excursao", id=id)
    try:
        jpeg = drive_fotos.preparar_jpeg(formulario.cleaned_data["foto"])
    except ValueError as erro:
        messages.error(request, str(erro))
        return redirect("sire:editar_excursao", id=id)

    # PostgreSQL: bloqueia a linha da excursão ANTES de contar e enviar.
    # Requisições concorrentes à mesma excursão são serializadas até o commit;
    # sem o bloqueio, dois pedidos podem observar 5 fotos e gravar 7.
    with transaction.atomic():
        excursao = get_object_or_404(
            Excursao.objects.select_for_update(), pk=id, agencia=perfil.agencia
        )
        if excursao.fotos.count() >= drive_fotos.LIMITE_FOTOS:
            messages.error(request, "Limite de seis fotos por excursão.")
            return redirect("sire:editar_excursao", id=id)
        try:
            identificador = drive_fotos.enviar(excursao.id, jpeg)
        except drive_fotos.FalhaDrive:
            messages.error(request, "Não foi possível enviar ao Google Drive. Nenhuma foto foi cadastrada.")
            return redirect("sire:editar_excursao", id=id)
        try:
            FotoExcursao.objects.create(excursao=excursao, drive_id=identificador)
        except Exception:
            # Compensação: arquivo remoto não pode ficar órfão após falha do banco.
            try:
                drive_fotos.excluir(identificador)
            except drive_fotos.FalhaDrive:
                logger.error("Upload de foto: não foi possível compensar falha de persistência.")
            raise
    messages.success(request, "Foto enviada ao Google Drive e vinculada à excursão.")
    return redirect("sire:editar_excursao", id=id)

@login_required
@require_POST
def remover_foto(request, id, foto_id):
    perfil = exigir_perfil(request, TipoPerfil.AGENTE)
    excursao = get_object_or_404(Excursao, pk=id, agencia=perfil.agencia)
    foto = get_object_or_404(FotoExcursao, pk=foto_id, excursao=excursao)
    try:
        drive_fotos.excluir(foto.drive_id)
    except drive_fotos.FalhaDrive:
        messages.error(request, "Não foi possível remover do Google Drive; a referência foi preservada.")
        return redirect("sire:editar_excursao", id=id)
    foto.delete()
    from django.core.cache import cache
    cache.delete(f"sire_foto:{foto_id}")
    messages.success(request, "Foto removida da excursão e do Google Drive.")
    return redirect("sire:editar_excursao", id=id)


def imagem_excursao(request, foto_id):
    """Entrega pública só imagens de excursões publicadas; sem link direto ao Drive."""
    foto = get_object_or_404(
        FotoExcursao.objects.select_related("excursao", "excursao__agencia"), pk=foto_id
    )
    publicada = foto.excursao.status == StatusExcursao.PUBLICADA
    perfil = getattr(request.user, "perfil", None) if request.user.is_authenticated else None
    propria = bool(
        perfil
        and perfil.tipo == TipoPerfil.AGENTE
        and perfil.agencia_id == foto.excursao.agencia_id
    )
    if not publicada and not propria:
        raise Http404("Foto não encontrada.")
    if not drive_fotos.configurado():
        raise Http404("Foto temporariamente indisponível.")
    from django.core.cache import cache
    chave = f"sire_foto:{foto.pk}"
    dados = cache.get(chave)
    if dados is None:
        try:
            dados = drive_fotos.baixar(foto.drive_id)
        except drive_fotos.FalhaDrive:
            raise Http404("Foto temporariamente indisponível.")
        cache.set(chave, dados, 3600)
    resposta = HttpResponse(dados, content_type="image/jpeg")
    resposta["X-Content-Type-Options"] = "nosniff"
    # Mesmo após despublicação ou exclusão, não deixar cópias reutilizáveis
    # em navegador, CDN, proxy compartilhado ou cache de página.
    resposta["Cache-Control"] = "private, no-store, no-cache, max-age=0, must-revalidate"
    resposta["Pragma"] = "no-cache"
    resposta["Expires"] = "0"
    return resposta


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
    filtros = FiltroCatalogoForm(request.GET or None)
    excursoes = Excursao.objects.filter(status=StatusExcursao.PUBLICADA).select_related(
        "agencia"
    ).prefetch_related("fotos")
    if filtros.is_valid():
        criterios = {
            "destino__icontains": filtros.cleaned_data["destino"],
            "data_saida__gte": filtros.cleaned_data["saida_de"],
            "data_saida__lte": filtros.cleaned_data["saida_ate"],
            "tipo_pacote": filtros.cleaned_data["tipo_pacote"],
        }
        excursoes = excursoes.filter(
            **{campo: valor for campo, valor in criterios.items() if valor}
        )
    elif filtros.is_bound:
        excursoes = excursoes.none()
    return render(
        request, "sire/catalogo.html", {"excursoes": excursoes, "filtros": filtros}
    )


def buscar_excursoes(request):
    return catalogo(request)


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
