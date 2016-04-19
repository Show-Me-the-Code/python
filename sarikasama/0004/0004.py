#!/usr/bin/env python3
#count words in a textfile

from pprint import pprint
import re

def main():
    res = {}
    with open('test','r') as f:
        content = f.read()
    tmp = re.split(r"[^a-zA-Z]",content)
    for w in tmp:
        if not w:
            continue
        w = w.lower()
        if w not in res:
            res[w] = 1
        else:
            res[w] += 1
    pprint(res)

if __name__ == "__main__":
    main()
