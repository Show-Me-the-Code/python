#!/usr/bin/env
'''
Self-defined activation code

1. has length of 10
2. mixture of letters and numbers
3. unique throughtout 200 combos

Pros: 
total of 3656158440062976 combos, randomly generation of 200 is almost 
guaranteed to be unique; Confident level if high without look up opeations.
And without look up, it's super fast :) The more codes needed, the effect 
is more obvious.

Cons: 
Without back tracking, small chance would occur of duplication.
'''
import random

codeSeedA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def digit(raw):
	l = len(raw)
	return raw[random.randrange(l)] 

def codeGen(n):
	codes_pool = []
	for i in range(n-1):
		code = ""
		for i in range(10):
			code += digit(codeSeedA)
		codes_pool.append(code)
	return codes_pool

codes = codeGen(200)