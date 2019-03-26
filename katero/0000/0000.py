"""
问题
0000：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
"""
from PIL import Image, ImageDraw, ImageFont, ImageColor

def write_num_on_img(filePath, num):
    img = Image.open(filePath)
    draw = ImageDraw.Draw(img)

    #设置数字颜色为红色
    colour = (255, 0, 0)
    #设置字体
    ttfont = ImageFont.truetype('C:/windows/fonts/Candara.ttf', 100)
    #位置，内容，颜色，字体
    draw.text((img.size[0]-60, 0), str(num), fill=colour, font=ttfont)

    #显示一幅已载入的图像
    img.show()
    img.save('restult.jpg')

if __name__ == '__main__':
    write_num_on_img("img.jpeg", 4)
