#!/usr/bin.env python

import os


def main():
    f = open('code.cpp')
    blanks = 0
    comments = 0
    lines = 0

    for line in f.readlines():
        if len(line.split()) == 0:
            blanks += 1
        elif line.startswith("//"):
            comments += 1
        elif line.startswith("/*"):
            comments += 1

        lines += 1

    print 'blank lines', blanks
    print 'comment lines', comments
    print 'all lines', lines


if __name__ == '__main__':
    main()