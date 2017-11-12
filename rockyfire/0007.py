#0007
import os


def get_text_file_by_walk(path):
    path_list = []
    for dirpath_str, dirnames_list, filenames_list in os.walk(path):
        for i in filenames_list:
            file_ext = i.split('.')[-1]
            img_ext = ['txt', 'java', 'py', 'xml']
            if file_ext in img_ext:
                path_list.append(os.path.join(dirpath_str, i))
    return path_list


dicts = {
    "注释": 0,
    "空行": 0,
    "代码": 0,
    "总行": 0,
}


def parse_txt(text):
    str_list = text.split('\n')  # String[]
    note = ['#', '//', '/*', '*/', '<!--', '-->']
    for string in str_list:
        # if string.find(note[index]) != -1:
        #     dicts["注释"] = dicts.get("注释") + 1
        # elif string == "":
        #     dicts["空行"] = dicts.get("空行") + 1
        # else:
        #     dicts["代码"] = dicts.get("代码") + 1
        dicts["总行"] = dicts.get("总行") + 1
        for x in note:
            if string.find(x) != -1:
                dicts["注释"] = dicts.get("注释") + 1
        if string == "":
            dicts["空行"] = dicts.get("空行") + 1

        dicts["代码"] = dicts.get("总行") - dicts.get("空行") - dicts.get("注释")
    print("----")
    for key, value in dicts.items():
        print(key, value)


text = get_text_file_by_walk("/pythontext/PythonNotes/test")
for i in text:
    with open(i, "r") as f:
        # print (f.read())
        parse_txt(f.read())
