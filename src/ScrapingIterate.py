import bs4
import  requests

base_url = 'https://multiplayer.it'

#headers =  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
videogames_links = []
for x in range (1,3): #il numero del range è 3327 per comodità testiamo su 2
    r = requests.get(f'https://multiplayer.it/giochi/?o=i-migliori&page={x}')
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    videogame_list = soup.find_all('h3', class_='media-heading mb-1 lh-1')
    for item in videogame_list:
        for link in item.find_all('a', href = True):
            videogames_links.append(base_url + link['href'])

#test_link = 'https://multiplayer.it/giochi/mario-galaxy-2-per-wii.html'
for link in videogames_links:
    r = requests.get(link) #, headers=headers)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    name_and_console = soup.find('h1', class_='gamecard-title font-weight-bold ls-n1 lh-1 mb-3 mb-md-1 position-relative').text.rstrip()
    description = soup.find('div', class_='py-3').text.rstrip()
    try:
        banner_prince = soup.find('a', class_='btn btn-block text-uppercase btn-warning lh-1 ls-n05').text.rstrip()
    except:
        banner_prince = 'no rating'

    games = {
        'name_and_console':name_and_console,
        'description': description,
        'banner_prince':banner_prince
    }
   
    f = open('risultati_scraping.csv', 'a')
    f.write('%s\n' % games)
    f.close()
    #print(games)