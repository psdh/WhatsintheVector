from sorted_output import tokens
from index import index 

def main():
	print "import done	"
	for tok in tokens:
		print tok
		try:
			a = index[tok]
		#print tok
		except KeyError:
			continue 
		nl = []
		starter = a[0]
		i = 1
		if len(a) == 1:
			nl.append((starter, 1))
		counter = 1
		while i < len(a):
			if a[i] == starter:
				counter += 1
				i += 1
			else:
				nl.append((a[i-1], counter))
				counter = 1
				starter = a[i]
				i += 1
			
		index[tok] = nl

	f = open('index2.py', 'w')
	f.write("index = " + str(index))
	f.close()

if __name__ == '__main__':
	main()