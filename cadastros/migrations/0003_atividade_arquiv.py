# Generated by Django 4.0.4 on 2022-05-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_atividade_usuario_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='arquiv',
            field=models.FileField(default=9, upload_to='arquivos/'),
            preserve_default=False,
        ),
    ]
