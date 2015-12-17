#!/usr/bin/env python3
#filter sensitive words in user's input

def replace_sensitive_words(input_word):
    s_words = []
    with open('filtered_words','r') as f:
        line = f.readline()
        while line != '':
            s_words.append(line.strip())
            line = f.readline()
    for word in s_words:
        if word in input_word:
            input_word = input_word.replace(word, "**")
    print(input_word)

if __name__ == '__main__':
    while True:
        input_word = input('--> ')
        replace_sensitive_words(input_word)
