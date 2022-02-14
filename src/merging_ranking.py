def loaddata(results):
    """inserisco il titolo del videogioco e il punteggio calcolato da Whoosh in una lista, in modo da gestire più
    comodamente i dati nell'algoritmo di threshold"""
    l = []
    for hit in results:
        l.append(hit['title'])
        l.append(hit.score)
    return l


def threshold_edited(L1, L2, k):
    top_k = []
    results = {}
    for i in range(0, max(len(L1), len(L2)), 2):  # di 2 in 2 perchè i titoli si trovano negli indici pari della lista
        T = L1[i + 1] + L2[i + 1]  # calcolo T
        if L1[i] in L2:
            score = L1[i + 1] + L2[L2.index(L1[i]) + 1]
            top_k.append(L1[i])
            top_k.append(score)
        if L2[i] in L1:
            score = L2[i + 1] + L1[L1.index(L2[i]) + 1]
            top_k.append(L2[i])
            top_k.append(score)
    # controllo se in top k abbiamo i punteggi > T
    for j in range(1, len(top_k), 2):  # parto da 1 perchè so che i punteggi sono negli indici dispari
        if top_k[j] > T:
            results[top_k[j - 1]] = top_k[j]  # aggiungo il documento al dizionario dei risultati
        # devono esserci massimo k elementi nel dizionario!!!!!!!


    return results
            # non serve piu (?)
            # for j in range(0,max(len(L1) | len(L2))):
            #     if L1[i][1] == L2[j][1] :
            #         somma=L1[i][0] + L2[j][0]
            #         top_k.append([L1[i][0]+somma,L1[i][1]])






"""fino a quando abbiamo k documenti con punteggio > T: (non è detto che ci siano, quindi se si arriva alla fine della
    lista,restituire i primi k risultati)
        prendi i due documenti, calcola T 
        cerca il corrispondente documento nell'altra lista e somma i loro punteggi, farlo per entrmabi i documenti
        mettili nel buffer e verifica che i primi k documenti abbiano punteggio > T
        se lo hanno, fine algoritmo e restituisci k risultati, altrimenti continua 


"""
