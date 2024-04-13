from django.db import models

# Create your models here.

# lembrando: SEMPRE que modificar ou acrescentar uma models a gnt tem q fazer os comandos:
# python manage.py makemigrations
# e em seguida:
# python manage.py migrate


#informações do cliente
class Cliente(models.Model):
    cliente_nome = models.CharField(max_length=100)
    aparelho = models.CharField(max_length=100)
    garantia = models.BooleanField() # ainda vai ter que criar a opção 'sim' e 'não'
    contato = models.CharField(max_length=20) # considerando formato "DDD + número"
    data_nascimento = models.DateField()
    descricao_problema = models.TextField()

    def __str__(self):
        return self.cliente_nome