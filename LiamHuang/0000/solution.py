# coding: utf-8
"""
0000：
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
类似于图中效果 http://i.imgur.com/sg2dkuY.png?1

笔记参见：
http://liam0205.me/2015/04/22/pil-tutorial-basic-usage/
http://liam0205.me/2015/05/05/pil-tutorial-imagedraw-and-imagefont/
"""

from PIL import Image, ImageDraw, ImageFont

sourceFileName = "../public/source.png"
avatar         = Image.open(sourceFileName)
drawAvatar     = ImageDraw.Draw(avatar)

xSize, ySize = avatar.size
fontSize     = min(xSize, ySize) // 11

myFont       = ImageFont.truetype("/Library/Fonts/OsakaMono.ttf", fontSize)

drawAvatar.text([0.9 * xSize, 0.1 * ySize - fontSize],\
    "3", fill = (255, 0, 0), font = myFont)
del drawAvatar

avatar.show()
