#coding=utf-8
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy,random,numexpr
path = os.path.split(os.path.realpath(__file__))[0]
NewArray = numpy.zeros((100,300,3),dtype=numpy.uint8)
Sh = NewArray.shape
for i in range(Sh[0]):
	for j in range(Sh[1]):
		for k in range(Sh[2]):
			NewArray[i][j][k]=random.randint(0,255)
im = Image.fromarray(NewArray)
D = ImageDraw.Draw(im)
L = [chr(i+65) for i in range(26)]+[chr(i+97) for i in range(26)]
for i in range(4):
	D.text((75*i+10+random.randint(-10,10),random.randint(0,40)), random.choice(L), font=ImageFont.truetype(os.path.split(path)[0]+"/public/msyh_3.ttf",55),fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
im.save(path+"/code.jpg")