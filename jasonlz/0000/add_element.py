# coding=utf-8
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont

def add_num(image, num):
	img = Image.open(image)
	x,y = img.size
	draw = ImageDraw.Draw(img)

	afront = ImageFont.truetype('arial.ttf', x/4)
	draw.text((3*x/4,0), str(num), (0,0,0), afront)
	del draw
	img.save('result.jpg')
	img.show();
if __name__ == '__main__':
	add_num('profile.jpg',99)