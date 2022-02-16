from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.query import Every

ix = open_dir("../indexdir_instant_gaming")
r = ix.searcher().search(Every('title'), limit=None, sortedby='title')
f = open('titoli_instant_gaming.txt','w')
for x in r:
    f.write(x['title'])
    f.write('\n')
f.close()

ix = open_dir("../indexdir_multiplayer")
r = ix.searcher().search(Every('title'), limit=None, sortedby='title')
g = open('titoli_multiplayer.txt','w')
for x in r:
    g.write(x['title'])
    g.write('\n')
g.close()
