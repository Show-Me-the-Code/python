from PIL import Image, ImageDraw, ImageFont, ImageColor


def drawPic(fileName):
    img = Image.open(fileName)
    x, y = img.size
    fnt = ImageFont.truetype("arial.ttf", size=30)
    draw = ImageDraw.Draw(img)
    draw.text((x - 50, 10), font=fnt, fill=128, text='14')
    img.show()
if __name__ == '__main__':
    drawPic('sample.png')
