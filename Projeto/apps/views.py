from django.shortcuts import render, redirect, get_object_or_404
from . models import *

def servicos(request):
    clientes = Cliente.objects.all()
    return render(request, "apps/servicos.html", {'clientes': clientes})

def detalhes_cliente(request, id):
    return ...


