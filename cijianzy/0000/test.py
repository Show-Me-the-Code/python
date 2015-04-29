import Image
import ImageDraw
import ImageFont
im = Image.open(u'test.jpg')

#im.show()
#n = im.size
x = ImageDraw.Draw(im)
n = im.size
font = ImageFont.truetype('arial.ttf', n[0]/5)

x.text((n[0]*4/5,0),"7",fill = (255,0,0),font = font)

im.show()
im.save('output.jpg','JPEG')
