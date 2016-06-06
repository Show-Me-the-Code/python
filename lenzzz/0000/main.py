from PIL import Image,ImageDraw,ImageFont

im = Image.open("pic.jpg")
x,y = im.size
font = ImageFont.truetype("verdana.ttf", x/3)
dr = ImageDraw.Draw(im)
dr.text((3*x/4,0),font=font,text="4",fill="#FF0000")
im.save("pictuer_has_number.jpg")



