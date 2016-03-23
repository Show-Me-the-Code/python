# encoding = utf-8

from html.parser import HTMLParser


class DXHTMLParser(HTMLParser):
    def __init__(self, tag, tag_name, url):
        HTMLParser.__init__(self)
        self.tag = tag
        self.tag_name = tag_name
        self.url = url
        self.rets = []

    def handle_starttag(self, tag, attrs):
        if tag == self.tag:
            for name,value in attrs:
                if name == self.tag_name:
                    if value.startswith("/") and len(self.url) > 0:
                        value = self.url + value
                    self.rets.append(value)

    def getrets(self):
        return self.rets