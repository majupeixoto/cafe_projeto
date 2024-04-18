from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

def servicos(request):
    clientes = OrdemServico.objects.all()
    return render(request, "apps/servicos.html", {'clientes': clientes})

def cadastrar_os(request):
    if request.method == 'POST':
        nome_completo = request.POST['nome_completo']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
        contato = request.POST['contato']
        aparelho = request.POST['aparelho']
        garantia = request.POST.get('garantia', False)
        descricao_problema = request.POST['descricao_problema']
        email = request.POST['email']
        senha = request.POST['senha']

        # Verificar se o email já está cadastrado
        if OrdemServico.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return redirect('criar_os')

        # Criar a OS
        nova_os = OrdemServico(
            nome_completo=nome_completo,
            cpf=cpf,
            data_nascimento=data_nascimento,
            contato=contato,
            aparelho = aparelho,
            garantia=garantia,
            descricao_problema=descricao_problema,
            email=email,
            senha=senha  # Você deve armazenar a senha criptografada
        )
        nova_os.save()

        return redirect("...", os_id=nova_os.id) # direcionar para a página home do cliente
    else:
        return render(request, 'apps/cadastrar_os.html') # retornar dnv para a mesma página de "cadastrar nova os"


def login(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')

        if tipo_usuario == 'cliente':
            return redirect("login_cliente")  # Substitua 'pagina_cliente' pela URL da página do cliente
        elif tipo_usuario == 'funcionario':
            return redirect("login_funcionario")  # Substitua 'pagina_funcionario' pela URL da página do funcionário

    return render(request, 'apps/login.html')  # Nome do template que contém o formulário

def login_funcionario(request ):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        # Autenticar o usuário
        user = authenticate(request, email=email, senha=senha)

        if user is not None:
            # Se as credenciais são válidas, fazer login
            login(request, user)
            return redirect('...')  # redirecionar para a página inicial do cliente
        else:
            # Se as credenciais são inválidas, exibir uma mensagem de erro
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    # Se o método da requisição for GET, renderizar o template de login
    
    return render(request, 'apps/login_funcionario.html')

def login_cliente(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        # Autenticar o usuário
        user = authenticate(request, email=email, senha=senha)

        if user is not None:
            # Se as credenciais são válidas, fazer login
            login(request, user)
            return redirect('...')  # redirecionar para a página inicial do cliente
        else:
            # Se as credenciais são inválidas, exibir uma mensagem de erro
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    # Se o método da requisição for GET, renderizar o template de login
    return render(request, 'apps/login_cliente.html')


def login_cad_cliente(request):
    if request.method == 'POST':
        nome_completo = request.POST['nome_completo']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
        contato = request.POST['contato']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'apps/login_cad_cliente.html')

        if OrdemServico.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return render(request, 'apps/login_cad_cliente.html')

        user = OrdemServico.objects.create_user(username=email, email=email, password=senha)
        user.first_name = nome_completo
        user.save()

        login(request, user)

        return redirect('...')  # redirecionar para a página inicial do cliente

    return render(request, 'apps/login_cad_cliente.html')

