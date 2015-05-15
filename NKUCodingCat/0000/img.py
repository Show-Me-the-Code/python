#coding=utf-8
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
path = os.path.split(os.path.realpath(__file__))[0]
src = path+"/img.jpg"
dst = path+"/res.jpg"
s = Image.open(src)
D = ImageDraw.Draw(s)
w,h = s.size
D.text((w-100,0), u"4", font=ImageFont.truetype(os.path.split(path)[0]+"/public/msyh_3.ttf",100),fill = (255,0,0))
s.save(dst)