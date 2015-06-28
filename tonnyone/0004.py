#!/usr/bin/env python
#coding=utf-8
'''任一个英文的纯文本文件，统计其中的单词出现的个数。'''
__author__ = 'tonnytwo'

filepath=r"E:/eversec/A_document/python/mit/笔记/9test/filescan.py"
upath = unicode(filepath,'utf8')
f = open(upath,'r')
a = (word for line in f for word in line.split())
dict={}
for b in a:
    if b not in dict:
        dict[b] = 1
    else:
        dict[b]=dict[b] + 1

for k in dict:
    print k,dict[k]