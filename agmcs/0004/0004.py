import re
with open('test.txt','r')as f:
    data = f.read()
result = re.split(r"[^a-zA-Z]",data)
print len([x for x in result if x!= ''])
