#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。'

__author__ = 'Drake-Z'

from PIL import Image, ImageDraw, ImageFont

def add_num(filname, text = '4', fillcolor = (255, 0, 0)):
    img = Image.open(filname)
    width, height = img.size
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=width//8)
    fillcolor = (255, 0, 0)
    draw = ImageDraw.Draw(img)
    draw.text((width-width//8, 0), text, font=myfont, fill=fillcolor)
    img.save('1.jpg','jpeg')
    return 0

if __name__ == '__main__':
    filname = '0.jpg'
    text = '4'
    fillcolor = (255, 0, 0)
    add_num(filname, text, fillcolor)