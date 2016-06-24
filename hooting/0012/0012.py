# -*- coding: utf-8 -*-
__author__ = 'hooting'
with open('filtered_words.txt','r')as f:
    filter = [line.rstrip() for line in f]

while True:
    text = raw_input("please input:")
    for x in filter:
        if x in text:
            print len(x)
            text = text.replace(x, '*'*len(x))
    print text
