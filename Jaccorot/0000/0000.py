#!/usr/local/bin/python
#coding=utf-8

"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

from PIL import Image, ImageDraw, ImageFont

number = str(5)
color = (255, 0, 0)
windows_font = 'Arial.ttf'

def draw_text(text, fill_color, windows_font):
    im = Image.open('0.jpg')
    x, y = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(windows_font, 35)
    draw.text((x-20, 7), text, fill_color, font)

    im.save('1.jpg')

draw_text(number, color, windows_font)
