from django.test import TestCase, override_settings
from django.urls import reverse

from alunos.models import Aluno
from disciplinas.models import Disciplina
from .models import Nota


@override_settings(SECURE_SSL_REDIRECT=False)
class NotaDeleteTests(TestCase):
    def setUp(self):
        self.aluno = Aluno.objects.create(nome='Ana Silva', matricula='A001')
        self.disciplina = Disciplina.objects.create(nome='Matematica', codigo='MAT01')
        self.nota = Nota.objects.create(
            aluno=self.aluno,
            disciplina=self.disciplina,
            nota1=8,
            nota2=7,
        )

    def test_get_delete_page_does_not_delete_nota(self):
        response = self.client.get(reverse('deletar_nota', args=[self.nota.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notas/confirmar_exclusao.html')
        self.assertTrue(Nota.objects.filter(id=self.nota.id).exists())

    def test_post_delete_removes_nota(self):
        response = self.client.post(reverse('deletar_nota', args=[self.nota.id]))

        self.assertRedirects(response, reverse('lista_notas'))
        self.assertFalse(Nota.objects.filter(id=self.nota.id).exists())
