#!/usr/bin/env python3
#get the most important word in the text

import os, re
from pprint import pprint

def most_important_word(f):
    #get the count of words in the text
    res = {}
    content = f.read()
    tmp = re.split(r"[^a-zA-Z]",content)
    for w in tmp:
        if not w:
            continue
        w = w.lower()
        if w not in res:
            res[w] = 1
        else:
            res[w] += 1

    #get the word of most importance
    res['']=0
    max = ''
    for i in res:
        if res[i] > res[max]:
            max = i
    return max

def main():
    res = {}
    os.chdir('test')
    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            with open(file,'r') as f:
                res[f.name]=most_important_word(f)
    return res

if __name__ == "__main__":
    res = main()
    pprint(res)
