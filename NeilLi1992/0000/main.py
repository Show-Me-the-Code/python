from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

file_name = raw_input("Please input the image name, including file appendix: ")
try:
    img = Image.open("test.jpg")
    s = raw_input("Please input the number to display: ")
    try:
        num = int(s)
        img_width = img.size[0]
        img_height = img.size[1]

        font_size = 60 * img_height / 480
        font_height = 60
        font_width = 40
        text_x = img_width - font_width * len(str(num))
        text_y = 0

        font = ImageFont.truetype("Arial.ttf", font_size)

        draw = ImageDraw.Draw(img)
        draw.text((text_x, text_y), str(num), (255,0,0), font=font)

        img.save("new_image.jpg")
    except:
        print "The input is not a number!"
except:
    print "Can't find specified file!"
