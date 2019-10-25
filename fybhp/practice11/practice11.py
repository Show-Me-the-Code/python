# -*- coding:utf-8 -*-

list = []
file = open('filter_words.txt','r')
content = file.read().decode('gbk')
allwords = content.split()
#print allwords
checkword = raw_input('>').decode('utf-8')
if checkword in allwords:
    print 'Freedom'
else:
    print 'Hunam Rights'