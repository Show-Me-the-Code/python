# -*- coding: cp936 -*-
import random
#生成200组长度为8的优惠码，字典集是数字加字母
def generate_key(number=200,length=8):
    char_set="abcdefghijklmnopqrstuvwxyz0123456789"
    result=""
    for i in range(0, number):
        temp=""
        while(temp==""):
            for j in range(0,length):
                temp=temp+char_set[random.randint(0,35)]
#判断新生成的优惠吗是否与之前的重复
            if(result.find(temp)==-1):
                result=result+"%d  "%(i+1)+temp
            else:
                temp=""      
        result=result+'\n'
    return result
def file_write():
    fp=open("result.txt",'w')
    fp.writelines(generate_key())
    fp.close()
if __name__ == '__main__':
	file_write()
