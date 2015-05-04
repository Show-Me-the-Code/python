#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 17-03-15
# Author: Liang

'''
第 0007 题：
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来.
'''

'''
Not to specific code files yet, like "py", "cpp" .etc.
Not consider different comment methods like ''' ''' yet.
Not consider sub-directory yet.
'''

import os

# set codes path
codes_path = "codes/"


def line_counter(dir):
    codes = os.listdir(dir)
    code_lines = 0
    empty_lines = 0
    comment_lines = 0
    for i in codes:
        with open(dir + i) as code_file:
            codes_lines = code_file.readlines()

            for line in codes_lines:
                line = line.strip()
                if line.startswith("#"):
                    comment_lines += 1
                elif line == "":
                    empty_lines += 1
                else:
                    code_lines += 1
    print("There are " +
          str(code_lines) + " code lines, " +
          str(comment_lines) + " comment lines, and " +
          str(empty_lines) + " empty lines.")

if __name__ == '__main__':
    line_counter(codes_path)
