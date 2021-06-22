# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import os
'''
os.getcwd()：
获取当前代码文件所在路径。

os.walk()
获取指定路径下的路径、子文件夹（数组形式）、文档（数组形式），以迭代器格式返回。
'''

def change_resolution():
    # 变当前工作目录到指定的路径
    os.chdir('images')
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            im = Image.open(f)
            if im.size[0] > 1136:
                im.resize([1136, im.size[1]])
            if im.size[1] > 640:
                im.resize([im.size[0], 640])
            im.save('images/result' + im.filename)

change_resolution()
