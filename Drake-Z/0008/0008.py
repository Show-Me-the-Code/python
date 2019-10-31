#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0008 题：一个HTML文件，找出里面的正文。'

__author__ = 'Drake-Z'

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    in_zhengwen = False
    in_huanhang = False
    def handle_starttag(self, tag, attrs):
        if ('class', 'zh-summary summary clearfix') in attrs and tag=='div' :
            self.in_zhengwen = True
        elif ('class', 'zm-editable-content clearfix') in attrs and tag=='div' :
            self.in_zhengwen = True
        elif tag=='br':
            print('\n')
        else:
            self.in_zhengwen = False

    def handle_data(self, data):
        if self.in_zhengwen:
            print(data.strip())
        else:
            pass

if __name__ == '__main__':
    parser = MyHTMLParser()
    f = open('test.html', 'r', encoding = 'utf-8').read()
    parser.feed(f)