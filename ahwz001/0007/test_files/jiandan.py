# coding:utf-8

from lxml import etree
import requests
import time
import urllib.request
import random

num = 0

def getxpath(url):
    r = requests.get(url).content
    # print(r)
    return etree.HTML(r)


def get_img(s):    
    global num
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]    
    # opener.addheaders = header
    urllib.request.install_opener(opener)
    for i in s.xpath('//p/img/@src'):
        j  = 'http:' + i
        # print(j)
        name = i.split('/')[-1]
        print(name)        
        urllib.request.urlretrieve(j, name)
        num += 1
        print(num)
        time.sleep(random.randint(0,5))


def main():
    url_0 = 'http://jandan.net/ooxx/page-'

    url_list  = [url_0 + str(i) for i in range(1980,2008)]
    print(url_list)
    page = 0    
    for k in url_list:
        t = getxpath(k)
        get_img(t)
        print(page )
        page += 1

if __name__ == "__main__":
    main()
