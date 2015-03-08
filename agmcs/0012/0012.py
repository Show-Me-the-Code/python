#coding:utf-8
with open('filtered_words.txt','r')as f:
    data = f.read().decode('gbk')
    
filt = data.split('\n')

while True:
    text = raw_input("please input:")
    text  = text.decode('gbk')
    for x in filt:
        if text.find(x) != -1:
            text = text.replace(x,'*'*len(x))
    print text
