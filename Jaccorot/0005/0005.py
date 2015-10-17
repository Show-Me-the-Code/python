#!/usr/local/bin/python
#coding=utf-8

"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
import os
from PIL import Image

iPhone5_WIDTH = 1136
iPhone5_HEIGHT = 640

def resize_iPhone5_pic(path, new_path, width=iPhone5_WIDTH, height=iPhone5_HEIGHT):
    im = Image.open(path)
    w,h = im.size

    if w > width:
        h = width * h // w
        w = width
    if h > height:
        w = height * w // h
        h = height

    im_resized = im.resize((w,h), Image.ANTIALIAS)
    im_resized.save(new_path)


def walk_dir_and_resize(path):
    for root, dirs, files in os.walk(path):
        for f_name in files:
            if f_name.lower().endswith('jpg'):
                path_dst = os.path.join(root,f_name)
                f_new_name = 'iPhone5_' + f_name
                resize_iPhone5_pic(path=path_dst, new_path=f_new_name)

if __name__ == '__main__':
    walk_dir_and_resize('./')
