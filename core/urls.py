# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('cadastro/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
     path('epis/cadastrar/', views.cadastrar_epi, name='cadastrar_epi'),
    path('epis/', views.listar_epi, name='listar_epi'),
]

