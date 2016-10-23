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

'''
1. 坐标 (0, 0) 表示左上角，整个图片类似镶嵌在坐标的第四像限；img.size 是一个二位数组，依次位图片的宽和高。
2. 在图片上添加内容时注意对应内容也会占位置，所以不能当作点即 pixel 来看待，实际处理时需要考虑添加对象的 size，这就对应代码中右上角坐标position的获取。
3. ImageFont 的获取有很多方法，其中较简单的方法从 truetype 中获取，对应 font 存放的位置一般是 /usr/share/fonts/...
'''

from PIL import Image, ImageDraw, ImageFont

def add_num(picPath, num):
    img = Image.open(picPath)
    xSize, ySize = img.size
    fontsize = ySize / 4
    position = xSize - fontsize
    myfont = ImageFont.truetype('Futura.ttf', fontsize)
    ImageDraw.Draw(img).text((position, 0), str(num), font = myfont, fill='red')
    img.save('icon_with_num.jpg')

if __name__ == '__main__':
    add_num('/Users/xu/Udacity/python/BrambleXu/play0/icon.jpg', 3)
