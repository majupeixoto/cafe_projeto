from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib import auth
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')


        if tipo_usuario == 'cliente':
            return redirect("cliente_login")
        elif tipo_usuario == 'funcionario':
            return redirect("funcionario_login")

    return render(request, 'apps/login.html')

def logout_view(request):
    logout(request)

    if "usuario" in request.session:
        del request.session["usuario"]
    return redirect(login_view)


def cliente_login(request): # VIEW CORRETA
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        user = authenticate(username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect(home_cliente)
        else:
            messages.error(request, 'Erro ao autenticar o cliente. Por favor, tente novamente.')
            return redirect('cliente_login')

    return render(request, 'apps/cliente_login.html')

def funcionario_login(request): # VIEW CORRETA
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        user = authenticate(username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect(servicos)
        else:
            messages.error(request, 'Erro ao autenticar o cliente. Por favor, tente novamente.')
            return redirect('funcionario_login')
    
    return render(request, 'apps/funcionario_login.html')

def cliente_cadastro(request): # VIEW CORRETA
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']
        contato = request.POST['contato']

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem. Por favor, tente novamente.')
            return render(request, 'apps/cliente_cadastro.html')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'apps/cliente_cadastro.html', {"erro": "Usuário já existe"})
        elif User.objects.filter(email=email).exists():
            return render(request, 'apps/cliente_cadastro.html', {"erro": "Email já está sendo usado"})

        user = User.objects.create_user(username=username, email=email, password=senha)
        Perfil.objects.create(username=username, funcionario=0, cpf = cpf, contato = contato)

        login(request, user)
        request.session["usuario"] = username
        return redirect(home_cliente)

    return render(request, 'apps/cliente_cadastro.html')

def funcionario_cadastro(request): # VIEW CORRETA
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
        Perfil.objects.create(username=username, funcionario=1)

        login(request, user)
        request.session["usuario"] = username
        return redirect(servicos)
    
    return render(request, 'apps/funcionario_cadastro.html')



# PÁGINAS CIENTE
@login_required
def home_cliente(request):
    user = request.user

    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 1:
        return redirect(cliente_login)
    else:
        return render(request, 'apps/home_cliente.html')

@login_required
def registrar_os(request):
    user = request.user
    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 1:
        return redirect(cliente_login)
    else:
        if request.method == 'POST':
            aparelho = request.POST['aparelho']
            garantia = request.POST['']
            descricao_problema = request.POST['descricao_problema']

            os = OrdemServico.objects.create(aparelho = aparelho, garantia = garantia, 
                                            descricao_problema=descricao_problema)
            
        return render(request, 'apps/#')


# PÁGINAS FUNCIONÁRIO
@login_required
def servicos(request):
    user = request.user

    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 0:
        return redirect(funcionario_login)
    else:
        return render(request, 'apps/servicos.html')