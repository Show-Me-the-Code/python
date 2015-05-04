from PIL import ImageFont, Image, ImageDraw
import random


class YZMInfo:

    def __init__(self, img, code):
        self.img = img
        self.code = code


def ygm(font_size=20, count_min=4, count_max=10, code_height=30,
        string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
        font_color=['black', 'darkblue', 'darkred', 'darkgreen'],
        font_family='arial.ttf'):
    if count_max < count_min:
        count_max = count_min
    code_count = random.randrange(count_min, count_max)
    background = (random.randrange(230, 255),
                  random.randrange(230, 255),
                  random.randrange(230, 255))
    line_color = [(random.randrange(0, 255),
                   random.randrange(0, 255),
                   random.randrange(0, 255)),
                  (random.randrange(0, 255),
                   random.randrange(0, 255),
                   random.randrange(0, 255)),
                  (random.randrange(0, 255),
                   random.randrange(0, 255),
                   random.randrange(0, 255))]
    img_width = (font_size + 1) * code_count
    img_height = code_height + font_size
    verify = ''
    im = Image.new('RGB', (img_width, img_height), background)
    draw = ImageDraw.Draw(im)
    code = random.sample(string, code_count)
    draw = ImageDraw.Draw(im)
    for i in range(random.randrange(code_count / 2, code_count)):
        xy = (random.randrange(0, img_width), random.randrange(0, img_height),
              random.randrange(0, img_width), random.randrange(0, img_height))
        draw.line(xy, fill=random.choice(line_color), width=1)
    x = font_size / 2
    for i in code:
        y = random.randrange(0, code_height)
        font = ImageFont.truetype(
            font_family, font_size + random.randrange(-font_size/3, font_size/3))
        draw.text((x, y), i, font=font, fill=random.choice(font_color))
        x += font_size
        verify += i
    return YZMInfo(img=im, code=verify.upper())


info = ygm(font_size=16,
           code_height=10,
           string='#@%&$abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
info.img.save("0010.GIF")
print info.code
