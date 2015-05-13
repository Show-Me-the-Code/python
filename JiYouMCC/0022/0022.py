# using PIL in http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image


def change_image_size(image_path='0005.jpg', size=(1136, 640)):
    im = Image.open(image_path)
    size = (size[1], size[0]) if im.size[1] > im.size[0] else size
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('result-' + image_path)

change_image_size('0005-r.jpg')
change_image_size('0005.jpg')

# ip6
change_image_size(image_path='0005.jpg', size=(1334, 750))

# ip6plus
change_image_size(image_path='0005.jpg', size=(1920, 1080))
