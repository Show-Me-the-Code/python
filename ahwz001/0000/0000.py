#coding:utf-8
"""
* 0000
* by ahwz001
* 2017/7/22
"""
from PIL import Image, ImageDraw, ImageFont

def addNumToImg(img):
    drawImg = ImageDraw.Draw(img) # 创建一个绘画对象，在img上面画
    font = ImageFont.truetype("wqy-microhei.ttc",40) # ImageFont对象
    # print(img.size)
    drawImg.text((img.width-40, 20),"5",(255, 0, 0),font) # 确定好坐标不能超了！！！
    img.save("modified.jpg","jpeg") # 保存修改后的图片，（修改后的名字，格式）

    modified_img = Image.open("modified.jpg")
    modified_img.show()


if __name__ == '__main__':
    img = Image.open("me.jpg")
    addNumToImg(img)
    img.close()