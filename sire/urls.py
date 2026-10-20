from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'sire'
urlpatterns = [
    path('', views.pagina_inicial, name='catalogo'),
    path('cadastro/', views.cadastro_passageiro, name='cadastro_passageiro'),
    path('login/', LoginView.as_view(template_name='sire/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
