from whoosh.index import open_dir
from whoosh.qparser import QueryParser

ix = open_dir("../indexdir")
qp = QueryParser("title", schema=ix.schema)
q= qp.parse(u"Grand theft auto IV")

with ix.searcher() as s:
    results = s.search(q)
    print(results)