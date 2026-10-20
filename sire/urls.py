"""URLs da aplicação SIRE. As demais rotas virão nos próximos blocos."""
from django.urls import path
from . import views

app_name = "sire"
urlpatterns = [
    path("", views.pagina_inicial, name="catalogo"),
]
