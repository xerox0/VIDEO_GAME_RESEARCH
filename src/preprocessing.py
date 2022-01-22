import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

def stopWords():
    stop_words = set(stopwords.words('italian'))
    file1 = open('/home/toore/gestione_dell_informazione/video_games_research/database/risultati_scraping.txt')
    line = file1.read()
    words = line.split()

    for r in words:
        if not r in stop_words:
            appendFile = open('/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext.txt','a')
            appendFile.write(" "+r)
            appendFile.close()
    with open("/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext.txt", "r") as f:
        with open('/home/toore/gestione_dell_informazione/video_games_research/database/risultati_scraping.txt', "w") as f1:
            for line in f:
                f1.write(line)

    file2 = open('/home/toore/gestione_dell_informazione/video_games_research/database/giochi.txt')
    line2 = file2.read()
    words2 = line2.split()
    for g in words2:
            if not g in stop_words:
                appendFile2 = open('/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext2.txt', 'a')
                appendFile2.write(" "+g)
                appendFile2.close()
    with open("/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext2.txt", 'r') as l:
            with open('/home/toore/gestione_dell_informazione/video_games_research/database/giochi.txt', 'w') as l1:
                for line2 in l:
                    l1.write(line2)


stopWords()


file_content = open('/home/toore/gestione_dell_informazione/video_games_research/database/risultati_scraping.txt').read()
token = word_tokenize(file_content)

file_content2 = open('/home/toore/gestione_dell_informazione/video_games_research/database/giochi.txt').read()
token2 = word_tokenize(file_content2)

g = open('/home/toore/gestione_dell_informazione/video_games_research/database/tokenizzazione.txt', 'a')
g.write('%s\n' % token)
g.write('&s\n' % token2)
g.close()

os.remove("/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext2.txt")
os.remove("/home/toore/gestione_dell_informazione/video_games_research/database/filteredtext.txt")
#print(token2)
#print(token)

