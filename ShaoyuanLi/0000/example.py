import Image,ImageDraw,ImageFont

myfont=ImageFont.truetype("arial.ttf", 35)
im=Image.open("touxiang.png")
draw=ImageDraw.Draw(im)
x,y=im.size
draw.text((x-x/5,y/8),"8",fill=(255,0,0),font=myfont)
im.save("result.png", "PNG")

