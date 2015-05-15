#!/usr/bin/env python

'''
Draw a number on the image
'''

try:
	from PIL import Image
	from PIL import ImageDraw
	from PIL import ImageFont
except ImportError:
	import Image,ImageFont,ImageDraw

def draw_number(path = '/root/Desktop/1.jpg',num = 4):
	im = Image.open(path)#open the picture
	size = im.size#get the size of the picture
	fontsize = size[0]/4
	draw = ImageDraw.Draw(im)#the ImageDraw.Draw will rerturn a object then you can draw it
	font = ImageFont.truetype('/usr/share/fonts/dejavu/DejVuSans.ttf',fontsize)#define the font and size of the number 
	draw.text((3*fontsize,0),str(num),(255, 0, 0),font)#draw it 
	im.save('/root/Desktop/2.jpg')#save
draw_number()
