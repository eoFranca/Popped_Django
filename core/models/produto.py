from django.db import models

from uploader.models import Image

from .categoria import Categoria


class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True)
    descricao = models.CharField(max_length=100, blank=False, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    # capa = models.ImageField(upload_to='uploads/', null=True, blank=True)
    def __str__(self):
        return f"{self.nome} - {self.descricao}"
