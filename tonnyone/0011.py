#!/usr/bin/env python
#coding=utf-8
__author__ = 'tonnytwo'

from PIL import Image,ImageDraw,ImageFont
import random
import string

def colorRandom():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    a = 200
    return (r,g,b,a)

def letterRandom():
    return random.choice(string.letters)

wigth = 200
high = 50
txt = Image.new('RGBA', (wigth,high), (255,255,255,0))
d = ImageDraw.Draw(txt)

fnt = ImageFont.truetype('arial.ttf', 40)

for w in range(1,wigth):
    for h in range(1,high):
        d.point([(w,h),(w,h)],fill = colorRandom())

d.text((wigth/8,high/8), letterRandom(),font=fnt,fill =colorRandom())
d.text((wigth/8*2,high/8), letterRandom(),font=fnt,fill =colorRandom())
d.text((wigth/8*4,high/8), letterRandom(),font=fnt,fill =colorRandom())
d.text((wigth/8*6,high/8), letterRandom(),font=fnt,fill =colorRandom())
txt.show()
