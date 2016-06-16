#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）'

__author__ = 'Drake-Z'

import random

def randChar(filename, digit=4, num=200):
    f = open(filename, 'a')
    for i in range(0, num):     
        for m in range(0, digit):
            f.write(chr(random.randint(65, 90)))
        f.write('\n')
    f.close()
    print('Done!')
    return 0

if __name__ == '__main__':
    filename = 'active_code.txt'
    digit = 4
    num = 200
    rndChar(filename, digit, num)