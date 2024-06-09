# Generated by Django 5.0.4 on 2024-06-07 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_remove_ordemservico_funcionario_responsavel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='funcionario_responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordens_responsavel', to='apps.perfil'),
        ),
    ]
