#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'natezhang93'

'''
    第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
    当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''

class Filter:
    def __init__(self):
        self.data = []
        try:
            with open("filtered_words.txt", 'r') as fin:
                self.data = (fin.read().splitlines())
                fin.close()
        except:
            raise IOError

    def check(self, word):
        try:
            self.data.index(word)
            result = 'Freedom'
        except:
            result = 'Human Rights'
        return result

def main():
    try:
        fil = Filter()
    except:
        print "ERROR OPENING FILE"
        return

    while True:
        word = raw_input("> ")
        word = fil.check(word)
        print word

if __name__ == "__main__":
    main()