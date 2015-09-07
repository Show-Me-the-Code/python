from collections import Counter
import re

__author__ = "PyBeaner"

with open(r"F:\Program Files\Git\doc\git\html\RelNotes\1.5.0.1.txt") as f:
    word_pat = re.compile("^[A-Za-z]+$")
    file_words = [word for line in f for word in line.split()
                  if len(word) > 1 and word_pat.match(word)]

print(Counter(file_words))
