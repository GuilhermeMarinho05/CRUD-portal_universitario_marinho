from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from alunos.models import Aluno
from disciplinas.models import Disciplina
from users.models import Profile
from .models import Falta


@override_settings(SECURE_SSL_REDIRECT=False)
class FaltaAccessTests(TestCase):
    def setUp(self):
        self.disciplina = Disciplina.objects.create(nome='Matematica', codigo='FAL101')

    def test_professor_can_create_falta(self):
        professor = User.objects.create_user(username='professor_faltas_teste', password='professor12345')
        Profile.objects.create(user=professor, role='professor')
        aluno = Aluno.objects.create(nome='Ana Silva', matricula='F101')
        self.client.force_login(professor)

        response = self.client.post(
            reverse('criar_falta'),
            {
                'aluno': aluno.id,
                'disciplina': self.disciplina.id,
                'data': '2026-05-13',
                'justificada': '',
            }
        )

        self.assertRedirects(response, reverse('lista_faltas'))
        self.assertTrue(Falta.objects.filter(aluno=aluno).exists())

    def test_student_only_sees_own_faltas(self):
        aluno_user = User.objects.create_user(username='aluno_faltas_teste', password='aluno12345')
        Profile.objects.create(user=aluno_user, role='aluno')
        aluno = Aluno.objects.create(user=aluno_user, nome='Ana Silva', matricula='F102')
        outro_aluno = Aluno.objects.create(nome='Bruno Lima', matricula='F103')
        Falta.objects.create(aluno=aluno, disciplina=self.disciplina, data=date(2026, 5, 13))
        Falta.objects.create(aluno=outro_aluno, disciplina=self.disciplina, data=date(2026, 5, 12))
        self.client.force_login(aluno_user)

        response = self.client.get(reverse('lista_faltas'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ana Silva')
        self.assertNotContains(response, 'Bruno Lima')
