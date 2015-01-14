#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jinyang'


def calcWords(path):
    file = open(path, 'r')
    inputStr = file.read()
    wordsNum = 0
    for i in inputStr:
        if i == ' ' or i == '\n':
            wordsNum += 1

    file.close()
    print wordsNum + 1

if __name__ == '__main__':
    calcWords('input.txt')
