import codecs
from  nltk import stem, word_tokenize
from nltk.corpus import stopwords
import os

def main():
	base = '/home/psd/Downloads/19cTexts/'
	porter = stem.porter.PorterStemmer()
	os.chdir(base)

	list_dir = os.listdir(base)

	print list_dir

	tokens = []

        os.chdir(base)
	f = open('output.py', 'w')
	#f.write('tokens = [')
        f.close()

        for dire in list_dir:
		currdir = base + dire
                if 'output.py' in currdir:
                    continue
                os.chdir(currdir)

		list_file = os.listdir(currdir)

                for fil in list_file:
			f = codecs.open(fil, 'r', encoding='utf8')
			t = f.read()
                        temp_tokens = word_tokenize(t)
			temp_tokens = [porter.stem(tok) for tok in temp_tokens]
			temp_tokens = [tok for tok in temp_tokens if tok not in stopwords.words('english')]
                        temp_tokens = [tok for tok in temp_tokens if tok not in ';@#$%^&*()_+=-<>?|: ,./!``~\'\'s"[]{\\}']
                        tokens.append(temp_tokens)
			f.close()
			print temp_tokens
                        os.chdir(base)

                        w = open('output.py', 'w+')
                        for tok in temp_tokens:
                            w.write(" " + tok.encode('ascii', 'ignore'))
                        w.close()
                        
                        os.chdir(currdir)
        os.chdir(base)
	f = open('output.py', 'w')
	f.write('tokens = ')
	f.write(tokens)

if __name__ == "__main__":
	main()
