# -*- coding: utf-8 -*-
__author__ = 'PatchLion'

result = {}

def doCount(c):
    if c in result.keys():
        result[c] = result[c]+1
    else:
        result[c]=1

def countChar(file_path):
    with open(file_path, 'rt') as f:
        txt = f.read()
        f.close()
        list(map(doCount, txt))

countChar('PrivacyPolicy.txt')

print(result)
print(len(result))
