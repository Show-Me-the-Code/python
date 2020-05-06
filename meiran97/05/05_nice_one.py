# -*- coding: utf-8 -*-
# **第 0005 题：**
# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
# 学习了os.listdir(), join, mkdir


from PIL import Image
import os

path = './pics'
resultPath = './result'
if not os.path.isdir(resultPath):
    os.mkdir(resultPath)
for picName in os.listdir(path):
    picPath = os.path.join(path, picName)  # 注意这里以上的部分
    print(picPath)
    with Image.open(picPath) as im:
        w, h = im.size
        n = w / 1366 if (w / 1366) >= (h / 640) else h / 640
        im.thumbnail((w / n, h / n))
        im.save(resultPath+'/finish_' + picName.split('.')[0] + '.jpg', 'jpeg')