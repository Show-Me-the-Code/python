'''
Self-defined activation code

Type A:
1. has length of 10
2. mixture of letters and numbers
3. unique throughtout 200 combos

Pros: 
total of 3656158440062976 combos, randomly generation of 200 is almost 
guaranteed to be unique; Confident level if high without look up opeations

Cons: 
Without back tracking, small chance would occur of duplication.
'''
import random

codeSeedA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def digit(raw):
	l = len(raw)
	return raw[random.randrange(l)] 

def typeACodeGen(n):
	codes_pool = []
	for i in range(n-1):
		code = ""
		for i in range(10):
			code += digit(codeSeedA)
		codes_pool.append(code)
	return codes_pool

codes = typeACodeGen(200)