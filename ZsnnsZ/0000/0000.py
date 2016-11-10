#!/usr /bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import random

origin_image = 'ori_img.jpg'
marked_image = 'new_img.jpg'

def draw_text(text, color):
    try:
        im = Image.open(origin_image)
    except:
        print ("Unable to load image")
    width, height =  im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('Arial.ttf', 35)
    draw.text((width * 0.8, height * 0.1), text, color, font)      
    im.save(marked_image)
    im.show()
    
if __name__ == "__main__":
	number = str(random.randint(1,99))
	color = (255, 0, 0)
	draw_text(number, color)