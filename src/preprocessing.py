import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#nltk.download('stopwords')


def stopWords (tokens, file_preprocessing):

    stop_words = set(stopwords.words('italian'))

    with open("./filteredtext.txt", "a") as f:
        for r in tokens:
            if r not in stop_words:
                f.write(" "+r)

    #  scrivo i token su file
    with open("./filteredtext.txt", "r") as f:
        with open(file_preprocessing, "w") as f1:
            for line in f:
                f1.write(line)

    os.remove("./filteredtext.txt")


file_content = open('./scrape_multiplayer.txt').read()
token = word_tokenize(file_content)

file_content2 = open('./scrape_instant_gaming.txt').read()
token2 = word_tokenize(file_content2)


file1_preprocessing = './preprocessing_multiplayer.txt'
stopWords(token, file1_preprocessing)

file2_preprocessing = './preprocessing_instant_gaming.txt'
stopWords(token2, file2_preprocessing)


print(token2)
print(token)
