# coding=utf-8

import urllib2

from bs4 import BeautifulSoup

"""
0008:一个HTML文件，找出里面的正文。
"""


def show_content(url, content_tag, content_tag_class):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)
    for tag in  soup.find_all(content_tag, content_tag_class):
        print tag.text


if __name__ == '__main__':
    show_content('http://v2ex.com/t/157721#reply10', 'div', 'topic_content')
