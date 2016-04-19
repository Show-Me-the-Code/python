#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: key
# @Date:   2015-11-16 15:48:35
# @Last Modified by:   key
# @Last Modified time: 2015-11-16 23:10:41

#---------------------------------
#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
#---------------------------------

import cv2
from PIL import Image,ImageFont,ImageDraw

DEBUG = True

#The picture size is 200px*200px

#opencv 3.0
def opencv(filename,num):
    img = cv2.imread(filename,1)
    font = cv2.FONT_HERSHEY_PLAIN
    width,height,channel = img.shape
    cv2.putText(img,str(num),(int(width*5/6),int(height/4)),font,3,(0,0,255),2,cv2.LINE_AA)
    cv2.imwrite("result_opencv.png",img)
    if DEBUG:
        cv2.imshow("Key",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

zho
#Pillow
def pillow(filename,num):
    img = Image.open(filename)
    x,y = img.size
    font = ImageFont.truetype("arial.ttf",int(x/3))
    ImageDraw.Draw(img).text((x*4/5,0),str(num),font=font,fill = 'red')
    img.save("result_pillow.png",)
    if DEBUG:
        img.show()

if __name__ == '__main__':
    opencv("alice_icon_sm.jpg",4)
    pillow("alice_icon_sm.jpg",4)




