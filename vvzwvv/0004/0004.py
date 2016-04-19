#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
import re

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	# src="http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C302%3Bap%3D%C9%BC%B1%BE%D3%D0%C3%C0%B0%C9%2C90%2C310/sign=8800a2e3b3119313c743ffb855036fa7/1e29460fd9f9d72abb1a7c3cd52a2834349bbb7e.jpg" bdwater=
	reg = r'src="(.+?\.jpg)" bdwater='
	img_re = re.compile(reg)
	img_list = re.findall(img_re, html)
	return img_list

def saveImg(img_list):
	x = 0
	for img_url in img_list:
		urllib.urlretrieve(img_url, '%s.jpg' % x)
		x += 1


if __name__ == "__main__":
	html = getHtml("http://tieba.baidu.com/p/2166231880")
	saveImg(getImg(html))