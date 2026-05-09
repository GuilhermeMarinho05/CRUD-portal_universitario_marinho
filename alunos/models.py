from django.db import models

# Create your models here.
class aluno(models.Model):
    nome = models.CharField(max_length=100)
    matrícula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nome} - {self.matricula}"