from django.db import models

from uploader.models import Image


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.descricao}"
