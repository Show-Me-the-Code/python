import re

with open("english.txt") as f:
    print len(re.findall("\w+", f.read()))