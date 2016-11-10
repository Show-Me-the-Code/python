#!/usr /bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import random

ori_img = 'ori_img.jpg'
new_img = 'new_img.jpg'

def add_num(text, color):
    try:
        im = Image.open(ori_img)
    except:
        print ("Unable to load image")
    width, height = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('Arial.ttf', 35)
    draw.text((width * 0.8, height * 0.1), text, color, font)      
    im.save(new_img)
    im.show()
    
if __name__ == "__main__":
	number = str(random.randint(1,99))
	color = (255, 0, 0)
	add_num(number, color)