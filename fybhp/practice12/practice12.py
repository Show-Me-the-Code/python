# -*- coding:utf-8 -*-
import re
list = []
file = open('filter_words.txt','r')
content = file.read().decode('gbk')
allwords = content.split()
#print allwords
yourword = raw_input('>').decode('utf-8')
for mingan in allwords:
    if mingan in yourword:
        yourword = re.sub(mingan,'*'*len(mingan),yourword)
print yourword