from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from users.models import Profile
from .models import Aluno


class AlunoUrlTests(SimpleTestCase):
    def test_aluno_crud_urls_are_registered(self):
        self.assertEqual(reverse('minha_area'), '/alunos/minha-area/')
        self.assertEqual(reverse('lista_alunos'), '/alunos/')
        self.assertEqual(reverse('criar_aluno'), '/alunos/novo/')
        self.assertEqual(reverse('editar_aluno', args=[1]), '/alunos/editar/1/')
        self.assertEqual(reverse('excluir_aluno', args=[1]), '/alunos/excluir/1/')
        self.assertEqual(reverse('dashboard_aluno', args=[1]), '/alunos/dashboard/1/')

    @override_settings(SECURE_SSL_REDIRECT=False)
    def test_home_renders_login(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Acessar portal')


@override_settings(SECURE_SSL_REDIRECT=False)
class AlunoPageRenderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='professor_teste',
            password='admin12345'
        )
        Profile.objects.create(user=self.user, role='professor')
        self.client.force_login(self.user)

    def test_lista_alunos_renders_successfully(self):
        Aluno.objects.create(nome='Ana Silva', matricula='A101')

        response = self.client.get(reverse('lista_alunos'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ana Silva')

    def test_dashboard_aluno_renders_successfully(self):
        aluno = Aluno.objects.create(nome='Ana Silva', matricula='A102')

        response = self.client.get(reverse('dashboard_aluno', args=[aluno.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard de Ana Silva')

    def test_lista_alunos_requires_login(self):
        self.client.logout()

        response = self.client.get(reverse('lista_alunos'))

        self.assertRedirects(response, '/?next=/alunos/')

    def test_student_is_redirected_to_own_area_from_portal(self):
        aluno_user = User.objects.create_user(
            username='aluno_portal_teste',
            password='aluno12345'
        )
        Profile.objects.create(user=aluno_user, role='aluno')
        Aluno.objects.create(
            user=aluno_user,
            nome='Ana Silva',
            matricula='A103',
            curso='Sistemas de Informação'
        )
        self.client.force_login(aluno_user)

        response = self.client.get(reverse('portal'))

        self.assertRedirects(response, reverse('minha_area'))

    def test_student_cannot_access_aluno_crud(self):
        aluno_user = User.objects.create_user(
            username='aluno_bloqueado_teste',
            password='aluno12345'
        )
        Profile.objects.create(user=aluno_user, role='aluno')
        self.client.force_login(aluno_user)

        response = self.client.get(reverse('lista_alunos'))

        self.assertEqual(response.status_code, 403)
