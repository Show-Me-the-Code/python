#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date: 10-03-15
# Author: Liang

import re
import operator

# Read the file
myfile = open('english_text.txt', 'r')
# Extract words from file excluding punctuation and /n
words = re.findall(r"[\w']+", myfile.read())

# Dictionary contains all the words and frequencies
words_dictionary = {}

# Count frequencies
for word in words:
    if word not in words_dictionary:
        # Put word in dictionary
        words_dictionary[word] = 0
        for item in words:
            if item == word:
                words_dictionary[word] += 1

# Sort the words by frequencies
sort_words_dictionary = sorted(
    words_dictionary.items(), key=operator.itemgetter(1), reverse=True)

print(sort_words_dictionary)
