# -*- coding: utf-8 -*-
__author__ = 'PatchLion'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def randChar():
    #65-90 A-Z
    return chr(random.randint(65, 90))

def randColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def createIdentifyingCode(size, charcount=4):
    width=size*charcount
    height=size

    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randColor())

    font = ImageFont.truetype("../0000/Varela-Regular.otf", size=size)
    #draw.text((0, 0), randChar(), fill=randColor())
    for i in range(charcount):
        draw.text((i*size + 10, -10), randChar(), fill=randColor(), font=font)

    img = img.filter(ImageFilter.BLUR)
    img.save('ic.jpg', 'jpeg')

createIdentifyingCode(60)

