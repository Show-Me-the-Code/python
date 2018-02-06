#0022 iphone5 image
from PIL import Image
import os

path = "../0005/image"
trans_path ="./trans_image"
iphonesize = {"iphone5":(640,1136),"iphone6s":(1125,2000),"iphone6sp":(1242,2208)}


filelists = os.listdir(path)
for f in filelists:
    filename = os.path.join(path,f)
    try:
        im = Image.open(filename)
    except IOError:
        print ("error read file")
        
    for phonetype in iphonesize.keys():
        thum = im.copy()
        thum.thumbnail(iphonesize[phonetype])
        newfilename = trans_path+"/"+phonetype+"_"+f
        thum.save(newfilename)
        thum.close()
        
im.close()
