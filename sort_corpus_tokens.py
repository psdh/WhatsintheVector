import os

def main():
    base = "/home/varunwachaspati/Downloads/Information Retrieval /WhatsintheVector"
    os.chdir(base)
    q = open("output.txt","r")
    w = q.read()
    tok = list(w.split(" "))
    tok.sort()
    tok.remove("")
    print tok
    q.close()
    f = open("sorted_output.py","w")
    f.write(str(tok))
    f.close()



if __name__ == '__main__':
    main()
