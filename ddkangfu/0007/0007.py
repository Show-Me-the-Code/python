# coding=utf-8

import os
import re

"""
0007：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

def source_statistic(file_name):
    total = 0
    blank = 0
    comment = 0

    with open(file_name) as f:
        lines = f.readlines()
        total += len(lines)

        pattern1 = re.compile(r'^\s*$')
        pattern2 = re.compile(r'^\s*\#+')

        for line in lines:
            if pattern1.match(line):
                blank += 1
            elif pattern2.match(line):
                comment += 1

    return total, blank, comment


def walk_dir(image_path):
    total = 0
    blank = 0
    comment = 0

    for root, dirs, files in os.walk(image_path):
        for f in files:
            if f.lower().endswith('.py'):
                full_path = os.path.join(root, f)
                #resize_image(full_path)
                print full_path
                result = source_statistic(full_path)
                total += result[0]
                blank += result[1]
                comment += result[2]

    return total, blank, comment


if __name__ == '__main__':
    result = walk_dir("source")
    print 'Total Lines: %d, Blank Lines: %d, Comment Lines: %d' % result
