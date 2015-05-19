#!/usr/bin/env python


import os
import Image
import ImageDraw
import ImageFont

def drawFont(img):
    font = ImageFont.truetype("DejaVuSansMono.ttf", 20)
    draw = ImageDraw.Draw(img)
    draw.ink = 255
    draw.text((img.size[0] - 20,  5), "2", font=font)


def main():
    img = Image.open("avatar.jpg")
    drawFont(img)
    img.save("avatar_num.jpg")




if __name__ == '__main__':
    main()
