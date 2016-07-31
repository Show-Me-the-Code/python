import os
from PIL import Image, ImageDraw, ImageFont
from random import randint


# s = "3"
# a = Image.open("1.jpg")
# f = ImageFont.truetype("arial.ttf", 40)
# b = ImageDraw.Draw(a)
# b.text((90, 90), s, fill='red', font=f)
# a.save("2.jpg")




def add_num(filename='1.jpg', text='?', size=40, color='red', newname="2.jpg"):
    a = Image.open(filename)
    print(a.size)
    f = ImageFont.truetype("arial.ttf", size)
    b = ImageDraw.Draw(a)
    x, y = a.size
    xy = (x - 40, y - 170)
    b.text(xy, text, fill=color, font=f)
    a.save(newname)


# add_num(text="3")

for root, dirs, files in os.walk("C:\\Users\\housh\\Desktop\\tx"):
    for file in files:
        print(type(file))
        add_num("C:\\Users\\housh\\Desktop\\tx\\" + file, newname='new' + file)