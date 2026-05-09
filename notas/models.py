from django.db import models
from alunos.models import Aluno
from disciplinas.models import Disciplina


# Create your models here.

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.aluno.nome} - {self.disciplina.nome} - {self.valor}"