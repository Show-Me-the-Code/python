#!"C:\Python34\python.exe"
#import Image
from  PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys, os, random

num = str(random.randint(1,99))
imagePath =os.path.join(sys.path[0], 'wechat.jpg')
savePath=os.path.join(sys.path[0], '0000-01-result-wechat_number.jpg')

def add_num(im, wDraw, hDraw):
    font =  ImageFont.truetype('arial.ttf', 30)
    draw =  ImageDraw.Draw(im)
    draw.ellipse(
        (radioX, radioY, radioX + 30, radioY + 30), fill ='red', outline='red')
    draw.text((wDraw, hDraw), num, font=font, fill='white')
    im.save(savePath, 'jpeg')

if __name__ == '__main__':
    im =  Image.open(imagePath)
    w, h = im.size
    print('Original image size:  %sx%s' %(w,h))
    wDraw = int(0.8 * w)
    hDraw = int(0.01 * h)
    radioX = wDraw
    radioY = hDraw
    print('radioX:', radioX)
    print('radioY:', radioY)
    add_num(im, wDraw, hDraw)