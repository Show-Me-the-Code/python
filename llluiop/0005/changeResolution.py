#!/usr/bin/env python

from __future__ import division
import os
import Image


resolution_IP4 = (800, 600)

def ChgResolution(image):
    img = Image.open(image)
    ratio = max(img.size[0]/resolution_IP4[0], img.size[1]/resolution_IP4[1])
    if ratio > 1:
        imgNew = img.resize(( int(img.size[0]/ratio), int(img.size[1]/ratio) ))
        imgNew.save(os.path.split(image)[-1])



def ImageFiles(path):
    if os.path.exists(path):
        for file in os.listdir(path):
            if 'jpg' in file:
                yield os.path.join(path, file)

def main():
    for image in ImageFiles("images"):
        ChgResolution(image)



if __name__ == "__main__":
    main()
