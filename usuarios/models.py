from django.db import models


class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_usuario
