# -*- coding: utf-8 -*-
"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
from PIL import Image
import os

__author__ = 'Chris5641'


def change_resolution(path):
    for picname in os.listdir(path):
        picpath = os.path.join(path, picname)
        with Image.open(picpath) as im:
            w, h = im.size
            n = w/1366 if (w/1366) >= (h/640) else h/640
            im.thumbnail((w/n, h/n))
            im.save('finish_'+picname.split('.')[0]+'.jpg', 'jpeg')


if __name__ == '__main__':
    change_resolution('/home/chris/pictures/123')
