#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-13 10:50:36
# @Last Modified by:   30987
# @Last Modified time: 2015-01-13 11:11:35
# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

from PIL import Image


def change_img(path,size=(1136,640)):
	im = Image.open(path)
	size=(size[1],size[0]) if im.size[1]>im.size[0] else size
	im.thumbnail(size,Image.ANTIALIAS) #后一个参数为滤镜
	im.save('result-'+path)
	#im.show()


if __name__ == '__main__':
	change_img('1.jpg')