# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
涉及模块/库：
    1.Pillow
    2.os
    3.glob
核心方法:
    1.Image.resize(size, resample=0):
        Returns a resized copy of this image.
        此方法需立即执行.save()进行存储，否测resize信息失效
    2.Image.thumbnail(size, resample=1):
        Make this image into a thumbnail.
        略缩图方式更改分辨率
想法思路:
    1.对比图片的宽高是否满足要求分辨率
    2.获得图片原分辨率和目标分辨率的变化率
    3.比较宽度变化率和高度变化率，以大的一方为基准
    4.原分辨率除以基准，得到目标分辨率
'''

import glob, os
from PIL import Image
size = (640, 1136)

def resize(imagefile, name, ext):
    try:
        im = Image.open(imagefile)
    except:
        print('error')
    im.thumbnail(size)
    im.save(name + '_thum' + ext)

def resize2(imagefile, name, ext, awidth=640, aheight=1136):
    try:
        im = Image.open(imagefile)
    except:
        print('error')
    bwidth, bheight = im.size
    change_width = bwidth / awidth
    change_height = bheight / aheight
    if change_width or change_height > 1:
        change = change_width if change_width > change_height else change_height
        im.resize((int(bwidth/change), int(bheight/change))).save(name + 'thum' + ext)

if __name__ == '__main__':
    path = '.'
    for infile in glob.glob(path + "/*.jpg"): #匹配符查找文件
        filename, ext = os.path.splitext(infile) #分离文件名和扩展名
        resize2(infile, filename, ext)
