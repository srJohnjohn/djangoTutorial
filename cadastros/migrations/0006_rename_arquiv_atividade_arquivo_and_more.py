# Generated by Django 4.0.4 on 2022-05-17 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_aluno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividade',
            old_name='arquiv',
            new_name='arquivo',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='potos',
        ),
    ]
