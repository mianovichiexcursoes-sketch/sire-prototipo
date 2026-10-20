"""Formulários dos UC01, UC06–UC08 e UC10–UC11."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from .models import Excursao, PerfilUsuario, PontoEmbarque, TipoPerfil


class CadastroPassageiroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")

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
