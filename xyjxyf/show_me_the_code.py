# coding = utf-8

from tools import imager
from PIL import ImageFont


# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字
def add_num(image_path):
    im = imager.open_image(image_path)
    if im is not None:
        font = ImageFont.truetype('Arial.ttf', 20)
        w, h = im.size
        point = (w - 10, 0)
        imager.draw_text(im, "8", point, font)
        im.show()


import uuid
# 第 0001 题：使用 Python 生成 200 个激活码（或者优惠券）
def create_activation_code(num=200):
    codes = []
    for i in range(num):
        code = str(uuid.uuid1())
        code = code.replace('-', '')
        codes.append(code)

    return codes


# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

# 第 0008 题：一个HTML文件，找出里面的正文。

# 第 0009 题：一个HTML文件，找出里面的链接。


# 第 0010 题：使用 Python 生成字母验证码图片
def create_verification_code():
    im, str = imager.verification_code()
    im.show()

if __name__ == "__main__":
    # add_num("./header.jpg")
    # create_verification_code()
    create_activation_code()