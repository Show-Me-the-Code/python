# -*- coding: utf-8 -*-
#!/usr/bin/env python
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter

def create_strs(draw, chars, length, font_type, font_size, width, height, fg_color):
    c_chars = ''.join([random.choice(chars) for i in range(length)])
    font = ImageFont.truetype(font_type, font_size)
    x0 = 9
    for c in c_chars:
        xt = random.randint(0, font_size / 3)
        yt = random.randint(2, 6)
        draw.text((x0 + xt, yt), c, font = font, fill = fg_color)
        x0 = x0 + xt + font_size
    return c_chars

def create_lines(draw, n_line, width, height):
    line_num = random.randint(n_line[0],n_line[1])
    for i in range(line_num):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=(0, 0, 0))

def create_points(draw, point_chance, width, height):
    chance = min(100, max(0, int(point_chance)))
    for w in range(width):
        for h in range(height):
            tmp = random.randint(0, 100)
            if tmp > 100 - chance:
                draw.point((w, h), fill = (0, 0, 0))

def valiadate_img(
    size = (120, 30), 
    chars = string.ascii_uppercase,
    img_type = 'PNG',
    mode = 'RGB',
    bg_color = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255)),
    fg_color = (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128)),
    font_size = 18,
    font_type = 'arial.ttf',
    length = 4,
    draw_lines = True,
    n_line = (1, 2),
    draw_points = True,
    point_chance = 2):
    width, height = size
    img = Image.new(mode, size, bg_color)
    draw = ImageDraw.Draw(img)
    if draw_lines:
        create_lines(draw, n_line, width, height)
    if draw_points:
        create_points(draw, point_chance, width, height)
    strs = create_strs(draw, chars, length, font_type, font_size, width, height, fg_color)

    params = [
    	1 - float(random.randint(1, 2) / 100),
    	0,
    	0,
    	0,
    	1 - float(random.randint(1, 10) / 100),
    	float(random.randint(1, 2) / 500),
    	0.001,
    	float(random.randint(1, 2) / 500)]

    img = img.transform(size, Image.PERSPECTIVE, params)

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return img, strs

if __name__ == "__main__":
    code_img = valiadate_img()
    code_img[0].save("validate.png", "GIF")
    print(code_img[1])
