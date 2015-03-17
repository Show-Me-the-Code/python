#! /usr/bin/env python
#coding:utf-8

import urllib,re

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_img(html):
    #这里其实一句就可以了，当然整体代码水平比我高太多了，如此精简
    imglist = re.findall(r'src="(.*?\.jpg)" bdwater=', html)
    i = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg'%i)
        i+=1
html = get_html('http://tieba.baidu.com/p/2166231880')
print get_img(html)