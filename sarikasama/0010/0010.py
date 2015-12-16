#!/usr/bin/env python3
#generate random verification codes in letters

import random, string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def gene_verification_code_pic():
    #initialize
    im = Image.new('RGB', (200, 50), (255, 255, 255))
    font = ImageFont.truetype('arial.ttf', 30)
    draw = ImageDraw.Draw(im)
    
    #init background with light color
    for i in range(200):
        for j in range(50):
            draw.point((i, j), fill=(random.randint(128,255),random.randint(128,255),random.randint(128,255)))
    
    #init letters with deep color
    for t in range(4):
        draw.text((50*t+10, 10), random.choice(string.ascii_letters), font=font, fill=(random.randint(0,127), random.randint(0,127), random.randint(0,127)))
    
    #make the pic blurred
    im = im.filter(ImageFilter.BLUR)
    return im

if __name__ == '__main__':
    im = gene_verification_code_pic()
    im.show()
    im.save('res.jpg')
