from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

from alunos.models import Aluno
from disciplinas.models import Disciplina
from django.contrib.auth.models import User


# 1. Modelo de falta individual (já existente, com campos de data automática)
class Falta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='faltas')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='faltas')
    data = models.DateField()
    justificada = models.BooleanField(default=False)
    
    # Datas automáticas
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['aluno', 'disciplina', 'data']  # evita duplicidade
        ordering = ['-data']

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} - {self.data}"


# 2. Sistema de chamada em massa (marcar vários alunos de uma vez)
class Chamada(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='chamadas')
    data = models.DateField(default=date.today)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chamadas')
    realizado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['disciplina', 'data']
        ordering = ['-data']

    def __str__(self):
        return f"{self.disciplina} - {self.data}"


class PresencaChamada(models.Model):
    chamada = models.ForeignKey(Chamada, on_delete=models.CASCADE, related_name='presencas')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presente = models.BooleanField(default=True)  # True = presente, False = falta

    class Meta:
        unique_together = ['chamada', 'aluno']

    def __str__(self):
        status = "Presente" if self.presente else "Falta"
        return f"{self.aluno} - {self.chamada.disciplina} - {self.chamada.data} - {status}"


# 3. Limite de faltas por disciplina
class LimiteFaltas(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='limites')
    carga_horaria_total = models.IntegerField(help_text="Carga horária em horas")
    percentual_maximo = models.FloatField(
        default=25.0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentual máximo de faltas (ex: 25%)"
    )

    class Meta:
        unique_together = ['disciplina']

    @property
    def faltas_maximas(self):
        if self.percentual_maximo is None or self.carga_horaria_total is None:
            return 0

        return int((self.percentual_maximo / 100) * self.carga_horaria_total)