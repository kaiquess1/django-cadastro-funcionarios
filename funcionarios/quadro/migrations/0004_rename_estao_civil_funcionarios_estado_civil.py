# Generated by Django 4.2.4 on 2023-08-30 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quadro', '0003_funcionarios_cargo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionarios',
            old_name='estao_civil',
            new_name='estado_civil',
        ),
    ]