from random import random
import requests
from jsonpath import jsonpath

HEADERS = {'Authorization': 'Token 236131ba6d799a790e8dcd88c098437b681217ff'}

URL_BASE = 'http://localhost:8000/api/v2/'

CURSO_BODY = {
    "titulo": "Python Avançado",
    "url": f"http://www.pythonavancado{str(random())}.com.br",
}

CURSO_BODY_PUT = {
    "titulo": "Python Avançado",
    "url": CURSO_BODY["url"],
}

AVALIACAO_BODY = {
    "nome": "José da Silva",
    "comentario": "Python é demais!",
    "email": str(random()) + "jsilva@gmail.com",
    "avaliacao": "4",
    "curso": 2
}

res_curso = requests.post(url=URL_BASE + 'cursos/',
                          headers=HEADERS, data=CURSO_BODY)

res_avaliacoes = requests.post(
    url=URL_BASE + 'avaliacoes/', headers=HEADERS, data=AVALIACAO_BODY)

# Testando o código de status HTTP 201 - Cursos
assert res_curso.status_code == 201

res_curso_id = jsonpath(res_curso.json(), 'id')[0]

# Testando o curso com ID res_curso_id
res_curso_get = requests.get(
    url=URL_BASE + f'cursos/{res_curso_id}/', headers=HEADERS)
assert jsonpath(res_curso_get.json(), 'id')[0] == res_curso_id

# Testando a atualização do curso com ID res_curso_id
res_put_curso = requests.put(
    url=URL_BASE + f'cursos/{res_curso_id}/', headers=HEADERS, data=CURSO_BODY_PUT)
assert res_put_curso.status_code == 200

# Testando o valor do campo titulo do curso atualizado
assert jsonpath(res_put_curso.json(), 'titulo')[0] == CURSO_BODY_PUT["titulo"]

# Testando o DELETE do curso com ID res_curso_id
res_delete_curso = requests.delete(
    url=URL_BASE + f'cursos/{res_curso_id}/', headers=HEADERS)
assert res_delete_curso.status_code == 204

# Testando se o tamanho do conteúdo da resposta é 0
assert len(res_delete_curso.content) == 0

# Testando o get do curso com ID res_curso_id deletado
res_curso_get_deleted = requests.get(
    url=URL_BASE + f'cursos/{res_curso_id}/', headers=HEADERS)
assert res_curso_get_deleted.status_code == 404
