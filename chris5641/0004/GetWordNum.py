# -*- coding: utf-8 -*-
"""
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import re
__author__ = 'Chris5641'


def get_num():
    num = 0
    f = open('test.txt', 'r')
    for line in f.readlines():
        num += len(re.findall(r'[a-zA-Z0-9\']+', line))
    f.close()
    return num


if __name__ == '__main__':
    print(get_num())
