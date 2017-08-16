#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0009
* by ahwz001
* 2017/8/16
* Thanks for this project. I learned a lot here.
"""

import requests
from bs4 import BeautifulSoup


def get_links(html):
    """get the links in a html and return as a list."""
    url_base = "http://chuansong.me"
    res = []
    soup = BeautifulSoup(html, 'lxml')
    for tag in  soup.find_all('a'):
        if tag['href'].startswith("http"):
            res.append(tag['href'])
        elif tag['href'].startswith('/n') or tag['href'].startswith('/account'):
            t = url_base + tag['href']
            res.append(t)
        else:
            continue
    return res


def main():
    test_url = 'http://chuansong.me/n/1983157622806'
    headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res = requests.get(test_url,headers=headers)    
    for link in get_links(res.content):
        print link


if __name__ == '__main__':
    main()


