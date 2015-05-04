# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-08
# Python 3.4

"""

第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率（1136*640）的大小。

"""

from PIL import Image
import os
import sys


def resize_image(image):
    im = Image.open(image)
    weight, height = im.size
    if weight > 1136 or height > 640:
        dw = weight / 1136
        dh = height / 640
        ds = max(dw, dh)
        new_weight = int(weight / ds)
        new_height = int(height / ds)
        im = im.resize((new_weight, new_height))
        print("Succeed to resize the image %s to %s*%s " % (image,  new_weight, new_height))
        im.save(image)
    else:
        print("The image %s doesn't need to be resized." % image)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter. Try to execute 'python 0005.py $dir_path'")
    else:
        for dir_path in sys.argv[1:]:
            for image_name in os.listdir(dir_path):
                image_path = os.path.join(dir_path, image_name)
                resize_image(image_path)

