#!/usr/bin/env python

'''
It can generate the activation code
'''

import random
#import string

f = open('C:\Users\zzl\Desktop\2.txt','w')
for x in range(200):
	words = [chr(a) for a in range(65,91)]+[chr(a) for a in range(97,122)]+[str(a) for a in range(0,11)]
	# It is equal to string.ascii_letters + string.digits
	slice = random.sample(words,10)
	temp = str(words)
	f.write(temp)
f.close()
