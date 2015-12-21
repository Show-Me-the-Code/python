#!/usr/bin/env python
#coding=utf-8

"""用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 """

import requests
from PIL import Image,ImageDraw,ImageFont
from StringIO import StringIO
from bs4 import BeautifulSoup

__author__ = 'tonnytwo'

r = requests.get('http://tieba.baidu.com/p/2166231880')
#r = requests.get('http://ent.ifeng.com/a/20150626/42440289_0.shtml')

string = ''
if r.status_code==200:
    string = r.text
    soup = BeautifulSoup(''.join(string),from_encoding="utf-8")
    content = soup.findAll('img',src=True)
    a=0
    for img in content:

        a=a+1
        src = img["src"]
        print src
        try:
            tempr = requests.get(src)
            if tempr.status_code==200:
                i = Image.open(StringIO(tempr.content))
                i.save("E://temp//"+str(a) + ".jpg", "JPEG")
        except IOError:
            print "error"
            pass



