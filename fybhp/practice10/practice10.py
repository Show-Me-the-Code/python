# -*- coding:utf-8 -*-
import string
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

def numgenerator(size=4, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def getcolor():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def getfont():
    font = ImageFont.truetype('Arial.ttf',random.randint(50,65))
    return font

check = numgenerator()
imageFile = "./bacdgroud.jpg"
img = Image.open(imageFile)
draw = ImageDraw.Draw(img)
for i in range(4):
    draw.text((72*i+random.randint(15,20), random.randint(5,10)),check[i],getcolor(),font=getfont())
    draw = ImageDraw.Draw(img)
image = img.filter(ImageFilter.BLUR)

image.save("./test1.jpg")
