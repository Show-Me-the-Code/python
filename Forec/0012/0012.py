# coding = utf-8
__author__ = 'Forec'
word_filter = set()
with open('filtered_words.txt',"r") as f:
    for x in f.readlines():
        word_filter |= {x.strip('\n')}
while True:
    s = input()
    if s =='exit':
        break
    for x in word_filter:
        if x in s:
            s = s.replace(x,'*'*len(x))
    print(s)