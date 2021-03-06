# Generated by Django 4.0.4 on 2022-05-12 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('detalhes', models.CharField(max_length=200)),
                ('potos', models.DecimalField(decimal_places=1, max_digits=4)),
                ('campo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.campo')),
            ],
        ),
    ]
