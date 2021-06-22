from PIL import Image, ImageDraw, ImageFont


def add_num(num, fill, font_name, in_path, out_path):
    im = Image.open(in_path)
    x_size, y_size = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_name, x_size // 4, 0, 'UTF-8')
    draw.text((y_size // 5 * 4, 0), num, fill, font)

    im.save(out_path)


num = '4'
fill = (255, 0, 255)
font_name = "arial.ttf"
in_path = 'icon.png'
out_path = 'result.png'

add_num(num, fill, font_name, in_path, out_path)
