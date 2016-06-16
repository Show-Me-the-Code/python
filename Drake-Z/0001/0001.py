#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）'

__author__ = 'Drake-Z'

import random

def rndChar(filename, digit=4, num=200):
    f = open(filname, 'a')
    a = 0
    for i in range(1, 201):
        while a < 4:
            f.write(chr(random.randint(65, 90)))
            a += 1
        f.write('\n')
    f.close()
    print('Done!')
    return 0

if __name__ == '__main__':
    filname = 'activecode.txt'
    digit = 4
    num = 200
