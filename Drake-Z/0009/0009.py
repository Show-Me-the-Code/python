#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0009 题：一个HTML文件，找出里面的链接。'

__author__ = 'Drake-Z'

import re

def analysis(a):
    b = re.findall(r'href="(http://.*?.zhihu.com/.*?)"', a)         #以知乎为例
    for i in b:
        print(i)

if __name__ == '__main__':
    with open('testzhihu.html', encoding='utf-8') as html:
        analysis(html.read())