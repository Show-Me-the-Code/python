#! /usr/bin/env python
#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright By PyLyria
# CreateTime: 2016-03-01 23:04:58

import re
from string import punctuation
from operator import itemgetter

def remove_punctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()

def split(file_name):
    with open(file_name,'rt') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            yield re.split(r'[;,\s]\s*', line)

if __name__ == '__main__':
    word2count = {}
    for line in split('chapter1.txt'):
        words = (remove_punctuation(word) for word in line)
        for word in words:
            word2count[word] = word2count.get(word, 0) + 1
    sorted_word2count = sorted(word2count.items(),key=itemgetter(0))
    print(sorted_word2count)
