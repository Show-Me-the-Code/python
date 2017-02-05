#!/usr/bin/env python
#coding: utf-8
from bs4 import BeautifulSoup
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 要分析的网页url
url = 'http://www.ruanyifeng.com/blog/2015/05/co.html'

def findAllLink(url):
    '''
    提取网页中的超链接
    '''
    # 获取协议，域名
    proto, rest = urllib.splittype(url)
    domain = urllib.splithost(rest)[0]
    # 读取网页内容
    html = urllib2.urlopen(url).read()
    # 提取超链接
    a = BeautifulSoup(html).findAll('a')
    # 过滤
    alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j']
    # 将形如#comment-text的锚点补全成http://www.ruanyifeng.com/blog/2015/05/co.html,将形如/feed.html补全为http://www.ruanyifeng.com/feed.html
    alist = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, alist)
    return alist

if __name__ == '__main__':
    for i in findAllLink(url):
        print i
