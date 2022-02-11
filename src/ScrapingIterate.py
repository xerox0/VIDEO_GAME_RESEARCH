import bs4
import  requests
import  nltk
import re

base_url = 'https://multiplayer.it'

#headers =  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
videogames_links = []
for x in range (1,100): #il numero del range è 3327 per comodità testiamo su 2
    r = requests.get(f'https://multiplayer.it/giochi/?o=i-migliori&page={x}')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    videogame_list = soup.find_all('h3', class_='media-heading mb-1 lh-1')
    for item in videogame_list:
        for link in item.find_all('a', href = True):
            videogames_links.append(base_url + link['href'])

#test_link = 'https://multiplayer.it/giochi/mario-galaxy-2-per-wii.html'
g = open('../database/scrape_multiplayer.txt', 'w')

for link in videogames_links:
    r = requests.get(link) #, headers=headers)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    name_and_console = soup.find('h1', class_='gamecard-title font-weight-bold ls-n1 lh-1 mb-3 mb-md-1 position-relative').text.strip('\n')
    description = soup.find('div', class_='py-3')

    views = soup.findAll("a", class_="d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold")
    view='d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold'
    views2 = soup.findAll("a", class_="d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold")
    view2='d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold'
    for view in views:
        dev = ("".join(re.findall(r"\w", view["title"])))  # <-- find only digits in "title" attribute
    platform = soup.find('a', class_='font-weight-bold d-inline-block d-md-inline pb-3 pb-md-0 pr-3 pr-md-0').text.strip('\n').rstrip('\n')


    console = name_and_console.split()
    name = console[:-1]
    name = " ".join(name)
    console = console[-1]
   # print(name, console)

    g.write(
        f'{name}\n'
        f'{dev}\n'
        f'{console}\n'
    )
    for string in description.stripped_strings :  # estrae la descrizione, senza i tag html
        string = string.replace('\r', ' ')
        string = string.replace('\n', ' ')
        string = string.replace('\r\n', ' ')
        g.write(f'{string}')
    g.write('\n')

g.write('EOF')
g.close()
