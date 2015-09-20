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
	#f = open('output.py', 'a')
	#f.write('tokens = [')
        #f.close()
        errors = []

        for dire in list_dir:
		currdir = base + dire
                if 'output.py' in currdir:
                    continue
                os.chdir(currdir)

		list_file = os.listdir(currdir)

                for fil in list_file:
                        print "\n\n" + "trying for file, " + currdir+ "/" + fil +"\n\n"
                        os.chdir(currdir)
                        try:
                            f = codecs.open(fil, 'r', encoding='utf8')
			    t = f.read()
                        except:
                            errors.append(currdir+"/"+fil)
                            continue
                        temp_tokens = word_tokenize(t)
			temp_tokens = [porter.stem(tok).lower() for tok in temp_tokens]
			temp_tokens = [tok for tok in temp_tokens if tok not in stopwords.words('english')]
                        temp_tokens = [tok for tok in temp_tokens if tok not in ';@#$%^&*()_+=-<>?|: ,./!``~\'\'s"[]{\\}']
                        tokens.append(temp_tokens)
			f.close()
			#print temp_tokens
                        os.chdir(base)
                        temp_tokens = set(temp_tokens)
                        temp_tokens = list(temp_tokens)

                        temp2 = []
                        for toks in temp_tokens:
                            if toks not in tokens:
                                temp2.append(toks)

                        tokens += temp2
                        w = open('output.py', 'a')
                        for tok in temp2:
                            w.write(" " + tok.encode('ascii', 'ignore'))
                        w.close()

                        os.chdir(currdir)
        os.chdir(base)
        f.open('errors', 'w')
        for x in errors:
            f.write(x)

        f.close()
if __name__ == "__main__":
	main()
