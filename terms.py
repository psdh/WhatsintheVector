from termcolor import colored
from  nltk import stem, word_tokenize
from nltk.corpus import stopwords
import string
import unicodedata
import math
import os
import sys
from pprint import pprint
from vector_mod import vector_mod_dict


PATH = "/home/varunwachaspati/Downloads/Information Retrieval /WhatsintheVector/"
TOKENS = PATH + "tokens"
INDICES = PATH + "indices"
SCORES = PATH + "doc_vector"



def results(ranks):
    ranks = sorted(ranks,key=lambda tup: tup[1])
    pprint(ranks)
    i = 0
    for x in ranks:
        i = i + 1
        if i%10==0:
            f = raw_input("press y for more")
            if f == "y" or f == "Y":
                continue
            else:
                break


def create_query_vector(tokens):
    vector = []
    sorted_list = os.listdir(INDICES)
    sorted_list.sort()
    os.chdir(PATH)
    for index in sorted_list:
        if ".pyc" in index or "__init__" in index:
            continue
        exec("from indices." + index[:-3] + " import ii")
        df = len(ii)
        tf = 0
        for word in tokens:
            if word == index[2:-3]:
                tf = tf + 1
        tf = math.log(1+tf,2)
        vector.append(tf*df)
    mod = 0
    for num in vector:
        mod = mod + num*num
    mod = math.sqrt(mod)
    return vector, mod


def search(query_vector,query_mod):
    os.chdir(PATH)
    ranks = []
    for score_file in os.listdir(SCORES):
        if ".pyc" in score_file or "__init__" in score_file:
            continue
        exec("from doc_vector." + score_file[:-3] + " import vect")
        mod_vector  = vector_mod_dict[score_file[:-3]]
        dotproduct = 0
        for i in xrange(0,len(vect)):
            dotproduct = dotproduct + vect[i]*query_vector[i]
        angle = math.acos(dotproduct/(mod_vector*query_mod))
        ranks.append((score_file,angle))
    return ranks

def main():
    while True:
        query = raw_input("Enter Your Query Here or Press Q to Exit\n$")
        porter = stem.porter.PorterStemmer()
        if query == "Q" or query == "q":
            print "Thank You"
            sys.exit()
        r = query
        r = r.translate(None, string.punctuation)
        t = word_tokenize(r)

        t = [porter.stem(tok).lower() for tok in t]
        t = [tok for tok in t if tok not in stopwords.words('english')]
        query_vector, query_mod = create_query_vector(t)
        ranks = search(query_vector,query_mod)
        results(ranks)

if __name__ == "__main__":
    main()