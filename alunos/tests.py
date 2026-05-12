from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from .models import Aluno


class AlunoUrlTests(SimpleTestCase):
    def test_aluno_crud_urls_are_registered(self):
        self.assertEqual(reverse('lista_alunos'), '/alunos/')
        self.assertEqual(reverse('criar_aluno'), '/alunos/novo/')
        self.assertEqual(reverse('editar_aluno', args=[1]), '/alunos/editar/1/')
        self.assertEqual(reverse('excluir_aluno', args=[1]), '/alunos/excluir/1/')
        self.assertEqual(reverse('dashboard_aluno', args=[1]), '/alunos/dashboard/1/')

    @override_settings(SECURE_SSL_REDIRECT=False)
    def test_home_redirects_to_alunos(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/alunos/')


@override_settings(SECURE_SSL_REDIRECT=False)
class AlunoPageRenderTests(TestCase):
    def test_lista_alunos_renders_successfully(self):
        Aluno.objects.create(nome='Ana Silva', matricula='A001')

        response = self.client.get(reverse('lista_alunos'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ana Silva')

    def test_dashboard_aluno_renders_successfully(self):
        aluno = Aluno.objects.create(nome='Ana Silva', matricula='A001')

        response = self.client.get(reverse('dashboard_aluno', args=[aluno.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard de Ana Silva')
