#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by xixijun
# Date: 15-5-13
# Blog: morningchen.com


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class AddNumToPic(object):

    """
        第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
        类似于微信未读信息数量那种提示效果。 类似于图中效果
    """
    def __init__(self):
        self.font = None
        self.img = None

    def open(self, img_path):
        self.img = Image.open(img_path)
        return True

    def set_font(self, font_path, size):
        self.font = ImageFont.truetype(font_path, size)
        return True

    def draw_text(self, str, color, ttf):
        xSize, ySize = self.img.size
        fontSize = min(xSize, ySize) // 11
        position = (0.9 * xSize, 0.1 * ySize - fontSize)
        draw = ImageDraw.Draw(self.img)
        draw.text(position, str, fill=color, font=ttf)
        self.img.show()
        self.img.save(str + "number" + '.png')
        return True

if __name__ == '__main__':
    pic = AddNumToPic()
    pic.open('img.png')
    pic.set_font('microsoft_yahei.TTF', 80)
    pic.draw_text('4', 'red', pic.font)
