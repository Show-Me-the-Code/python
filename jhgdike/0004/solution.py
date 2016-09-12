# coding: utf-8

import re
from collections import Counter


def word_count(txt):
    word_pattern = r'[a-zA-Z-]+'
    words = re.findall(word_pattern, txt)
    return Counter(words).items()

if __name__ == '__main__':
    txt = open('test.txt', 'r').read().lower()
    print word_count(txt)
