__author__ = 'Tracy'

import io, re

count = 0

with io.open('text.txt', 'r') as file:
    for line in file.readlines():
        list = re.findall("[a-zA-Z]+'*-*[a-zA-Z]*", line)
        count += len(list)
print(count)

