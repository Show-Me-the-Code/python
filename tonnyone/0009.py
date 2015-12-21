#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonnytwo'
"""一个HTML文件，找出里面的链接。"""
from bs4 import BeautifulSoup
import requests
import re

def getCon():

    #r = requests.get('https://api.github.com', auth=('user', 'pass'))
    r = requests.get('http://www.baidu.com/s?wd=python%20re&rsv_spt=1&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=8&rsv_sug1=6')
    r.status_code
    string = ''
    if r.status_code==200:
        string = r.text
    print string
    for a in  re.finditer(r"http://\w*[\.\w+]+[/\w+]*\?[\w+\=.+&]*[\w+=.+]",string):
    #for a in  re.finditer(r"http://\w*[\.\w+]+[/\w+]*\?.*",string):
        print a.group()
    # for a in re.finditer(r"http://.+",string):
    #     print a.group()
getCon();