from PIL import Image, ImageDraw, ImageFont

def add_number(img):
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('ARLRDBD.TTF', 30)
    width, height = img.size
    draw.text((width*0.8,0),"12",font=fnt,fill="#ff0000")
    img.save("newImage.jpg")

if __name__ == "__main__":
    im = Image.open("image.jpg")
    add_number(im)