from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.query import Every



#  ix = open_dir(f"indexdir_{website}"")
#  r = ix.searcher().search(Every('title'), limit=None, sortedby='title')
#  print(len(r))
#  for x in r:
#      print(x['title'])

 # ix = open_dir("../indexdir_multiplayer")
 # qp = QueryParser("title", schema=ix.schema)
 # q= qp.parse(u"Grand theft auto IV")
 #
 # with ix.searcher(weighting=scoring.TF_IDF()) as l:
 #     qp = QueryParser("title", schema=ix.schema)
 #     q = qp.parse(u"Grand theft auto ")
 #     with ix.searcher() as s:
 #         results = s.search(q, filter="title")
 #         for hit in results:
 #             print(hit.score, hit['title'])

