from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

@login_required
def servicos(request):
    funcionario = request.user
    ordens_servico = OrdemServico.objects.filter(responsavel=funcionario)

    if request.method == 'POST':
        ordem_servico_id = request.POST.get('ordem_servico_id')
        
        # Verificar se a ordem de serviço existe
        try:
            ordem_servico = OrdemServico.objects.get(id=ordem_servico_id)
        except OrdemServico.DoesNotExist:
            messages.error(request, 'Ordem de serviço não encontrada.')
            return render(request, "apps/servicos.html", {'ordens_servico': ordens_servico})

        # Atribuir a ordem de serviço ao funcionário logado
        ordem_servico.responsavel = funcionario
        ordem_servico.save()

        messages.success(request, f'Ordem de serviço {ordem_servico_id} atribuída a {funcionario.email} com sucesso.')
        return redirect('servicos')

    return render(request, "apps/servicos.html", {'ordens_servico': ordens_servico})

# @login_required
def cadastrar_os(request):
    if request.method == 'POST':
        # Obter os dados do formulário
        aparelho = request.POST['aparelho']
        garantia = request.POST.get('garantia', False)
        descricao_problema = request.POST['descricao_problema']

        # Obter o cliente logado
        cliente = request.user

        # Criar a OS
        nova_os = OrdemServico(
            nome_completo=cliente.nome_completo,
            cpf=cliente.cpf,
            data_nascimento=cliente.data_nascimento,
            contato=cliente.contato,
            aparelho=aparelho,
            garantia=garantia,
            descricao_problema=descricao_problema,
            email=cliente.email,
            senha=cliente.senha  # Você deve armazenar a senha criptografada
        )
        nova_os.save()

        return redirect("...", os_id=nova_os.id)  # direcionar para a página home do cliente
    else:
        return render(request, 'apps/cadastrar_os.html')  # retornar de novo para a mesma página de "cadastrar nova os"


def login(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')

        if tipo_usuario == 'cliente':
            return redirect("login_cliente")  # Substitua 'login_cliente' pela URL da página do cliente
        elif tipo_usuario == 'funcionario':
            return redirect("login_funcionario")  # Substitua 'login_funcionario' pela URL da página do funcionário

    return render(request, 'apps/login.html')  # Nome do template que contém o formulário

def logout(request):
    logout(request)
    if "usuario" in request.session:
        del request.session["usuario"]
    return redirect(login)


def login_funcionario(request):
    title = "Login"
    next_url = request.GET.get('next', '')
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect(next_url or 'servicos')
        else:
            return render(request, 'apps/login_funcionario.html', {"erro": "Usuário não encontrado"})
    return render(request, 'apps/login_funcionario.html', {'next': next_url})



def login_cliente(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        # Verificar se o botão de cadastro foi clicado
        if 'cadastro' in request.POST:
            return redirect('login_cad_cliente')  # redirecionar para a página de cadastro de cliente

        # Autenticar o usuário
        user = authenticate(request, email=email, senha=senha)

        if user is not None:
            # Se as credenciais são válidas, fazer login
            login(request, user)
            return redirect('...')  # redirecionar para a página inicial do cliente
        else:
            # Se as credenciais são inválidas, exibir uma mensagem de erro
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    # Se o método da requisição for GET ou se o POST falhar, renderizar o template de login
    return render(request, 'apps/login_cliente.html')


def login_cad_cliente(request):
    if request.method == 'POST':
        # Obter os dados do formulário
        nome_completo = request.POST['nome_completo']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
        contato = request.POST['contato']
        email = request.POST['email']
        aparelho = request.POST['aparelho']
        descricao_problema = request.POST['descricao_problema']
        garantia = request.POST['garantia']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']

        # Verificar se as senhas coincidem
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'apps/login_cad_cliente.html')

        # Verificar se o email já está cadastrado
        if Cliente.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return render(request, 'apps/login_cad_cliente.html')

        # Criar um novo cliente
        novo_cliente = Cliente(
            nome_completo=nome_completo,
            cpf=cpf,
            data_nascimento=data_nascimento,
            contato=contato,
            email=email,
            aparelho = aparelho,
            garantia = garantia,
            descricao_problema = descricao_problema,
            senha=senha  # Você deve armazenar a senha criptografada
        )
        novo_cliente.save()

        # Autenticar e fazer login do cliente
        user = authenticate(request, email=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('pagina_inicial_cliente')  # redirecionar para a página inicial do cliente
        else:
            messages.error(request, 'Erro ao criar o usuário. Tente novamente.')
    return render(request, 'apps/login_cad_cliente.html')

def login_cad_func(request):
    if request.method == 'POST':
        # Obter os dados do formulário
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar_senha = request.POST['confirmar_senha']
        nome_completo = request.POST['nome_completo']

        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'apps/login_cad_func.html')

        if Funcionario.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return render(request, 'apps/login_cad_func.html')

        # Criar um novo funcionário
        funcionario = Funcionario(email=email, nome_completo=nome_completo, senha=senha)
        funcionario.save()

        # Fazer login do funcionário
        login(request, funcionario)

        return redirect('servicos')

    return render(request, 'apps/login_cad_func.html')