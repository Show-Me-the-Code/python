#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 22-02-15
# Author: Liang


from PIL import Image, ImageDraw, ImageFont


def add_number(image_path, number):
    im = Image.open(image_path)
    width, height = im.size

    # get a drawing context
    avatar_draw = ImageDraw.Draw(im)
    # set the font of number to draw
    font_size = int(height / 4)
    number_font = ImageFont.truetype('microsoft_yahei.TTF', font_size)

    # Draw the image with a number(xy, text, color, font)
    avatar_draw.text(
        (width - font_size, 0), str(number), (255, 0, 0), font=number_font)

    im.save('./new_avatar.jpg')
    im.show()


add_number('avatar.png', 3)
