# -*- coding:utf-8 -*-
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

#设置字体，如果没有，也可以不设置
#font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf",13)

#打开底版图片
imageFile = "./icon.jpg"
im1=Image.open(imageFile)

# 在图片上添加文字 1
draw = ImageDraw.Draw(im1)
draw.text((90, 5),"2",(255,0,0))#,font=font)
draw = ImageDraw.Draw(im1)

# 保存
im1.save("./practice1/icon.png")