# -*- coding: utf-8 -*-
#!/usr/bin/env python

def is_sensitive(word):
	sensitive_words = [line.strip() for line in open('sensitive.txt', encoding='utf-8')]
	word = word.strip()
	if word.lower() in sensitive_words:
		return True
	else:
		return False

if __name__ == "__main__":
    while 1:
    	if is_sensitive(input()):
    		print('Freedom')
    	else:
    		print('Human Rights')
