#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-13 11:11:49
# @Last Modified by:   30987
# @Last Modified time: 2015-01-13 17:10:27

import re

def hot_words(file_path):
	file = open(file_path,'r')
	file_content = file.read()
    p = re.compile(r'[\W\d]*')
    word_list = p.split(file_content)

    word_dict = {}
    for word in word_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sort = sorted(word_dict.items(), key=lambda e: e[1], reverse=True)
	sort = sorted(word_dict.items(), key=lambda e: e[1], reverse=True)

	print("The most word in '%s' is '%s',it appears '%s' times" % (file_path,sort[1][0], sort[1][1]))

	file.close()


if __name__ == '__main__':
	hot_words('test.txt')