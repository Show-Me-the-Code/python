
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
verificationCode = ['K', 'L', 'K', 'B']


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255),
            random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))


width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)

# 背景
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 文字
for k in range(4):
    draw.text((60 * k + 10, 10), verificationCode[k], font=font, fill=rndColor2())

# 模糊

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
