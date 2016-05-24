#!/usr/local/bin/python
#coding=utf-8
__author__ = 'Dineshkarthik'

#0004 Title: any of a plain text file in English, statistics on the number of words appears.

import pandas as pd
import re

def word_count(file_path):
    word_string = [line.rstrip('\n') for line in open(file_path)]
    words = []
    for word in word_string:
        tt = word.lower()
        t=re.sub(r'[^\w]', ' ', tt)
        for word in t.split():
            words.append(word)

    p = pd.Series(words)
    #get the counts per word
    freq = p.value_counts()
    #how many max words do we want to give back
    freq = freq.ix[0:25]
    print freq
if __name__ == '__main__':
    word_count("input.txt")
           