# -*- coding: utf-8 -*-
import re


def word_change(input_word, filtered_words):
    result = input_word
    for word in filtered_words:
        if word in result:
            strinfo = re.compile(word)
            result = strinfo.sub('*' * len(word.decode('utf-8')), result)
    return result

file = open('filtered_words.txt')
filtered_words = [line.replace('\n', '') for line in file]

print word_change('lovely boy', filtered_words)
print word_change('程序员在上班。', filtered_words)
print word_change('我妈妈是农民。', filtered_words)


