#!/usr/bin/python
# coding=utf-8

"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
"""

import os
import urllib
from bs4 import BeautifulSoup
from urlparse import urlsplit


def catch_tieba_pics(url):
    content = urllib.urlopen(url)
    bs = BeautifulSoup(content, 'lxml')
    for i in bs.find_all('img', {"class": "BDE_Image"}):
        download_pic(i['src'])


def download_pic(url):
    image_content = urllib.urlopen(url).read()
    file_name = os.path.basename(urlsplit(url)[2])
    output = open(file_name, 'wb')
    output.write(image_content)
    output.close()


if __name__ == '__main__':
    catch_tieba_pics('http://tieba.baidu.com/p/2166231880')
