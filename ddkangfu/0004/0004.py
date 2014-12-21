#coding=utf-8

import collections
import re

"""
0004, 任一个英文的纯文本文件，统计其中的单词出现的个数。
"""


def count_word(file_name):
    f = open(file_name)

    line = f.readline()
    word_counter = collections.Counter()

    while line:
        words = re.findall("\w+", line.lower())
        word_counter.update(words)
        
        line = f.readline()

    f.close()

    return word_counter


if __name__ == '__main__':
    print count_word('english.txt')