from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# lembrando: SEMPRE que modificar ou acrescentar uma models a gnt tem q fazer os comandos:
# python manage.py makemigrations
# e em seguida:
# python manage.py migrate
# python manage.py runserver

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    contato = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    email_empresa = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.nome

