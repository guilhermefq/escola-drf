import pytest
import requests
from faker import Faker


class TestCursos:
    url_base = 'http://localhost:8000/api/v2/'
    headers = {'Authorization': 'Token ...'}
    curso_id = 0
    fake = Faker()

    # Deve-se seguir o padrão test_
    def test_get_cursos(self):
        res = requests.get(url=self.url_base + 'cursos/', headers=self.headers)

        assert res.status_code == 200

    def test_get_curso(self):
        res = requests.get(url=self.url_base + 'cursos/1/',
                           headers=self.headers)

        assert res.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de Testes com o PyTest",
            "url": self.fake.url(),
        }
        res = requests.post(url=self.url_base + 'cursos/',
                            headers=self.headers, data=novo)

        assert res.status_code == 201
        assert res.json()['titulo'] == novo['titulo']

        TestCursos.curso_id = res.json()['id']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Curso de Flutter Intermediário",
            "url": self.fake.url(),
        }
        res = requests.put(url=self.url_base + f'cursos/{TestCursos.curso_id}/',
                           headers=self.headers, data=atualizado)

        assert res.status_code == 200
        assert res.json()['titulo'] == atualizado['titulo']

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "Curso de Flutter Avançado",
            "url": self.fake.url(),
        }

        res = requests.put(
            url=self.url_base + f'cursos/{TestCursos.curso_id}/', headers=self.headers, data=atualizado)

        assert res.status_code == 200
        assert res.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        res = requests.delete(url=self.url_base + f'cursos/{TestCursos.curso_id}/',
                              headers=self.headers)

        assert res.status_code == 204
        assert len(res.content) == 0
