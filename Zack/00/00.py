from PIL import Image,ImageDraw,ImageFont

im = Image.open('image.png')
w,h = im.size

font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 200)
draw = ImageDraw.Draw(im)
draw.text((w*4/5,h/5),'4',(255,0,0),font=font)
im.save('new_image.png')