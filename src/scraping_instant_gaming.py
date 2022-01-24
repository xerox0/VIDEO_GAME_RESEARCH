from bs4 import BeautifulSoup
import requests


def start_soup(link):
    response = requests.get(link, allow_redirects=False)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

f = open('../database/giochi.txt', 'w')

for x in range(5, 100, 5):  # 5 solo per testare, poi bisogna aggiungerne altre
    base_link = f"https://www.instant-gaming.com/it/ricerca/?sort_by=avail_date_asc&page={x}"
    print(f'Scansiono la pag n.{x}')
    game_tag = start_soup(base_link).find_all('a', class_='cover')  # è il tag 'a' che contiene il link della pagina del gioco
    for tag in game_tag:
        try:
            game_link = tag.get('href')  # estraggo il link della pagina del singolo gioco, per fare lo scraping della pagina
            game_soup = start_soup(game_link)
            game_title = game_soup.find('h1').string  # estrae il titolo del gioco dal tag
            game_description = game_soup.find('div', itemprop='description')
            # ci sono pagine senza descrizione. In tal caso vado avanti
            if game_description is None:
                continue
            game_developer = game_soup.find('a', content='Developer').string.replace('\n', ' ')
            game_publisher = game_soup.find('a', content='Publisher').string.replace('\n', ' ')
        except:
            continue

        print(game_title)
        f.write(f'{game_title}\n '
                f'Sviluppato da: {game_developer}\n '
                f'Pubblicato da: {game_publisher}\n ')
        for string in game_description.stripped_strings:  # estrae la descrizione, senza i tag html
            f.write(string)
        f.write('\n\n')

f.close()