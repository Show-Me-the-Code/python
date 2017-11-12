#-*- coding:utf8 -*-

import re
with open("flask","r") as f:

    s="".join(f.readlines())
    str=re.split(' |\\n',s)

    str_dict={}
    for i,x in enumerate(str):
        if not str_dict:
            str_dict[x] = 1
        else:
            for key ,value in str_dict.items():
                count=value
                if key == x:
                    count+=1
                    break
                count=1
            str_dict[x]=count

    for key,value in str_dict.items():
        print(key,value)
