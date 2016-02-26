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


# 第 0001 题：使用 Python 生成 200 个激活码（或者优惠券）
import uuid

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
import re

def number_of_words(file_path=None):
    num = 0

    if file_path is None:
        return num

    file = open(file_path, 'r')
    content = file.read()
    content = " " + content
    pattern = re.compile(u'\s+\w+')
    match = pattern.findall(content)
    num = len(match)

    return num


# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
def reset_images_size(dir_path=None):
    if dir_path is None:
        return

    for root, dirs, files in os.walk(dir_path):
        for path in files:
            if path.startswith("."):
                continue

            file_path = os.path.join(root, path)
            image = imager.open_image(file_path)
            if image is not None:
                new_image = imager.reset_image_size(image, 640, 1136)
                imager.save(new_image, file_path)

# 第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
import os

# 注释://, #, /* */, """ """, ''' '''
def lines_of_codes(dir_path=None):
    code_num = 0
    note_num = 0
    blank_line_num = 0
    if dir_path is None:
        return code_num, note_num, blank_line_num

    for root, dirs, files in os.walk(dir_path):
        mut_note = None
        for path in files:
            if path.startswith("."):
                continue

            file_path = os.path.join(root, path)
            for count, line in enumerate(open(file_path, "rU")):

                # 判断是否是空行
                if not line.split():
                    blank_line_num += 1
                    continue

                # 判断是否多行注释
                if mut_note is not None:
                    note_num += 1
                    match_note = re.match("\*/|\"\"\"|\'\'\'", line)
                    if match_note is not None:
                        mut_note = None
                        match_note = re.match("\/\*|\"\"\"|\'\'\'", line)
                        if match_note is not None:
                            mut_note = line[match_note.pos:(match_note.endpos - 1)]

                    continue
                else:
                    match_note = re.match("\/\*|\"\"\"|\'\'\'", line)
                    if match_note is not None:
                        note_num += 1
                        mut_note = line[match_note.pos:(match_note.endpos - 1)]
                        continue

                # 判断单行注释
                match_note1 = re.match("\s*(#|//).*\n*", line)
                if match_note1 is not None:
                    note_num += 1
                    continue

                pass

            code_num += count + 1

    return code_num, note_num, blank_line_num

# 第 0008 题：一个HTML文件，找出里面的正文。

# 第 0009 题：一个HTML文件，找出里面的链接。


# 第 0010 题：使用 Python 生成字母验证码图片
def create_verification_code():
    im, str = imager.verification_code()
    im.show()


if __name__ == "__main__":
    # 0000
    # add_num("./0000.jpg")

    # 0001
    # create_activation_code()

    # 0002

    # 0003

    # 0004
    # number_of_words("./0004.txt")

    # 0005
    reset_images_size("./0005")

    # 0007
    # code, note, blank_line = lines_of_codes("./0007")
    # print("代码行数:%i\n注释行数:%i\n空行行数:%i" % (code, note, blank_line))

    # 0010
    # create_verification_code()
