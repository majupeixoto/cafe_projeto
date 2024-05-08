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
    STATUS_CHOICES = [
        ('Enviada', 'Ordem de serviço enviada'),
        ('Iniciada', 'Ordem de serviço iniciada'),
        ('Em_analise', 'Em análise'),
        ('Aguardando_peca', 'Aguardando peça'),
        ('Em_conserto', 'Em conserto'),
        ('Pronto', 'Pronto'),
    ]
    aparelho = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    garantia = models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])
    descricao_problema = models.CharField(max_length=255)
    perfil_os = models.ForeignKey(Perfil, on_delete=models.PROTECT, default = None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enviada')

    def detalhes(self):
        return {
            'aparelho': self.aparelho,
            'modelo': self.modelo,
            'garantia': 'Sim' if self.garantia else 'Não',
            'descricao_problema': self.descricao_problema,
            'cliente_nome': self.perfil_os.nome if self.perfil_os else None,
            'cliente_cpf': self.perfil_os.cpf if self.perfil_os else None,
            'cliente_contato': self.perfil_os.contato if self.perfil_os else None,
            # Adicione mais informações do cliente conforme necessário
            'status': self.get_status_display()  # Obter a representação legível do status
        }

    def __str__(self):
        return (self.aparelho) 