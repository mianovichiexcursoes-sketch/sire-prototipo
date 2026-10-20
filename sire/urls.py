from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'sire'
urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('cadastro/', views.cadastro_passageiro, name='cadastro_passageiro'),
    path('login/', LoginView.as_view(template_name='sire/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
urlpatterns += [
    path('agente/excursoes/', views.agente_excursoes, name='agente_excursoes'),
    path('agente/excursoes/nova/', views.cadastrar_excursao, name='cadastrar_excursao'),
    path('agente/excursoes/<int:id>/editar/', views.editar_excursao, name='editar_excursao'),
]
urlpatterns += [
    path('agente/excursoes/<int:id>/embarques/novo/', views.cadastrar_ponto_embarque, name='cadastrar_ponto_embarque'),
    path('agente/excursoes/<int:id>/publicar/', views.publicar_excursao, name='publicar_excursao'),
]

urlpatterns += [
    path('buscar/', views.buscar_excursoes, name='buscar_excursoes'),
    path('excursao/<int:id>/', views.detalhe_excursao, name='detalhe_excursao'),
]
urlpatterns += [path('excursao/<int:id>/reservar/', views.realizar_reserva, name='realizar_reserva')]
