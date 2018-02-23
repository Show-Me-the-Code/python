from PIL import Image
import string
import os


#config
PIC_PATH = './Sources/pics/'
RES_X = 1136
RES_Y = 640
# iphone 5 resolution: 1136*640

def modPic(picpath):

    im = Image.open(picpath);
    im_x, im_y = im.size;
    im.thumbnail((RES_X, RES_Y));
    im.save(picpath, 'JPEG');
    im.close();
    return 'successfully transform picture ' + string.split(picpath)[0];

if __name__ == '__main__':
    ls = os.walk(PIC_PATH).next()[2];
    for f in ls:
        if(f != '.DS_Store'):
            print modPic(PIC_PATH + f);
