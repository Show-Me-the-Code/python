# -*- coding: utf-8 -*-

import re

def count(filepath):
    f = open(filepath, 'rb')
    s = f.read()
    words = re.findall(r'[a-zA-Z0-9]+', s)
    return len(words)

if __name__ == '__main__':
    num = count('count_test.txt')
    print num
