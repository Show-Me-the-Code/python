#!/usr/bin/env python3
#change the resolution of pics in dir 'test' to at most 1136*640 for iphone5, 1334*750 for iphone6, or 1920*1080 for iphone6 Plus.
from PIL import Image
import os

def main():
    os.chdir('test')
    flag = input("Which shen do you use?\n1:iphone5\n2:iphone6\n3:iphone Plus")
    for root,dirs,files in os.walk(os.getcwd()):
        for f in files:
            im = Image.open(f)
            if flag == 1:
                if im.size[0] > 1136:
                    im.resize([1136,im.size[1]])
                if im.size[1] > 640:
                    im.resize([im.size[0],640])
            elif flag == 2:
                if im.size[0] > 1334:
                    im.resize([1136,im.size[1]])
                if im.size[1] > 750:
                    im.resize([im.size[0],750])
            elif flag == 3:
                if im.size[0] > 1920:
                im.resize([1136,im.size[1]])
                if im.size[1] > 1080:
                    im.resize([im.size[0],1080])
            else:
                print("Input fault.")
            im.save('test_'+im.filename)

if __name__=='__main__':
    main()
