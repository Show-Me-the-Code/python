#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'natezhang93'

'''
    第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
    当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''
import string

class Filter:
    def __init__(self):
        self.data = []
        try:
            with open("filtered_words.txt", 'r') as fin:
                self.data = (fin.read().splitlines())
                fin.close()
        except:
            raise IOError

    def check(self, checkword):
        result = ""
        for word in self.data:
            temp = string.replace(checkword, word, "**")
            if temp != checkword:
                result = temp
        if not result:
            result = checkword
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