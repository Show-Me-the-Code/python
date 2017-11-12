#-*- coding:utf8 -*-

'''
  sudo apt-get update
  sudo apt-get install python-dev
  sudo apt-get install libtiff5-dev
  libjpeg8-dev zlib1g-dev
  libfreetype6-dev liblcms2-dev libwebp-dev
  tcl8.6-dev tk8.6-dev python-tk

  sudo pip3 install pillow

'''
# 把右上角图变成小图

infile="you.jpg"
outfile="you"

size=(80,80)

small_img=Image.open(infile)
small_img.thumbnail(size)
small_img.save(outfile,"JPEG")

region=Image.open(outfile).copy()
boxs=(img.size[0]-80,0,img.size[0],80)

img.paste(region,boxs)
img.save("you&me","JPEG")

# 参考 http://www.cnblogs.com/apexchu/p/4231041.html

# 水印

# http://www.cnblogs.com/apexchu/p/4231032.html

def text2img(text,font_color="Blue",font_size=25):
    """生成内容为 TEXT 的水印"""
    # 查看linux的字体 fc-list 字体目录: /usr/share/fonts/truetype/*
    # fc-list:lang=zh 中文字体
    # 新增字体 http://bbs.chinaunix.net/thread-2025374-1-1.html
    font=ImageFont.truetype('SIMSUN.TTC',font_size)

    mark_width=0
    (width,height) = font.getsize(text)
    if mark_width < width:
        mark_width = width
    mark_height =  height
    # Image.new(mode, size, color=None)
    # color的默认值是黑色
    mark=Image.new('RGBA',(mark_width,mark_height),(255, 0, 0))
    draw=ImageDraw.ImageDraw(mark,"RGBA")
    # draw.setfont(font)
    draw.text((0,0),text,fill=font_color,font=font)

    return mark

def set_opacity(im, opacity):
    """设置透明度"""

    assert opacity >=0 and opacity < 1
    if im.mode != "RGBA":
        im = im.convert('RGBA')
    else:
        im = im.copy()
    # Red（红色）Green（绿色）Blue（蓝色）和Alpha的色彩空间
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)

    im.putalpha(alpha)
    return im








