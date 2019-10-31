
from PIL import Image, ImageDraw, ImageFont

def add_num():
    im = Image.open('in.jpg')
    xsize, ysize = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", xsize // 3)
    draw.text((ysize // 5 * 4, 0), '3',    (250,128,114), font)
    im.save('out.jpg')

add_num()
