from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Curso

# Create your tests here.


class CursosTest(APITestCase):
    url_base = 'http://localhost:8000/api/v2/'
    headers = {'Authorization': 'Token 236131ba6d799a790e8dcd88c098437b681217ff'}
    curso_id = 0
    faker = Faker()

    def test_get_cursos(self):
        """
        Testa se o endpoint de cursos está funcionando corretamente
        """
        url = reverse('cursos-list')
        data = {
            'titulo': 'Curso de Testes com o PyTest',
            'url': self.faker.url(),
        }
        response = self.client.post(
            url, data, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(Curso.objects.get().titulo, data['titulo'])
