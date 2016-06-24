#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。'

__author__ = 'Drake-Z'

import os
import re
import glob
from collections import OrderedDict

def get_num(key_word, filename):
    '''获得词汇出现次数'''
    f = open(filename, 'r', encoding='utf-8').read()
    re_zhengze = re.compile(r'[\s\,\;\.\n]{1}'+key_word+r'[\s\,\;\.\n]{1}')
    numbers = re_zhengze.findall(f)
    return len(numbers)

def article_analysis(dirs):
    article = glob.glob(r'*.txt')
    dictdata = OrderedDict()
    for m in article:
        doc = open(m, 'r', encoding='utf-8').read()
        doc = re.findall(r'[\w\-\_\.\']+', doc)                    #获得单词list
        doc = list(map(lambda x: x.strip('.'), doc))            #去除句号
        for n in doc:
            dictdata[n] = get_num(n, m)
        a = OrderedDict(sorted(dictdata.items(), key=lambda x: x[1], reverse = True))   #dict排序
        print('在 %s 中出现次数最多的单词是：' % m)
        for c in a:
            print(c+' : %s 次' % a[c])
            break
    return 0

if __name__ == '__main__':
    file = '.'
    article_analysis(file)
