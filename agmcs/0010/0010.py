from PIL import Image, ImageDraw, ImageFont
import random

im = Image.new('RGBA',(120,50),(255,255,255))
text = random.sample('abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ',4)

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("msyh.ttf",40)

x=0
y=0
for i in xrange(200):
    x1 = random.randint(0,120)
    y1 = random.randint(0,50)
    x2 = random.randint(0,120)
    y2 = random.randint(0,50)    
    fill = (random.randint(130,250),random.randint(130,250),random.randint(130,250))
    draw.line(((x1,y1),(x2,y2)),fill=fill)

for word in text:
    fill = (random.randint(0,130),random.randint(0,130),random.randint(0,130))
    draw.text((x,y),word,font=font,fill=fill)
    x+=30
    
for i in xrange(1000):
    x1 = random.randint(0,119)
    y1 = random.randint(0,49)
    fill = (random.randint(20,250),random.randint(20,250),random.randint(20,250))
    im.putpixel((x1,y1),fill)

im.save('1.jpg')
