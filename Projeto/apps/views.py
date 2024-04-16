from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.contrib import messages

def servicos(request):
    clientes = OrdemServico.objects.all()
    return render(request, "apps/servicos.html", {'clientes': clientes})

def detalhes_cliente(request, id):
    return ...

def criar_os(request):
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
        return render(request, '...') # retornar dnv para a mesma página de "cadastrar nova os"