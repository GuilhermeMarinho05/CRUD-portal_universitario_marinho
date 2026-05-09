from django.db import models

# Create your models here.

class disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"