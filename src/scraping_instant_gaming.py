from bs4 import BeautifulSoup
import requests


def start_soup(link):
    response = requests.get(link)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

f = open('giochi.csv', 'a')

for x in range(1, 5):  # 5 solo per testare, poi bisogna aggiungerne altre
    base_link = f"https://www.instant-gaming.com/it/ricerca/?page={x}"
    print(f'Scansiono la pag n.{x}' )
    game_tag = start_soup(base_link).find_all('a', class_='cover') # è il tag 'a' che contiene il link della pagina del gioco
    for tag in game_tag:
        game_link = tag.get('href')  # estraggo il link della pagina del singolo gioco, per fare lo scraping della pagina
        game_soup = start_soup(game_link)
        game_title = game_soup.find('h1').string # estrae il titolo del gioco dal tag
        game_description = game_soup.find('div', itemprop='description')
        if game_description is None:
            continue
        f.write(f'{game_title},{game_description}\n')
        # print(game_title)
        # for string in game_description.stripped_strings: #  estrae la descrizione
        #     print(string)
f.close()
  # requests.exceptions.TooManyRedirects: Exceeded 30 redirects. Troppe richieste ?
