#!/usr/bin/env python
#coding=utf-8

"""你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。"""
__author__ = 'tonnytwo'

import os
from PIL import Image,ImageDraw,ImageFont

def scanPic(path):

    if(os.path.isdir(path)):
        files = os.listdir(path)
        for f in files:
            if(os.path.isdir(path+os.sep+f)):
                scanPic(path+os.sep+f)
            else:
                try:
                    im = Image.open(path+os.sep+f)
                    im.thumbnail((200,200))
                    im.save("D:/pic/"+f+"refac.jpeg", "JPEG");
                except IOError:
                    pass

scanPic("D:/pic");
