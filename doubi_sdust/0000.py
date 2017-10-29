'''

第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

'''
from PIL import Image, ImageDraw, ImageFont
#PIL https://pillow.readthedocs.org/
def add_num(img):
    draw = ImageDraw.Draw(img)
    #加载TrueType或OpenType字体文件，并创建一个字体对象。
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=20)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), '2', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')
    return 0

image = Image.open('image.jpg')
print(image.format,image.size,image.mode)
add_num(image)