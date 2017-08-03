#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0004
* by ahwz001
* 2017/8/3
* thanks this project, I learned some very useful Program.
"""

import string


def process_file(filename):
    """open a file,and call process_line() by line."""
    hist = dict()
    with open(filename) as fobj:
        for line in fobj:
            process_line(line, hist)
    return hist


def process_line(line, hist):
    """process line,and count every word."""
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


def most_frequent(hist):
    """save the histgrom to a list,and sort it, return the it."""
    res = []
    for x, freq in hist.iteritems():
        res.append((freq, x))
    res.sort(reverse=True)
    return res


def main():
    hist = process_file('test_text.txt')
    print "the top 10 is :"
    t = most_frequent(hist)
    print t[:10]


if __name__ == '__main__':
    main()