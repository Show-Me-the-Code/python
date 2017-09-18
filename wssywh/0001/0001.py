#coding:utf-8

"""第0001题：做为Apple Store App独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用Python如何生成200个激活码（或者优惠券）？"""



import uuid

def get_id(num):
    list_id = []
    for i in range(num):
        id = str(uuid.uuid1()).replace('-','')
        list_id.append(id)
    return list_id
id = get_id(200)
with open("file_id.txt","w") as file:
    for i in id:
        file.write(i+"\n")