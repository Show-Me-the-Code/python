# -*- coding: utf-8 -*-
#!/usr/bin/env python
#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os
from PIL import Image

def get_path(root = os.curdir):
    root += os.sep
    for path, dirs, files in os.walk(root):
        for file_name in files:
            yield path, file_name

def get_size(width, heigh, max_width, max_heigh):
    if width > max_width:
        heigh = heigh * (max_width / width)
        width = max_width
    if heigh > max_heigh:
        width = width * (max_heigh / heigh)
        heigh = max_heigh
    return width, heigh


if __name__ == '__main__':
    paths = get_path()
    image_format = ('.jpg', '.jpeg', 'png', 'bmp')
    max_size = (640, 1136)
    for path, file_name in paths:
        if file_name.endswith(image_format):
            img = Image.open(path + os.sep + file_name)
            size = get_size(*(img.size + max_size))
            if size != img.size:
                img.thumbnail(size)
                img.save(path + os.sep + 'thumbnailed_' + file_name)
