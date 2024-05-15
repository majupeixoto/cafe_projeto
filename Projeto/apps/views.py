from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.http import HttpResponse

#VIEWS DE LOGIN
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
    return redirect('login')


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
            messages.error(request, 'Erro ao autenticar o funcionário. Por favor, tente novamente.')
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

# FINAL DAS VIEWS DE LOGIN


# VIEWS DA CONTA CLIENTE
@login_required
def home_cliente(request):
    user = request.user

    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 1:
        return redirect(login)
    else:
        if request.user.is_anonymous:
            return redirect(login)
        else:
            ordens = OrdemServico.objects.filter(perfil_os=usuario)
            return render(request, 'apps/home_cliente.html', {'ordens': ordens})


@login_required
def cadastrar_os_cliente(request):
    user = request.user
    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 1:
        return redirect(login)
    else:
        if request.method == 'POST':
            aparelho = request.POST['aparelho']
            garantia = request.POST['garantia'] == 'True'
            modelo = request.POST['modelo']
            descricao_problema = request.POST['descricao_problema']

            # Cria uma nova OrdemServico associada ao perfil do usuário logado
            OrdemServico.objects.create(
                aparelho=aparelho,
                modelo=modelo,
                garantia=garantia,
                descricao_problema=descricao_problema,
                perfil_os = usuario
            )

            return redirect(home_cliente)

        return render(request, 'apps/cadastrar_os_cliente.html')

#FINAL DAS VIEWS DA CONTA CLIENTE


# VIEWS DO FUNCIONÁRIO
@login_required
def servicos(request):
    user = request.user

    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 0:
        return redirect(login)
    else:
        # colocar aq a opção de filter o que ele editou
        ordens_servico = OrdemServico.objects.filter(funcionario_responsavel=usuario)
        return render(request, 'apps/servicos.html', {'funcionario': 1, 'ordens_servico': ordens_servico})

@login_required
def listar_os(request): #listar todas as os feitas 
    user = request.user

    usuario = Perfil.objects.get(username=user)

    if usuario.funcionario == 0:
        return redirect(login)
    else:
        if request.user.is_anonymous:
            return redirect(login)
        else:
            ordens = OrdemServico.objects.all()
            return render(request, 'apps/listar_os.html', {'funcionario': 1, 'ordens': ordens})

@login_required
def detalhes_os(request, os_id):
    user = request.user
    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 0:
        return redirect(login)
    else:
        if request.user.is_anonymous:
            return redirect(login)
        else:
            os = get_object_or_404(OrdemServico, id=os_id)
            detalhes_da_os = os.detalhes()

            if request.method == 'POST':
                if os.status == 'Enviada' and 'responsabilizar' in request.POST:
                    os.funcionario_responsavel = usuario
                    os.status = 'Iniciada'
                    os.save()
                
                # Verifica se o formulário de atualização do status foi submetido
                if 'atualizar_status' in request.POST:
                    # Atualiza o status da ordem de serviço com base no valor selecionado no formulário
                    novo_status = request.POST.get('status')
                    os.status = novo_status
                    # Salva as alterações na ordem de serviço
                    os.save()

            # Adicione o nome do funcionário responsável ao contexto
            funcionario_responsavel = os.funcionario_responsavel.username if os.funcionario_responsavel else None

    return render(request, 'apps/detalhes_os.html', {'funcionario': 1, 'os': os, 'detalhes_da_os': detalhes_da_os, 'funcionario_responsavel': funcionario_responsavel})

# VIEW DOS DOIS
def excluir_os(request, pk):
    os = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        os.delete()
        return redirect('listar_os')  # Redireciona para a lista de OS após a exclusão
    return render(request, 'excluir_os.html', {'os': os})