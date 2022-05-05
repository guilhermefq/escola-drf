import requests
from jsonpath import jsonpath

BASE_URL = 'http://localhost:8000/api/v2/'

# GET Avaliacões
r = requests.get(BASE_URL + 'avaliacoes/')

avaliacoes = jsonpath(r.json(), 'results')[0]

# print(avaliacoes)

for avaliacao in avaliacoes:
    print(avaliacao['id'], avaliacao['nome'])


# Nome de todos que avaliaram o curso
nomes = jsonpath(r.json(), 'results[*].nome')
print(nomes)

# Todas as notas das avaliações
notas = jsonpath(r.json(), 'results[*].avaliacao')
print(notas)
