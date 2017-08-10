#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0006
* by ahwz001
* 2017/8/10
* thanks this project, I learned some very useful Program.
* Please refer to the project folder AK-wang, I learned this code from that and write some comments.
"""

import glob
import re
import os
from collections import Counter


def list_txt():
    """get the *.txt file list,and return it.
    This is the Elegant and concise code."""
    return glob.glob("*.txt")

# def list_txt():
#     """another version of function list_txt, it is not the best, however it works well, and I write the code by myself.
#     the feel is wonderful!"""
#     res = []
#     for i in os.listdir('.'):
#         if i.endswith('.txt'):
#             res.append(i)
#     return res


def word_count(filename):
    """count how times of every word in a file happens.
    And return the most common one."""
    data_list = []
    with open(filename) as fobj:
        for line in fobj:
            content = re.sub("\"|,|\.","",line)
            te = content.strip().split()
            data_list.extend(te)
    # print data_list
    result = Counter(data_list)
    # an object like dict, but more Convenient
    return result.most_common(1)


def most_comm():
    all_txt = list_txt()
    for txt in all_txt:
        print word_count(txt)


if __name__ == '__main__':
    most_comm()
    # print map(word_count,list_txt())
