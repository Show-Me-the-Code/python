#!/usr/bin/env python
#-*- coding: utf-8 -*-

import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_image(image_size = (300, 100),
			   background_color = (255, 255, 255),
			   font_type = "arialbd.ttf",
			   font_size = 50,
			   text_num = 4,
			   point_chance = 50):

	im = Image.new("RGB", image_size, background_color)
	draw = ImageDraw.Draw(im)
	image_width, image_height = image_size

	def create_text():
		text_font = ImageFont.truetype(font_type, font_size)
		font_width, font_height = text_font.getsize("A")
		for i in range(text_num):
			text = random.choice(string.ascii_uppercase)
			text_loc = ((image_width - font_width) / text_num * (i + 0.5), (image_height - font_height) / 2.3)
			draw.text(text_loc, text, font = text_font, fill = (random.randint(0, 255) / 2, random.randint(0, 255) / 2, random.randint(0, 255) / 2))

	def create_points():
		for w in range(image_width):
			for h in range(image_height):
				tmp = random.randint(0, 100)
				if tmp > point_chance:
					draw.point((w, h), fill = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
	
	create_text()
	create_points()
	im = im.filter(ImageFilter.BLUR)

	return im

if __name__ == "__main__":
	im = create_image()
	im.show()
