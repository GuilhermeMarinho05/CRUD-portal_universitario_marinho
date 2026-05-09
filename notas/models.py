from django.db import models
from alunos.models import aluno
from disciplinas.models import disciplina


# Create your models here.

class nota(models.Model):
    aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(disciplina, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.aluno.nome} - {self.disciplina.nome} - {self.valor}"