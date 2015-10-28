#!/usr/bin/env python
#coding: utf-8
import Image, ImageDraw, ImageFont, ImageFilter
import string, random

fontPath = "/usr/share/fonts/truetype/ttf-devanagari-fonts/"

# 获得随机四个字母
def getRandomChar():
    return [random.choice(string.letters) for _ in range(4)]

# 获得颜色
def getRandomColor():
    return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))

# 获得验证码图片
def getCodePiture():
    width = 240
    height = 60
    # 创建画布
    image = Image.new('RGB', (width, height), (180,180,180))
    font = ImageFont.truetype(fontPath + 'kalimati.ttf', 40)
    draw = ImageDraw.Draw(image)
    # 创建验证码对象
    code = getRandomChar()
    # 把验证码放到画布上
    for t in range(4):
        draw.text((60 * t + 10, 0), code[t], font=font, fill=getRandomColor())
    # 填充噪点
    for _ in range(random.randint(1500,3000)):
        draw.point((random.randint(0,width), random.randint(0,height)), fill=getRandomColor())
    # 模糊处理
    image = image.filter(ImageFilter.BLUR)
    # 保存名字为验证码的图片
    image.save("".join(code) + '.jpg', 'jpeg');

if __name__ == '__main__':
    getCodePiture()