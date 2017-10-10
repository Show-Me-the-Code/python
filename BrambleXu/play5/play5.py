# -*- coding:utf-8 -*-
# *第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import glob, os

size = 100, 100

def thumbnail_rel(path):
    for infile in glob.glob("**/*.jpg"):
        file, ext = os.path.splitext(infile)
        # print (file)
        # print (ext)
        img = Image.open(infile)
        img.thumbnail(size)
        img.save( file + ".thum.jpg")
        #print (im.format, im.size, im.mode)
    print ('Done!')

def thumbnail_abs(path):
    for infile in glob.glob("**/*.jpg"):
        file, ext = os.path.split(infile)
        # print (file)
        # print (ext)
        img = Image.open(infile)
        img.thumbnail(size)
        img.save( path + '/output/' + ext)
        #print (im.format, im.size, im.mode)
    print ('Done!')


if __name__ == '__main__':
    path = '.'
    thumbnail_rel(path)
    thumbnail_abs(path)
