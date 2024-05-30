from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Página inicial do projeto
    path('cliente_login/', views.cliente_login, name='cliente_login'),  # Login do cliente
    path('cliente_cadastro/', views.cliente_cadastro, name='cliente_cadastro'),  # Cadastro do cliente
    path('servicos/', views.servicos, name='servicos'),  # Página de serviços (funcionário)
    path('detalhes_os/<int:os_id>/', views.detalhes_os, name='detalhes_os'),
    path('editar_os/<int:os_id>/', views.editar_os, name='editar_os'),
    path('funcionario_login/', views.funcionario_login, name='funcionario_login'),  # Login do funcionário
    path('logout/', views.logout_view, name='logout'),
    path('funcionario_cadastro/', views.funcionario_cadastro, name='funcionario_cadastro'),  # Cadastro do funcionário
    path('home_cliente/', views.home_cliente, name='home_cliente'),  # Cadastro do funcionário
    path('cadastrar_os_cliente/', views.cadastrar_os_cliente, name='cadastrar_os_cliente'),  # Cadastro OS por parte do cliente
    path('listar_os/', views.listar_os, name='listar_os'),  # Listas de todas as OS cadastradas 
    path('excluir_os/<int:pk>/', views.excluir_os, name='excluir_os'),
    path('detalhes_os_cliente/<int:os_id>/', views.detalhes_os, name='detalhes_os_cliente'),
    path('funcionario_perfil/', views.funcionario_perfil, name='funcionario_perfil'),
    path('cliente_perfil/', views.cliente_perfil, name='cliente_perfil'),
    path('conta/excluir_conta/', views.excluir_conta, name='excluir_conta'),
    path('cliente_editar_perfil/', views.cliente_editar_perfil, name='cliente_editar_perfil'),
    path('funcionario_editar_perfil/', views.funcionario_editar_perfil, name='funcionario_editar_perfil'),
    path('avaliar_os/<int:os_id>/', views.avaliar_os, name='avaliar_os'),
]
