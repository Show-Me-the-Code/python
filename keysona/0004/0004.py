#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-17 14:15:01
# @Last Modified by:   key
# @Last Modified time: 2015-11-17 17:26:46

#--------------------------------
#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
#--------------------------------


from collections import Counter

def words():
    c = Counter()
    with open('test.txt') as f:
        for line in f:
            c.update(line.split(' '))
    return sum(c.values())

if __name__ == '__main__':
    print(words())

