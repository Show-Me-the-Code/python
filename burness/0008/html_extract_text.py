# #-*- coding: utf-8-*-

# # Source:https://github.com/Show-Me-the-Code/show-me-the-code
# # Author:Burness Duan
# # Date:2014-12-28
# # Python 2.7


from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import urllib2

class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text


if __name__ == '__main__':
    url = 'http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html'
    html = urllib2.urlopen(url)
    html_code = html.read()
    html_code = sub('<script>(.*?)</script>','',html_code)
    # print dehtml(html_code).decode('gbk').encode('utf-8')
    with open('result.txt','w') as f:
        f.write(dehtml(html_code).decode('gbk').encode('utf-8'))
