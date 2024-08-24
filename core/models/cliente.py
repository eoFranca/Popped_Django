from django.db import models

class Cliente (models.Model):
    nome = models.CharField(max_length=100,blank=False,null=True)
    email = models.EmailField(max_length=100,blank=False,null=True)
    password = models.CharField(max_length=30,blank=False,null=True)
    
    def __str__(self):
        return f"{self.nome} - {self.email}"