import random
import string
from PIL import Image,ImageDraw,ImageFilter,ImageFont

class Create_Image():
    def __init__(self,width,height,font_sum):
        self.width=width
        self.height=height
        self.font_sum=font_sum

    # 随机颜色1:
    def rndColor(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 随机颜色2:
    def rndColor2(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    def create_image(self):
        global RGB_MAX
        #  1,Image.new()
        image = Image.new('RGB', (self.width, self.height), (RGB_MAX, RGB_MAX, RGB_MAX))
        #  2,字体样式
        font = ImageFont.truetype('SIMSUN.TTC', 36)
        #  3,图层
        draw = ImageDraw.Draw(image)
        
        #  4,填充每个像素:
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=self.rndColor())
        #  5,验证码
        for t in range(self.font_sum):
            # text:xy,第一个参数是xy 英文文档是Top left corner of the text. 置于左上角的位置
            draw.text((60 * t + 10, 10), random.choice(string.ascii_letters), font=font, fill=self.rndColor2())
        #  6,保存
        image.save('code.jpg', 'jpeg')
        image.show()
        # size=(123,123)
        # image.thumbnail(size) 缩略图
        # DETAIL：细节滤波
        image.filter(ImageFilter.DETAIL)
if __name__ == "__main__":
    width = 240
    height = 60
    RGB_MAX = 255

    img = Create_Image(width, height, 4)
    img.create_image()
