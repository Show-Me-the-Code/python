#0012
#-*- encoding:utf-8 -*-
import string

filteredwords=[]

with open('filtered_words.txt','r')as f:
    #print(f.readlines().encoding('utf8'))
    for l in f.readlines():
        filteredwords.append(l.strip())

#print filteredwords
ins = raw_input("please input:")

for fw in filteredwords:
    if ins.find(fw )!= -1:
        ins = ins.replace(fw,"*")
print(ins)
