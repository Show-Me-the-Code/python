# coding = utf-8

from tools import imager
from PIL import Image, ImageFont

# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字
def add_num(image_path):
    im = imager.open_image(image_path)
    if im is not None:
        font = ImageFont.truetype('Arial.ttf', 20)
        w, h = im.size
        point = (w - 10, 0)
        imager.draw_text(im, "8", point, font)
        # imager.save(im, "./header_tmp.jpg")
        im.show()

if __name__ == "__main__":
    add_num("./header.jpg")