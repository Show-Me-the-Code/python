#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0010
* by ahwz001
* 2017/8/10
* Thanks for this project. I learned a lot here.
* Please refer to the project folder renzongxian, I learned this code from that and write some comments.
"""

from PIL import Image, ImageDraw, ImageFont
import string
import random
import os


def random_color():
    # Generate random color, and return as a tuple
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def generate_authenticode():
    # Generate random letters:
    letters = []
    for i in range(4):
        letters.append(random.choice(string.letters))

    # Set the size of the image        
    width = 150
    height = 60

    # Generate an image
    im = Image.new('RGB',(width,height),(255,255,255))

    # Draw letters on the image
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype('msyhbd.ttf',40)

   # Draw letters on the image
    for i in range(4):
        dr.text((5+i*33,5), letters[i],random_color(),font)
    del dr
    
    # Change the background color
    for x in range(width):
        for y in range(height):
            if im.getpixel((x,y)) == (255,255,255):
                im.putpixel((x,y), random_color())

    # Save img.
    im.save('0010.jpg')


if __name__ == '__main__':
    generate_authenticode()
    os.system('display *.jpg')
