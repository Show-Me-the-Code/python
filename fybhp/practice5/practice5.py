# -*- coding:utf-8 -*-
from __future__ import division
from PIL import Image
import os

#按比例缩放
picdir = r'./pic'
file_list = os.walk(picdir)
thumbdir = r'./iphone5/'
ip5lo = 1136
ip5sh = 640
if not os.path.exists(thumbdir):
    os.mkdir(thumbdir)
for root, dirs, files in file_list:
    #print file
    for file in files:
        filedir = os.path.join(picdir,file)
        img = Image.open(filedir)
        imgSize = img.size
        lo = max(imgSize)
        sh = min(imgSize)
        rate = lo/sh
        newfiledir = os.path.join(thumbdir,file)
        if sh > ip5sh or lo > ip5lo :
            #此处亦有两种方法 sh2 = ip5lo/rate，再进行四种分类。
            #可将两方法相比，计算收缩比率，收缩比率小的获胜，有必要时再如此处理吧。
            lo2 = ip5sh*rate
            print lo2
            if lo2 > ip5lo and imgSize[0] > imgSize[1]:
                    new_img = img.resize((ip5lo,int(ip5lo/rate)),Image.ANTIALIAS)
            elif lo2 > ip5lo and imgSize[0] < imgSize[1]:
                    new_img = img.resize((int(ip5lo/rate),ip5lo),Image.ANTIALIAS)
            elif lo2 < ip5lo and imgSize[0] > imgSize[1]:
                    new_img = img.resize((int(lo2),ip5sh),Image.ANTIALIAS)
            else:
                    new_img = img.resize((ip5sh,int(lo2)),Image.ANTIALIAS)
            new_img.save(newfiledir,quality = 100)
        else:
            img.save(newfiledir,quality = 100)
