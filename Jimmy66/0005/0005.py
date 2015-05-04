#!/bin/env python
# -*- coding: utf-8 -*- 

#随便查了下为iphone5的分辨率为1136x640像素，因为自己也不用，所以不清楚，也懒得具体求证了

#导入模块,顺便一提我在OS X 环境下用的是pillow，直接pip安装PIL老是出错，希望能帮到遇到同样问题的人
from PIL import Image
import glob

#得到当前目录下的图片文件列表
def get_list():
	return  glob.glob('*.jpg')

#图像处理
def  image_process(imagename,number):
	im = Image.open(imagename)
	im2 = im.resize((1136,640))
	number = str(number)
	im2.save('./'+number+'.jpg', 'jpeg')

#主函数，循环遍历图像列表进行处理
def  main():
	imagelist = get_list()
	n = 1
	for name in imagelist:
		image_process(name,n)
		n += 1

if __name__ == '__main__':
	main()

