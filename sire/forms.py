from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import PerfilUsuario, TipoPerfil


class CadastroPassageiroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    @transaction.atomic
    def save(self, commit=True):
        if not commit:
            return super().save(commit=False)
        usuario = super().save()
        PerfilUsuario.objects.create(usuario=usuario, tipo=TipoPerfil.PASSAGEIRO)
        return usuario

from django import forms
from .models import Excursao


class ExcursaoForm(forms.ModelForm):
    class Meta:
        model = Excursao
        fields = ('titulo', 'destino', 'data_saida', 'data_retorno', 'valor', 'capacidade')
        widgets = {
            'data_saida': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'data_retorno': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

from .models import PontoEmbarque


class PontoEmbarqueForm(forms.ModelForm):
    class Meta:
        model = PontoEmbarque
        fields = ('local', 'horario')
        widgets = {'horario': forms.TimeInput(format='%H:%M', attrs={'type': 'time'})}
