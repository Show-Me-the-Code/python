import re

#sometimes dislike to use Recycling. bad.
def sub_with_spark(matched):
   # for g in matched.groups():
     #   print g
    
    return  '*' * len(matched.group(0))

    
filter_words=''
with open('filtered_words.txt','r') as f:
    for line in f:
        filter_words += line.strip()+'|'

filter_words = filter_words.strip('|')
fw = re.compile(filter_words)

content= raw_input("input:")
#print content
print fw.sub(sub_with_spark, content)




