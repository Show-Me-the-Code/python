# coding=utf-8

import urllib2

from bs4 import BeautifulSoup

"""
0009:一个HTML文件，找出里面的链接。
"""


def show_href(url):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)
    for tag in  soup.find_all('a'):
        print tag['href']


if __name__ == '__main__':
    show_href('http://v2ex.com/t/157721')
