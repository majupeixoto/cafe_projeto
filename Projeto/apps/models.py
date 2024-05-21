from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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
        ('Aguardando_reparo', 'Aguardando reparo'),
        ('Em_reparo', 'Em reparo'),
        ('Pronto', 'Pronto'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enviada')

    TIPOS_ATENDIMENTO = [
        ('-', '-'),
        ('FON', 'Fora on site'),
        ('FB', 'Fora Balcão'),
        ('GS', 'Garantia serviço'),
        ('GB', 'Garantia balcão'),
        ('GON', 'Garantia on site'),
        ('GIN', 'Garantia instalação'),
        ('GRIN', 'Garantia reincidência'),
    ]
    tipo_atendimento = models.CharField(max_length=4, choices=TIPOS_ATENDIMENTO, default='-')

    aparelho = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    garantia = models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')])
    descricao_problema = models.CharField(max_length=255)
    perfil_os = models.ForeignKey(Perfil, on_delete=models.PROTECT, default = None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enviada')

    # Adicione este campo para representar o funcionário responsável
    funcionario_responsavel = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordens_responsavel')

    # Novos campos
    comentarios_cliente = models.TextField(blank=True, null=True)
    anotacoes_internas = models.TextField(blank=True, null=True)
    problema_detectado = models.TextField(blank=True, null=True)

    numero = models.CharField(max_length=10, unique=True)  # Campo para armazenar o número da ordem de serviço

    def save(self, *args, **kwargs):
        if not self.numero:  # Verifica se o número da ordem já foi atribuído
            year = datetime.now().year  # Obtém o ano atual
            prefix = str(year)[-2:]  # Obtém os últimos dois dígitos do ano
            last_order = OrdemServico.objects.filter(numero__startswith=prefix).order_by('-numero').first()
            if last_order:  # Se já existem ordens de serviço cadastradas no ano corrente
                last_number = int(last_order.numero[-3:])  # Obtém o número da última ordem de serviço
                new_number = last_number + 1  # Calcula o novo número da ordem de serviço
            else:
                new_number = 1  # Se não há ordens de serviço cadastradas no ano corrente, o número será 1
            self.numero = f"{prefix}{new_number:03d}"  # Formata o número da ordem de serviço com três dígitos, ex: 25001
        super().save(*args, **kwargs)

    def detalhes(self):
        return {
        'aparelho': self.aparelho,
        'modelo': self.modelo,
        'garantia': 'Sim' if self.garantia else 'Não',
        'descricao_problema': self.descricao_problema,
        'cliente_nome': self.perfil_os.username if self.perfil_os else None,
        'cliente_cpf': self.perfil_os.cpf if self.perfil_os else None,
        'cliente_contato': self.perfil_os.contato if self.perfil_os else None,
        'status': self.get_status_display(),  # Obter a representação legível do status
        'comentarios_cliente': self.comentarios_cliente,
        'anotacoes_internas': self.anotacoes_internas,
        'problema_detectado': self.problema_detectado,
        'tipo_atendimento': self.get_tipo_atendimento_display(),  # Obter a representação legível do tipo de atendimento
    }

    def __str__(self):
        return (self.aparelho) 