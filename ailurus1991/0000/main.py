#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'jinyang'

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def imageWriter(filePath, number = 1):
    img = Image.open(filePath)
    size = img.size
    # set the font size
    fontSize = size[1] / 4
    draw = ImageDraw.Draw(img)
    # create a font instance
    ttFont = ImageFont.truetype("/Library/Fonts/Skia.ttf", fontSize)
    draw.text((size[0]-fontSize, 0), str(number), font=ttFont)
    img.show()

print imageWriter("test.jpg")