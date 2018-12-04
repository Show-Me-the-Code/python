import os


if __name__ == '__main__':

    s1 = os.getcwd() + "\\tests.txt"
    print("初始文件路径：", s1)
    s2 = os.path.splitext(s1)
    print("文件路径分离后：", s2)
    print("*********************")
    name, span = s2
    print("文件名："+name+'\n'+"后缀："+span)
    new_name = name +"_new" + span
    print("构造后新的文件路径：", new_name)