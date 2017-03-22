# -*- coding: utf-8 -*-
"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)[http://tieba.baidu.com/p/2166231880]
"""
import os

import requests
from bs4 import BeautifulSoup

url='http://tieba.baidu.com/p/2166231880'
html =requests.get(url)
soup =BeautifulSoup(html.text,'html.parser')
img_urls=soup.findAll('img',bdwater='杉本有美吧,1280,860')
for img_url in img_urls:
    img_src=img_url['src']
    os.path.split(img_src)[1]
    with open('source/0013/'+os.path.split(img_src)[1],'wb') as f:
        f.write(requests.get(img_src).content)
