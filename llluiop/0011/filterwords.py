#!/usr/bin/env python

import os



def Words(path):
    filterwords = []
    f = open(path)
    for word in f.readlines():
        filterwords.append(word.strip('\n'))

    return filterwords


if __name__ == '__main__':
    filteredwords = Words('filtered_words.txt')

    while(True):
        input = raw_input("input your line:").split()

        if set(input).intersection(filteredwords):
                print 'Freedom'
        else:
            print 'Human Rights'


