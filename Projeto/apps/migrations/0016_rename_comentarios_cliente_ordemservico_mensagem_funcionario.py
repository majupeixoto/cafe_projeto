# Generated by Django 5.0.4 on 2024-06-07 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0015_ordemservico_avaliacao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordemservico',
            old_name='comentarios_cliente',
            new_name='mensagem_funcionario',
        ),
    ]
