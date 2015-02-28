import os
from PIL import Image

def resize(path):
    im = Image.open(path)
    w,h = im.size
    if w>640:
        x = w/640.0
        w=640
        h = int(h//x)
    if h>1136:
        x = h/1136.0
        h=1136
        w = int(w//x)
    print w,h
    im = im.resize((w,h),Image.ANTIALIAS)
    im.show()
    im.save(path)

path = 'img/'
dirlist = os.listdir(path)

for img in dirlist:
    abspath = os.path.join(path,img)
    if os.path.isfile(abspath):
        resize(abspath)
