# codeing: utf-8

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import string
import random


def get4char():
    return [random.choice(string.ascii_letters) for _ in range(4)]  # 可以把‘_’换做任意字母，‘_’说明后续不用


def getcolor():
    return random.randint(30, 100), random.randint(30, 100), random.randint(30, 100)


def getpicture():
    width = 240
    height = 60

    image = Image.new('RGB', (width, height), (180, 180, 180))
    font = ImageFont.truetype('arial.ttf', 40)

    draw = ImageDraw.Draw(image)
    code = get4char()
    for ch in range(4):
        draw.text((60 * ch,30), code[ch], font=font, fill=getcolor())

    for _ in range(random.randint(1500, 3000)):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=getcolor())

    image = image.filter(ImageFilter.BLUR)
    image.save("".join(code) + '.jpg')


getpicture()
