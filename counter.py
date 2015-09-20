import os
from sorted_output import tokens

def main():
    base = "/home/varunwachaspati/Downloads/Information Retrieval /WhatsintheVector/"
    os.chdir(base)

    f = open('tfidf.py', 'a')
    
    for token in tokens:
    	print token
    	os.chdir(base + 'tokens/')
        
        listdir = os.listdir(base + 'tokens/')
        f.write(str(token) + " = ")
        
        for token_file in listdir:
        	exec("from " + token_file + " import lis")

        	print lis
        	# p = open(token_file, 'r')
        	# t = p.read()
        	# token_list = t[6:-1]
        	# token_list = token_list.split(",")
        	# print token_list

        	# p.close()
    #     	token_list.sort()
        	
    #     	count = 0
        	
    #     	for x in token_list:
    #     		print token[1:-1] + " " + x[3:-1] 
    #     		if token[1:-1] == x[2:-1]:
    #     			count+=1
    #     	print count
    #     	if count > 0:
    #     	    f.write("(" + str(token_file) + "," + str(count)+")"+",")
        

    # 	f.write("]\n")
    
    # f.close()
    # q.close()

if __name__ == '__main__':
    main()
