#!/usr/bin/env python3
#filter sensitive words in user's input

def filter_sensitive_words(input_word):
    s_words = []
    with open('filtered_words','r') as f:
        line = f.readline()
        while line != '':
            s_words.append(line.strip())
            line = f.readline()
    if input_word in s_words:
        print("Freedom")
    else:
        print("Human Rights")

if __name__ == '__main__':
    while True:
        input_word = input('--> ')
        filter_sensitive_words(input_word)
