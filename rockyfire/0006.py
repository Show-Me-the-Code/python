#0006
import os
import time

def get_text_file_by_walk(path):
    path_list = []
    for dirpath_str, dirnames_list, filenames_list in os.walk(path):
        for i in filenames_list:
            file_ext = i.split('.')[-1]
            img_ext = ['txt']
            if file_ext in img_ext:
                path_list.append(os.path.join(dirpath_str, i))
    return path_list
dicts={}
def parse_txt(text):
    string=text.split("\n") #String[]
    sum=1
    for str in string:
        for wordstr in str.split(" "): #空格分割
            if wordstr == "":
                continue   
#           MapReduce
            if wordstr in dicts.keys(): 
                dicts[wordstr]=dicts.get(wordstr)+1
            else:
                dicts[wordstr]=sum
    print("----")
    for key,value in dicts.items():
        print (key,value)

text=get_text_file_by_walk("/pythontext/PythonNotes")
for i in text:
    with open(i,"r") as f :
        # print (f.read())
        parse_txt(f.read())
