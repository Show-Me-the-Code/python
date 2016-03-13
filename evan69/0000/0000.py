# coding=utf-8
from PIL import Image,ImageFont,ImageDraw
import sys
def add_number(filename,number):
	mystr = str(min(99,number))
	al = 0.4
	if number > 99:
		mystr += '+'
		al = 0.25
	print mystr
	img = Image.open(filename)
	fontsize = min(img.size[0],img.size[1])
	print img.size
	fontsize = int(fontsize * al)
	font = ImageFont.truetype('Arial.ttf',size = fontsize)
	position = img.size[0] - font.getsize(mystr)[0]
	dr = ImageDraw.Draw(img)
	dr.text((position,0),mystr,font = font,fill = (255,0,0,255))
	return img

filename = sys.argv[1]
num = sys.argv[2]
add_number(filename,int(num)).save(num + '_' + filename)
