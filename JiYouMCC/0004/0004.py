# -*- coding: utf-8 -*-
# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
import io
import operator


def get_count_table(file='0004.txt', ignore=[',', '.', ':', '!', '?', '”', '“', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], lower=True):
    txt = open(file).read()
    for i in ignore:
        txt = txt.replace(i, ' ')
    if lower:
        txt = txt.lower()
    words = txt.split(' ')
    dic = {}
    for word in words:
        if word is '':
            continue
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic


result = sorted(
    get_count_table().items(), key=operator.itemgetter(1), reverse=True)
for item in result:
    print item[0], item[1]
