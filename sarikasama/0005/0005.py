#!/usr/bin/env python3
#change the resolution of pics in dir 'test' to at most 1136*640 for iphone5
from PIL import Image
import os

def main():
    os.chdir('test')
    for root,dirs,files in os.walk(os.getcwd()):
        for f in files:
            im = Image.open(f)
            if im.size[0] > 1136:
                im.resize([1136,im.size[1]])
            if im.size[1] > 640:
                im.resize([im.size[0],640])
            im.save('test_'+im.filename)

if __name__=='__main__':
    main()
