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
            return redirect('home_cliente')
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
        Perfil.objects.create(username=username, funcionario=0, cpf=cpf, contato=contato, nome=nome)

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
        Perfil.objects.create(
            username=username, 
            funcionario=1,
            nome=nome
        )

        login(request, user)
        request.session["usuario"] = username
        return redirect(servicos)
    
    return render(request, 'apps/funcionario_cadastro.html')

# FINAL DAS VIEWS DE LOGIN


@login_required
def cliente_perfil(request):
    user = request.user
    try:
        # Suponho que o modelo Perfil esteja vinculado ao User pelo campo 'username'.
        # Se não for, ajuste para o campo correto que conecta Perfil ao User.
        usuario = Perfil.objects.get(username=user.username)
    except Perfil.DoesNotExist:
        # Se o perfil não for encontrado, redirecione para um local apropriado,
        # como a página de login ou uma página de erro.
        return redirect('nome_da_url_de_login')

    if usuario.funcionario == 1:
        # Redirecione se o usuário for funcionário para a página de login ou outra página adequada.
        return redirect('nome_da_url_de_login_ou_outra')
    else:
        # Passe todas as informações relevantes para o template.
        context = {
            'nome_completo': usuario.nome,
            'email': user.email,
            'cpf': usuario.cpf,
            'contato': usuario.contato
        }
        return render(request, 'apps/cliente_perfil.html', context)

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
            imagem = request.FILES.get('imagem')  # Obtém a imagem do formulário

            # Cria uma nova OrdemServico associada ao perfil do usuário logado
            OrdemServico.objects.create(
                aparelho=aparelho,
                modelo=modelo,
                garantia=garantia,
                descricao_problema=descricao_problema,
                perfil_os=usuario,
                imagem=imagem  # Adiciona a imagem ao objeto OrdemServico
            )

            return redirect(home_cliente)

        return render(request, 'apps/cadastrar_os_cliente.html')

#FINAL DAS VIEWS DA CONTA CLIENTE


# VIEWS DO FUNCIONÁRIO
@login_required
def funcionario_perfil(request):
    user = request.user
    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 0:
        return redirect(login)
    else:
        nome_completo = usuario.nome
        return render(request, 'apps/funcionario_perfil.html', {'funcionario': 1, 'nome_completo': nome_completo})

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
def editar_os(request, os_id):
    os = get_object_or_404(OrdemServico, id=os_id)
    user = request.user
    usuario = Perfil.objects.get(username=user.username)

    if usuario.funcionario == 0:
        return redirect(login)
    else:
        if os.funcionario_responsavel != usuario:
            return redirect('detalhes_os', os_id=os.id)

        if request.method == 'POST':
            os.status = request.POST.get('status')
            os.comentarios_cliente = request.POST.get('comentarios_cliente')
            os.anotacoes_internas = request.POST.get('anotacoes_internas')
            os.problema_detectado = request.POST.get('problema_detectado')
            os.tipo_atendimento = request.POST.get('tipo_atendimento')
            os.save()
            return redirect('detalhes_os', os_id=os.id)

    return render(request, 'apps/editar_os.html', {'funcionario': 1, 'os': os})


# VIEW DOS DOIS
@login_required
def detalhes_os(request, os_id):
    user = request.user
    usuario = Perfil.objects.get(username=user.username)
    os = get_object_or_404(OrdemServico, id=os_id)
    detalhes_da_os = os.detalhes()
    numero_os = os.numero

    if usuario.funcionario == 1:
        # Lógica para funcionários
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
                os.descricao_problema = request.POST.get('descricao_problema')
                os.comentarios_cliente = request.POST.get('comentarios_cliente')
                os.anotacoes_internas = request.POST.get('anotacoes_internas')
                os.problema_detectado = request.POST.get('problema_detectado')
                os.tipo_atendimento = request.POST.get('tipo_atendimento')  # Atualiza o tipo de atendimento
                os.save()

        # Adicione o nome do funcionário responsável ao contexto
        funcionario_responsavel = os.funcionario_responsavel.username if os.funcionario_responsavel else None

        context = {
            'funcionario': 1, 
            'os': os, 
            'detalhes_da_os': detalhes_da_os, 
            'funcionario_responsavel': funcionario_responsavel,
            'numero_os': numero_os
        }

        return render(request, 'apps/detalhes_os.html', context)

    else:
        # Lógica para clientes
        context = {
            'funcionario': 0, 
            'os': os, 
            'detalhes_da_os': detalhes_da_os, 
            'numero_os': numero_os
        }
        return render(request, 'apps/detalhes_os_cliente.html', context)

@login_required
def excluir_os(request, pk):
    os = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        os.delete()
        return redirect('listar_os')  # Redireciona para a lista de OS após a exclusão
    return render(request, 'excluir_os.html', {'os': os})

@login_required
def excluir_conta(request):
    usuario = Perfil.objects.get(username=request.user.username)

    if request.method == 'POST':
        usuario.delete()
        request.user.delete()
        return redirect('login')
    
    if usuario.funcionario == 0:
        return render(request, 'apps/excluir_conta.html')
    else:
        return render(request, 'apps/excluir_conta.html', {'funcionario': 1})


@login_required
def cliente_editar_perfil(request):
    try:
        # Tenta recuperar o perfil baseado no nome de usuário associado ao usuário atual.
        usuario = Perfil.objects.get(username=request.user.username)
    except Perfil.DoesNotExist:
        # Se o perfil não existir, opcionalmente, redirecione ou exiba uma mensagem.
        messages.error(request, 'Perfil não encontrado.')
        return redirect('alguma_url_de_fallback')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        contato = request.POST.get('contato')
        email = request.POST.get('email')

        user = request.user
        user.email = email
        user.save()

        # Atualiza o perfil do usuário com as novas informações.
        usuario.nome = nome
        usuario.cpf = cpf
        usuario.contato = contato
        usuario.save()

        # Mensagem de sucesso após salvar as alterações.
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('cliente_perfil')

    return render(request, 'apps/cliente_editar_perfil.html', {'perfil': usuario})

@login_required
def funcionario_editar_perfil(request):
    # Usando get_object_or_404 para simplificar a busca e tratamento de erro
    perfil = get_object_or_404(Perfil, username=request.user.username)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        contato = request.POST.get('contato')
        email = request.POST.get('email')

        user = request.user
        if email:  # Verifica se o campo email foi preenchido
            user.email = email
            user.save()

        # Atualizações do perfil são feitas apenas se os campos foram devidamente preenchidos
        if nome:
            perfil.nome = nome
        if cpf:
            perfil.cpf = cpf
        if contato:
            perfil.contato = contato

        perfil.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('funcionario_perfil')
    else:
        # Passa o perfil ao template para preencher os campos existentes com dados atuais
        return render(request, 'apps/funcionario_editar_perfil.html', {'perfil': perfil})