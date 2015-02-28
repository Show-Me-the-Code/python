#!/usr/bin/env
'''
Pre-request:
1.Have Pillow installed ( $ pip install Pillow)

The reason why I am using the shitty method of "line" is because I CANT NOT USE 
ImageFont!! anyone knows why??
>___,<
'''
from PIL import Image, ImageDraw
import os
# open the base pic
minion = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"zizi.gif")).convert('RGBA')
# new a transparent canvas for the annoying number :)
annoying = Image.new('RGBA', minion.size, (255, 255, 255, 0))
# get the drawing context , note that ImageDraw is the actionable module that will CREATE canvas on the base pic
num = ImageDraw.Draw(annoying)
# draw a number with halp opacity
num.line((minion.size[0]-8, 5, minion.size[0]-8, 25), fill=(255, 0, 0, 200), width=3)
num.line((minion.size[0]-8, 5, minion.size[0]-13, 11), fill=(255, 0, 0, 200), width=3)
num.line((minion.size[0]-14, 25, minion.size[0]-2, 25), fill=(255, 0, 0, 200), width=3)
out = Image.alpha_composite(minion, annoying)
out.show()
