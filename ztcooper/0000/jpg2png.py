from __future__ import print_function
import os
from PIL import Image

all_files = os.listdir(os.curdir)   #获取所有文件
for infile in all_files:     
    f, e = os.path.splitext(infile)     #分离文件名与扩展名(f=name,e=extension)
    outfile = f + '.png'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)    #save()第二个参数指定图片格式
        except IOError:
            print('cannot convert', infile)
