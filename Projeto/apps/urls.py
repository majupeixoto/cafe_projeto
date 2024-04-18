from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.servicos, name = 'servicos'),
    path('login/', views.login, name = 'login'),
    path('cadastrar_os/', views.cadastrar_os, name = 'cadastrar_os'),
    path('login_funcionario/', views.login_funcionario, name = 'login_funcionario'),
]