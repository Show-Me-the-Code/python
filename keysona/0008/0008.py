#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-18 21:26:32
# @Last Modified by:   key
# @Last Modified time: 2015-11-18 21:58:46

'''
第 0008 题：一个HTML文件，找出里面的正文。
'''


import requests as req
from bs4 import BeautifulSoup

url = "https://github.com/keysona/show-me-the-code"

response = req.get(url=url)

soup = BeautifulSoup(response.content,"lxml")

print(soup.article)




