#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def add_text(img, str):
    im = Image.open(img)
    tfont = ImageFont.truetype('times.ttf', 20)
    draw = ImageDraw.Draw(im)
    width, height = im.size
    draw.text((width-40,10), str, fill=(0,0,0), font=tfont)
    im.save(img, 'jpeg')

if __name__ == '__main__':
    add_text('001.jpg', '911')
