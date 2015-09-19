import os
from nltk import word_tokenize
from nltk.corpus import stopwords

def main():
    os.chdir('/home/psd/Downloads/19cTexts/')
    
    w = open('output.txt', 'a')
    f = open('output.py', 'r')

    r = f.read()

    for x in r:
        if x in "~`!@#$%^&*()_+-=|}{[]:\"';<>?/.,\\":
            continue
        else:
            w.write(x)

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
