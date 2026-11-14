"""Formulários dos UC01, UC06–UC08 e UC10–UC11."""

from django import forms
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from .models import Excursao, PerfilUsuario, PontoEmbarque, TipoPerfil


class LoginSireForm(AuthenticationForm):
    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": "Usuário ou senha inválidos. Confira os dados e tente novamente.",
    }

    def clean_username(self):
        username = self.cleaned_data["username"]
        variantes = User.objects.filter(username__iexact=username).values_list(
            "username", flat=True
        )
        nomes = list(variantes[:2])
        # Só resolve um nome alternativo se houver uma única conta possível.
        # Com colisão, o Django ainda pode autenticar a grafia exata.
        return nomes[0] if len(nomes) == 1 else username


class RecuperacaoSenhaForm(PasswordResetForm):
    def clean_email(self):
        if not settings.SIRE_RESET_DOMAIN:
            raise forms.ValidationError("A recuperação por e-mail não está disponível neste ambiente.")
        return self.cleaned_data["email"]

    def get_users(self, email):
        return (
            user for user in super().get_users(email)
            if user.username.lower() not in {"demo_passageiro", "demo_agente"}
        )

    def save(self, **kwargs):
        kwargs.update(domain_override=settings.SIRE_RESET_DOMAIN, use_https=True)
        super().save(**kwargs)


class CadastroPassageiroForm(UserCreationForm):
    # O e-mail é obrigatório e único para que a recuperação de senha (extensão,
    # fora da baseline) funcione para toda conta nova. Usa o campo email já
    # existente no User do Django: não há campo, tabela ou migration novos.
    email = forms.EmailField(
        label="E-mail",
        help_text="Obrigatório. Usado para recuperar a senha.",
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Já existe uma conta com este e-mail.")
        return email

    @transaction.atomic
    def save(self, commit=True):
        if not commit:
            return super().save(commit=False)
        usuario = super().save()
        PerfilUsuario.objects.create(usuario=usuario, tipo=TipoPerfil.PASSAGEIRO)
        return usuario


class ExcursaoForm(forms.ModelForm):
    class Meta:
        model = Excursao
        fields = (
            "titulo",
            "destino",
            "data_saida",
            "data_retorno",
            "valor",
            "capacidade",
        )
        widgets = {
            "data_saida": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "data_retorno": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }


class PontoEmbarqueForm(forms.ModelForm):
    class Meta:
        model = PontoEmbarque
        fields = ("local", "horario")
        widgets = {"horario": forms.TimeInput(format="%H:%M", attrs={"type": "time"})}


class ReservaForm(forms.Form):
    ponto_embarque = forms.ModelChoiceField(
        queryset=PontoEmbarque.objects.none(),
        label="Ponto de embarque",
        empty_label="Selecione o embarque",
    )

    def __init__(self, *args, excursao, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["ponto_embarque"].queryset = excursao.pontos_embarque.all()
