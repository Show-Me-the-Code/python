# 统计代码行数，空行数，注释行数
import os
import sys
sys.path.append('..')
from collections import Counter
from pprint import pprint
from q0005.q0005 import find_suffix


def count_lines(*data):
    cl = {}
    for fn in data:
        c = Counter()
        file_name = os.path.splitext(os.path.basename(fn))[0]
        with open(fn) as fp:
            for i in fp.readlines():
                if i.startswith('#'):
                    c['comment'] += 1
                if not i.strip():
                    c['blank'] += 1
                c['text'] += 1
        cl.update({file_name: c})
    return cl


def summary(**data):
    c = Counter()
    for fn in data:
        for k in data[fn]:
            c[k] += data[fn][k]
    return c


if __name__ == '__main__':
    file_list = find_suffix('.', ['.py'])
    c = count_lines(*file_list)
    s = summary(**c)
    print('\t\t---- I\'m summary ----')
    print(s)
    print('\t\t--- I\'m details ----')
    pprint(c)
