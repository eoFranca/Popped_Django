from django.db import models

class Produto (models.Model):
    nome = models.CharField(max_length=100,blank=False,null=True)
    descricao = models.CharField(max_length=100,blank=False,null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'{self.nome} - {self.descricao} '