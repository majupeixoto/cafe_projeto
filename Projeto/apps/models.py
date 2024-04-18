from django.db import models

# Create your models here.

# lembrando: SEMPRE que modificar ou acrescentar uma models a gnt tem q fazer os comandos:
# python manage.py makemigrations
# e em seguida:
# python manage.py migrate


#informações do cliente
class OrdemServico(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)  # No formato xxx.xxx.xxx-xx
    data_nascimento = models.DateField()
    contato = models.CharField(max_length=15)  # No formato (xx) xxxx-xxxx
    aparelho = models.CharField(max_length=225)
    garantia = models.BooleanField()
    descricao_problema = models.TextField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)  # Você deve armazenar a senha criptografada

    def __str__(self):
        return self.nome_completo
    
class CadFunc(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.email