import operator

def loaddata(results):
    """inserisco il titolo del videogioco e il punteggio calcolato da Whoosh in una lista, in modo da gestire più
    comodamente i dati nell'algoritmo di threshold"""
    l = []
    for hit in results:
        l.append(hit['title'])
        l.append(hit.score)
    return l


def threshold_edited(L1, L2, k):
    top_k = {}
    results = {}
    for i in range(0, max(len(L1), len(L2)), 2):  # di 2 in 2 perchè i titoli si trovano negli indici pari della lista
        T = L1[i + 1] + L2[i + 1]  # calcolo T
        if L1[i] in L2:
            score = L1[i + 1] + L2[L2.index(L1[i]) + 1]
            top_k[L1[i]] = score
        if L2[i] in L1:
            score = L2[i + 1] + L1[L1.index(L2[i]) + 1]
            top_k[L2[i]] = score

        sorted_tuples = sorted(top_k.items(), key=operator.itemgetter(1))
        sorted_dict = {k: v for k, v in sorted_tuples}

        for c,v in sorted_dict.items():
            if v > T:
                if len(results) < k:
                    results[c] = v # inserisco in results l'elemento
                elif len(results) == k:
                        return results

    results = {c: sorted_dict[c] for c in list(sorted_dict)[0:k]} #SUPERPYTHONICO!!!!!!!!!
    return results
