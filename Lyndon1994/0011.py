# -*- coding: utf-8 -*-
"""
第 0011 题：
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
"""
word_filter=set()
with open('source/0011/filtered_words.txt') as f:
    for w in f.readlines():
        word_filter.add(w.strip())

while True:
    s=input()
    if s == 'exit':
        break
    if s in word_filter:
        print('Freedom')
    else:
        print('Human Rights')
