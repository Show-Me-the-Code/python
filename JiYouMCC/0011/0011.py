# -*- coding: utf-8 -*-
def word_check(input_word, filtered_words):
    for word in filtered_words:
        if word in input_word:
            return 'Freedom'
    return 'Human Rights'

file = open('filtered_words.txt')
filtered_words=[line.replace('\n','') for line in file]
print word_check('程序员在上班。', filtered_words)
print word_check('我妈妈是农民。', filtered_words)
