#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0001
* by ahwz001
* 2017/7/22
"""

import random

char = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def random_str(num, length=8 ):    
    fobj = open('result.txt','w')
    for i in range(num):
        s = [random.choice(char) for j in range(length)]
        fobj.write(''.join(s) + '\n')
    fobj.close()


def random_str0(num, length=8):
    bill = []
    for i in range(num):
        s = [random.choice(char) for j in range(length)]
        t = ''.join(s) + '\n'
        bill.append(t)        
    with open('result0.txt','w') as fobj:
        fobj.writelines(bill)
    return bill


def main():
    print "the function random_str(200)(first ten str):"
    random_str(200)
    with open('result.txt') as fn:
        t = [ line for line in fn]
        for i in t[:10]:
            print i,
    print '\n'
    print "the function random_str0(200)(first ten str):"
    test = random_str0(200)
    for j in test[:10]:
        print j,

if __name__ == '__main__':
    main()
    