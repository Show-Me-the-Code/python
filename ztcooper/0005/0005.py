# 1136*640
from __future__ import print_function
import os
from PIL import Image

size = (1136, 640)
types = ['.jpg','.png','.gif']
all_files = os.listdir(os.curdir)
for file in all_files:
    if os.path.splitext(file)[1] in types:
        try:
            im = Image.open(file)
            h, w = im.size
            if h <= 1136 and w<= 640:
                print(file,'is ok')
            elif h < w:
                im.resize((1136,640), Image.ANTIALIAS)
                im.save(os.path.splitext(file)[0]+'new.jpg')
            else:
                im.resize((1136,640), Image.ANTIALIAS)
                im.save(os.path.splitext(file)[0]+'new.jpg')
        except IOError:
            print('cannot create')
                
