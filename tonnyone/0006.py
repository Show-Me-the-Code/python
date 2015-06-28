#!/usr/bin/env python
#coding=utf-8

"""你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。"""
__author__ = 'tonnytwo'

filist=["to","today","is","my","you",'he',"she","good","nice"]
dict={}
def importWord(path):
    f = open(path,'r')
    words = (word for line in f for word in line.split())
    for w in words:

        w = w.lower()
        if w not in filist:
            if w not in dict:
                dict[w]=1
            else:
                dict[w]=dict[w]+1

    count=0
    keyword = ""
    for w in dict:
        if(dict[w]>count):
            count = dict[w]
            keyword = w
    print keyword
    #print dict[keyword]

importWord("D:/Python32/MySQL-python-wininst.log")
