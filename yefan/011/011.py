#!/bin/env python
# -*- coding: utf-8 -*- 
import codecs
def read_txt():
    l=[]
    with codecs.open(r'c:\python27\oneday_one\1.txt') as fp:
        for line in fp.readlines():
           l.append(line.strip())
    return l

def check(l):
    word=raw_input('word:')
    for each_word in l:
        if word==each_word:
            print 'Freedom'
            return None
    print 'Human rights'
    return None

def main():
    l=read_txt()
    check(l)
    print l

if __name__=='__main__':
    main()
    
    
