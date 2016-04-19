# -*- coding: cp936 -*-
import re
fin=open("example.txt","r")
fout=open("result.txt","w")
str=fin.read()
#匹配正则表达式
reObj=re.compile("\b?([a-zA-Z]+)\b?")
words=reObj.findall(str)
#建立空字典
word_dict={}
#以单词的小写作为键值进行统计，同时要
for word in words:
    if(word_dict.has_key(word)):
        word_dict[word.lower()]=max(word_dict[word.lower()],words.count(word.lower())+words.count(word.upper())+words.count(word))
    else:
        word_dict[word.lower()]=max(0,words.count(word.lower())+words.count(word.upper())+words.count(word))       
for(word,number) in word_dict.items():
    fout.write(word+":%d\n"%number)
    
