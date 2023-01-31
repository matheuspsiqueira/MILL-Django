from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Produto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=200)
    codigo_produto = models.IntegerField()
    quantidade_produto = models.IntegerField()
    nome_fornecedor = models.CharField(max_length=100)
    valor_unitario = models.FloatField()
    date_produto = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nome_produto