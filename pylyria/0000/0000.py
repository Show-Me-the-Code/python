# -*- coding: utf-8 -*-
#!/usr/bin/env python
#第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from PIL import Image, ImageFont, ImageDraw, ImageColor

def image_add(file_name, text):
  im = Image.open(file_name)
  w, h = im.size
  fnt = ImageFont.truetype('Arial.ttf', size=w//5)
  draw = ImageDraw.Draw(im)
  draw.text((w-w//5-10,10), font=fnt, fill=128, text=text)
  im.show()

if __name__ == '__main__':
  image_add('icon.jpg', 'V')
