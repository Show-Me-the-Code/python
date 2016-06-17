#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。'

__author__ = 'Drake-Z'

import os
import re

def filter_word(a):
    sensitive = False
    strs = '**'
    f = open('filtered_words.txt', 'r', encoding = 'utf-8').readlines()
    for i in f: 
        i = i.strip()                                                           #去除\n
        b = re.split(r'%s' % (i), a)                                      #分解字符串
        if len(b) > 1:
            c = i
            sensitive = True   
        else:
            pass
    if sensitive == True:
        b = re.split(r'%s' % (c.strip()), a)
        print(strs.join(b))
    else:
        print(a)
    return 0

z = input('请输入：')
filter_word(z)