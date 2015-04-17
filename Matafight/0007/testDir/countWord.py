#_*_ encoding: utf-8 _*_
import re

inputfile=file("test.txt",'r');
count=0;
for line in inputfile.readlines():
    word=re.findall(r"\w+",line);
    count+=len(word);
print "total wordcount is "+ str(count);
inputfile.close();
