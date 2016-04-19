#!/usr/bin/env python

import os


def DiaryFiles(path):
    if os.path.exists(path):
        for file in os.listdir(path):
            if 'diary' in file:
                yield os.path.join(path, file)

def CalcWords(file, dict1):
    f = open(file)
    for line in f.readlines():
        for word in line.split():
            if word in dict1.keys():
                dict1[word] += 1
            else:
                dict1[word] = 1

def Words(path):
    dict1 = {}
    for file in DiaryFiles(path):
        CalcWords(file, dict1)

    maxvalue =  max(dict1.values())

    for key in dict1:
        if dict1[key] == maxvalue:
            print key,':', maxvalue



if __name__ == '__main__':
    Words('diary')

