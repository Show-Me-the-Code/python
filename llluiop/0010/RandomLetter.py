#!/usr/bin.env python



from random import choice
import string
import Image
import ImageDraw
import ImageFont
import ImageFilter

def generateRandomLetters():
    return ''.join([choice(string.ascii_uppercase) for x in range(4)])


def createVerifyImg(str):
    img = Image.new('RGB', (240,60), (255,255,255))
    font = ImageFont.truetype('DejaVuSansMono.ttf', 36)
    draw = ImageDraw.Draw(img)

    for x in range(240):
        for y in range(60):
            draw.point((x,y), tuple([choice(range(128,255)) for color in range(3)]))



    for x in range(len(str)):
        draw.text((60 * x + 10, 10), str[x], tuple([choice(range(32,127)) for color in range(3)]), font)

    img = img.filter(ImageFilter.BLUR)
    return img



if __name__ == "__main__":
    img = createVerifyImg(generateRandomLetters())
    img.show()
    img.save("verifyImg.jpg")
