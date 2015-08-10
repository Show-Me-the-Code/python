# 图片右上角添加数字
from PIL import Image, ImageFont, ImageDraw


def add_badge(input_file, output_file, fontsize, margin=0, output_size=None):
    ''' 先压缩后添加标识符 '''
    im = Image.open(input_file)
    if output_size:
        im = im.resize(output_size)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('SourceCodePro-Black', fontsize)
    location = (im.width - margin - fontsize, margin)

    draw.text(location, '4', font=font, fill=(255, 0, 0))
    im.save(output_file)


if __name__ == '__main__':
    add_badge('logo.jpg', 'logo_with_badge.jpg', 80, output_size=(300, 300))
