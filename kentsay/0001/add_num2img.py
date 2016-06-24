"""
Question:
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
"""

import sys
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def add_number2img(image, number):
	font = ImageFont.truetype("/Library/Fonts/Chalkduster.ttf", 28)
	draw = ImageDraw.Draw(image)
	draw.text((200,0), str(number),(255, 255, 255), font=font)
	draw = ImageDraw.Draw(image)
	image.save("mask_with_num.png")
	image.show()


origin = Image.open("mask.png")
add_number2img(origin, sys.argv[1])