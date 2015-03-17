#!/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
from pyquery import PyQuery as pq
from lxml import etree
import re


def get_html(url):
    html = urllib2.urlopen(url).read()
    return html 

def get_content(html):
    match = re.search(r'<div class="content">([^$]*)<div class="article-copyright">',html)
    content = match.group(1)
    return content

def get_result(content):
    content = content.decode('utf-8')
    jq = pq(content)
    l = jq('p')
    result = []
    for string in l:
        result.append(pq(string).text()) 
    return result


def main():
    url = 'http://jimmy66.com/164.html'
    html = get_html(url)
    content = get_content(html)
    result = get_result(content)
    for line in result:
        print line
if __name__ == '__main__':
    main()