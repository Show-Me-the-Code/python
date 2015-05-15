#!/usr/bin/env python

import random
import os

def radom_generate():
	string = ''
	for n in range(1,9):
		number = int(random.uniform(0,9))
		string += str(number) 
	string += '\n'
	return	string 

def file_write():
	fp = open("result.txt",'ab')
	string = radom_generate()
	fp.write(string)  
	fp.close() 

if __name__ == '__main__':
    for n in range(1,201):
    	 file_write()
