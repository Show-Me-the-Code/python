# -*- coding: utf-8 -*-
'''
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片
'''

import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#captcha size
size = (240, 60)

#random chars
def gen_random():
    charlist = [random.choice(string.ascii_uppercase) for i in range(4)]
    chars = ''.join(charlist)
    return chars

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), \
            random.randint(0, 255))


def gen_captcha():
    im = Image.new('RGBA', size, color = 0)
    draw = ImageDraw.Draw(im)

    #background   
    for w in range(size[0]):
        for h in range(size[1]):
            draw.point((w, h), random_color())

    #draw text
    chars = gen_random()
    #font and size
    fnt = ImageFont.truetype('arial.ttf', int(size[1] * 0.8))
    x = 0
    y = size[1] * 0.1

    for i in range(4):
        x += size[0] * 0.2
        draw.text((x, y), chars[i], font = fnt, fill = random_color())

    #blur
    im = im.filter(ImageFilter.BLUR)
    im.save('captchar.jpg')
    im.show()
    
if __name__ == '__main__':
    gen_captcha()
