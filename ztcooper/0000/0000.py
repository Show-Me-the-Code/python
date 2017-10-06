from PIL import Image, ImageFont, ImageDraw

im = Image.open('0.jpg')
w,h = im.size
font = ImageFont.truetype('arial.ttf', 50)
draw = ImageDraw.Draw(im)
draw.text((4*w/6, h/6), '+1', fill=(255, 10,10), font=font)
im.save('0+.jpg', 'JPEG')
