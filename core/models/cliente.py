from django.db import models

from uploader.models import Image


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=100, blank=False, null=True)
    password = models.CharField(max_length=30, blank=False, null=True)
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.nome} - {self.email}"
