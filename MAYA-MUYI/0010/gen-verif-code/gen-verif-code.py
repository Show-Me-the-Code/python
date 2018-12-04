# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 背景颜色:
def rndBgColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 字体颜色:
def rndTxtColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def gen_verif_code(verifcode_name):
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    
    # 创建Font对象:
    font = ImageFont.truetype('arial.ttf', 36)

    # 创建Draw对象:
    draw = ImageDraw.Draw(image)

    # 填充背景颜色:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndBgColor())

    # 生成随机验证码:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndTxtColor())

    # 模糊:
    image = image.filter(ImageFilter.BLUR)

    # 保存:
    image.save(verifcode_name, 'jpeg')

if __name__ == '__main__':
    gen_verif_code('verifcode.jpg')

