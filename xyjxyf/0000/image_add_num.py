# coding = utf-8

from tools import imager
from PIL import Image, ImageFont

im = imager.open_image("./header.jpg")
if im is not None:
    font = ImageFont.truetype('Arial.ttf', 20)
    w, h = im.size
    point = (w - 10, 0)
    imager.draw_text(im, "8", point, font)
    imager.save(im, "./header_tmp.jpg")
    im.show()

