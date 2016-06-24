#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-18 21:38:31
# @Last Modified by:   key
# @Last Modified time: 2015-11-18 21:58:29

'''
第 0009 题：一个HTML文件，找出里面的链接。
'''

import requests as req
from bs4 import BeautifulSoup

url = "https://github.com/keysona/show-me-the-code"

response = req.get(url=url)

soup = BeautifulSoup(response.content,"lxml")

urls = [a_tag.get('href') for a_tag in soup.find_all('a') if a_tag.get('href').startswith('http')]

print(urls)
