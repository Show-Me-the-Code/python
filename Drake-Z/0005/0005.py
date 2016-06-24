#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率(1136x640)的大小。'

__author__ = 'Drake-Z'

import os
import glob
from PIL import Image

def thumbnail_pic(path):
    a = glob.glob(r'*.jpg')
    for x in a:
        name = os.path.join(path, x)
        im = Image.open(name)
        im.thumbnail((1136, 640))
        print(im.format, im.size, im.mode)
        im.save(name, 'JPEG')
    print('Done!')

if __name__ == '__main__':
    path = '.'
    thumbnail_pic(path)