# -*- coding:utf-8 -*-
#**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
'''
In this file, I want to count how many time each word showed in a text
function:
clean_file: input is the file path, output is a list contain every words in the file.
A word may show many time.
like this -> ['This', 'module', 'implements', 'specialized', 'container', 'datatypes', 'providing', 'alternatives', 'to', 'Python\xe2\x80\x99s', 'general', 'purpose', 'builtin', 'containers', 'dict', 'list', 'set', 'and', 'tuple', 'In', 'addition', 'to', 'the', 'concrete', 'container', 'classes', 'the', 'collections', 'module', 'provides', 'abstract', 'base', 'classes', 'that', 'can', 'be', 'used', 'to', 'test', 'whether', 'a', 'class', 'provides', 'a', 'particular', 'interface', 'for', 'example', 'whether', 'it', 'is', 'hashable', 'or', 'a', 'mapping', 'In', 'some', 'ways', 'the']

count_words: use Counter class to get a dict telling us how many time a word showed

'''

import string # used to clean the file
from collections import Counter
#import re

def count_words(file_path):
    processed_file = clean_file(file_path)
    #print processed_file
    word_dict = Counter(processed_file)
    print word_dict

def clean_file(file_path):
    with open(file_path, 'r') as f:
        #i = 0
        file_as_list = []
        for line in f.readlines():
            if line != "\n":
                #print i
                file_as_list.extend(line.strip().translate(None, string.punctuation).split().lower())
    return file_as_list

if __name__ == '__main__':
    counts = count_words('text.txt')
    #print "the number of words in the file is: %s" % counts
    #print "the number of words in the file is: %s" % counts.most_common(10)
