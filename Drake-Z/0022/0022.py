#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。'''

__author__ = 'Drake-Z'

from PIL import Image
import os

def thumbnail_pic(a, b =1136, c=640):
    for x in a:
        name = os.path.join('.', x)
        im = Image.open(name)
        print('Before:'+im.format, im.size, im.mode)
        im.thumbnail((b, c))
        print('After:'+im.format, im.size, im.mode)
        im.save(name, 'JPEG')

a = os.listdir('.') 
PHONE = {'iPhone5':(1136,640), 'iPhone6':(1134,750), 'iPhone6P':(2208,1242)}
width,height = PHONE['iPhone6']
thumbnail_pic(a, width, height)