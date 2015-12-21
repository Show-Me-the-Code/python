#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonnytwo'
"""一个HTML文件，找出里面的正文"""

from bs4 import BeautifulSoup
import requests

def getCon():

    #r = requests.get('https://api.github.com', auth=('user', 'pass'))
    r = requests.get('http://ent.ifeng.com/a/20150626/42440289_0.shtml')
    r.status_code
    string = ''
    if r.status_code==200:
        string = r.text
    #print string
    soup = BeautifulSoup(''.join(string),from_encoding="utf-8")
    content = soup.findAll(['h2','h3','h4','h5', 'p'])
    for con in content:
        print con.string
    #content = soup.body
    # pTag = soup.p
    #content = pTag.contents
    #print str(content)
    # print soup.prettify()
getCon();