from django.db import models

from .produto import Produto


class Pedido(models.Model):

    data_criacao = models.DateTimeField(auto_now_add=True)
    endereco = models.CharField(max_length=100)
    # produto = models.ForeignKey(Produto, on_delete=models.PROTECT, null=True, blank=True)
    produto = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return f"{self.id} - " + str(
            ", ".join(str(produto.nome) + ": R$" + str(produto.valor) for produto in self.produto.all())
        )
