#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0008
* by ahwz001
* 2017/8/16
* thanks this project, I learned many very useful Programs.
"""

import requests
from bs4 import BeautifulSoup


test_url = 'http://chuansong.me/n/1983157622806'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

res = requests.get(test_url,headers=headers)

with open("test_html",'w') as fobj:
    fobj.write(res.content)

soup = BeautifulSoup(res.text, 'lxml')

print soup.body.text
