from random import random
import requests
from jsonpath import jsonpath

HEADERS = {'Authorization': 'Token 236131ba6d799a790e8dcd88c098437b681217ff'}

URL_BASE = 'http://localhost:8000/api/v2/'

CURSO_BODY = {
    "titulo": "Python para Zumbis",
    "url": f"http://www.pythonzombies{str(random())}.com.br",
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

# Testando se o título do curso é Python para Zumbis
assert jsonpath(res_curso.json(), 'titulo') == ['Python para Zumbis']

# Testando o código de status HTTP 201 - Avaliações
assert res_avaliacoes.status_code == 201

# Testando se a avaliação é 4
assert jsonpath(res_avaliacoes.json(), 'avaliacao') == ['4.0']
