from tkinter.tix import MAX
from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    email = models.EmailField(max_length=45)
    nomeloja = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=14)

    #cnpj = models.OneToOneField(Loja, on_delete=models.CASCADE)
    #admin = models.BooleanField(default=False)

class Comentario(models.Model):
    comentario = models.TextField(max_length=225)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

#class Funcionario(models.Model):
    #nome = models.CharField(max_length=45)
    #email = models.EmailField(max_length=45)
    #senha = models.CharField(max_length=16)
    #usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    #cnpj = models.OneToManyField(Loja, on_delete=models.CASCADE)

#class Loja(models.Model):
    #nomeloja = models.CharField(max_length=45)
    #telefone = models.CharField(max_length=11)
    #cnpj = models.CharField(max_length=14)
 