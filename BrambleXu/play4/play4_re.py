# -*- coding:utf-8 -*-
#**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def count_words(file_path):
    f = open(file_path, 'rb')
    text = f.read()
    words = re.findall(r'[a-zA-Z0-9]+', text)
    return len(words)

if __name__ == '__main__':
    count = count_words('text.txt')
    print "the number of words in the file is: %s" % count
