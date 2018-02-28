#0013
#coding=utf-8

import urllib2
import time
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:8.0.1) Gecko/20100101 Firefox/8.0.1'}
url='http://tieba.baidu.com/p/3055145055#!/l/p1'
req = urllib2.Request(url,None,header)
site = urllib2.urlopen(req)
soup = BeautifulSoup(site.read())
for img in soup.find_all('img'):
    picsrc = img.get('src')
    #print picsrc
    if picsrc != None and picsrc.find('http') != -1:
        imgfile = 'gyy/%s.jpg'%(time.time())
        pic = open(imgfile,'wb')
        pic.write(urllib2.urlopen(picsrc).read())
        pic.close()
        
