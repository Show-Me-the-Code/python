#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jinyang'

from PIL import Image
import glob

def reSize(dirPath, sizeX = 100, sizeY = 100):
    for file in glob.glob(dirPath + '*.jpg'):
        print file
        ori = Image.open(file)
        modi = ori.resize((sizeX, sizeY))
        #modi.save(os.path.splitext(file)[0] + '_modifid' + '.jpg')

if __name__ == '__main__':
    reSize('pics/', 300, 200)