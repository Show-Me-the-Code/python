# Author:      illuz <iilluzen[at]gmail.com>
# File:        add_number_to_image.py
# Create Date: 2015-02-08 23:52:01
# Descripton:  Add a number to right top corner of images.
#              Will backup the image in ./[file]_bak.[ext]
# Usage:       add_number_to_image.py [image] [number]

'''
第 0000 题：
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果.
'''

from PIL import Image, ImageDraw, ImageFont
import sys, shutil


# backup file
# @return nothing
def back_file(filename):
    p = filename.rfind('.')
    shutil.copyfile(filename, filename[:p] + '_bak' + filename[p:])


# add number to right top corner
# @return nothing
def add_number_to_image(im, num):
    xsize, ysize = im.size
    left, top = int(xsize / 20.0 * 13), int(xsize / 20.0)
    right, bottom = int(xsize / 20.0 * 19), int(xsize / 20.0 * 7)
    draw = ImageDraw.Draw(im)
    draw.ellipse([left, top, right, bottom], (255, 0, 0))
    font=ImageFont.truetype("DroidSansMono.ttf", int(xsize / 20 * 4))
    draw.text((left + xsize / 10.0, top + xsize / 30), str(num), (0, 0, 0), font=font)
    del draw


# open image and deal font and get Draw
# @return a ImageDraw
def deal(f, num):
    if (num == None):
        num = 0
    if (num > '9'):
        num = '9+'
    im = Image.open(f)
    add_number_to_image(im, num)
    im.save(f)


def main():
    if len(sys.argv) <= 1:
        print "Need at least 1 parameter."
        return
    for i in range(1, len(sys.argv), 2):
        f = sys.argv[i]
        n = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        try:
            back_file(f)
            deal(f, n)
            print "Success add number to image file", f
        except IOError:
            print "Cannot open image", f, '!'
            pass


if __name__ == '__main__':
    main()

