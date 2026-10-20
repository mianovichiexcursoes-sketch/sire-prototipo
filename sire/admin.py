"""Admin restrito ao pré-cadastro interno; não gerencia reservas."""

from django.contrib import admin
from .models import Agencia, PerfilUsuario

admin.site.register(Agencia)


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "tipo", "agencia")
    list_filter = ("tipo", "agencia")
