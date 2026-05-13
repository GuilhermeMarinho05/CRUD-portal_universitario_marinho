from django.db import models
from django.conf import settings


class Aluno(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='aluno',
        verbose_name='usuario de acesso'
    )
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10, unique=True)
    curso = models.CharField(max_length=120, blank=True, default='')
    disciplinas = models.ManyToManyField(
        'disciplinas.Disciplina',
        blank=True,
        related_name='alunos'
    )

    def __str__(self):
        return f"{self.nome} - {self.matricula}"
