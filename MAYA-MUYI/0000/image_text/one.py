from PIL import Image, ImageDraw, ImageFont

def img_addnum(img_name, num):
    #打开一个图像文件
    im = Image.open(img_name)

    #创建一个可以在给定图像上绘图的对象。
    draw = ImageDraw.Draw(im)

    #获得图像尺寸，也可以使用w,h = im.size
    w = im.width
    h = im.height

    #创建Font对象
    fnt = ImageFont.truetype('arial.ttf', int(h * 0.15))
    #输出文字
    draw.text((w * 0.9, h * 0.05), num, font=fnt, fill=(255, 0, 0, 128))
    #文件保存，第一个参数是保存路径，第二个是格式
    im.save(img_name.split('.')[0] + '2.jpg')





if __name__ == '__main__':
    img_addnum('cat.jpg', '1')



