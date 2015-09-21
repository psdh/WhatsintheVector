import os
from index2 import index
from sorted_output import tokens

def main():
	os.chdir('./indices/')
	for tok in tokens:
		f = open(tok + ".py", 'w')
		print tok
		try:
			a = index[tok]
		except:
			f.write("ii = []")
			f.close()
			continue
		f.write("ii = " + str(a))
		f.close()

if __name__ == '__main__':
	main()