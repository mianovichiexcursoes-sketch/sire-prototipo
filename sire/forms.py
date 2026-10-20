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
