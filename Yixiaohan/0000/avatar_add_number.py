#!/usr /bin/env python
# -*- coding: utf-8 -*-

"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
Pillow：Python Imaging Library
PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
"""

from PIL import Image, ImageDraw, ImageFont

original_avatar = 'weChat_avatar.png'
saved_avatar = 'new_avatar.png'
windows_font = 'Arial.ttf'
color = (255, 0, 0)

def draw_text(text, fill_color, windows_font):
    try:
        im = Image.open(original_avatar)
        x, y =  im.size
        print "The size of the Image is: "
        print(im.format, im.size, im.mode)
        im.show()
        
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(windows_font, 35)
        draw.text((x-20, 7), text, fill_color, font)
        
        im.save(saved_avatar)
        im.show()

    except:
        print "Unable to load image"

if __name__ == "__main__":
    #number = str(raw_input('please input number: '))
    number = str(4)
    draw_text(number, color, windows_font)