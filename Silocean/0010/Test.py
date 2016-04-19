__author__ = 'Tracy'
import Image,ImageDraw,ImageFont,ImageFilter
import random

image = Image.new('RGB', (50*4, 50), (255,255,255))

font = ImageFont.truetype('DejaVuSansMono.ttf', 24)

draw = ImageDraw.Draw(image)

def randColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

def randColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

def randChar():
    return chr(random.randint(65,90))

for x in range(50*4):
    for y in range(50):
        draw.point((x, y), randColor())

for x in range(4):
    draw.text((50*x+10, 10), randChar(), randColor2(), font)

image = image.filter(ImageFilter.BLUR)
image.save('Result.jpg')
image.show()