#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。'

__author__ = 'Drake-Z'

import os
import re

def filter_word(a):

    f = open('filtered_words.txt', 'r', encoding = 'utf-8').read()
    if a == '':
        print('Human Rights !')  
    elif len(re.findall(r'%s' % (a), f)) == 0:
        print('Human Rights !')                 #非敏感词时，则打印出 Human Rights !
    else:
        print('Freedom !')              #输入敏感词语打印出 Freedom !

z = input('请输入词语：')
filter_word(z)