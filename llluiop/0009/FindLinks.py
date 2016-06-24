#!/usr/bin.env python


from HTMLParser import HTMLParser
from re import sub
import urllib2
import sys


class HtmlParserMainText(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value and 'http' in value:
                self.text.append(''.join(value) + '\n')




def GetLinks():
    url = "http://www.cnbeta.com/"
    html = urllib2.urlopen(url).read()

    parser = HtmlParserMainText()
    parser.feed(html)
    parser.close()

    return ''.join(parser.text).strip()


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print GetLinks()
