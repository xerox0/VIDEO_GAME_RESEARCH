import bs4
import  requests
import  nltk
import re
nltk.download('punkt')

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
videogames_names = []
videogames_description = []
videogames_dev = []
videogames_pub = []
for link in videogames_links:
    r = requests.get(link) #, headers=headers)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    name_and_console = soup.find('h1', class_='gamecard-title font-weight-bold ls-n1 lh-1 mb-3 mb-md-1 position-relative').text.strip('\n').strip('\n')
    description = soup.find('div', class_='py-3').text.rstrip('\n').strip('\n')

    views = soup.findAll("a", class_="d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold")
    view='d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold'
    views2 = soup.findAll("a", class_="d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold")
    view2='d-inline-block pb-3 pb-md-0 pr-3 pr-md-0 font-weight-bold'
    for view in views:
        dev = ("".join(re.findall(r"\w", view["title"])))  # <-- find only digits in "title" attribute
    platform = soup.find('a', class_='font-weight-bold d-inline-block d-md-inline pb-3 pb-md-0 pr-3 pr-md-0').text
    #print(platform)
    try:
        banner_prince = soup.find('a', class_='btn btn-block text-uppercase btn-warning lh-1 ls-n05').text.strip('\n').strip('\n')
    except:
        banner_prince = 'no rating'
    videogames_names.append(name_and_console + '\n')
    videogames_description.append(description + '\n')
    videogames_dev.append(dev + '\n')
    #videogames_pub.append(pub + '\n')
    from nltk.stem import PorterStemmer
#aggiungere sviluppatore, pubblicatore , woosh.

    # ps = nltk.PorterStemmer()
    # for w in videogames_description:
    #     rootWord = ps.stem(w)
    #     #print(rootWord)
    #     g = open('./database/risultatiStamming.txt','a')
    #     g.write('%s\n' % rootWord)
    #     g.close()
    #print([nltk.word_tokenize(t) for t in videogames_names])
    games = {
        'name_and_console': name_and_console,
        'description': description + "\n",
        'banner_prince': banner_prince,
        'developer': dev,
        #'publisher': pub
    }
   
    # f = open('./database/risultati_scraping.csv', 'a')
    # f.write('%s\n' % games)
    # f.close()
    #print(games)
    g = open('./scrape_instant_gaming.txt', 'a')
    g.write('%s\n' % games)
    g.close()
