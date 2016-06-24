from PIL import Image, ImageDraw, ImageFont

def add_num(num, fill, font_name):
    im = Image.open('in.jpg')
    xsize , ysize = im.size
    draw = ImageDraw.Draw(im)
    text = str(num)
    font = ImageFont.truetype(font_name, xsize//3)
    draw.text((ysize//5 * 4, 0), text, fill, font)
    im.save("out.jpg")

num = 4
fill = (255, 0, 255)
font_name = "verdana.ttf"
add_num(num, fill, font_name)