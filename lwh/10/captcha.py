"""
    生成图片验证码
"""
import PIL
import string
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

image_path = "C:\\Users\\lwhil\\Desktop\\captcha.jpg"
save_path = "C:\\Users\\lwhil\\Desktop\\captcha_f.jpg"
font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 60)
color = ["red", "black", "green", "blue", "yellow"]
letters = string.ascii_letters


def generate_captcha():
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    for i in range(1, 6):
        nums = str(random.randint(0, 9))
        width, height = image.size
        print(width, height)
        point = (50 + i * 100, 200 + random.randint(-100, 100))
        draw.text(point, nums, font=font, fill=color[random.randint(0, 4)])
    # image.rotate(90) #文档只有整张图片的倾斜效果,效果不好,不如不要

    # 产生模糊效果
    GaussBlur = ImageFilter.GaussianBlur(radius=5)
    image = image.filter(GaussBlur)

    image.save(save_path)

if __name__ == "__main__":
    generate_captcha()
