from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# lembrando: SEMPRE que modificar ou acrescentar uma models a gnt tem q fazer os comandos:
# python manage.py makemigrations
# e em seguida:
# python manage.py migrate
# python manage.py runserver

class Perfil(models.Model):
    nome = models.CharField(max_length=255)
    username = models.CharField(max_length=30, unique=True)
    cpf = models.CharField(max_length=11)
    contato = models.CharField(max_length=11)

    funcionario = models.IntegerField()

    def __str__(self):
        return (self.nome)
    

class OrdemServico(models.Model):
    status = [
        (None, "Ordem de serviço enviada"),
        ('Ordem de serviço iniciada', 'Ordem de serviço iniciada'),
        ('Em análise', 'Em análise'),
        ('Aguardando peça', 'Aguardando peça'),
        ('Em conserto', 'Em conserto'),
        ('Pronto', 'Pronto'),
    ]
    aparelho = models.CharField(max_length=255)
    garantia = models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])
    descricao_problema = models.CharField(max_length=255)
    perfil_os = models.ForeignKey(Perfil, on_delete=models.PROTECT, default = None)

    def __str__(self):
        return (self.aparelho) 