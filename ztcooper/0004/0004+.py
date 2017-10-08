#用nltk做了一下

from nltk.tokenize import word_tokenize
from nltk.probability import *

with open('whenyouareold.txt') as f:
    text = f.read()
    
tokens = word_tokenize(text.lower())
puncs = [',','.',';']
clean = [token for token in tokens if token not in puncs]
freq = FreqDist(clean)

with open('result2.txt', 'w') as f:
    for k, v in freq.items():
        f.write(str(k)+':'+str(v)+'\n')
