#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright By PyLyria
# CreateTime: 2016-03-03 20:51:40
import os
import re
import math
import heapq
from string import punctuation
from operator import itemgetter

def remove_punctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()

def split(file_name):
    with open(file_name,'rt',encoding='utf-8') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            yield re.split(r'[;,\s]\s*', line)

def get_path(root = os.curdir):
    root += os.sep
    for path, dirs, files in os.walk(root):
        for file_name in files:
            yield path, file_name

def get_tf(file_name):
    word2count = {}
    for line in split(file_name):
        words = (remove_punctuation(word) for word in line)
        for word in words:
            word2count[word] = word2count.get(word, 0) + 1
    total = sum(word2count.values())
    TF = {key : (value, value / total) for (key, value) in word2count.items()}
    return TF

def get_IDF(total_TF):
    IDF = {}
    for file_name in total_TF.keys():
        for keyword in total_TF[file_name].keys():
            IDF[keyword] = IDF.get(keyword, 0) + 1
    IDF = {keyword: math.log(len(total_TF)/IDF[keyword], 2) for keyword in IDF.keys()}
    return IDF

def get_weight(TF, IDF):
    weight = {key:TF[key][1]*IDF[key] for key in TF}
    return weight

if __name__ == '__main__':
    paths = get_path()
    format = ('.txt')
    total_TF = {}
    word_weight = {}

    for path, file_name in paths:
        if file_name.endswith(format):
            total_TF[file_name] = get_tf(path + os.sep + file_name)

    IDF = get_IDF(total_TF)

    for file_name in total_TF.keys():
        word_weight[file_name] = get_weight(total_TF[file_name], IDF)
        print(heapq.nlargest(5, word_weight[file_name].items(), key=itemgetter(1)))
