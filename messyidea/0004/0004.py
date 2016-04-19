#!/usr/bin/env python
# coding=utf-8

filename = 'input.txt'
dict = {}
f = open(filename, 'r')
for eachLine in f:
    temp = eachLine.split()
    for i in temp:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

#print dict
for key in dict:
    print key, dict[key]
