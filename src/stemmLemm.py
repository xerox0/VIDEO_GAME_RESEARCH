from nltk.corpus import wordnet as wn
import nltk
import os
from nltk.stem import PorterStemmer
from nltk.stem  import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.snowball import ItalianStemmer
from nltk.stem import  wordnet
nltk.download('wordnet')
nltk.download('omw')



def LemmStem():
    file_lemm = open('/home/toore/gestione_dell_informazione/video_games_research/database/tokenizzazione.txt', "r")
    righe = file_lemm.read()
    word = righe.split()

    lemma = WordNetLemmatizer()
    #stem = SnowballStemmer("italian")

    for parole in word:
        parola = lemma.lemmatize(parole, pos="v")
        appendFile = open('/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext3.txt', 'a')
        appendFile.write(" "+str(parola))
        appendFile.close()

    with open("/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext3.txt","r") as t:
        with open("/home/toore/gestione_dell_informazione/video_games_research/database/index_term.txt","a") as t1:
            for line in t:
                t1.write(line)

LemmStem()

os.remove("/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext3.txt")