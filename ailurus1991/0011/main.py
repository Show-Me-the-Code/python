#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jinyang'


def readFile(filePath):
    file = open(filePath, 'r')
    words = []
    for word in file.readlines():
#        print word.strip('\n')
        words.append(word.strip('\n'))

    return words

def check(testWord):
    realWords = readFile('filtered_words.txt')
    for i in realWords:
        if i == testWord:
            print 'Freedom'
            return
    else:
        print 'Human Rights'
        return

if __name__ == '__main__':
    check('sss')