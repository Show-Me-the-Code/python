#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 11-03-15
# Author: Liang

import os
from PIL import Image

# Set input and output path
img_path = "img/"
new_img_path = "new_img/"
# list all the files in dir
dirs = os.listdir(img_path)

# iphone 5 resolution
iphone_width = 640
iphone_height = 1136


def resizer(img, iwidth, iheight):
    im = Image.open(img_path + img)
    width, height = im.size
    # To decide the ratio to resize
    if width > iwidth or height > iheight:
        if width / iwidth > height / iheight:
            ratio = width / iwidth
        else:
            ratio = height / iheight
        resized_img = im.resize(
            (int(width / ratio), int(height / ratio)), Image.ANTIALIAS)
    else:
        resized_img = im
    print("The new size is: ", end=" ")
    print(resized_img.size)
    resized_img.save(new_img_path + img)


for img in dirs:
    resizer(img, iphone_width, iphone_height)
