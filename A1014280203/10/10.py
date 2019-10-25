from PIL import Image, ImageFont, ImageDraw, ImageFilter
import string
import random


def make_rand_char():
    return random.choice(string.ascii_letters)


def generator_bgcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def generator_font_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def producer():
    width = 60*4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=generator_bgcolor())
    for i in range(4):
        draw.text((i*60+10, 10), make_rand_char(), font=font, fill=generator_font_color())
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

if __name__ == '__main__':
    producer()
