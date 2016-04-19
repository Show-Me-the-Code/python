import Image
import ImageDraw
import ImageFont
im = Image.open(u'test.jpg')
#打开图片
x = ImageDraw.Draw(im)
#绘制图片
n = im.size
#得到大小
font = ImageFont.truetype('arial.ttf', n[0]/5)
#设置字体和字体大小
x.text((n[0]*4/5,0),"7",fill = (255,0,0),font = font)
#输入文字
#im.show()
im.save('output.jpg','JPEG')
#保存图片

