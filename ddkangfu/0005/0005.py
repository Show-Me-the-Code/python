# coding=utf-8

import os

from PIL import Image

"""
0005：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

# iphone 5 1136×640
IPHONE5_X = 1136
IPHONE5_Y = 640


def get_resized_file_name(file_name):
    return "%s_thumb.jpg" % file_name[:-4]


def resize_image(file_name):
    img = Image.open(file_name)
    x, y = img.size
    img_resize = None

    if x > IPHONE5_X:
        new_y = int(max(y * IPHONE5_X / x, 1))
        print (IPHONE5_X, new_y)
        img_resize = img.resize((IPHONE5_X, new_y))
    elif y > IPHONE5_Y:
        new_x = int(max(x * IPHONE5_Y / y, 1))
        print (new_x, IPHONE5_Y)
        img_resize = img.resize((new_x, IPHONE5_Y))

    if img_resize:
        file_resize = get_resized_file_name(file_name)
        print 'Resize file: %s ' % file_resize
        img_resize.save(file_resize, "JPEG")


def walk_dir(image_path):
    for root, dirs, files in os.walk(image_path):
        for f in files:
            if f.lower().endswith('jpg') and not f.lower().endswith('_thumb.jpg'):
                full_path = os.path.join(root, f)
                resize_image(full_path)


if __name__ == '__main__':
    walk_dir("images")
    #get_resized_file_name("001.jpg")