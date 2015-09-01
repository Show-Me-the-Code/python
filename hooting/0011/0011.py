# -*- coding: utf-8 -*-
__author__ = 'hooting'
with open('filtered_words.txt','r')as f:
    data = f.read()
    
filter = data.split('\n')

while True:
    text = raw_input("please input:")
    for x in filter:
        if x in text:
            print "Freedom"
            break
    else:
        print "Human Rights"
