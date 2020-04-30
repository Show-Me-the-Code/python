# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
# chr() & ord()
# pillow
# random

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def rndcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rndcolor2():
    return (random.randint(13, 63), random.randint(13, 63), random.randint(13, 63))


def rndchar():
    return chr(random.randint(ord('A'), ord('Z')))


image = Image.new('RGB', (240, 60), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Library/Fonts/Arial.ttf', 36)
for x in range(240):
    for y in range(60):
        draw.point((x, y), rndcolor())
for t in range(4):
    draw.text((60 * t + 10, 10), rndchar(), font=font, fill=rndcolor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')