from django.db import models
from alunos.models import Aluno

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey('disciplinas.Disciplina', on_delete=models.CASCADE)

    nota1 = models.FloatField()
    nota2 = models.FloatField()

    class Meta:
        unique_together = ('aluno', 'disciplina')  # 🚨 evita duplicação

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def __str__(self):
        return f"{self.aluno.nome} - {self.disciplina.nome}"