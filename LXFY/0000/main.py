from PIL import Image, ImageDraw, ImageFont

def add_num(filePath, num=1):
    img = Image.open(filePath)
    size = img.size
    fontsize = size[1]/4
    myfont = ImageFont.truetype('Futura.ttf', fontsize)
    ImageDraw.Draw(img).text((2 * fontsize, 0), str(num), font = myfont, fill = 'red')
    img.save('avatar_added.jpg')
    img.show()