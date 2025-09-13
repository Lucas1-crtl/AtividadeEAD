# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('cadastro/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
]

urlpatterns = [
    path('', views.home, name='home'),  # rota vazia redireciona para o cadastro
    path('cadastro/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
]