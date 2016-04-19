# coding = utf-8

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from tools import colorer, stringer
import types, os


# 打开
def open_image(image_path=None):
    if image_path is None or len(image_path) == 0:
        return None

    im = Image.open(image_path)
    return im


# 显示
def show_image(image_path=None):
    im = open_image(image_path)
    im.show()


# 保存
def save(image=None, to_path=None):
    if image is None or to_path is None or len(to_path) == 0:
        return

    f, e = os.path.splitext(to_path)
    if e is None or len(e) == 0:
        image.save(to_path, "JPEG")
    else:
        image.save(to_path)


# 大小
def image_size(image=None):
    ret_size = (0, 0)

    if image is None:
        return ret_size

    return image.size


# 拷贝
def image_copy(image=None):
    if image is None:
        return None

    return image.copy()


# 裁剪
def image_crop(image=None, box=None):
    if image is None or box is None:
        return None

    return image.crop(box)


# 压缩
def get_thumb(image=None, ratio=0.6):
    if ratio > 1:
        return image
    if ratio <= 0 or image is None:
        return None

    w, h = image.size()

    return image.thumbnail((w * ratio, h * ratio))

# # 合并
# def paste(image=None, sub_image=None, origin=(0, 0)):
#     if image is None or sub_image is None:
#         return None
#
#     im = image
#     if type(image) is types.StringType:
#         im = Image.open(image)
#         if im is None:
#             return None
#
#     sub_im = sub_image
#     if type(sub_image) is types.StringType:
#         sub_im = Image.open(sub_image)
#         if sub_im is None:
#             return None
#
#     im_size = im.size
#     sub_size = sub_im.size
#     # 如果sub_image在image范围内,不需要创建新的图片
#     if origin[0] >= 0 and origin[1] >= 0:
#         right = origin[0] + sub_size[0]
#         bottom = origin[1] + sub_size[1]
#         if right <= im.size[0] and bottom <= im_size[1]:
#             return im.paste(sub_im, (origin(0), origin(1), right, bottom))
#
#     right = im_size(0)
#     if im_size(0) < sub_size(0):
#         width = sub_size(0)
#     height = im_size(1)
#     if im_size(1) < sub_size(1):
#         height = sub_size(1)
#
#
#     image = Image.new('RGB', (width, height), (255, 255, 255))
#
#
#     return im.paste(sub_im, box)


# 添加文字
def draw_text(image=None, text=None, origin=(0, 0), font=None, fill='red'):
    if image is None or text is None or len(text) == 0:
        return None

    context = ImageDraw.Draw(image)
    context.text(origin, text, font=font, fill=fill)
    return image


# 旋转
def image_rotate(image=None, rotate=0):

    if image is None:
        return None

    if rotate == 0:
        return image

    return image.rotate(rotate)


# 转换色彩模式, mode: 'P'虚化,'L'或者'1'黑白,'LA'怀旧
def image_convert(image=None, mode='P'):
    if image is None:
        return None

    return image.convert(mode)


# 生成验证码图片:数字和字母
def verification_code(num=4, width=240, height=60, font_size=30):
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Arial.ttf', font_size)
    draw = ImageDraw.Draw(image)

    # 背景填充
    for x in range(width):
        for y in range(height):
            draw.point((x, y), colorer.randRGB(min=64))

    # 文字
    tw = width / num
    margin = (tw - font_size) / 2
    ty = (height - font_size) / 2
    tx = margin
    str = ""
    for t in range(num):
        char = stringer.rand_char()
        draw.text((tx, ty), char, font=font, fill=colorer.randRGB(0, 100))
        tx = tx + tw
        str = str + char

    # 模糊效果
    image = image.filter(ImageFilter.BLUR)

    return image, str

# 生成中文验证码

# 重置图片大小
def reset_image_size(image=None, max_width=None, max_height=None):
    if image is None or max_width is None or max_height is None:
        return

    if image.size[0] <= max_width and image.size[1] <= max_height:
        return

    rotate = image.size[0] / image.size[1]
    if rotate > 1:
        new_width = max_width
        new_height = max_width / rotate
    else:
        new_height = max_height
        new_width = max_height * rotate

    new_image = image.resize((int(new_width), int(new_height)), Image.BILINEAR)
    return new_image
