#!"C:\Python34\python.exe"

from PIL import Image, ImageDraw, ImageFont
import sys, os, random

num = str(random.randint(1,99))
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('c:/windows/fonts/Arial.ttf', size=40)
    fillcolor =  "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), num, font=myfont, fill=fillcolor)
    img.save('C:/java/pythonProjects/Learning/YixiaohanDailyTask/0000/0000-02-result.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    image = Image.open('C:/java/pythonProjects/Learning/YixiaohanDailyTask/0000/image.jpg')
    add_num(image)