# signals.py
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from notifications.signals import notify
from .models import *
@receiver(pre_save, sender=OrdemServico)
def ordem_servico_pre_save(sender, instance, **kwargs):
    if instance.pk:
        old_instance = OrdemServico.objects.get(pk=instance.pk)
        instance._old_status = old_instance.status
        instance._old_mensagem_funcionario = old_instance.mensagem_funcionario

@receiver(post_save, sender=OrdemServico)
def ordem_servico_post_save(sender, instance, created, **kwargs):
    if not created:
        cliente = instance.perfil_os
        if cliente.funcionario == 0:  # Certifique-se de que o perfil é de um cliente
            recipient_username = cliente.username  # Obtém o nome de usuário do cliente
            try:
                recipient_user = User.objects.get(username=recipient_username)  # Encontra o usuário com base no nome de usuário
                funcionario_responsavel = instance.funcionario_responsavel
                if funcionario_responsavel:
                    funcionario_responsavel_nome = funcionario_responsavel.nome
                    # Verifica se o status foi alterado
                    if hasattr(instance, '_old_status') and instance.status != instance._old_status:
                        message = f"{funcionario_responsavel_nome} atualizou o status do seu equipamento #{instance.numero} para '{instance.get_status_display()}'. Vá conferir!"
                        notify.send(instance, recipient=recipient_user, verb='', target=instance, description=message)

                    # Verifica se a mensagem do funcionário foi alterada
                    if hasattr(instance, '_old_mensagem_funcionario') and instance.mensagem_funcionario != instance._old_mensagem_funcionario:
                        message = f"{funcionario_responsavel_nome} enviou uma nova mensagem sobre seu equipamento #{instance.numero}"
                        notify.send(instance, recipient=recipient_user, verb='', target=instance, description=message)
            except User.DoesNotExist:
                # Lida com o caso em que o usuário não é encontrado
                # Você pode registrar um aviso, lançar um erro ou lidar com isso de acordo com sua lógica de negócios
                pass