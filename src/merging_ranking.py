import operator


def threshold_edited(L1, L2, k):
    """ funzione che unisce i due ranking e il contenuto delle informazioni della stessa entità del mondo reale.
    Tramite il titolo del videogioco riconosciamo che due entità provenienti da due fonti diverse sono la stessa entità
    nel mondo reale.
    Per la fusione del ranking si è presa ispirazione dall'algoritmo di Threshold di Fagin."""

    top_k = {}
    top_k_sorted = {}
    visited = []  # nomi di vidoegiochi già inseriti in top_k, per i quali non ho bisogno di ricalcolare lo score
    results = {}  # conterrà i risultati da mostrare all'utente
    """L1 ed L2 sono due liste che contengono i risultati delle ricerche effettuate sui due corpus di documenti. Per
    ogni gioco verranno occupate 5 "posizioni" della lista, quindi :
    L[i] = nome del videogioco
    L[i +1] = score del gioco nel ranking restituito dalla ricerca sul singolo indice
    L[i + 2] = descrizione del gioco
    L[i + 3] = sviluppatore
    L[i + 4] = platform/console """
    for i in range(0, min(len(L1), len(L2)), 5):
        T = L1[i + 1] + L2[i + 1]  # calcolo la soglia T, sommando gli score
        if L1[i] in visited and L2[i] in visited:
            continue

        if L1[i] not in visited:
            if L1[i] in L2:
                visited.append(L1[i])
                score = L1[i + 1] + L2[L2.index(L1[i]) + 1]
                description = L1[i + 2] + "\n\n" + L2[L2.index(L1[i]) + 2]  # unisco le descrizioni
                developer = L1[i + 3]
                platform = L1[i + 4]
                """ aggiungiamo al dizionario top_k il gioco. La chiave corrisponde alla somma degli score che le due 
                ricerche mi hanno restituito, il valore sarà una lista con gli altri dati del gioco """
                top_k[score] = [L1[i], description, developer, platform]

        if L2[i] not in visited:
            if L2[i] in L1:
                visited.append(L2[i])
                score = L2[i + 1] + L1[L1.index(L2[i]) + 1]
                description = L2[i + 2] + "\n\n" + L1[L1.index(L2[i]) + 2]
                developer = L2[i + 3]
                platform = L2[i + 4]
                top_k[score] = [L2[i], description, developer, platform]

        # ordino il buffer top k per punteggio decrescente, mettendo tutto in un nuovo dizionario
        sorted_tuples = sorted(top_k.items(), key=operator.itemgetter(0))
        top_k_sorted = {c: v for c, v in sorted_tuples}

        # controllo che gli elementi in top_k superino T
        for c, v in top_k_sorted.items():
            if c > T:
                if len(results) < k:
                    results[c] = v  # inserisco in results l'elemento
                elif len(results) == k:
                    return results

    # può capitare che la fusione dei ranking produca pochissimi risultati. In tal caso ne aggiungiamo alcuni,
    # andandoli a prendere dai risultati più rilevanti che le ricerche sui singoli indici ci hanno restituito
    if 0 < len(results) < k:
        for i in range(0, 5*k, 5):
            if L1[i+1] >= L2[i+1]:
                results[L1[i + 1]] = [L1[i], L1[i + 2], L1[i + 3], L1[i + 4]]
            else:
                results[L2[i + 1]] = [L2[i], L2[i + 2], L2[i + 3], L2[i + 4]]
        return results

    if len(results) == 0:
        if not L1:  # se L1 è vuota, prendo i risultati soltanto da L2
            for i in range(0, len(L2), 5):
                results[L2[i+1]] = [L2[i], L2[i+2], L2[i+3], L2[i+4]]
            return results
        elif not L2:
            for i in range(0, len(L1), 5):
                results[L1[i + 1]] = [L1[i], L1[i + 2], L1[i + 3], L1[i + 4]]
            return results
        else:
            for i in range(0, len(L1), 5):
                results[L1[i + 1]] = [L1[i], L1[i + 2], L1[i + 3], L1[i + 4]]
            return results

    results = {c: top_k_sorted[c] for c in list(top_k_sorted)[0:k]}
    return results
