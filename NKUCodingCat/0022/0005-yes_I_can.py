#coding=utf-8
from __future__ import division
import os
from PIL import Image
def transfer(img_path,dst_width,dst_height,dst_path):
	
	im = Image.open(img_path)
	s_w,s_h = im.size
	if dst_width/s_w < dst_height/s_h:
		ratio = dst_width/s_w
	else:
		ratio = dst_height/s_h
	resized_img = im.resize((int(ratio*s_w), int(ratio*s_h)), Image.ANTIALIAS)  
	resized_img.save(dst_path)
path = os.path.split(os.path.realpath(__file__))[0]+"/"
src = "img/"
dst = "dst_img/"
imgs = os.listdir(path+src)
for i in imgs:
	transfer(path+src+i,1136,640,path+dst+"5-"+i) #iphone5
	transfer(path+src+i,1334,750,path+dst+"6-"+i) #iphone6
	transfer(path+src+i,2208,1242,path+dst+"6+-"+i) #iphone6+