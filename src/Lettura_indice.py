from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring

ix = open_dir("../indexdir")
qp = QueryParser("title", schema=ix.schema)
q= qp.parse(u"Grand theft auto IV")

with ix.searcher(weighting=scoring.TF_IDF()) as l:
    qp = QueryParser("title", schema=ix.schema)
    q = qp.parse(u"Grand theft auto ")
    with ix.searcher() as s:
        results = s.search(q)
        for hit in results:
            print(hit.score, hit['title'])
