from PIL import Image
import os
from os.path import join

#iPhone 5 display resolution
i5size = (1136, 640)
def change_size(picdir):
    
    for root, dirs, files in os.walk(picdir):
        for name in files:
            filename = join(root, name)
            print filename
            change_picsize(filename)
            
            
def change_picsize(filename):
    im = Image.open(filename)
    w = im.width;
    h = im.height;
    
    if(w > i5size[0]):
        im = im.resize((i5size[0], h))
    else:
        pass

    if(h > i5size[1]):
        im = im.resize((im.width, i5size[1]))
    else:
        pass
    im.save(filename.split('.')[0] + '2.jpg')
            
if __name__ == '__main__':
    change_size('test')


