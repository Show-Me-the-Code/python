# -*- coding: utf-8 -*-
__author__ = 'PatchLion'

from PIL import Image, ImageDraw,ImageFont

def drawNumberOnIcon(imgpath, number):
    img = Image.open(imgpath)
    if (None == img):
        print('打开图片失败')
        return

    img = img.resize((160, 160))

    print(imgpath, "->", img.format, img.size, img.mode)
    draw = ImageDraw.Draw(img)
    img_size = img.size

    font = ImageFont.truetype("Varela-Regular.otf", size=int(img_size[1]/4))
    text_size = font.getsize(str(number))

    draw.text((img_size[0]-text_size[0], 0), str(number), font=font, fill=(255, 0, 0))

    img.save('icon_withnumber.jpg')

    print('生成图片成功')


drawNumberOnIcon("icon.jpg", 21)