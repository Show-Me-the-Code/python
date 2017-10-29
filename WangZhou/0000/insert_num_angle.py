from PIL import Image, ImageDraw, ImageFont


def insert_angle_num(img):
    """
    Insert a num on the right-upper angle,then save the new image.
    :param img:string : filename of an Image object
    """
    with Image.open(img) as im:
        width, height = im.size
        draw_image = ImageDraw.Draw(im)
        color = '#ff0000'
        num_font = ImageFont.truetype('consolab.ttf', 100)
        draw_image.text((width - 80, 20), '7', font=num_font, fill=color)
        im.save('new_message.jpg')


if __name__ == "__main__":
    img = 'wz0000.jpg'
    insert_angle_num(img)
