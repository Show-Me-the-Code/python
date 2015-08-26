__author__ = 'friday'

from PIL import Image, ImageDraw, ImageFont

def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('futura-normal.ttf', x // 3)
    ImageDraw.Draw(img).text((2 * x / 3, 0), str(num), font = myfont, fill = 'red')
    img.save('123_.jpg')

if __name__ == '__main__':
    add_num('123.jpg', 9)