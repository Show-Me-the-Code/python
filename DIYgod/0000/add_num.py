# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

from PIL import Image, ImageDraw, ImageFont

def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('Futura.ttf', x / 3)
    ImageDraw.Draw(img).text((2 * x / 3, 0), str(num), font = myfont, fill = 'red')
    img.save('pic_with_num.jpg')

if __name__ == '__main__':
    add_num('pic.jpg', 9)
