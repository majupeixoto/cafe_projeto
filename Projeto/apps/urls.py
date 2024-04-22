from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.login, name = 'login'),
    path('login_cliente/', views.login_cliente, name = 'login_cliente'),
    path('servicos/', views.servicos, name = 'servicos'),
    path('login_funcionario/', views.login_funcionario, name = 'login_funcionario'),
    path('login_cad_cliente/', views.login_cad_cliente, name = 'login_cad_cliente'),
    path('login_cad_func/', views.login_cad_func, name = 'login_cad_func'),
    path('home_cliente/', views.home_cliente, name = 'home_cliente'),
]