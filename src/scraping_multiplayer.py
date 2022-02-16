import bs4
import requests
import re

base_url = 'https://multiplayer.it'

videogames_links = []
for x in range(1, 100):
    r = requests.get(f'https://multiplayer.it/giochi/?o=i-migliori&page={x}')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    videogame_list = soup.find_all('h3', class_='media-heading mb-1 lh-1')
    for item in videogame_list:
        for link in item.find_all('a', href=True):
            videogames_links.append(base_url + link['href'])

g = open('../database/scrape_multiplayer.txt', 'w')

for link in videogames_links:
    r = requests.get(link)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    name_and_console = soup.find('h1', class_='gamecard-title font-weight-bold ls-n1 lh-1 mb-3 mb-md-1 position-relative').text.strip('\n')
    description = soup.find('div', class_='py-3')

    views = soup.findAll("a", class_="d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold")
    view = 'd-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold'
    for view in views:
        dev = ("".join(re.findall(r"\w", view["title"])))
    platform = soup.find('a', class_='font-weight-bold d-inline-block d-md-inline pb-3 pb-md-0 pr-3 pr-md-0').text.strip('\n').rstrip('\n')

    console = name_and_console.split()
    name = console[:-1]
    name = " ".join(name)
    console = console[-1]

    g.write(
        f'{name}\n'
        f'{dev}\n'
        f'{console}\n'
    )
    # estrae la descrizione, senza i tag html, rimuove caratteri che impediscono una buona formattazione del file
    for string in description.stripped_strings:
        string = string.replace('\r', ' ')
        string = string.replace('\n', ' ')
        string = string.replace('\r\n', ' ')
        g.write(f'{string}')
    g.write('\n')

g.write('EOF')
g.close()
