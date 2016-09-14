# -*- coding: utf-8 -*-
"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
"""
from PIL import Image, ImageFont, ImageDraw
import time
import 

def img_add_num(size=100,num=1):
    # 打开图片
    im = Image.open('my.jpg')
    # 读取图片的大小
    w, h = im.size
    # truetype(字体(优先读取文件位置，没有则去系统字体库中查询)，大小(要求为int)
    my_font = ImageFont.truetype('ALGER.TTF', size)
    # 定义一个实例，开始编辑img
    my_draw = ImageDraw.Draw(im)
    # text((横坐标，纵坐标)，内容，字体，颜色)
    # hint:这边的num需要是一个可迭代的值，所以需要从int转换成str。
    my_draw.text((w*7//8,h-(h*7//8)), str(num), font = my_font, fill = 'red')
    # 保存图片
    im.save('my_2.jpg')


if __name__ == '__main__':
    img_add_num(100,5)



