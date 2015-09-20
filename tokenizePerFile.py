import codecs
from  nltk import stem, word_tokenize
from nltk.corpus import stopwords
import os
import string
import sys
import unicodedata

def main():
    base = '/home/psd/Downloads/19cTexts/'
    porter = stem.porter.PorterStemmer()
    os.chdir(base + '1830-39/')

    listdir = os.listdir(base + '1830-39')

    for fil in listdir:
        print "Trying for file: " + fil + "\n\n"
        os.chdir(base + '1830-39/')
        f = codecs.open(fil, 'r', encoding='utf8')
        r = unicodedata.normalize('NFKD', f.read()).encode('ascii', 'ignore')
        f.close()

        r = r.translate(None, string.punctuation)
        t = word_tokenize(r)

        t = [porter.stem(tok).lower() for tok in t]
        t = [tok for tok in t if tok not in stopwords.words('english')]

        retval = "lis = " + str(t)

        os.chdir(base + 'tokens/')
        w = open(fil, 'w')
        w.write(retval)
        w.close()


if __name__ == '__main__':
    main()