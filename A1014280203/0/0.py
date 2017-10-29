from PIL import Image, ImageFont, ImageDraw

image = Image.open('0.png')
w, h = image.size
font = ImageFont.truetype('arial.ttf', 50)
draw = ImageDraw.Draw(image)
draw.text((4*w/5, h/5), '5', fill=(255, 10, 10), font=font)
image.save('0.0.png', 'png')
