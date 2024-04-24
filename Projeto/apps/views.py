from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Usuario

def login(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')

        if tipo_usuario == 'cliente':
            return redirect("cliente_login")
        elif tipo_usuario == 'funcionario':
            return redirect("funcionario_login")

    return render(request, 'apps/login.html')

def Logout(request):
    logout(request)
    return redirect(login)

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

        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request)
            request.session["usuario"] = username
            return redirect('servicos')
        else:
            return render(request, 'apps/funcionario_login.html', {"erro": "Usuário não encontrado"})
    
    return render(request, 'apps/funcionario_login.html')

def cliente_cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem. Por favor, tente novamente.')
            return render(request, 'apps/cliente_cadastro.html')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'apps/cliente_cadastro.html', {"erro": "Usuário já existe"})
        elif User.objects.filter(email=email).exists():
            return render(request, 'apps/cliente_cadastro.html', {"erro": "Email já está sendo usado"})

        user = User.objects.create_user(username=username, email=email, password=senha)
        Usuario.objects.create(user=user, funcionario=0)

        login(request, user)
        request.session["usuario"] = username
        return redirect('home_cliente')

    return render(request, 'apps/cliente_cadastro.html')

def funcionario_cadastro(request):
    if request.method == "POST":
        username = request.POST['username']
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem. Por favor, tente novamente.')
            return render(request, 'apps/funcionario_cadastro.html')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'apps/funcionario_cadastro.html', {"erro": "Usuário já existe"})
        elif User.objects.filter(email=email).exists():
            return render(request, 'apps/funcionario_cadastro.html', {"erro": "Email já está sendo usado"})
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        Usuario.objects.create(user=user, funcionario=1)

        login(request, user)
        request.session["usuario"] = username
        return redirect('servicos')
    
    return render(request, 'apps/funcionario_cadastro.html')

@login_required
def servicos(request):
    try:
        usuario = Usuario.objects.get(user=request.user)
    except Usuario.DoesNotExist:
        return render(request, 'apps/login.html', {'error_message': 'Usuário não encontrado'})

    return render(request, 'apps/servicos.html', {'usuario': usuario})
