from bs4 import BeautifulSoup
import requests


def start_soup(link):
    response = requests.get(link)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


<<<<<<< HEAD
f = open('../database/giochi.txt', 'w')

for x in range(1, 6):  # 5 solo per testare, poi bisogna aggiungerne altre
=======
for x in range(1, 2):  # 5 solo per testare, poi bisogna aggiungerne altre
>>>>>>> 4a5102fd4a2b2c68229ddccfc2f3a3f896943487
    base_link = f"https://www.instant-gaming.com/it/ricerca/?page={x}"
    print(f'Scansiono la pag n.{x}')
    game_tag = start_soup(base_link).find_all('a',class_='cover')  # è il tag 'a' che contiene il link della pagina del gioco
    for tag in game_tag:
        game_link = tag.get('href')  # estraggo il link della pagina del singolo gioco, per fare lo scraping della pagina
        game_soup = start_soup(game_link)
<<<<<<< HEAD
        game_title = game_soup.find('h1').string  # estrae il titolo del gioco dal tag
        game_description = game_soup.find('div', itemprop='description')
        # ci sono pagine senza descrizione. In tal caso vado avanti
=======
        game_title = game_soup.find('div',class_='infos mainshadow') # estrae il titolo del gioco dal tag
        game_description = game_soup.find('div', itemprop='description readmore')
>>>>>>> 4a5102fd4a2b2c68229ddccfc2f3a3f896943487
        if game_description is None:
            continue

        try:
            game_developer = game_soup.find('a', content='Developer').string.replace('\n', ' ')
            print(game_developer)
            game_publisher = game_soup.find('a', content='Publisher').string.replace('\n', ' ')
            print(game_publisher)
        except:
            continue

        # print(game_title)
        f.write(f'{game_title}\n '
                f'Sviluppato da: {game_developer}\n '
                f'Pubblicato da: {game_publisher}\n ')
        for string in game_description.stripped_strings:  # estrae la descrizione, senza i tag html
            f.write(string)
        f.write('\n\n')

f.close()
# requests.exceptions.TooManyRedirects: Exceeded 30 redirects. Troppe richieste ?
