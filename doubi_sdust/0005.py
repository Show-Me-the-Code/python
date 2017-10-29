'''
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
from PIL import Image
import os.path

def Size(dirPath, size_x, size_y):
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == '.jpg':
            img = Image.open(i)
            img.thumbnail((size_x,size_y))
            img.save(i)
            print(i)
Size('D:\PyCharm 2017.1.3\projects', 1136, 640)