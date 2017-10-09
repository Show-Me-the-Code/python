import os
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

files = os.listdir(os.curdir)
for file in files:

	if os.path.splitext(file)[1] == '.txt':
		with open(file) as f:
			text = f.read()

			tokens = word_tokenize(text.lower())
			sw = stopwords.words('english')
			puncs = [',', '.', ';', ':', '"',"''"]
			clean = [token for token in tokens if (token not in sw) and (token not in puncs)]

			freq = FreqDist(clean)
			m = max([v for v in freq.values()])

			for k,v in freq.items():
				if v == m:
					target = k

			with open('result.txt','a') as w:
				w.write(os.path.splitext(file)[0]+" : "+target+'\n')