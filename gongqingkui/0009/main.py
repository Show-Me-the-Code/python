#0009
import urllib2
from bs4 import BeautifulSoup
import re

url="http://www.iscas.ac.cn/xwdt2016/rdxw2016/201712/t20171201_4905565.html"

def processHTML(html):
    soup = BeautifulSoup(html)
    for d in soup.find_all("a"):
        print(d.text)
    
if __name__ =="__main__":
    html = urllib2.urlopen(url).read()
    processHTML(html)
