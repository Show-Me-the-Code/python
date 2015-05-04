#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 30987
# @Date:   2015-01-12 16:06:03
# @Last Modified by:   30987
# @Last Modified time: 2015-01-12 17:03:30
#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont
class Image_unread_message:
	def open(self,path):
		self.im=Image.open(path)
		return True
	def __init__(self):
		self.fnt=None
		self.im=None

	def setFont(self,font_path,size):
		self.fnt=ImageFont.truetype(font_path,size)
		return True
	def draw_text(self,position,str,colour,fnt):
		draw=ImageDraw.Draw(self.im)
		draw.text(position,str,fill=colour,font=fnt)
		self.im.show()
		self.im.save(str+'num'+'.jpg')
		return True


test=Image_unread_message()
test.open('1.png')
test.setFont('ahronbd.ttf',80)
test.draw_text((200,-20),'4',(255,0,0),test.fnt)

