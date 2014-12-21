# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-07
# Python 3.4

"""

第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

"""

import sys


def word_count(file_path):
    file_object = open(file_path, 'r')

    word_num = 0
    for line in file_object:
        line_list = line.split()
        word_num += len(line_list)

    file_object.close()
    return word_num

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter. Try to execute 'python 0004.py $image_path'")
    else:
        for infile in sys.argv[1:]:
            try:
                print("The total number of words is ", word_count(infile))
            except IOError:
                print("Can't open file!")
                pass

