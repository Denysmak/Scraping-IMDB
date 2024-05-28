import pandas as pd
import requests
from bs4 import BeautifulSoup

HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
listaFilmes = []


url = 'https://www.imdb.com/chart/top/'
try:
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    filmes = soup.find('ul', attrs={'role': 'presentation'})
    for i in filmes:
        titulo = i.find('h3').text.split()[1:]
        titulo = " ".join(titulo)
        anoEDuracao = i.find('div', class_='cli-title-metadata')
        ano = anoEDuracao.find_all('span')[0].text
        duracao = anoEDuracao.find_all('span')[1].text
        estrelas = i.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating').text.split()[0]
        listaFilmes.append([titulo, ano, duracao, estrelas])
    df = pd.DataFrame(listaFilmes, columns=['Título', 'Ano de lançamento', 'Duração do filme', 'Avaliação'])
    df.index += 1
    df.to_excel('Filmes.xlsx')


    








except Exception as e:
    print(e)
