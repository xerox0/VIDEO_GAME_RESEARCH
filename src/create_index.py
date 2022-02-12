from whoosh.index import create_in, open_dir
from whoosh.fields import *
import os.path

from whoosh.qparser import QueryParser
from nltk.corpus import stopwords
from nltk.stem.snowball import ItalianStemmer


def preprocessing(text):
    stop_words = set(stopwords.words('italian'))
    text_processed = []
    for r in text:
        if r not in stop_words:
            text_processed.append(r)

    stem = ItalianStemmer("italian")
    text_stemmed = []
    for parola in text_processed:
        text_stemmed.append(stem.stem(parola))

    text_stemmed = " ".join(text_stemmed)

    return text_stemmed


def indexing(file, website):
    schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), content_preprocessed=TEXT,
                    platform=TEXT(stored=True), developer=TEXT(stored=True))

    if not os.path.exists(f"indexdir_{website}"):
        os.mkdir(f"../indexdir_{website}")
    ix = create_in(f"../indexdir_{website}", schema)
    f = open(file, 'r')
    l = []  # inserirò i nomi dei giochi. servirà poi per verificare se un gioco è stato già inserito
    while True:
        writer = ix.writer()
        scraped_title = f.readline()
        if scraped_title == 'EOF':  # controllo se sono arrivato alla fine del file
            break

        scraped_developer = f.readline()
        scraped_platform = f.readline()
        scraped_content = f.readline()

        if scraped_title in l:  # se il gioco è stato già inserito nell'indice, non reinserirlo
            writer.commit()
            continue

        l.append(scraped_title)
        print(scraped_title)
        # ix = open_dir("../indexdir")
    # searcher = ix.searcher()
    # parser = QueryParser("title", ix.schema)
    #
    # query = parser.parse(scraped_title)
    # results = searcher.search(query)
    # print(results)
    # if results:
    #     writer.commit()
    #     continue

        preprocessed_content = preprocessing(scraped_content)

        writer.add_document(title=scraped_title, content=scraped_content, content_preprocessed=preprocessed_content,
                            platform=scraped_platform, developer=scraped_developer)
        writer.commit()


# creo un indice per entrambi i file di scraping
indexing('../database/scrape_multiplayer.txt', 'multiplayer')
indexing('../database/scrape_instant_gaming.txt', 'instant_gaming')
