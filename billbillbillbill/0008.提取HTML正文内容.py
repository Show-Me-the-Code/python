#!/usr/bin/env python
#coding: utf-8
from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 要分析的网页url
url = 'http://www.ruanyifeng.com/blog/2015/05/thunk.html'

def extract(url):
    '''
    提取网页正文
    '''
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text



if __name__ == '__main__':
    print extract(url)
