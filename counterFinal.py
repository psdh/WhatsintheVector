import os
from sorted_output import tokens

def main():
    base = os.getcwd()
    os.chdir(base)

    w = open('index.py', 'w')
    w.close()
    empty = []
    os.chdir(base + '/tokens/')
    listdir = os.listdir(base + '/tokens/')

    ans = {}

    for token_file in listdir:
        if token_file == "index.py" or token_file == "__init__.py" or ".pyc" in token_file:
            continue

        #print token_file

        r = open(token_file, 'r').read()

        exec("from tokens." + token_file[:-3] + " import lis")

        for tok in lis:
            if ans.get(tok) is None:
                ans[tok] = [token_file]
            else:
                ans[tok] += [token_file]
#            print tok, ans.get(tok)

    os.chdir(base)
    w = open('index.py', 'a')
    w.write("index = " + str(ans))
    w.close()
    # for token in tokens:
    #     os.chdir(base)

    #     f = open('index.py', 'a')

    #     # if unicode(token, "utf-8")[0].isnumeric():
    #     #     f.write("n"+str(token) + " = ")
    #     # else:
    #     #     f.write(str(token) + " = ")

    #     #print str(token)
    #     f.close()

    #     doc_freq = []

    #     for token_file in listdir:
    #         if token_file == "__init__.py":
    #             continue
    #         if ".pyc" in token_file:
    #             continue;
    #         # print token_file
    #         os.chdir(base)
    #         f = open('tfidf.py', 'a')
    #         #print os.getcwd()
    #         exec("from tokens." + token_file[:-3] + " import lis")

    #         # p = open(token_file, 'r')
    #         # t = p.read()
    #         # token_list = t[6:-1]
    #         # token_list = token_list.split(",")
    #         # print token_list

    #         # p.close()
    # #       token_list.sort()

    #         count = 0

    #         for x in lis:
    #             if token == x:
    #                 count+=1
    # #       print count
    #         if count > 0:
    #             term_freq = (token_file, count)
    #             # print term_freq
    #             doc_freq.append(term_freq)

    #     f.write(str(doc_freq))
    #     #if count == 0:
    #     #    f.write(str(empty))
    #     f.write("\n")
    #     f.close()

    # #   f.write("]\n")

    # q.close()

if __name__ == '__main__':
    main()
