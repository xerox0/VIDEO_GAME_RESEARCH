from bs4 import BeautifulSoup
import requests


def start_soup(link):
    response = requests.get(link, allow_redirects=False)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


f = open('../database/scrape_instant_gaming.txt', 'w')

for x in range(5 ,120, 5):  # i giochi sono in ordine di uscita, facendo così prendo giochi usciti in un lungo lasso di tempo
    base_link = f"https://www.instant-gaming.com/it/ricerca/?sort_by=avail_date_asc&page={x}"
    print(f'Scansiono la pag n.{x}')
    game_tag = start_soup(base_link).find_all('a', class_='cover')  # è il tag 'a' che contiene il link della pagina del gioco
    for tag in game_tag:
        try:
            game_link = tag.get('href')  # prendo il link della pagina del singolo gioco, per fare lo scraping della pagina
            game_soup = start_soup(game_link)
            game_title = game_soup.find('h1').string.replace('\n', '')  # estrae il titolo del gioco dal tag
            game_description = game_soup.find('div', itemprop='description')
            # ci sono pagine senza descrizione. In tal caso vado avanti
            if game_description is None:
                continue
            game_developer = game_soup.find('a', content='Developer').string.replace('\n', '')

            # estrazione della piattaforma
            platform = game_soup.find('div', class_='subinfos').contents[1]
            l = []
            for string in platform.strings:
                l.append(string)
            platform = l[1].replace('\n', "")
        except:
            continue

        print(game_title)
        f.write(
                f'{game_title}\n'
                f'{game_developer}\n'
                f'{platform}\n'
                )
        for string in game_description.stripped_strings:  # estrae la descrizione, senza i tag html
            string = string.replace('\n', ' ')
            f.write(string)
        f.write('\n')

f.write('EOF')
f.close()
