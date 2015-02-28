#-*- coding: utf-8-*-

# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:Burness Duan
# Date:2014-12-29
# Python 3.3


import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def random_string(y):
	'''
	生成指定长度的随机字符串
	'''
	return ''.join(random.choice(string.ascii_letters) for x in range(y))


def create_verifi_image(strs,
	size=(120, 30),
	img_type = 'jpg',
	mode = 'RGB',
	bg_color= (255, 255, 255),
	fg_color = (0, 0, 255),
	font_size =18,
	font_type = 'ahronbd.ttf',
	draw_lines=True,
	n_line=(1, 2),
	draw_points=True,
	point_chance = 2,
	):

	width, height = size
	img = Image.new(mode, size, bg_color)
	draw = ImageDraw.Draw(img)
	if draw_lines:
		line_num = random.randint(*n_line)
		for i in range(line_num):
			begin = (random.randint(0, size[0]), random.randint(0, size[1]))
			end = (random.randint(0, size[0]), random.randint(0, size[1]))
			draw.line([begin, end], fill=(0, 0, 0))

	if draw_points:
		chance = min(100, max(0, int(point_chance)))
		for w in range(width):
			for h in range(height):
				tmp = random.randint(0,100)
				if tmp >100 -chance:
					draw.point((w,h),fill =(0,0,0))
	font = ImageFont.truetype(font_type, font_size)
	font_width, font_height = font.getsize(strs)
	draw.text(((width-font_width)/3,(height-font_height)/3),strs,font=font, fill=fg_color)
	params = [1 - float(random.randint(1, 2)) / 100, 0, 0, 0, 1 - float(random.randint(1, 10)) / 100, 
	float(random.randint(1, 2)) / 500,
	0.001,
	float(random.randint(1, 2)) / 500
	]
	img = img.transform(size, Image.PERSPECTIVE, params)
	img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
	return img


if __name__ == '__main__':
	strs = random_string(4)
	code_img = create_verifi_image(strs)
	code_img.show()
	code_img.save('validate.jpg')




