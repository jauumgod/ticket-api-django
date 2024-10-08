# Generated by Django 5.1.1 on 2024-09-25 12:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0006_tickets_produto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operacoes',
            new_name='Empresas',
        ),
        migrations.RenameModel(
            old_name='UserOperacao',
            new_name='UserEmpresa',
        ),
        migrations.RenameField(
            model_name='sequencia',
            old_name='operacao',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='tickets',
            old_name='operacao',
            new_name='empresa',
        ),
    ]
