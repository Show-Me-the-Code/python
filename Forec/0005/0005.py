from PIL import Image, ImageOps
import os, os.path

L = [ x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.jpg' ] 

for x in L:
    img = Image.open(x)
    xsize, ysize = img.size
    xsize = 500
    ysize = ysize * 500 // xsize
    img = ImageOps.fit(img,(xsize,ysize))
    img.save("out"+x)