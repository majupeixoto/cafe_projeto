from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Página inicial do projeto
    path('cliente_login/', views.cliente_login, name='cliente_login'),  # Login do cliente
    path('cliente_cadastro/', views.cliente_cadastro, name='cliente_cadastro'),  # Cadastro do cliente
    path('servicos/', views.servicos, name='servicos'),  # Página de serviços (funcionário)
    path('funcionario_login/', views.funcionario_login, name='funcionario_login'),  # Login do funcionário
    path('funcionario_cadastro/', views.funcionario_cadastro, name='funcionario_cadastro'),  # Cadastro do funcionário
    path('home_cliente/', views.home_cliente, name='home_cliente'),  # Cadastro do funcionário
]
