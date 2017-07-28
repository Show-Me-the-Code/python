#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0001
* by ahwz001
* 2017/7/22
"""

import random

BASE_STR = '0123456789ABCDEF'

# def random_str(num, length=8 ):    
#     fobj = open('result.txt','w')
#     for i in range(num):
#         s = [random.choice(char) for j in range(length)]
#         fobj.write(''.join(s) + '\n')
#     fobj.close()


def random_str0(num, length=8):
    bill = []
    while len(bill) < num:
        s = [random.choice(BASE_STR) for j in range(length)]
        t = ''.join(s) + '\n'
        if t not in bill:
            # Adding key that are not duplicate.
            bill.append(t)
        else:
            continue        
    # print "*********"
    # print len(bill)
    # print "*********"
    with open('result.txt','w') as fobj:
        fobj.writelines(bill)
    return bill


def main():
    print "the function random_str0(200)(first ten str):"
    test = random_str0(200)
    for j in test[:10]:
        print j,

if __name__ == '__main__':
    main()
    