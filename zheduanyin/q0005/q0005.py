# 批量检查/缩放图片
import os

from PIL import Image
from collections import namedtuple
from pprint import pprint


def resize_img(img_path):
    resolution = namedtuple('resolution', ['width', 'height'])
    iphone5 = resolution(1136, 640)
    with Image.open(img_path) as img:
        if img.width > iphone5.width or img.height > iphone5.height:
            print('- resizing %s' % img_path)
            img = img.resize((min(img.width, iphone5.width), min(img.height, iphone5.height)))
            img.save(img_path)


def find_suffix(root_path, suffix_list, verbose=False):
    file_list = []
    for level in os.walk(root_path):
        for fn in level[2]:
            if os.path.splitext(fn)[1] in suffix_list:
                file_list.append(os.path.join(level[0], fn))
    if verbose:
        print('- found these files:')
        pprint(file_list)
    return file_list

if __name__ == '__main__':
    print('- start working ..')
    img_list = find_suffix('.', ['.jpg'])
    for img_file in img_list:
        try:
            resize_img(img_file)
        except OSError:
            print('- not an image: %s' % img_file)
    print('- done ..')
