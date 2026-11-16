from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views
from .forms import LoginSireForm, RecuperacaoSenhaForm

app_name = "sire"
urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("cadastro/", views.cadastro_passageiro, name="cadastro_passageiro"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="sire/login.html",
            authentication_form=LoginSireForm,
            # O link de recuperação só aparece com o envio de e-mail configurado.
            extra_context={"recuperacao_ativa": bool(settings.SIRE_RESET_DOMAIN)},
        ),
        name="login",
    ),
    # Recuperação por código (extensão): funciona para toda conta, sem e-mail.
    path("recuperar-acesso/", views.recuperar_por_codigo, name="recuperar_por_codigo"),
    path("minha-conta/codigo/", views.meu_codigo, name="meu_codigo"),
    path(
        "recuperar-senha/",
        views.RecuperarSenhaView.as_view(
            form_class=RecuperacaoSenhaForm,
            template_name="sire/recuperar_senha.html",
            email_template_name="sire/recuperar_senha_email.txt",
            subject_template_name="sire/recuperar_senha_assunto.txt",
            success_url=reverse_lazy("sire:recuperacao_enviada"),
        ),
        name="recuperar_senha",
    ),
    path(
        "recuperar-senha/enviado/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="sire/recuperacao_enviada.html",
        ),
        name="recuperacao_enviada",
    ),
    path(
        "redefinir-senha/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="sire/redefinir_senha.html",
            success_url=reverse_lazy("sire:senha_redefinida"),
        ),
        name="redefinir_senha",
    ),
    path(
        "redefinir-senha/concluida/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="sire/senha_redefinida.html",
        ),
        name="senha_redefinida",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
urlpatterns += [
    path("agente/excursoes/", views.agente_excursoes, name="agente_excursoes"),
    path("agente/excursoes/nova/", views.cadastrar_excursao, name="cadastrar_excursao"),
    path(
        "agente/excursoes/<int:id>/editar/",
        views.editar_excursao,
        name="editar_excursao",
    ),
]
urlpatterns += [
    path(
        "agente/excursoes/<int:id>/embarques/novo/",
        views.cadastrar_ponto_embarque,
        name="cadastrar_ponto_embarque",
    ),
    path(
        "agente/excursoes/<int:id>/publicar/",
        views.publicar_excursao,
        name="publicar_excursao",
    ),
]

urlpatterns += [
    path("buscar/", views.buscar_excursoes, name="buscar_excursoes"),
    path("excursao/<int:id>/", views.detalhe_excursao, name="detalhe_excursao"),
]
urlpatterns += [
    path("excursao/<int:id>/reservar/", views.realizar_reserva, name="realizar_reserva")
]
urlpatterns += [path("minhas-reservas/", views.minhas_reservas, name="minhas_reservas")]
urlpatterns += [
    path(
        "agente/excursoes/<int:id>/reservas/",
        views.reservas_excursao,
        name="reservas_excursao",
    ),
    path(
        "agente/excursoes/<int:id>/passageiros/",
        views.passageiros_excursao,
        name="passageiros_excursao",
    ),
]
