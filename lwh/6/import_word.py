import os
import re
from collections import Counter
from os.path import join, getsize

root_dir = os.getcwd() + "\\myrecord"


for root, dirs, files in os.walk(root_dir):
    for i in files:
        with open(root_dir + "\\" + i, "r") as f:
            cont = f.read()
            # print(cont)
            re_cont = re.compile(r"[a-zA-Z]+")
            word_cont = re_cont.findall(cont)
            cnt = Counter(word_cont)
            print(cnt.most_common(1))
