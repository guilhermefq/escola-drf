import requests

HEADERS = {'Authorization': 'Token ...'}

URL_BASE = 'http://localhost:8000/api/v2/'

res_curso = requests.get(url=URL_BASE + 'cursos/', headers=HEADERS)
res_avaliacoes = requests.get(url=URL_BASE + 'avaliacoes/', headers=HEADERS)

# Testando se o status code é 200 - Cursos
assert res_curso.status_code == 200

# Testando se o status code é 200 - Avaliações
assert res_avaliacoes.status_code == 200
