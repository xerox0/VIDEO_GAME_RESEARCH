from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser, QueryParser, OrGroup, AndGroup
from whoosh import query


def filtering(q, schema):
    dev_parser = QueryParser("developer", schema)
    plat_parser = QueryParser("platform", schema)
    # dev_plat_parser = MultifieldParser(['developer', 'platform'], schema, group=AndGroup)
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
    print(filter)
    with ix.searcher() as s:
        results = s.search(user_q, filter=filter)
        print(results)
        for x in results:
            print(x)
    # r = ix.searcher().search(Every('title'), limit=None, sortedby='title')
diz = {'text': 'super mario', 'developer': 'nintendo', 'platform': '3ds'}
process_query(diz, 'multiplayer')

"""
se platform:
    se dev:
        cerca dev e plat
    else
        cerca plat
elif dev:
    cerca dev
else
    nulla (pass)
        """
# print(len(r))
# for x in r:
#     print(x['title'])
