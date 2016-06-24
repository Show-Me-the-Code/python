#! /usr/bin/env python
#! -*- coding:utf-8 -*-

import random, string
__author__ = 'Sophie'

def randomSequence(r,l):
    s = string.letters + string.digits + '@#$%&*'
    random_seq = []

    # Method_1
    #for i in range(r):
    #    random_seq.append(''.join(random.sample(s,l)))
    #return random_seq

    # Method_2
    sl = list(s)
    print sl
    for i in range(r):
        random.shuffle(sl)
        random_seq.append(''.join(sl[:l]))
    return random_seq

if __name__ == '__main__':
    result = randomSequence(200,8)
    for i in range(len(result)):
        print result[i]