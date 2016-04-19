#!/usr/bin/env python3
#Add a number on my icon with the name "icon.png".
#My icon is a little ... big.
#Problem0000

from PIL import Image, ImageDraw, ImageFont

def add_number(num):
    im = Image.open("icon.png")
    #make a image for showing the number
    txt = Image.new('RGBA', im.size, (255,255,255,0))
    #use the font "arial.ttf"
    fnt = ImageFont.truetype("arial.ttf",40)
    #draw context
    d = ImageDraw.Draw(txt)
    #draw the number
    d.text((im.size[0]-50 ,5), str(num), font=fnt, fill=(255,0,0,255))

    out = Image.alpha_composite(im, txt)
    out.show()
    out.save("icon_"+str(num)+".png")

if __name__ == '__main__':
    add_number(42)
