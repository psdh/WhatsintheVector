import os
from sorted_output import tokens

def main():
    base = os.getcwd()
    os.chdir(base)

    # f = open('tfidf.py', 'w')
    # f.close()
    empty = []
    os.chdir(base + '/tokens/')
    listdir = os.listdir(base + '/tokens/')

    for token in tokens:
        # started with herdsman, due to problem changed to < hindlegs
        if token < "hindlegs":
            continue
        os.chdir(base)

        f = open('tfidf.py', 'a')

        if unicode(token, "utf-8")[0].isnumeric():
            f.write("n"+str(token) + " = ")
        else:
            f.write(str(token) + " = ")

        #print str(token)
        f.close()

        doc_freq = []

        for token_file in listdir:
            if token_file == "__init__.py":
                continue
            if ".pyc" in token_file:
                continue;
            # print token_file
            os.chdir(base)
            f = open('tfidf.py', 'a')
            #print os.getcwd()
            exec("from tokens." + token_file[:-3] + " import lis")

            # p = open(token_file, 'r')
            # t = p.read()
            # token_list = t[6:-1]
            # token_list = token_list.split(",")
            # print token_list

            # p.close()
    #       token_list.sort()

            count = 0

            for x in lis:
                if token == x:
                    count+=1
    #       print count
            if count > 0:
                term_freq = (token_file, count)
                # print term_freq
                doc_freq.append(term_freq)

        f.write(str(doc_freq))
        #if count == 0:
        #    f.write(str(empty))
        f.write("\n")
        f.close()

    #   f.write("]\n")

    q.close()

if __name__ == '__main__':
    main()
