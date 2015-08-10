# 生成彩色验证码
import functools
import random
import string

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter


def generate(path=None, mode='RGBA', font='SourceCodePro-Black', length=4, font_size=30, margin=0, bg_color=(255, 255, 255)):
    size = (font_size * (length + 1) + length * margin, round(font_size * 1.5))
    charset = string.ascii_letters
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, font_size)
    random_color = functools.partial(random.randint, a=50, b=200)
    position = (font_size / 2, font_size / 4)
    for c in range(length):
        draw.text(position, random.choice(charset), font=font,
                  fill=tuple(random_color() for i in range(len(mode))))
        position = (position[0] + margin + font_size, position[1])
    img = img.filter(ImageFilter.RankFilter(3, 4))
    img.show()
    if path:
        img.save(path)
    return img


if __name__ == '__main__':
    generate(font_size=30, margin=-10)
