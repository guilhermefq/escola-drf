import requests

BASE_URL = 'http://localhost:8000/api/v2/'

# GET Avaliacões
avaliacoes = requests.get(BASE_URL + 'avaliacoes/')

if avaliacoes.status_code == 200:
    print('Avaliacoes: ', avaliacoes.json()['count'])

    next_link = avaliacoes.json().get('next')
    while next_link:
        next_page = requests.get(next_link)
        if next_page.status_code == 200:
            print('Avaliacoes: ', next_page.json()['count'])
            next_link = next_page.json().get('next')
        else:
            print('Erro: ', next_page.status_code)
            break

    # avaliacoes_next = requests.get(avaliacoes.json()['next'])
    # # print(avaliacoes_next.json())

    # results = avaliacoes_next.json()['results']

    # for result in results:
    #     print(result['id'], result['nome'])
