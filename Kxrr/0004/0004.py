#!/usr/bin/env python
# encoding: utf-8
__author__ = 'Kxrr'

import re

with open('0004.txt', 'r') as f:
    dictResult = {}

    # Find the letters each line
    for line in f.readlines():
        listMatch = re.findall('[a-zA-Z]+', line.lower()) # remember to lower the letters

    # Count
        for eachLetter in listMatch:
            eachLetterCount = len(re.findall(eachLetter, line.lower()))
            dictResult[eachLetter] = dictResult.get(eachLetter, 0) + eachLetterCount

    # Sort the result
    result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)
    for each in result:
        print each