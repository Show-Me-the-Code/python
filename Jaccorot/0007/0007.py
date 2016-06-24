#!/usr/bin/python
#coding:utf-8

"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import os

def walk_dir(path):
    file_path = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.lower().endswith('py'):
                file_path.append(os.path.join(root, f))
    return file_path


def count_the_code(path):
    file_name = os.path.basename(path)
    note_flag = False
    line_num = 0
    empty_line_num = 0
    note_num = 0
    with open(path) as f:
        for line in f.read().split('\n'):
            line_num += 1
            if line.strip().startswith('\"\"\"') and not note_flag:
                note_flag =True
                note_num += 1
                continue

            if line.strip().startswith('\"\"\"'):
                note_flag = False
                note_num += 1

            if line.strip().startswith('#') or note_flag:
                note_num += 1

            if len(line) == 0:
                empty_line_num += 1

    print u"在%s中，共有%s行代码，其中有%s空行，有%s注释"% (file_name, line_num, empty_line_num, note_num)


if __name__ == '__main__':
    for f in walk_dir('.'):
        count_the_code(f)
