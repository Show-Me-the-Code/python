#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonnytwo'

def isSensitive(str,filterlist):
    if str in filterlist:
        print "FreeDom"
    else:
        print "Human Rights"

def Test():
    f = open("./filtered_words.txt","r")
    filterlist = []
    for a in f:
        filterlist.append(a.strip().decode("utf-8"))

    print filterlist
    while True:
        input = raw_input("please input a sentense:")
        print input.decode("utf-8")
        isSensitive(input.decode("utf-8"),filterlist)

Test()