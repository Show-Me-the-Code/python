#coding:utf-8
#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image, ImageDraw, ImageFont

__author__ = 'Hunter'

def picture_num(img,num):
    im = ImageDraw.Draw(img)
    print(img.size)
    numFont = ImageFont.truetype("ahronbd.ttf",300)
    im.text((260, -50), num, fill=(255, 0, 0),font=numFont)
    img.save("wechat_100.jpg")
    img.show()


if __name__ == '__main__':
    img = Image.open("wechat.jpg")
    picture_num(img,"100")