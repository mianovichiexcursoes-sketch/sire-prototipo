"""Formulários dos UC01, UC06–UC08 e UC10–UC11."""

from django import forms
from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from . import recuperacao
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
            if not recuperacao.conta_compartilhada(user)
        )

    def save(self, **kwargs):
        kwargs.update(domain_override=settings.SIRE_RESET_DOMAIN, use_https=True)
        super().save(**kwargs)


class RecuperacaoPorCodigoForm(forms.Form):
    """Usuário + código de recuperação + senha nova (sem e-mail)."""

    ERRO = "Usuário ou código de recuperação inválidos."

    username = forms.CharField(label="Usuário", max_length=150)
    codigo = forms.CharField(
        label="Código de recuperação",
        max_length=40,
        help_text="O código mostrado quando a conta foi criada. Com ou sem hífens.",
    )
    new_password1 = forms.CharField(
        label="Senha nova",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="Confirmação da senha nova",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def clean(self):
        dados = super().clean()
        if self.errors:
            return dados
        # Mesma regra do login: a grafia alternativa só vale para conta única.
        contas = list(User.objects.filter(username__iexact=dados["username"])[:2])
        if len(contas) == 2:
            contas = [c for c in contas if c.username == dados["username"]]
        usuario = contas[0] if len(contas) == 1 else None
        if (
            usuario is None
            or not usuario.is_active
            or recuperacao.conta_compartilhada(usuario)
            or not recuperacao.confere(usuario, dados["codigo"])
        ):
            # Uma única mensagem: não revela se o usuário existe.
            raise forms.ValidationError(self.ERRO)
        if dados["new_password1"] != dados["new_password2"]:
            self.add_error("new_password2", "As duas senhas não são iguais.")
            return dados
        try:
            password_validation.validate_password(dados["new_password1"], usuario)
        except forms.ValidationError as erro:
            self.add_error("new_password1", erro)
            return dados
        self.usuario = usuario
        return dados

    def save(self):
        self.usuario.set_password(self.cleaned_data["new_password1"])
        self.usuario.save(update_fields=["password"])
        return self.usuario


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
