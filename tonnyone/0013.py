#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonnytwo'

def isSensitive(str,filterlist):
    if str in filterlist:
        return True
    else:
        return False

def Test():
    f = open("./filtered_words.txt","r")
    filterlist = []
    for a in f:
        filterlist.append(a.strip().decode("utf-8"))

    print filterlist
    while True:
        input = raw_input("please input a sentense:")
        for keywork in filterlist:
            unicodeinput = input.decode("utf-8")
            if keywork in unicodeinput:
                print unicodeinput.replace(keywork,len(keywork)* "*")
                #print unicodeinput

Test()