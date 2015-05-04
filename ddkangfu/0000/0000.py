# coding=utf-8

from PIL import Image, ImageDraw, ImageFont

"""
0000：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
类似于图中效果 http://i.imgur.com/sg2dkuY.png?1
"""


def draw_number(file_name, number):
    image = Image.open(file_name)
    pos = (image.size[0] - 90, 0)
    font = ImageFont.truetype('Arial.ttf', 140)

    draw = ImageDraw.Draw(image)
    draw.text(pos, number, fill=(255,0,0), font=font)

    image.show()


if __name__ == '__main__':
    draw_number("507583.jpeg", "2")