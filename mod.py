import os
import math

PATH = "/home/varunwachaspati/Downloads/Information Retrieval /WhatsintheVector/"
SCORES = PATH + "doc_vector/"
os.chdir(PATH)

f  = open("vector_mod.py","w")

dic = {}

lists  = os.listdir(SCORES)

os.chdir(PATH)
for files in lists:
	if ".pyc" in files or "init" in files:
		continue
	# print os.getcwd()
	exec("from doc_vector." + files[:-3] + " import vect")
	score = 0
	for vector in vect:
		score =  score + vector*vector
	score = math.sqrt(score)
	dic[files[:-3]] = score

f.write(str(dic))
f.close()