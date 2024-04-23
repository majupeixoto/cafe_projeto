from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import *

def login(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')

        if tipo_usuario == 'cliente':
            return redirect("cliente_login")  
        elif tipo_usuario == 'funcionario':
            return redirect("funcionario_login")

    return render(request, 'apps/login.html')

def cliente_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(username=username, password=senha)

        if user is not None:
            login(request, user)
            return redirect('home_cliente')  
        else:
            messages.error(request, 'Erro ao autenticar o cliente. Por favor, tente novamente.')
            return redirect('cliente_login')

    return render(request, 'apps/cliente_login.html')

def funcionario_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(username=username, password=senha)

        if user is not None:
            login(request, user)
            return redirect('servicos')
        else:
            messages.error(request, 'Erro ao autenticar o funcionário. Por favor, tente novamente.')
            return redirect('funcionario_login')

    return render(request, 'apps/funcionario_login.html')

def cliente_cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            senha = form.cleaned_data['senha']
            user.senha = senha  # Definindo a senha diretamente aqui
            user.save()
            user = authenticate(username=user.username, password=senha)
            if user is not None:
                login(request, user)
                return redirect('home_cliente')
            else:
                messages.error(request, 'Erro ao autenticar o cliente. Por favor, tente novamente.')
                return redirect('cliente_cadastro')
    else:
        form = ClienteForm()
    return render(request, 'apps/cliente_cadastro.html', {'form': form})

def funcionario_cadastro(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nome_da_pagina_de_sucesso')  # Substitua 'nome_da_pagina_de_sucesso' pelo nome da sua página de sucesso
    else:
        form = FuncionarioForm()
    return render(request, 'apps/funcionario_cadastro.html', {'form': form})


def servicos(request):
    return(request, 'apps/servicos.html')