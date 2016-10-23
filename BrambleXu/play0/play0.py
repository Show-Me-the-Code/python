# -*- coding:utf-8 -*-
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
'''
PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
Draws the string at the given position.

Parameters:
xy – Top left corner of the text.
text – Text to be drawn. If it contains any newline characters, the text is passed on to mulitiline_text()
fill – Color to use for the text.
font – An ImageFont instance.
'''

from PIL import Image, ImageDraw, ImageFont

def add_num(picPath, num):
    img = Image.open(picPath)
    xSize, ySize = img.size
    #fontsize = min(xSize, ySize)/4
    myfont = ImageFont.truetype('Futura.ttf', xSize/4)
    ImageDraw.Draw(img).text((ySize//5 * 4, 0), str(num), font = myfont, fill='red')
    img.save('icon_with_num.jpg')

if __name__ == '__main__':
    add_num('/Users/xu/Udacity/python/BrambleXu/play0/icon.jpg', 3)
