#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* 0022
* by ahwz001
* 2017/10/03
* Thanks for this project. I learned a lot here.
"""

import os
import re
from PIL import Image

Start_path = './img_test/'
Out_path = './img_out/'


def deal_img(bill):
    count = 0
    for pic in bill:
        path = Start_path + pic
        print path
        im = Image.open(path)
        out = im.resize((1334,750))
        # out = im.resize((1136,640),Image.ANTIALIAS)
        new_pic = re.sub(pic[:-4],pic[:-4]+'_new',pic)
        print new_pic
        new_path = Out_path + new_pic
        out.save(new_path)
        count += 1
        print "the img " + pic + " has been modifed."

    print "%d imgs has been modified." % count


def thumbnail_pic(bill):
    for x in bill:
        print x
        name = os.path.join(Start_path, x)
        im = Image.open(name)
        im.thumbnail((1334, 750))
        print(im.format, im.size, im.mode)
        new_pic = Out_path + x
        im.save(new_pic)
    print('END')


def main():
    bill = os.listdir(Start_path)
    print bill
    thumbnail_pic(bill)
    # deal_img(bill)
    # both of two functions works well.


if __name__ == '__main__':
    main()