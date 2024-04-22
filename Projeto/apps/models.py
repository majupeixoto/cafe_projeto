from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# lembrando: SEMPRE que modificar ou acrescentar uma models a gnt tem q fazer os comandos:
# python manage.py makemigrations
# e em seguida:
# python manage.py migrate

class Cliente(models.Model):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=255)
    username = models.CharField(max_length=100) # username para login
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    contato = models.CharField(max_length=15)
    senha = models.CharField(max_length=255)  # Armazenar a senha sem criptografia

    def __str__(self):
        return self.nome_completo

class Funcionario(models.Model):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=255)  # Adicionado o campo nome_completo
    username = models.CharField(max_length=100) # username para login
    senha = models.CharField(max_length=255)  # Armazenar a senha sem criptografia

    def __str__(self):
        return self.nome_completo

class OrdemServico(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    aparelho = models.CharField(max_length=225)
    garantia = models.BooleanField()
    descricao_problema = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('aberta', 'Aberta'),
            ('em_andamento', 'Em Andamento'),
            ('fechada', 'Fechada'),
        ],
        default='aberta'
    )
    responsavel = models.ForeignKey('Funcionario', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"OS {self.id} - {self.cliente.nome_completo}"
