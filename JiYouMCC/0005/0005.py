# -*- coding: utf-8 -*-
# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# using PIL in http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image


def change_image_size(image_path='0005.jpg', size=(1136, 640)):
    im = Image.open(image_path)
    size = (size[1], size[0]) if im.size[1] > im.size[0] else size
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('result-' + image_path)

change_image_size('0005-r.jpg')
change_image_size('0005.jpg')
