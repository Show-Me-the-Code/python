#!/usr/bin/env python

from HTMLParser import HTMLParser
import urllib2

class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.picUrls = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            if len(attrs) > 0:
                for key, value in attrs:
                    if key == "src":
                        self.picUrls.append(value)




def Pic(picurls):
    count = 1
    for picurl in picurls:
        conn = urllib2.urlopen(picurl)
        f = open(str(count)+".jpg", 'wb')
        f.write(conn.read())
        f.close()
        count += 1



if __name__ == '__main__':
    html = urllib2.urlopen("http://tieba.baidu.com/p/2166231880").read()

    htmlParser = MyHtmlParser()
    htmlParser.feed(html)
    htmlParser.close()


    Pic(htmlParser.picUrls)



