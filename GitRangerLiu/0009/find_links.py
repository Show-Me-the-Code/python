# -*- coding: utf-8 -*-
'''
第 0009 题：一个HTML文件，找出里面的链接
'''

import urllib3 as urllib
import certifi
import urllib3.contrib.pyopenssl as pyopenssl
from bs4 import BeautifulSoup as bs

def find_links(url):
    li = []
    html = get_html(url)
    soup = bs(html, 'html.parser')
    for link in soup.find_all('a'):
        li.append(link.get('href'))

    for item in li:
        print item
    
def get_html(url):
    #certificate for python2.7
    pyopenssl.inject_into_urllib3()
    mgr = urllib.PoolManager(cert_reqs = 'CERT_REQUIRED', \
                             ca_certs = certifi.where())
                       
    res = mgr.request('GET', url)
    return res.data

if __name__ == '__main__':
    #url = 'https://github.com/GitRangerLiu/python'
    url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text'
    find_links(url)
