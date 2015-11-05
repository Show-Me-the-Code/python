# -*- coding: utf-8 -*- 
import Image, ImageDraw, ImageFont

org = Image.open('./origin.jpg')
draw = ImageDraw.Draw(org)
w, h = org.size
fontsize = min(w, h) / 4
font = ImageFont.truetype('GenBkBasI.ttf', fontsize)
draw.text((w - fontsize, 0), '3', font = font, fill = (255, 0, 0))
org.save('rst.jpg', 'jpeg')
