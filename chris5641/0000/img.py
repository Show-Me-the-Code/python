# -*- coding: utf-8 -*-
"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
"""
from PIL import Image, ImageFont, ImageDraw

__author__ = 'Chris5641'


def img_add_num(num=1):
    img = Image.open('img.png')
    w, h = img.size
    font = ImageFont.truetype('arial.ttf', w // 4)
    draw = ImageDraw.Draw(img)
    draw.text((w*3//4, 0), str(num), font=font, fill='red')
    img.save('img2.png')


if __name__ == '__main__':
    img_add_num(5)
