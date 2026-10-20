"""Rotas principais do SIRE (Bloco 1)."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Admin será utilizado internamente para pré-cadastrar agências e agentes.
    path("admin/", admin.site.urls),
    path("", include("sire.urls")),
]
