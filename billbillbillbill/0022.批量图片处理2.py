#!/usr/bin/env python
#coding: utf-8
import Image, os

# 源目录
myPath = '/home/bill/Pictures/'
# 输出目录
outPath = '/home/bill/Pictures/output/'
# 记录不同iPhone型号分辨率
size_config = {
    'iPhone5': {
        'height': 1136,
        'weight': 640
        },
    'iPhone6': {
        'height': 1334,
        'weight': 750
        },
    'iPhone6Plus': {
        'height': 2208,
        'weight': 1242
        }
}


def processImage(filesource, destsource, name, imgtype, phonetype='iPhone5'):
    '''
    filesource是存放待转换图片的目录
    destsource是存放输出转换后图片的目录
    name是文件名
    imgtype是文件类型
    phonetype是手机类型
    '''
    maxsize = size_config[phonetype]
    imgtype = 'jpeg' if imgtype == '.jpg' else 'png'
    #打开图片
    im = Image.open(filesource + name)
    # 缩放比例
    rate = max(im.size[0]/float(maxsize['weight']) if im.size[0] > maxsize['weight'] else 0, im.size[1]/float(maxsize['height']) if im.size[1] > maxsize['height'] else 0)
    if rate:
        im.thumbnail((im.size[0]/rate, im.size[1]/rate))
    im.save(destsource + name, imgtype)


def run(myPath, outPath, phonetype):
    # 切换到源目录，遍历源目录下所有图片
    os.chdir(myPath)
    for i in os.listdir(os.getcwd()):
        # 检查后缀
        postfix = os.path.splitext(i)[1]
        if postfix == '.jpg' or postfix == '.png':
            processImage(myPath, outPath, i, postfix, phonetype)

if __name__ == '__main__':
    run(myPath, outPath, 'iPhone6')



