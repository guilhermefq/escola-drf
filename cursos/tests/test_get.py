import requests

HEADERS = {'Authorization': 'Token 236131ba6d799a790e8dcd88c098437b681217ff'}

URL_BASE = 'http://localhost:8000/api/v2/'

res_curso = requests.get(url=URL_BASE + 'cursos/', headers=HEADERS)
res_avaliacoes = requests.get(url=URL_BASE + 'avaliacoes/', headers=HEADERS)

# Testando se o status code é 200 - Cursos
assert res_curso.status_code == 200

# Testando se o status code é 200 - Avaliações
assert res_avaliacoes.status_code == 200
