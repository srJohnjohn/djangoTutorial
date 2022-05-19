from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    numero = models.IntegerField()
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    detalhes = models.CharField(max_length=200)
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='arquivos/')

    def form_valid(self, form):
        form.instace.usuario = self.request.user

        url = super().form_valid(form)

        return url

    def __str__(self):
        return "{} ({})".format(self.descricao, self.campo)

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    matricola = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def form_valid(self, form):
        form.instace.usuario = self.request.user

        url = super().form_valid(form)

        return url