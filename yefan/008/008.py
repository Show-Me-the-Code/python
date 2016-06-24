#!/usr/bin/python
#coding=utf-8

"""
第 0008 题：一个HTML文件，找出里面的正文。
"""

from bs4 import BeautifulSoup

def find_the_content(path):
    with open(path) as f:
        text = BeautifulSoup(f, 'lxml')
        content = text.get_text().strip('\n')

        return content.encode('gbk','ignore')


if __name__ == '__main__':
    print find_the_content(r'D:\Show-Me-the-Code_show-me-the-code_1.html')
