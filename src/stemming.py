import os
from nltk.stem.snowball import ItalianStemmer


def stemming(filename, indexname):

    file_lemm = open(filename, "r")
    righe = file_lemm.read()
    words = righe.split()
    stem = ItalianStemmer("italian")

    with open("./filteredtext3.txt", "a") as t:
        for parole in words:
            parola = stem.stem(parole)
            t.write(" "+str(parola))

    with open("./filteredtext3.txt", "r") as t:
        with open(indexname, "w") as t1:
            for line in t:
                t1.write(line)

    os.remove("./filteredtext3.txt")


stemming('./preprocessing_multiplayer.txt', 'index_term_multiplayer.txt')
print('multiplayer fatto')
stemming('./preprocessing_instant_gaming.txt', 'index_term_instant_gaming.txt')
print('instant fatto')
