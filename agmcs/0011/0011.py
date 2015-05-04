#coding:utf-8
with open('filtered_words.txt','r')as f:
    data = f.read()
    
filt = data.split('\n')

while True:
    flag = False
    text = raw_input("please input:")
    for x in filt:
        if text.find(x) != -1:
            flag = True
    if flag:
        print "Freedom"
    else:
        print "Human Rights"
