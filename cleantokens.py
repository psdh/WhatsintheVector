from nltk import word_tokenize
from nltk.corpus import stopwords
import os
import string
import unicodedata

def main():
    os.chdir('/home/psd/Downloads/19cTexts/')

    w = open('output.txt', 'a')
    f = open('output.py', 'r')

    r = f.read()

    r = unicodedata.normalize('NFKD', f.read()).encode('ascii', 'ignore')
    r = r.translate(None, string.puntuation)
    w.write(w)

    w.close()
    f.close()

    f = open('output.txt', 'r')
    r = f.read()
    f.close()

    t = word_tokenize(r)
    t = set(t)
    t = list(t)
    t = [x for x in t if x not in stopwords.words('english')]
    w = open('output.txt', 'w')
    for x in t:
        if len(x) > 1:
            w.write(x + " ")
    w.close()

if __name__ == "__main__":
    main()
