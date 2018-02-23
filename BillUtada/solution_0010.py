from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import string

#config
pic_width = 60 * 4;
pic_height = 60;
font_path = '/Library/Fonts/Arial Black.ttf';
image_path = '/Users/billutada/pythonPractice/Sources/VertifyCode';

if __name__ == '__main__':
    image = Image.new('RGB', (pic_width, pic_height), 'black');
    draw = ImageDraw.Draw(image);
    font = ImageFont.truetype(font_path, 55);
    for w in range(pic_width):
        for h in range(pic_height):
            draw.point((w, h), fill = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)));
    for i in range(0, 4):
        char = random.choice(string.letters + string.digits);
        draw.text((i*60 + 10, -10), char, font = font, fill = (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)));

    image = image.filter(ImageFilter.BLUR);
    image.save(image_path, 'JPEG');
