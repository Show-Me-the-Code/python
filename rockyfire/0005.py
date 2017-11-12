import os
from PIL import Image

def get_image_file(path):
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path=os.path.split(path)        # 返回一个路径的目录名和文件名
        file_ext=file_path[1].split('.')[-1] # 后缀
        img_ext=['bmp','jpeg','gif','pasd','png','jpg']

        if file_ext in img_ext:
            print (path)
    elif os.path.isdir(path):
        for  x in os.listdir(path):
            get_image_file(os.path.join(path,x))
    else:
        print ("complate")


# 前面的 os.listdir 可以列出 dir 里面的所有文件和目录，但不包括子目录中的内容。
# os.walk 可以遍历下面的所有目录，包括子目录。
def get_image_file_by_walk(path):
    path_list=[]
    for dirpath_str,dirnames_list,filenames_list in os.walk(path):
        for i in filenames_list:
            file_ext=i.split('.')[-1]
            img_ext = ['bmp', 'jpeg', 'gif', 'pasd', 'png', 'jpg']
            if file_ext in img_ext:
                path_list.append(os.path.join(dirpath_str,i))
    return path_list


path_list=get_image_file_by_walk('/pythontext/PythonNotes')
# path_list=get_image_file('/pythontext/PythonNotes')
for img_file in path_list:
    with Image.open(img_file) as f:
        im_ss=f.resize((1136,640))
        f,ext=os.path.splitext(img_file)
        im_ss.save(f+".jpg")
