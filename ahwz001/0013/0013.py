#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0013
* by ahwz001
* 2017/8/16
* Thanks for this project. I learned a lot here.
"""

import requests
import time
from lxml import etree

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


def get_links(url):
    """get the img links and return as a list."""
    links = []
    res = requests.get(url,headers=header).content
    s = etree.HTML(res)
    for i in s.xpath('//img/@src'):
        if i.startswith('http') and i.endswith('.jpg'):
            links.append(i)
    # print links[:3]
    return links


def save_imgs(bill):
    """save imgs to current dir"""
    print "the total imgs is %d" % len(bill)
    print "Start to download the imgs......"
    count = 0
    for i in bill[:5]:
        name = str(count).zfill(4) + '.jpg' # 图片名称
        response = requests.get(i,headers=header)
        with open(name,'w') as fn:
            fn.write(response.content)
        count += 1
        print("Download the %d img" % count)
        # time.sleep(1)


def main():
    url = 'http://tieba.baidu.com/p/2166231880'
    # url = 'http://tieba.baidu.com/p/1165861759'
    bill = get_links(url)
    save_imgs(bill)


if __name__ == '__main__':
    main()
