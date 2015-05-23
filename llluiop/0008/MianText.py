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
        if tag == "p":
            self.text.append("\n")

    def handle_data(self, data):
        if len(data.strip()) > 0:
            self.text.append(data.strip())



def GetMainText():
    url = "http://www.bbc.com/"
    html = urllib2.urlopen(url).read()
    html_code = sub('<script[^>]*?>[^>]*?</script>','',html) #delete all scripts



    parser = HtmlParserMainText()
    parser.feed(html_code)
    parser.close()

    return ''.join(parser.text).strip()


if __name__ == "__main__":

    reload(sys)
    sys.setdefaultencoding('utf-8')
    print GetMainText()