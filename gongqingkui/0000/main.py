#--*-- encoding:utf-8 --*--
#Python 练习册，每天一个小程序
#https://github.com/Yixiaohan/show-me-the-code
#0000 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
from PIL import Image,ImageDraw,ImageFont

#add num to image
def addnum(image,num):
    with Image.open(image) as head:
        w,h = head.size
        font = ImageFont.truetype('arial.ttf',25)
        draw = ImageDraw.Draw(head)
        draw.text((0.8*w,0.1*h),str(num),fill=(255,0,0),font=font)
        head.save('head2.jpg')

if __name__ =='__main__':
    addnum('head.jpg',68)
