from PIL import Image
import os

resultPath = 'result/'

# iphone 5 size
i5size = (1136, 640)

def change_size(dir_name):  
    for root, dirs, files in os.walk(dir_name):
        for name in files:
            filename = os.path.join(root, name)
            print(filename)
            change_picsize(filename, name)

def change_picsize(filename, picname):
    #打开一张图片
    pic = Image.open(filename)
    w, h = pic.size
    n = w / i5size[0] if (w / i5size[0]) >= (h / i5size[1]) else h / i5size[1]
    #文件缩放
    pic.thumbnail((w / n, h / n))
    #pic.save(resultPath + picname.split('.')[0] + '_new.' + picname.split('.')[1])
    im_name, im_ext = os.path.splitext(picname)
    pic.save(resultPath + im_name + '_new' + im_ext)

if __name__ == '__main__':
    change_size('tests')
