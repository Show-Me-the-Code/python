from PIL import Image
import glob, os

def resize():
    for files in glob.glob('*.jpg'):
        filepath,filename = os.path.split(files) #分割文件名和路径名
        fname,fext = os.path.splitext(filename)
        im = Image.open(files)
        w,h = im.size
        if w > 640:
            x = w/640.0
            w = 640
            h = int(h/x)
        if h>1136:
            x = h/1136.0
            h = 1136
            w = int(w/x)
        print(w, h)
        im0 = im.resize((w,h),Image.ANTIALIAS)
        im0.save('0005'+filename)

resize()
