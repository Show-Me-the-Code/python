#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0013 题： 用 Python 写一个爬图片的程序，爬（http://tieba.baidu.com/p/2166231880）图片 :-)'

__author__ = 'Drake-Z'

import os
import re
import urllib
from urllib import request
from urllib.request import urlopen

def read_url(yuanshiurl):
    req = request.Request(yuanshiurl)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE /360/ /chrome/ig)')
    with request.urlopen(req) as f:
        Imageurl(f.read().decode('utf-8'))                      #输出Data
    return 0

def Imageurl(data):
    re_Imageurl = re.compile(r'src="(http://imgsrc.baidu.com/forum/.*?)"')
    data = re_Imageurl.findall(data)                            #输出图片链接
    downloadImage(data)

def downloadImage(pic_url):
    dirct = '0013'
    try:  
        if not os.path.exists(dirct):                                   #创建存放目录
            os.mkdir(dirct)  
    except:  
        print('Failed to create directory in %s' % dirct)
        exit()  
    for i in pic_url:
        data = urllib.request.urlopen(i).read()  
        i = re.split('/', i)[-1]
        print(i)
        path = dirct + '/' +i
        f = open(path, 'wb')
        f.write(data)
        f.close()
    print('Done !')

url = 'http://tieba.baidu.com/p/2166231880'
read_url(url)