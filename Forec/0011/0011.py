# coding = utf-8
__author__ = 'Forec'
word_filter = set()
with open('filtered_words.txt',"r") as f:
    for x in f.readlines():
        word_filter |= {x.rstrip('\n')}
while True:
    s = input()
    if s == 'exit':
        break
    elif s in word_filter:
        print('Freedom')
    else:
        print('Human Rights')
        