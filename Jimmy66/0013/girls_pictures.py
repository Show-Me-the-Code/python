#!/bin/env python
# -*- coding: utf-8 -*- 

#导入模块
import urllib2
import re
import os
import glob

#设定抓取页数
page_amount = 2

#抓取首页的html代码   
def get_page(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')      #缺省部分填上浏览器字符串
    response = urllib2.urlopen(req)
    html = response.read().decode('utf-8')
    return html

#抓取图片
def read_image(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')      #缺省部分填上浏览器字符串
    response = urllib2.urlopen(url)
    html = response.read()
    return html

#得到当前的最新页面数，从这个页面开始倒着爬，因为用了这个脚本以后以前的图可能已经看过了
def get_current_page_number(html):
	match = re.search(r'<span class="current-comment-page">\[(.*)\]</span>',html)
	return match.group(1)

#得到图片列表
def get_picturs_url_list(url):
	html = get_page(url)
	l = re.findall(r'<p><img src="http://.*.sinaimg.cn/mw600/.*jpg" /></p>',html)
	result = []
	for string in l:
		src = re.search(r'"(.*)"',string)
		result.append(str(src.group(1)))	#解决Unicode编码开头问题，有空好好补下编码和字符规范
	return result

#下载图片并存储到本地文件夹
def image_save(url,number):
	number = str(number)
	print '正在抓取第',number,'张'
	filename = number + '.jpg'
	with open(filename,'wb') as fp:
		img = read_image(url)
		fp.write(img)

#准备存放图片的文件夹，并进入到指定路径
def floder_prepare(floder):
	a = glob.glob('*')
	if floder not in a:
		os.mkdir(floder)
	os.chdir(floder)

#主函数
def main():
	html = get_page('http://jandan.net/ooxx')
	number = int(get_current_page_number(html))
	l = []
	amount = 0
	for n in range(0,page_amount):
		url = 'http://jandan.net/ooxx/page-' + str(number-n) + '#comments'
		l += get_picturs_url_list(url) 
	floder_prepare('picture')
	for url in l:
		amount += 1
		image_save(url,amount)

if __name__ == '__main__':
	main()
	print '全部抓完啦，你这个hentai'
