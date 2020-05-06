#第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

#get picture file names
import os
path = './pics/'
f_list = os.listdir(path)

from PIL import Image
for f in f_list:
   img = Image.open(path+f)
   img.thumbnail((1136,640))
   img.save('./new_pics/{}.jpg'.format(f))

