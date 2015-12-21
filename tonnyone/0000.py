#!/usr/bin/env python
#coding=utf-8
'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''

from PIL import Image,ImageDraw,ImageFont
from PIL import PSDraw
import sys

im = Image.open("D://6793701.jpg")
print im.format
print im.mode
print im.size

draw = ImageDraw.Draw(im)
# make a blank image for the text, initialized to transparent text color
# txt = Image.new('RGBA', im.size, (255,255,255,0))
# draw2 = ImageDraw.Draw(txt)
fnt = ImageFont.truetype('arial.ttf', 40)
# draw text, half opacity
draw.text((im.size[0]-40*3,0), "Hello", font=fnt, fill=(0,0,0,0))
# draw text, full opacity
#draw.text((0,60), "World", font=fnt, fill=(0,100,0,0))

del draw
# write to stdout
im.save("D:/new.png", "PNG")



