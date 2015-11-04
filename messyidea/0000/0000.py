# -*- coding: utf-8 -*- 
import Image, ImageDraw, ImageFont

org = Image.open('./origin.jpg')
draw = ImageDraw.Draw(org)
font = ImageFont.truetype('Arial.ttf', 36)
w, h = org.size
fontsize = min(w, h) / 4
draw.text((org.size[0] - fontsize), '3', font = font, fill = (255, 0, 0))
org.save('rst.jpg', 'jpeg')
