import operator


def threshold_edited(L1, L2, k):
    """ funzione che unisce i due ranking e il contenuto delle informazioni della stessa entità del mondo reale.
    Tramite il titolo del videogioco riconosciamo che due entità provenienti da due fonti diverse sono la stessa entità
    nel mondo reale.
    Per la fusone del ranking si è presa ispirazione dall'algoritmo di Threshold di Fagin"""
    top_k_sorted = {}
    top_k = {}
    visited = []  # nomi di vidoegiochi già inseriti in top_k
    results = {}  # conterrà i risultati da mostrare all'utente
    for i in range(0, min(len(L1), len(L2)), 5):  # di 5 in 5 perchè abbiamo tutti i field nelle liste
        print(i)
        T = L1[i + 1] + L2[i + 1]  # calcolo la soglia T
        print(T)
        if L1[i] in visited and L2[i] in visited:
            continue

        if L1[i] in L2:

                score = L1[i + 1] + L2[L2.index(L1[i]) + 1]
                description = L1[i + 2] + L2[L2.index(L1[i]) + 2]  # unisco le descrizioni
                developer = L1[i + 3]
                platform = L1[i + 4]
                top_k[score] = [L1[i], description, developer, platform]
        if L1[i] not in visited:
                visited.append(L1[i])
                score = L1[i + 1]
                description = L1[i + 2]
                developer = L1[i + 3]
                platform = L1[i + 4]
                top_k[score] = [L1[i], description, developer, platform]


                """ è l'elemento di un dizionario. Esempio del dizionario: 
                {15 : ['mario' , 'unione delle descrizioni' , 'nintendo' , 'wii'],
                20 : ['gta', 'unione delle descrizioni', 'sony' , 'ps3'] } . Ho dovuto mettere il punteggio come chiave (prima era il valore),
                perchè non si può usare una lista come chiave di un dizionario, quindi ho invertito """

        if L2[i] in L1:

                score = L2[i + 1] + L1[L1.index(L2[i]) + 1]
                description = L1[i + 2] + L2[L1.index(L2[i]) + 2]
                developer = L2[i + 3]
                platform = L2[i + 4]
                top_k[score] = [L2[i], description, developer, platform]
        if L2[i] not in visited:
                visited.append(L2[i])
                score = L2[i + 1]
                description = L1[i + 2]
                developer = L2[i + 3]
                platform = L2[i + 4]
                top_k[score] = [L2[i], description, developer, platform]

        # ordino il buffer top k per punteggio decrescente, mettendo tutto in un nuovo dizionario
        # prima c'era 1 nelle parentesi, perchè ordinava per valore, adesso ordina per chiave
        sorted_tuples = sorted(top_k.items(), key=operator.itemgetter(0))
        top_k_sorted = {c: v for c, v in sorted_tuples}
        print(top_k_sorted)
     # controllo che gli elementi in top_k superino T
        for c, v in top_k_sorted.items():
            if c > T:
                if len(results) < k:
                    results[c] = v # inserisco in results l'elemento
                elif len(results) == k:
                    return results

    """ arriviamo qui solo se non siamo riusciti a trovare k risultati che superano T. A questo punto prendiamo i primi
    k elementi di top_k """
    results = {c: top_k_sorted[c] for c in list(top_k_sorted)[0:k]}  # c è il punteggio, il valore è la lista
    print(results)
    return results
