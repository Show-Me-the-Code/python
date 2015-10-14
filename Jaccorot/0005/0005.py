#!/usr/local/bin/python
#coding=utf-8

"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

from PIL import Image

iPhone5_WIDTH = 1136
iPhone5_HEIGHT = 640

def resize_iPhone5_pic(path, width=iPhone5_WIDTH, height=iPhone5_HEIGHT, new_path='new.jpg'):
    im = Image.open(path)
    im_resized = im.resize((width,height), Image.ANTIALIAS)
    im_resized.save(new_path)

if __name__ == '__main__':
    resize_iPhone5_pic('0.jpg')