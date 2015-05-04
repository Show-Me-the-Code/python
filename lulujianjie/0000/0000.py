from PIL import Image, ImageDraw, ImageFont

im = Image.open('image.jpg')
w,h = im.size
font_size = h/4

draw = ImageDraw.Draw(im)
fnt = ImageFont.truetype ("Arial.ttf",font_size)

text_w,text_h = draw.textsize("8",font=fnt) # 给定文字message，返回所占像素(width,height)

draw.text((w-text_w,0), "8", fill=(255,0,0), font=fnt)#图片宽度减去字体宽度、要写的字符、颜色、字体


im.save('image_1.jpg')

#reference http://www.cnblogs.com/wei-li/archive/2012/04/19/2456725.html