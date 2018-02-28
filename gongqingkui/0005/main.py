#0005 iphone5 image
from PIL import Image
import os

path = "./image"
trans_path ="./trans_image"
iphone5size = (1136,640)

filelists = os.listdir(path)
for f in filelists:
    filename = os.path.join(path,f)
    try:
        im = Image.open(filename)
    except IOError:
        print ("error read file")
    thum = im.copy()
    thum.thumbnail(iphone5size)
    newfilename = trans_path+"/"+f
    thum.save(newfilename)
    im.close()
    thum.close()
