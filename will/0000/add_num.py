# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
'''
涉及模块/库：
    1.Pillow ：http://pillow-cn.readthedocs.io/zh_CN/latest/
    2.random
核心方法
    1.ImageFont Module：
        PIL.ImageFont.truetype(font=None, size=10, index=0, encoding='', filename=None)
    2.ImageDraw Module：
        PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)
想法思路：
    1.Pillow库所读的图片以左上角为原点，类似于第四象限
    2.数字添加在图片的右上角，注意控制图片的位置，及xy参数
'''


import random
from PIL import Image, ImageDraw, ImageFont
new = 'new.jpg'

def add_num(pic, text):
    'add a message number on pics'
    try:
        im = Image.open(pic)
    except:
        print('failed')
    width, height = im.size
    fontsize = height / 4
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', int(fontsize))
    draw.text((0.7*width, 0.02*height), text, font=font, fill='red')
    im.save(new)

if __name__ == "__main__":
    number = str(random.randint(1, 99))
    pic = './old.jpg'
    add_num(pic, number)
