# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
from html.parser import HTMLParser

def get_path(root = os.curdir):
    root += os.sep
    for path, dirs, files in os.walk(root):
        for file_name in files:
            yield path, file_name

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        TagStack.append(tag)
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    link.append((value, 'None'))

    def handle_endtag(self, tag, tag_flag = True):
        while tag_flag == True:
            if tag == TagStack[-1]:
                TagStack.pop()
                tag_flag = False
            else:
                TagStack.pop()

    def handle_data(self, data):
        if data.strip() and 'body' in TagStack and 'a' in TagStack:
            link[-1] = (link[-1][0], data.strip())

if __name__ == '__main__':
    paths = get_path()
    html_format = ('.html','.htm')
    TagStack = []
    parser = MyHTMLParser()
    link = []

    for path, file_name in paths:
        if file_name.endswith(html_format):
            parser.feed(open(path + os.sep + file_name, encoding='utf-8').read())

    print(link)
