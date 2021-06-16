# 使用 Python 生成类似于下图中的字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# generate the random code
def char():
    return chr(random.randint(65, 90))


def color(type):
    if type == 1:
        return (random.randint(0, 125), random.randint(0, 125), random.randint(0, 125))
    elif type == 2:
        return (random.randint(126, 255), random.randint(126, 255), random.randint(126, 255))


fontSize = 45
width = int(fontSize * 1.5 * 4)
height = int(fontSize * 1.5)

# create image instance
image = Image.new('JPG', (width, height), (255, 255, 255))
# create font instance
font = ImageFont.truetype("/Library/Fonts/Skia.ttf", 30)
# start ot draw
draw = ImageDraw.Draw(image)

# fill the whole picture
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=color(2))

# fill the text
for t in range(4):
    draw.text((t * height + fontSize * 0.8, fontSize * 0.8), char(), font=font, fill=color(2))

image.show()
