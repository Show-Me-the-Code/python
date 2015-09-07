# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:40:53 2015

@author: Tracy
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open('icon.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('DejaVuSansMono.ttf',100)

draw.text((img.size[0]-100,30),"3",(255,0,0), font)

img.save('result.jpg')
