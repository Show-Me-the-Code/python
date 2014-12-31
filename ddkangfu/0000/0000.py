# coding=utf-8

from PIL import Image, ImageDraw, ImageFont


def draw_number(file_name, number):
    image = Image.open(file_name)
    pos = (image.size[0] - 90, 0)
    font = ImageFont.truetype('Arial.ttf', 140)

    draw = ImageDraw.Draw(image)
    draw.text(pos, number, fill=(255,0,0), font=font)

    image.show()


if __name__ == '__main__':
    draw_number("507583.jpeg", "2")