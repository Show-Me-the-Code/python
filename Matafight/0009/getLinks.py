# _*_ encodeing: utf-8 _*_
from HTMLParser import HTMLParser
import urllib2

class myParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self);
        self.flag=0;
        self.links=[];

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name,value in attrs:
                if name =="href":
                    self.links.append(value);
                 

if __name__=="__main__":
    parser=myParser();
    myurl='http://www.baidu.com';
    html=urllib2.urlopen(myurl);
    htmlcode=html.read();
    parser.feed(htmlcode);
    print parser.links;

