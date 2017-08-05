#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0007
* by ahwz001
* 2017/8/4
* thanks this project, I learned some very useful Program.
"""

import os

total_lines = 0
empty_lines = 0
comment_lines = 0


def process_file(fn):
    global total_lines
    global empty_lines
    global comment_lines
    with open(fn) as fobj:
        for line in fobj:
            total_lines += 1
            if line.strip() == '':
                empty_lines += 1
            elif line.startswith('#'):
                comment_lines += 1
            else:
                pass


def process_dir(dir):
    bill = os.listdir(dir)
    os.chdir(dir)
    print "the current dir is :\n%s" % os.getcwd()
    for i in bill:
        if i.endswith('.py'):
            process_file(i)


def main():
    process_dir('test_files')
    print "the total lines is: %d" % total_lines
    print "the empty lines is %d" % empty_lines
    print "the comment lines is: %d" % comment_lines


if __name__ == '__main__':
    main()