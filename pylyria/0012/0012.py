# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

def sensitive_test(word):
    sensitive_words = [line.strip() for line in open('sensitive.txt', encoding='utf-8')]
    word = word.strip()
    for sensitive_word in sensitive_words:
        if sensitive_word.strip() in word.lower():
            word = re.sub(sensitive_word, '*' * len(sensitive_word), word, flags=re.IGNORECASE)
    return word

if __name__ == "__main__":
    line = True
    while line:
        line = input()
        line = line.strip()
        print(sensitive_test(line))
