from whoosh import scoring
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
from whoosh.searching import  Searcher

def LoadData(path, results):
    ix = open_dir(path)

    L1 = []

    with ix.searcher(weighting=scoring.TF_IDF()) as l:
          qp = QueryParser("title", schema=ix.schema)
          q = qp.parse(u"Grand theft auto ")
          with ix.searcher() as s:
              results = s.search(q)
              for hit in results:
                    L1.append(hit['title'])
                    L1.append(hit.score)

# l1 = ['titolo', 12, 'titolo2', 33]
# if 'aaa' in l1:

l1 = LoadData()
l2 = LoadData()
top_k = []
def ALGO_T(L1,L2,k):
    stop = 0
    while True:
            for i in range(0,len(l1), 2): # titoli
                T = L1[i+1] + L2[i+1]
                if L1[i] == L2[i]:
                    score = L1[i+1] + L2[i+1]
                    top_k.append(L1[i],score)
                if L1[i] in L2:
                    score = L1[i+1] + L2[L2.index(L1[i]) + 1]
                    top_k.append(L1[i], score)
                if L2[i] in L1:
                    score = L2[i+1] + L1[L1.index(L2[i]) + 1]
                    top_k.append(L2[i],score)

            for j in range(0,max(len(L1) | len(L2))):
                if L1[i][1] == L2[j][1] :
                    somma=L1[i][0] + L2[j][0]
                    top_k.append([L1[i][0]+somma,L1[i][1]])




            i = i +1




#LoadData(L1)
"""input: 2 liste di risultati.
while
    T = score_multi[x] + score_instant[x]
    cerca titolo_multi in instant
    se c'è
        somma punteggi
        inserisci titolo e somma in top_buffer
    cerca titolo_instant in multi
    se c'è
        somma punteggi
        inserisci titolo e somma in top_buffer

"""
