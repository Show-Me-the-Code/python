#0010
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def randomchar():
    return chr(random.randint(65,90))

def randomcolor():
    return (random.randint(60,255),random.randint(60,255),random.randint(60,255))

def randomcolor2():
    return (random.randint(0,255),random.randint(0,200),random.randint(0,200))

size = (100,50)
font = ImageFont.truetype('Arial.ttf',30)
image = Image.new("RGB",size,(255,255,255))
draw = ImageDraw.Draw(image)
a,b=size

for x in range(a):
    for y in range(b):
        draw.point((x,y),fill=randomcolor())
    
for i in range(4):
    draw.text((a/4*i,b/3),randomchar(),font=font,fill=randomcolor2())

image.save('test.jpg')
