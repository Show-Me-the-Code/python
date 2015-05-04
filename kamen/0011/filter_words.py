import re

filter_words=''
with open('filtered_words.txt','r') as f:
    for line in f:
        filter_words += line.strip()+'|'

filter_words = filter_words.strip('|')
fw = re.compile(filter_words)

content= raw_input("input:")
if(fw.search(content)):
    print "Freedom"
else:
    print "Human Rights"
    

