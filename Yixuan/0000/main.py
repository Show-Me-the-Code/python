#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont, ImageColor


'''
打开文件,
声明 text 的位置, 是什么, 字体, 颜色.

----
'''

original = Image.open("duck.jpg") #Open pic

font = ImageFont.truetype("msyh.ttf", 60)

d = ImageDraw.Draw(original)

d.text((500, 0), "2", font=font, fill=(255,0,0,255))

d = ImageDraw.Draw(original)

original.save("finnal.jpg")

