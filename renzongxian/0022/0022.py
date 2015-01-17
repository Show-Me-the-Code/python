# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-12-24
# Python 3.4

"""

第 0022 题： iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。

"""

from PIL import Image
import os
import sys


def resize_image(image, t_weight, t_height):
    im = Image.open(image)
    weight, height = im.size
    if weight > t_weight or height > t_height:
        dw = weight / t_weight
        dh = height / t_height
        ds = max(dw, dh)
        new_weight = int(weight / ds)
        new_height = int(height / ds)
        im = im.resize((new_weight, new_height))
        print("Succeed to resize the image %s to %s*%s " % (image,  new_weight, new_height))
        im.save(image)
    else:
        print("The image %s doesn't need to be resized." % image)


if __name__ == "__main__":
    trans_weight = 0
    trans_height = 0
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter. Try to execute 'python 0022.py $dir_path'")
    else:
        while True:
            flag = input("请选择你要转换的分辨率: 1. iPhone 6  2. iPhone 6 Plus:")
            if flag == '1':
                trans_weight = 750
                trans_height = 1334
                break
            elif flag == '2':
                trans_weight = 1080
                trans_height = 1920
                break
            else:
                print("输入有误，重新选择!")
        for dir_path in sys.argv[1:]:
            for image_name in os.listdir(dir_path):
                image_path = os.path.join(dir_path, image_name)
                resize_image(image_path, trans_weight, trans_height)

