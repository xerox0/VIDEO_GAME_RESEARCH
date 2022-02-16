from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser, QueryParser, OrGroup


def filtering(q, schema):
    """apllico il filtro di ricerca giusto in base a ciò che l'utente ha inserito nella User Interface """

    dev_parser = QueryParser("developer", schema)
    plat_parser = QueryParser("platform", schema)
    if q['platform']:
        if q['developer']:
            filters = dev_parser.parse(q['developer']) & plat_parser.parse(q['platform'])
        else:
            filters = plat_parser.parse(q['platform'])
    elif q['developer']:
        filters = dev_parser.parse(q['developer'])
    else:
        filters = None
    return filters


def process_query(q, website):
    ix = open_dir(f"../indexdir_{website}")
    parser = MultifieldParser(["title", "content"], schema=ix.schema, group=OrGroup)
    user_q = parser.parse(q['text'])

    filter = filtering(q, ix.schema)
    with ix.searcher() as s:
        results = s.search(user_q, filter=filter, limit=None)
        # salvo i risultati in una lista, in modo da manipolarli più comodamente nell'algoritmo di fusione dei ranking
        l = []
        for hit in results:
            l.append(hit['title'])
            l.append(hit.score)
            l.append(hit['content'])
            l.append(hit['developer'])
            l.append(hit['platform'])
        return l
