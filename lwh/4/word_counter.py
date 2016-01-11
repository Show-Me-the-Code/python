import re
#import collections.Counter
from collections import Counter

with open("test_doc.txt", "r") as file_obj:

    cont = file_obj.read()

    # 正则匹配精准度更高.使用切片会出现无法切换行符的情况
    re_cont = re.compile(r"[a-zA-Z]+")
    word_cont = re_cont.findall(cont)
    cnt = Counter(word_cont)
    print(cnt.most_common())

    while True:
        s = input("enter the key")
        if s == "":
            break
        print(word_dict[s])
