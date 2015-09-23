import os
import math

def main():
    base = "/home/varunwachaspati/Downloads/Information Retrieval /WhatsintheVector/"
    os.chdir(base)
    listdir = os.listdir(base + 'tokens/')    
    total_docs = len(listdir)

    for d in listdir:
        if d == "__init__.py" or ".pyc" in d:
                continue
        doc = []
        listd = os.listdir(base + 'indices/')
        listd.sort()
        for tok in listd:
            if tok == "__init__.py" or ".pyc" in tok:
                continue
            exec("from indices." + tok[0:-3] + " import ii")
            df = len(ii)
            if df == 0:
                idf = 0
            else:
                idf = math.log(total_docs/df)
            tf = 0
            for tup in ii:
                if tup[0][:-3] == d[:-3]:
                    tf = math.log(1 + tup[1],2)
            score = tf * idf
            doc.append(score)
        os.chdir(base+"doc_vector/")
        f = open(d,"w")
        f.write("vect = " + str(doc))
        f.close()


if __name__ == '__main__':
    main()
