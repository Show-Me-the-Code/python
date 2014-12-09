from PIL import Image, ImageDraw, ImageFont
text = "52"
im = Image.open('1.bmp')
w,h = im.size
font_size = h//4

draw = ImageDraw.Draw(im)
font = ImageFont.truetype ("Arial.ttf",font_size)

text_w,text_h = draw.textsize(text,font=font) 
draw.text((w-text_w,0), text, fill=(255,0,0), font=font)


im.save('heihei.bmp')
