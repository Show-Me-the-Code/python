from PIL import Image, ImageDraw, ImageFont


def add_num(filename, text='9', size=40, color='red'):
    a = Image.open(filename)
    print(a.size)
    f = ImageFont.truetype("arial.ttf", size)
    b = ImageDraw.Draw(a)
    x, y = a.size
    xy = (x - 40, y - 190)
    b.text(xy, text, fill=color, font=f)
    newname = "new" + filename
    a.save(newname)

if __name__ == "__main__":
    test = add_num("1.jpg")


