#!/usr/bin/env pyhton3
#get the link in a html file

import re, urllib.request
from lxml.html import parse

def get_link(url):
    dom = parse(url).getroot()
    links = dom.xpath('//a')
    for link in links:
        link = link
        try:
            print(link.attrib['href'])
        except:
            pass

if __name__ == '__main__':
    get_link('http://thwiki.cc/')
